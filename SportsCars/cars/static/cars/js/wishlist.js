
document.addEventListener("DOMContentLoaded", () => {

    // ========================================
    // WISHLIST SETTINGS
    // ========================================

    const STORAGE_KEY = "sportscars-wishlist";
    const MAX_SAVED = 100;

    const wishlistLink = document.getElementById(
        "wishlist-nav-link"
    );

    const wishlistFooterLink = document.getElementById(
        "wishlist-footer-link"
    );

    const wishlistCount = document.getElementById(
        "wishlist-count"
    );

    if (!wishlistLink) {
        return;
    }

    const wishlistBaseUrl = new URL(
        wishlistLink.href,
        window.location.origin
    );

    // ========================================
    // LOCAL STORAGE
    // ========================================

    function getSavedIds() {
        try {
            const stored = JSON.parse(
                localStorage.getItem(STORAGE_KEY) || "[]"
            );

            if (!Array.isArray(stored)) {
                return [];
            }

            const validIds = stored
                .map(value => Number(value))
                .filter(
                    value => Number.isSafeInteger(value)
                        && value > 0
                );

            return [...new Set(validIds)]
                .slice(0, MAX_SAVED);

        } catch (error) {
            console.warn(
                "Could not read wishlist:",
                error
            );

            return [];
        }
    }


    function saveIds(ids) {
        try {
            localStorage.setItem(
                STORAGE_KEY,
                JSON.stringify(ids)
            );

            return true;

        } catch (error) {
            console.warn(
                "Could not save wishlist:",
                error
            );

            return false;
        }
    }


    // ========================================
    // BUILD WISHLIST URL
    // ========================================

    function buildWishlistUrl(ids) {
        const url = new URL(wishlistBaseUrl.href);

        url.search = "";

        ids.forEach(id => {
            url.searchParams.append(
                "cars",
                String(id)
            );
        });

        return url.href;
    }


    function updateNavigation(ids) {
        const url = buildWishlistUrl(ids);

        wishlistLink.href = url;

        if (wishlistFooterLink) {
            wishlistFooterLink.href = url;
        }

        if (wishlistCount) {
            wishlistCount.textContent = ids.length;
        }

        wishlistLink.setAttribute(
            "aria-label",
            `Open wishlist with ${ids.length} saved cars`
        );
    }


    // ========================================
    // GET CAR ID FROM DETAIL LINK
    // ========================================

    function getCarIdFromLink(link) {
        if (!link) {
            return null;
        }

        const url = new URL(
            link.href,
            window.location.origin
        );

        const match = url.pathname.match(
            /\/cars\/(\d+)\/?$/
        );

        return match ? Number(match[1]) : null;
    }


    // ========================================
    // CREATE FAVORITE BUTTON
    // ========================================

    function createFavoriteButton(carId, isDetail) {
        const button = document.createElement("button");

        button.type = "button";
        button.className = isDetail
            ? "wishlist-toggle wishlist-detail-toggle"
            : "wishlist-toggle wishlist-card-toggle";

        button.dataset.carId = String(carId);

        const icon = document.createElement("span");
        icon.className = "material-symbols-outlined";
        icon.setAttribute("aria-hidden", "true");

        button.appendChild(icon);

        if (isDetail) {
            const label = document.createElement("span");
            label.className = "wishlist-button-label";

            button.appendChild(label);
        }

        button.addEventListener("click", () => {
            toggleFavorite(carId);
        });

        return button;
    }


    // ========================================
    // ADD HEART BUTTONS TO CAR CARDS
    // ========================================

    function setupCarCards() {
        const cards = document.querySelectorAll(".car-card");

        cards.forEach(card => {
            const detailLink = card.querySelector(
                'a[href*="/cars/"]'
            );

            const carId = getCarIdFromLink(detailLink);

            if (!carId) {
                return;
            }

            if (card.querySelector(".wishlist-toggle")) {
                return;
            }

            const button = createFavoriteButton(
                carId,
                false
            );

            card.appendChild(button);
        });
    }


    // ========================================
    // ADD FAVORITE BUTTON TO DETAIL PAGE
    // ========================================

    function setupDetailPage() {
        const detailInfo = document.querySelector(
            ".detail-info"
        );

        if (!detailInfo) {
            return;
        }

        const match = window.location.pathname.match(
            /\/cars\/(\d+)\/?$/
        );

        if (!match) {
            return;
        }

        const carId = Number(match[1]);

        if (!carId) {
            return;
        }

        const button = createFavoriteButton(
            carId,
            true
        );

        detailInfo.appendChild(button);
    }


    // ========================================
    // UPDATE BUTTON APPEARANCES
    // ========================================

    function updateButtons(ids) {
        const saved = new Set(ids);

        const buttons = document.querySelectorAll(
            ".wishlist-toggle"
        );

        buttons.forEach(button => {
            const carId = Number(button.dataset.carId);
            const isSaved = saved.has(carId);

            button.classList.toggle(
                "is-saved",
                isSaved
            );

            button.setAttribute(
                "aria-pressed",
                String(isSaved)
            );

            button.setAttribute(
                "aria-label",
                isSaved
                    ? "Remove car from wishlist"
                    : "Add car to wishlist"
            );

            const icon = button.querySelector(
                ".material-symbols-outlined"
            );

            if (icon) {
                icon.textContent = isSaved
                    ? "favorite"
                    : "favorite_border";
            }

            const label = button.querySelector(
                ".wishlist-button-label"
            );

            if (label) {
                label.textContent = isSaved
                    ? "REMOVE FROM WISHLIST"
                    : "ADD TO WISHLIST";
            }
        });
    }


    // ========================================
    // ADD / REMOVE FAVORITE
    // ========================================

    function toggleFavorite(carId) {
        const ids = getSavedIds();
        const exists = ids.includes(carId);

        let updatedIds;

        if (exists) {
            updatedIds = ids.filter(
                id => id !== carId
            );
        } else {
            if (ids.length >= MAX_SAVED) {
                window.alert(
                    "Wishlist limit reached."
                );
                return;
            }

            updatedIds = [...ids, carId];
        }

        const saved = saveIds(updatedIds);

        if (!saved) {
            window.alert(
                "Could not save your wishlist in this browser."
            );
            return;
        }

        updateNavigation(updatedIds);
        updateButtons(updatedIds);

        // Refresh the saved collection after removal.
        if (
            document.getElementById("wishlist-page")
        ) {
            window.location.assign(
                buildWishlistUrl(updatedIds)
            );
        }
    }


    // ========================================
    // WISHLIST PAGE INITIALIZATION
    // ========================================

    function syncWishlistPage(ids) {
        const wishlistPage = document.getElementById(
            "wishlist-page"
        );

        if (!wishlistPage) {
            return;
        }

        const params = new URLSearchParams(
            window.location.search
        );

        // When visiting /wishlist/ directly,
        // open the collection stored locally.
        if (!params.has("cars") && ids.length > 0) {
            window.location.replace(
                buildWishlistUrl(ids)
            );
        }
    }


    // ========================================
    // SYNC ACROSS BROWSER TABS
    // ========================================

    window.addEventListener("storage", event => {
        if (event.key !== STORAGE_KEY) {
            return;
        }

        const ids = getSavedIds();

        updateNavigation(ids);
        updateButtons(ids);

        if (document.getElementById("wishlist-page")) {
            window.location.replace(
                buildWishlistUrl(ids)
            );
        }
    });


    // ========================================
    // START
    // ========================================

    const savedIds = getSavedIds();

    setupCarCards();
    setupDetailPage();

    updateNavigation(savedIds);
    updateButtons(savedIds);
    syncWishlistPage(savedIds);

});
