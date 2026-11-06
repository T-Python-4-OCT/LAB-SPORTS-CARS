from django.shortcuts import redirect

def toggle_theme(request):
    """Dark / light mode: flip the 'theme' cookie, then go back to the same page."""
    new = "light" if request.COOKIES.get("theme") == "dark" else "dark"
    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("theme", new, max_age=60 * 60 * 24 * 365)
    return response