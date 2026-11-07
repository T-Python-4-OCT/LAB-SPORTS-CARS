
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import HttpResponseNotAllowed
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from .models import Car, CarInquiry


# ==========================================
# ADMIN DASHBOARD
# ==========================================

@staff_member_required(login_url="admin:login")
def dashboard(request):

    total_cars = Car.objects.count()

    featured_cars = Car.objects.filter(
        is_featured=True
    ).count()

    inquiry_stats = CarInquiry.objects.aggregate(
        total=Count("id"),
        new=Count(
            "id",
            filter=Q(status="new")
        ),
        in_progress=Count(
            "id",
            filter=Q(status="in_progress")
        ),
        completed=Count(
            "id",
            filter=Q(status="completed")
        ),
    )

    popular_cars = (
        Car.objects
        .annotate(
            inquiry_count=Count("inquiries")
        )
        .filter(inquiry_count__gt=0)
        .order_by("-inquiry_count", "name")[:5]
    )

    recent_inquiries = (
        CarInquiry.objects
        .select_related("car")
        .order_by("-created_at")[:8]
    )

    return render(
        request,
        "cars/dashboard.html",
        {
            "total_cars": total_cars,
            "featured_cars_count": featured_cars,
            "total_inquiries": inquiry_stats["total"],
            "new_inquiries": inquiry_stats["new"],
            "in_progress_inquiries": inquiry_stats["in_progress"],
            "completed_inquiries": inquiry_stats["completed"],
            "popular_cars": popular_cars,
            "recent_inquiries": recent_inquiries,
        },
    )


# ==========================================
# INQUIRY MANAGEMENT
# ==========================================

@staff_member_required(login_url="admin:login")
@permission_required(
    "cars.view_carinquiry",
    raise_exception=True
)
def manage_inquiries(request):

    search_query = request.GET.get(
        "search", ""
    ).strip()

    selected_status = request.GET.get(
        "status", "all"
    ).strip()

    valid_statuses = {
        "all",
        "new",
        "in_progress",
        "completed",
    }

    if selected_status not in valid_statuses:
        selected_status = "all"

    inquiries = CarInquiry.objects.select_related(
        "car"
    )

    if search_query:
        inquiries = inquiries.filter(
            Q(full_name__icontains=search_query)
            | Q(email__icontains=search_query)
            | Q(phone__icontains=search_query)
            | Q(car__name__icontains=search_query)
            | Q(message__icontains=search_query)
        )

    if selected_status != "all":
        inquiries = inquiries.filter(
            status=selected_status
        )

    inquiries = inquiries.order_by(
        "-created_at",
        "-id"
    )

    paginator = Paginator(inquiries, 8)

    page_obj = paginator.get_page(
        request.GET.get("page")
    )

    stats = CarInquiry.objects.aggregate(
        total=Count("id"),
        new=Count(
            "id",
            filter=Q(status="new")
        ),
        in_progress=Count(
            "id",
            filter=Q(status="in_progress")
        ),
        completed=Count(
            "id",
            filter=Q(status="completed")
        ),
    )

    return render(
        request,
        "cars/manage_inquiries.html",
        {
            "inquiries": page_obj,
            "page_obj": page_obj,
            "paginator": paginator,
            "search_query": search_query,
            "selected_status": selected_status,
            "results_count": paginator.count,
            "stats": stats,
            "can_change": request.user.has_perm(
                "cars.change_carinquiry"
            ),
        },
    )


# ==========================================
# UPDATE INQUIRY STATUS
# ==========================================

@staff_member_required(login_url="admin:login")
@permission_required(
    "cars.change_carinquiry",
    raise_exception=True
)
def update_inquiry_status(request, inquiry_id):

    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    inquiry = get_object_or_404(
        CarInquiry,
        pk=inquiry_id
    )

    new_status = request.POST.get(
        "status", ""
    )

    valid_statuses = {
        choice[0]
        for choice in CarInquiry.STATUS_CHOICES
    }

    if new_status not in valid_statuses:
        messages.error(
            request,
            "Invalid inquiry status."
        )

    else:
        if inquiry.status != new_status:
            inquiry.status = new_status
            inquiry.save(
                update_fields=["status"]
            )

            messages.success(
                request,
                "Inquiry status updated successfully."
            )

        else:
            messages.info(
                request,
                "This inquiry already has that status."
            )

    # Return to the filtered page the admin came from.
    fallback = reverse(
        "cars:manage_inquiries"
    )

    return_to = request.POST.get(
        "next", ""
    )

    if (
        return_to
        and url_has_allowed_host_and_scheme(
            url=return_to,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()
        )
        and return_to.startswith(
            reverse("cars:manage_inquiries")
        )
    ):
        return redirect(return_to)

    return redirect(fallback)
