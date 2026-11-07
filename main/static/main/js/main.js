
const menuToggle = document.getElementById("menuToggle");
const mobileMenu = document.getElementById("mobileMenu");

if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", () => {
        const isOpen = !mobileMenu.classList.toggle("hidden");

        menuToggle.setAttribute("aria-expanded", String(isOpen));
        menuToggle.querySelector("span").textContent = isOpen ? "close" : "menu";
    });
}


const searchToggle = document.getElementById("searchToggle");
const searchPanel = document.getElementById("searchPanel");
const searchInput = document.getElementById("searchInput");

if (searchToggle && searchPanel && searchInput) {
    searchToggle.addEventListener("click", () => {
        const isOpen = !searchPanel.classList.toggle("hidden");

        searchToggle.setAttribute("aria-expanded", String(isOpen));

        if (isOpen) {
            searchInput.focus();
        } else {
            searchInput.value = "";
        }
    });
}


const themeToggle = document.getElementById("themeToggle");

if (themeToggle) {
    const themeIcon = themeToggle.querySelector("span");

    function updateThemeIcon() {
        const isDark = document.documentElement.classList.contains("dark");
        themeIcon.textContent = isDark ? "light_mode" : "dark_mode";
    }

    updateThemeIcon();

    themeToggle.addEventListener("click", () => {
        const isDark = document.documentElement.classList.toggle("dark");

        localStorage.setItem("theme", isDark ? "dark" : "light");
        updateThemeIcon();
    });
}


const newsletterForm = document.getElementById("newsletterForm");
const newsletterMessage = document.getElementById("newsletterMessage");

if (newsletterForm && newsletterMessage) {
    newsletterForm.addEventListener("submit", (event) => {
        event.preventDefault();

        newsletterMessage.textContent = "Thank you for subscribing! (Demo)";
        newsletterForm.reset();
    });
}


const categoryFilter = document.getElementById("categoryFilter");
const carCards = document.querySelectorAll(".car-card");
const carsCount = document.getElementById("carsCount");
const noResults = document.getElementById("noResults");

if (categoryFilter && carsCount && noResults) {
    categoryFilter.addEventListener("change", () => {
        const selectedCategory = categoryFilter.value;
        let visibleCount = 0;

        carCards.forEach((card) => {
            const matches = selectedCategory === "all" ||
                card.dataset.category === selectedCategory;

            card.classList.toggle("hidden", !matches);

            if (matches) {
                visibleCount++;
            }
        });

        carsCount.textContent = `${visibleCount} Cars Found`;
        noResults.classList.toggle("hidden", visibleCount !== 0);
    });
}


const demoToast = document.getElementById("demoToast");

function showDemoMessage(message) {
    if (demoToast) {
        demoToast.textContent = message;
        demoToast.classList.remove("hidden");
    }
}

document.querySelectorAll("[data-demo]").forEach((button) => {
    button.addEventListener("click", () => {
        showDemoMessage(button.dataset.demo);
    });
});


const favoritesToggle = document.getElementById("favoritesToggle");
const favoritesCount = document.getElementById("favoritesCount");
const favoritesOverlay = document.getElementById("favoritesOverlay");
const favoritesPanel = document.getElementById("favoritesPanel");
const closeFavorites = document.getElementById("closeFavorites");
const favoritesList = document.getElementById("favoritesList");
const favoritesEmpty = document.getElementById("favoritesEmpty");
const favoritesSummary = document.getElementById("favoritesSummary");
const wishlistToggle = document.getElementById("wishlistToggle");

let lastFocusedElement = null;

function getFavorites() {
    try {
        const saved = JSON.parse(localStorage.getItem("crownFavorites") || "[]");

        if (!Array.isArray(saved)) {
            return [];
        }

        return saved.filter((car) => {
            return car &&
                Number.isInteger(car.id) &&
                car.id >= 1 &&
                car.id <= 6 &&
                typeof car.name === "string" &&
                typeof car.image === "string" &&
                typeof car.url === "string" &&
                car.url === `/cars/${car.id}/`;
        });
    } catch {
        return [];
    }
}


function saveFavorites(favorites) {
    try {
        localStorage.setItem("crownFavorites", JSON.stringify(favorites));
    } catch {
        showDemoMessage("Favorites could not be saved in this browser.");
    }

    updateFavorites();
}


function updateWishlistButton() {
    if (!wishlistToggle) {
        return;
    }

    const carId = Number(wishlistToggle.dataset.carId);
    const isSaved = getFavorites().some((car) => car.id === carId);
    const icon = wishlistToggle.querySelector(".material-symbols-outlined");

    wishlistToggle.setAttribute("aria-pressed", String(isSaved));
    wishlistToggle.setAttribute(
        "aria-label",
        isSaved ? "Remove from favorites" : "Add to favorites"
    );

    if (icon) {
        icon.textContent = isSaved ? "heart_check" : "favorite";
    }

    const labelNode = Array.from(wishlistToggle.childNodes).find((node) => {
        return node.nodeType === Node.TEXT_NODE && node.textContent.trim();
    });

    if (labelNode) {
        labelNode.textContent = isSaved
            ? " Remove from Favorites "
            : " Add to Favorites ";
    }
}


function createFavoriteCard(car) {
    const card = document.createElement("article");
    card.className = "overflow-hidden rounded-xl border border-[#B99A62]/30 bg-white shadow-sm dark:bg-[#263D46]";

    const imageLink = document.createElement("a");
    imageLink.href = car.url;
    imageLink.className = "flex h-44 items-center justify-center bg-white p-4";

    const image = document.createElement("img");
    image.src = car.image;
    image.alt = car.name;
    image.loading = "lazy";
    image.className = "h-full w-full object-contain";

    imageLink.appendChild(image);

    const content = document.createElement("div");
    content.className = "p-5";

    const heading = document.createElement("h3");
    heading.className = "font-['Phudu'] text-lg font-semibold text-[#111418] dark:text-[#F4F0E8]";
    heading.textContent = car.name;

    const actions = document.createElement("div");
    actions.className = "mt-5 flex flex-wrap items-center justify-between gap-3";

    const detailsLink = document.createElement("a");
    detailsLink.href = car.url;
    detailsLink.className = "text-sm font-semibold text-[#B99A62] hover:underline";
    detailsLink.textContent = "View Details";

    const removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.className = "inline-flex items-center gap-1 rounded-md border border-[#B99A62]/40 px-3 py-2 text-xs font-semibold transition hover:bg-[#B99A62] hover:text-[#111418]";
    removeButton.setAttribute("aria-label", `Remove ${car.name} from favorites`);

    const removeIcon = document.createElement("span");
    removeIcon.className = "material-symbols-outlined text-lg";
    removeIcon.textContent = "delete";

    const removeText = document.createElement("span");
    removeText.textContent = "Remove";

    removeButton.append(removeIcon, removeText);

    removeButton.addEventListener("click", () => {
        const updated = getFavorites().filter((item) => item.id !== car.id);
        saveFavorites(updated);
    });

    actions.append(detailsLink, removeButton);
    content.append(heading, actions);
    card.append(imageLink, content);

    return card;
}


function renderFavorites() {
    if (!favoritesList || !favoritesEmpty || !favoritesSummary) {
        return;
    }

    const favorites = getFavorites();

    favoritesList.replaceChildren();

    favoritesSummary.textContent = favorites.length === 1
        ? "1 car in your personal collection"
        : `${favorites.length} cars in your personal collection`;

    favoritesEmpty.classList.toggle("hidden", favorites.length > 0);
    favoritesEmpty.classList.toggle("flex", favorites.length === 0);

    favorites.forEach((car) => {
        favoritesList.appendChild(createFavoriteCard(car));
    });
}


function updateFavorites() {
    const favorites = getFavorites();

    if (favoritesCount) {
        favoritesCount.textContent = favorites.length;
    }

    updateWishlistButton();
    renderFavorites();
}


function openFavoritesPanel() {
    if (!favoritesPanel || !favoritesOverlay) {
        return;
    }

    lastFocusedElement = document.activeElement;

    renderFavorites();

    favoritesPanel.classList.remove("hidden");
    favoritesOverlay.classList.remove("hidden");

    document.body.classList.add("overflow-hidden");
    favoritesToggle.setAttribute("aria-expanded", "true");

    closeFavorites.focus();
}


function closeFavoritesPanel() {
    if (!favoritesPanel || !favoritesOverlay) {
        return;
    }

    favoritesPanel.classList.add("hidden");
    favoritesOverlay.classList.add("hidden");

    document.body.classList.remove("overflow-hidden");
    favoritesToggle.setAttribute("aria-expanded", "false");

    if (lastFocusedElement && lastFocusedElement.isConnected) {
        lastFocusedElement.focus();
    }
}


if (favoritesToggle) {
    favoritesToggle.addEventListener("click", () => {
        const isOpen = !favoritesPanel.classList.contains("hidden");

        if (isOpen) {
            closeFavoritesPanel();
        } else {
            openFavoritesPanel();
        }
    });
}

if (closeFavorites) {
    closeFavorites.addEventListener("click", closeFavoritesPanel);
}

if (favoritesOverlay) {
    favoritesOverlay.addEventListener("click", closeFavoritesPanel);
}

document.addEventListener("keydown", (event) => {
    if (!favoritesPanel || favoritesPanel.classList.contains("hidden")) {
        return;
    }

    if (event.key === "Escape") {
        closeFavoritesPanel();
        return;
    }

    if (event.key === "Tab") {
        const focusable = Array.from(
            favoritesPanel.querySelectorAll("a[href], button:not([disabled])")
        );

        if (focusable.length === 0) {
            event.preventDefault();
            favoritesPanel.focus();
            return;
        }

        const first = focusable[0];
        const last = focusable[focusable.length - 1];

        if (event.shiftKey && document.activeElement === first) {
            event.preventDefault();
            last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
            event.preventDefault();
            first.focus();
        }
    }
});


if (wishlistToggle) {
    wishlistToggle.addEventListener("click", () => {
        const carId = Number(wishlistToggle.dataset.carId);
        const name = document.querySelector("h1")?.textContent.trim();
        const image = document.querySelector(".hero-car img")?.getAttribute("src");
        const url = `/cars/${carId}/`;

        if (!Number.isInteger(carId) || carId < 1 || carId > 6 || !name || !image) {
            showDemoMessage("Unable to save this car.");
            return;
        }

        const favorites = getFavorites();
        const alreadySaved = favorites.some((car) => car.id === carId);

        if (alreadySaved) {
            saveFavorites(favorites.filter((car) => car.id !== carId));
            showDemoMessage(`${name} removed from favorites.`);
        } else {
            favorites.push({
                id: carId,
                name: name,
                image: image,
                url: url
            });

            saveFavorites(favorites);
            showDemoMessage(`${name} added to favorites.`);
        }
    });
}


window.addEventListener("storage", (event) => {
    if (event.key === "crownFavorites") {
        updateFavorites();
    }
});

updateFavorites();


const revealElements = document.querySelectorAll(".reveal");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (revealElements.length > 0 && !reducedMotion && "IntersectionObserver" in window) {
    document.documentElement.classList.add("motion-ready");

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("reveal-visible");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: "0px 0px 30px 0px"
    });

    revealElements.forEach((element) => {
        revealObserver.observe(element);
    });
}
