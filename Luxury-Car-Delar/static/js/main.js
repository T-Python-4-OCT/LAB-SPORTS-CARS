const WISHLIST_STORAGE_KEY = "velare-wishlist";
const THEME_STORAGE_KEY = "velare-theme";

function readStorage(key) {
    try {
        return localStorage.getItem(key);
    } catch (error) {
        return null;
    }
}

function writeStorage(key, value) {
    try {
        localStorage.setItem(key, value);
    } catch (error) {
        // The feature remains available for the current page.
    }
}

function initializeTheme() {
    const themeToggle = document.getElementById("themeToggle");
    const themeIcon = themeToggle
        ? themeToggle.querySelector("span")
        : null;

    const savedTheme = readStorage(THEME_STORAGE_KEY);

    if (savedTheme === "dark" || savedTheme === "light") {
        document.documentElement.dataset.theme = savedTheme;
    }

    if (!themeToggle || !themeIcon) {
        return;
    }

    function updateThemeButton() {
        const isDark = document.documentElement.dataset.theme === "dark";

        themeIcon.textContent = isDark ? "light_mode" : "dark_mode";
        themeToggle.setAttribute("aria-pressed", String(isDark));
        themeToggle.setAttribute(
            "aria-label",
            isDark ? "Switch to light mode" : "Switch to dark mode"
        );
    }

    updateThemeButton();

    themeToggle.addEventListener("click", () => {
        const isDark = document.documentElement.dataset.theme === "dark";
        const newTheme = isDark ? "light" : "dark";

        document.documentElement.dataset.theme = newTheme;
        writeStorage(THEME_STORAGE_KEY, newTheme);
        updateThemeButton();
    });
}

function initializeMobileNavigation() {
    const menuToggle = document.getElementById("menuToggle");
    const mobileNav = document.getElementById("mobileNav");
    const menuIcon = menuToggle
        ? menuToggle.querySelector("span")
        : null;

    if (!menuToggle || !mobileNav || !menuIcon) {
        return;
    }

    function closeMenu() {
        mobileNav.hidden = true;
        menuToggle.setAttribute("aria-expanded", "false");
        menuIcon.textContent = "menu";
    }

    menuToggle.addEventListener("click", () => {
        const isOpen = menuToggle.getAttribute("aria-expanded") === "true";

        menuToggle.setAttribute("aria-expanded", String(!isOpen));
        menuIcon.textContent = isOpen ? "menu" : "close";
        mobileNav.hidden = isOpen;
    });

    mobileNav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeMenu);
    });
}

function initializeGallery() {
    const gallery = document.querySelector("[data-car-gallery]");

    if (!gallery) {
        return;
    }

    const mainImage = gallery.querySelector("[data-gallery-main]");
    const counter = gallery.querySelector("[data-gallery-counter]");
    const tabs = gallery.querySelectorAll("[data-gallery-tab]");
    const panels = gallery.querySelectorAll("[data-gallery-panel]");
    const previousButton = gallery.querySelector("[data-gallery-prev]");
    const nextButton = gallery.querySelector("[data-gallery-next]");
    const expandButton = gallery.querySelector("[data-gallery-expand]");
    const lightbox = document.querySelector("[data-gallery-lightbox]");
    const lightboxImage = lightbox
        ? lightbox.querySelector("[data-lightbox-image]")
        : null;
    const lightboxClose = lightbox
        ? lightbox.querySelector("[data-lightbox-close]")
        : null;

    if (!mainImage || !counter) {
        return;
    }

    let activeGroup = "exterior";
    let activeIndex = 0;

    function getActivePhotos() {
        const panel = gallery.querySelector(
            `[data-gallery-panel="${activeGroup}"]`
        );

        return panel
            ? Array.from(panel.querySelectorAll("[data-gallery-photo]"))
            : [];
    }

    function showPhoto(index) {
        const photos = getActivePhotos();

        if (photos.length === 0) {
            return;
        }

        activeIndex = (index + photos.length) % photos.length;
        const selectedPhoto = photos[activeIndex];

        mainImage.src = selectedPhoto.dataset.photoSrc;
        mainImage.alt = selectedPhoto.dataset.photoAlt;
        mainImage.classList.remove("detail-gallery__photo--enter");
        void mainImage.offsetWidth;
        mainImage.classList.add("detail-gallery__photo--enter");

        photos.forEach((photo, photoIndex) => {
            const isActive = photoIndex === activeIndex;

            photo.classList.toggle("is-active", isActive);
            photo.setAttribute("aria-pressed", String(isActive));
        });

        counter.textContent = `${activeIndex + 1} / ${photos.length}`;
    }

    function switchGallery(group) {
        activeGroup = group;
        activeIndex = 0;

        tabs.forEach((tab) => {
            const isActive = tab.dataset.galleryTab === group;

            tab.classList.toggle("is-active", isActive);
            tab.setAttribute("aria-selected", String(isActive));
        });

        panels.forEach((panel) => {
            panel.hidden = panel.dataset.galleryPanel !== group;
        });

        showPhoto(0);
    }

    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            switchGallery(tab.dataset.galleryTab);
        });
    });

    gallery.querySelectorAll("[data-gallery-photo]").forEach((photo) => {
        photo.addEventListener("click", () => {
            const panel = photo.closest("[data-gallery-panel]");

            if (!panel) {
                return;
            }

            const group = panel.dataset.galleryPanel;
            const photos = Array.from(
                panel.querySelectorAll("[data-gallery-photo]")
            );

            if (group !== activeGroup) {
                switchGallery(group);
            }

            showPhoto(photos.indexOf(photo));
        });
    });

    if (previousButton) {
        previousButton.addEventListener("click", () => {
            showPhoto(activeIndex - 1);
        });
    }

    if (nextButton) {
        nextButton.addEventListener("click", () => {
            showPhoto(activeIndex + 1);
        });
    }

    gallery.addEventListener("keydown", (event) => {
        if (event.key === "ArrowRight") {
            event.preventDefault();
            showPhoto(activeIndex + 1);
        } else if (event.key === "ArrowLeft") {
            event.preventDefault();
            showPhoto(activeIndex - 1);
        }
    });

    if (expandButton && lightbox && lightboxImage && lightboxClose) {
        expandButton.addEventListener("click", () => {
            lightboxImage.src = mainImage.src;
            lightboxImage.alt = mainImage.alt;

            if (typeof lightbox.showModal === "function") {
                lightbox.showModal();
            }
        });

        lightboxClose.addEventListener("click", () => {
            lightbox.close();
        });

        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) {
                lightbox.close();
            }
        });
    }
}

function initializeScrollReveal() {
    const sections = document.querySelectorAll(".reveal");
    const reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    if (
        reduceMotion ||
        !("IntersectionObserver" in window) ||
        sections.length === 0
    ) {
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    sections.forEach((section) => {
        observer.observe(section);
    });

    document.documentElement.classList.add("has-scroll-reveal");
}

function initializeWishlist() {
    let savedCars = [];
    const storedCars = readStorage(WISHLIST_STORAGE_KEY);

    if (storedCars) {
        try {
            const parsedCars = JSON.parse(storedCars);

            if (Array.isArray(parsedCars)) {
                savedCars = parsedCars.filter(
                    (carSlug) => typeof carSlug === "string"
                );
            }
        } catch (error) {
            savedCars = [];
        }
    }

    const wishlist = new Set(savedCars);
    const wishlistButtons = document.querySelectorAll("[data-wishlist]");

    wishlistButtons.forEach((button) => {
        const carSlug = button.dataset.wishlist;
        const carName = button.dataset.wishlistName || "car";

        if (!carSlug) {
            return;
        }

        function updateWishlistButton() {
            const isSaved = wishlist.has(carSlug);

            button.classList.toggle("is-active", isSaved);
            button.setAttribute("aria-pressed", String(isSaved));
            button.setAttribute(
                "aria-label",
                isSaved
                    ? `Remove ${carName} from wishlist`
                    : `Add ${carName} to wishlist`
            );
        }

        updateWishlistButton();

        button.addEventListener("click", () => {
            if (wishlist.has(carSlug)) {
                wishlist.delete(carSlug);
            } else {
                wishlist.add(carSlug);
            }

            writeStorage(
                WISHLIST_STORAGE_KEY,
                JSON.stringify(Array.from(wishlist))
            );
            updateWishlistButton();
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    initializeTheme();
    initializeMobileNavigation();
    initializeGallery();
    initializeScrollReveal();
    initializeWishlist();
});
