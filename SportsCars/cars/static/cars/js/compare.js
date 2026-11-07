
document.addEventListener("DOMContentLoaded", () => {

    // ========================================
    // COMPARE ELEMENTS
    // ========================================

    const compareForm = document.getElementById(
        "compare-selection-form"
    );

    if (!compareForm) {
        return;
    }

    const checkboxes = Array.from(
        compareForm.querySelectorAll(
            'input[type="checkbox"][name="cars"]'
        )
    );

    const compareCounter = document.getElementById(
        "compare-counter"
    );

    const compareMessage = document.getElementById(
        "compare-message"
    );

    const compareSubmit = document.getElementById(
        "compare-submit"
    );

    const MIN_CARS = 2;
    const MAX_CARS = 3;


    // ========================================
    // UPDATE SELECTED CARS
    // ========================================

    function updateSelection() {

        const selected = checkboxes.filter(
            checkbox => checkbox.checked
        );

        const selectedCount = selected.length;

        // Update selection counter
        if (compareCounter) {
            compareCounter.textContent =
                `${selectedCount} / ${MAX_CARS} SELECTED`;
        }

        // Disable unselected checkboxes at the limit
        checkboxes.forEach(checkbox => {

            const reachedLimit =
                selectedCount >= MAX_CARS;

            checkbox.disabled =
                reachedLimit && !checkbox.checked;

            // Highlight selected cards
            const card = checkbox.closest(".car-card");

            if (card) {
                card.classList.toggle(
                    "compare-card-selected",
                    checkbox.checked
                );
            }

        });

        // Enable compare button only when valid
        if (compareSubmit) {
            compareSubmit.disabled =
                selectedCount < MIN_CARS ||
                selectedCount > MAX_CARS;
        }

        // Update helper message
        if (compareMessage) {

            if (selectedCount === 0) {
                compareMessage.textContent =
                    "Select at least 2 cars to start comparing.";
            }

            else if (selectedCount === 1) {
                compareMessage.textContent =
                    "Select 1 more car to compare.";
            }

            else if (selectedCount === 2) {
                compareMessage.textContent =
                    "Ready to compare! You can also select one more car.";
            }

            else if (selectedCount === 3) {
                compareMessage.textContent =
                    "Maximum of 3 cars selected. You're ready to compare!";
            }

        }

    }


    // ========================================
    // CHECKBOX EVENTS
    // ========================================

    checkboxes.forEach(checkbox => {

        checkbox.addEventListener(
            "change",
            updateSelection
        );

    });


    // ========================================
    // FORM VALIDATION
    // ========================================

    compareForm.addEventListener("submit", event => {

        const selectedCount = checkboxes.filter(
            checkbox => checkbox.checked
        ).length;

        if (
            selectedCount < MIN_CARS ||
            selectedCount > MAX_CARS
        ) {
            event.preventDefault();
            updateSelection();
        }

    });


    // ========================================
    // INITIAL STATE
    // ========================================

    updateSelection();

});
