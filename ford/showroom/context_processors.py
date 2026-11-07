def preferences(request):
    if request.user.is_authenticated:
        return {"account_favorites": list(
            request.user.favorite_set.values_list("car__slug", flat=True)
        )}
    return {"account_favorites": None}
