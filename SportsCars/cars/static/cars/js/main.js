
document.addEventListener("DOMContentLoaded", () => {

    // ========================================
    // DARK MODE
    // ========================================

    const themeToggle = document.getElementById("theme-toggle");

    const themeIcon = themeToggle?.querySelector(
        ".material-symbols-outlined"
    );

    let savedTheme = null;

    try {
        savedTheme = localStorage.getItem("sportscars-theme");
    } catch (error) {
        console.warn("Theme storage unavailable:", error);
    }

    function applyTheme(theme) {
        const isDark = theme === "dark";

        document.body.classList.toggle("dark-mode", isDark);

        if (themeIcon) {
            themeIcon.textContent = isDark
                ? "light_mode"
                : "dark_mode";
        }

        if (themeToggle) {
            themeToggle.setAttribute(
                "aria-pressed",
                String(isDark)
            );
        }
    }

    applyTheme(savedTheme === "dark" ? "dark" : "light");

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {

            const isDark = document.body.classList.contains(
                "dark-mode"
            );

            const newTheme = isDark ? "light" : "dark";

            applyTheme(newTheme);

            try {
                localStorage.setItem(
                    "sportscars-theme",
                    newTheme
                );
            } catch (error) {
                console.warn(
                    "Could not save theme preference:",
                    error
                );
            }

        });
    }


    // ========================================
    // 3D HERO
    // ========================================

    const viewer = document.getElementById("hero-car-model");

    const buttons = document.querySelectorAll(".switch-btn");

    const selectedCarName = document.getElementById(
        "selected-car-name"
    );

    const modelStatus = document.getElementById(
        "model-status"
    );

    const detailsLink = document.getElementById(
        "hero-details-link"
    );

    // Other pages do not have the 3D Hero.
    if (!viewer || !selectedCarName || !modelStatus) {
        return;
    }


    // ========================================
    // REDUCED MOTION
    // ========================================

    const reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    if (reduceMotion) {
        viewer.removeAttribute("auto-rotate");
    }


    // ========================================
    // LOADING STATUS
    // ========================================

    function showLoading() {
        modelStatus.textContent = "Loading 3D model...";
        modelStatus.classList.remove("is-hidden");
    }

    function hideLoading() {
        modelStatus.classList.add("is-hidden");
    }

    function showError() {
        modelStatus.textContent =
            "Unable to load this 3D car. Check the GLB file.";

        modelStatus.classList.remove("is-hidden");
    }


    // ========================================
    // CAR SWITCHER
    // ========================================

    buttons.forEach((button) => {

        button.addEventListener("click", () => {

            const modelPath = button.dataset.model;
            const carName = button.dataset.carName;
            const detailUrl = button.dataset.detailUrl;

            if (!modelPath || !carName) {
                return;
            }

            // Active button
            buttons.forEach((otherButton) => {

                otherButton.classList.remove("active");

                otherButton.setAttribute(
                    "aria-pressed",
                    "false"
                );

            });

            button.classList.add("active");

            button.setAttribute(
                "aria-pressed",
                "true"
            );

            // Car name
            selectedCarName.textContent = carName.toUpperCase();

            // Details URL
            if (detailsLink && detailUrl) {
                detailsLink.href = detailUrl;
            }

            // Change 3D model
            if (viewer.getAttribute("src") !== modelPath) {

                showLoading();

                viewer.setAttribute("src", modelPath);

                viewer.setAttribute(
                    "alt",
                    `Interactive 3D ${carName}`
                );

            }

        });

    });


    // ========================================
    // MODEL EVENTS
    // ========================================

    viewer.addEventListener("load", () => {
        hideLoading();
    });

    viewer.addEventListener("error", (event) => {

        console.error("3D model loading error:", event);

        showError();

    });

    if (viewer.loaded) {
        hideLoading();
    }

});
