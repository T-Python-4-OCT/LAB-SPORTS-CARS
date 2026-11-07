from .data import VEHICLES, SOCIAL_LINKS


def site_context(request):
    return {
        "vehicle_brands": sorted({vehicle["brand"] for vehicle in VEHICLES}),
        "vehicle_years": sorted({vehicle["year"] for vehicle in VEHICLES}, reverse=True),
        "home_hero": VEHICLES[1]["image"],
        "collection_hero": VEHICLES[1]["gallery"][1],
        "about_hero": VEHICLES[2]["image"],
        "experience_image": VEHICLES[1]["gallery"][2],
        "story_image": VEHICLES[0]["gallery"][0],
        "dealer_image": VEHICLES[2]["gallery"][1],
        "cta_image": VEHICLES[0]["gallery"][1],
        "social_links": SOCIAL_LINKS,
    }
