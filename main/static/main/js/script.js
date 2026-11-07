
document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const savedTheme = localStorage.getItem("theme");

    document.body.classList.toggle("dark-mode", savedTheme === "dark");

    function updateThemeIcon() {
        if (!themeToggle) return;

        const icon = themeToggle.querySelector(".material-symbols-outlined");

        if (!icon) return;

        icon.textContent = document.body.classList.contains("dark-mode")
            ? "light_mode"
            : "dark_mode";
    }

    updateThemeIcon();

    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            const isDark = document.body.classList.toggle("dark-mode");

            localStorage.setItem("theme", isDark ? "dark" : "light");

            updateThemeIcon();
        });
    }

    const brandFilter = document.getElementById("brand-filter");
    const modelFilter = document.getElementById("model-filter");
    const priceFilter = document.getElementById("price-filter");
    const yearFilter = document.getElementById("year-filter");
    const resetFilters = document.getElementById("reset-filters");
    const filterToggle = document.getElementById("filter-toggle");
    const carsCount = document.getElementById("cars-count");

    if (brandFilter && modelFilter && priceFilter && yearFilter) {
        const carCards = document.querySelectorAll(
            ".all-cars-section .car-card"
        );

        const filters = [
            brandFilter,
            modelFilter,
            priceFilter,
            yearFilter
        ];

        function filterCars() {
            let visibleCars = 0;

            carCards.forEach(function (card) {
                const matchesBrand =
                    brandFilter.value === "all" ||
                    brandFilter.value === card.dataset.brand;

                const matchesModel =
                    modelFilter.value === "all" ||
                    modelFilter.value === card.dataset.model;

                const matchesYear =
                    yearFilter.value === "all" ||
                    yearFilter.value === card.dataset.year;

                const carPrice = Number(card.dataset.price);

                const matchesPrice =
                    priceFilter.value === "all" ||
                    (priceFilter.value === "low" && carPrice < 400000) ||
                    (priceFilter.value === "medium" &&
                        carPrice >= 400000 && carPrice <= 500000) ||
                    (priceFilter.value === "high" && carPrice > 500000);

                const isVisible =
                    matchesBrand &&
                    matchesModel &&
                    matchesPrice &&
                    matchesYear;

                card.style.display = isVisible ? "" : "none";

                if (isVisible) {
                    visibleCars++;
                }
            });

            if (carsCount) {
                carsCount.textContent = visibleCars + " Cars Found";
            }
        }

        filters.forEach(function (filter) {
            filter.addEventListener("change", filterCars);
        });

        if (resetFilters) {
            resetFilters.addEventListener("click", function () {
                filters.forEach(function (filter) {
                    filter.value = "all";
                });

                filterCars();
            });
        }

        if (filterToggle) {
            filterToggle.addEventListener("click", function () {
                const filtersContainer = document.querySelector(".cars-filters");

                if (!filtersContainer) return;

                const isExpanded = filtersContainer.classList.toggle("filters-expanded");

                filterToggle.setAttribute("aria-expanded", String(isExpanded));
            });
        }

        filterCars();
    }
});
