
document.addEventListener("DOMContentLoaded", () => {

    // ========================================
    // ELEMENTS
    // ========================================

    const modal = document.getElementById(
        "inquiry-modal"
    );

    const openButton = document.getElementById(
        "open-inquiry-modal"
    );

    const closeButton = document.getElementById(
        "close-inquiry-modal"
    );

    const dialog = modal?.querySelector(
        ".inquiry-modal-dialog"
    );

    const form = document.getElementById(
        "inquiry-form"
    );

    if (!modal || !openButton || !closeButton || !dialog) {
        return;
    }

    let previousFocus = null;


    // ========================================
    // OPEN MODAL
    // ========================================

    function openModal() {

        if (!modal.hidden) {
            return;
        }

        previousFocus = document.activeElement;

        modal.hidden = false;

        document.body.classList.add(
            "inquiry-modal-open"
        );

        dialog.scrollTop = 0;

        closeButton.focus();
    }


    // ========================================
    // CLOSE MODAL
    // ========================================

    function closeModal() {

        if (modal.hidden) {
            return;
        }

        modal.hidden = true;

        document.body.classList.remove(
            "inquiry-modal-open"
        );

        if (
            previousFocus &&
            typeof previousFocus.focus === "function" &&
            previousFocus.isConnected
        ) {
            previousFocus.focus();
        } else {
            openButton.focus();
        }

    }


    // ========================================
    // BUTTON EVENTS
    // ========================================

    openButton.addEventListener(
        "click",
        openModal
    );

    closeButton.addEventListener(
        "click",
        closeModal
    );


    // ========================================
    // BACKDROP CLICK
    // ========================================

    modal.addEventListener("click", event => {

        if (
            event.target.hasAttribute(
                "data-close-inquiry"
            )
        ) {
            closeModal();
        }

    });


    // ========================================
    // KEYBOARD HANDLING
    // ========================================

    document.addEventListener("keydown", event => {

        if (modal.hidden) {
            return;
        }

        // ESC closes the modal.
        if (event.key === "Escape") {
            event.preventDefault();

            closeModal();
            return;
        }

        // Keep Tab navigation inside the dialog.
        if (event.key !== "Tab") {
            return;
        }

        const focusableElements = Array.from(
            dialog.querySelectorAll(
                'a[href], button:not([disabled]), ' +
                'input:not([disabled]), ' +
                'textarea:not([disabled]), ' +
                'select:not([disabled]), ' +
                '[tabindex]:not([tabindex="-1"])'
            )
        ).filter(element => {
            return element.getClientRects().length > 0;
        });

        if (focusableElements.length === 0) {
            event.preventDefault();
            dialog.focus();
            return;
        }

        const first = focusableElements[0];
        const last = focusableElements[
            focusableElements.length - 1
        ];

        if (
            event.shiftKey &&
            (document.activeElement === first ||
             document.activeElement === dialog)
        ) {
            event.preventDefault();
            last.focus();
        }

        else if (
            !event.shiftKey &&
            document.activeElement === last
        ) {
            event.preventDefault();
            first.focus();
        }

    });


    // ========================================
    // SUBMIT BUTTON STATE
    // ========================================

    if (form) {

        form.addEventListener("submit", event => {

            // Browser validation happens before submit.
            if (!form.checkValidity()) {
                return;
            }

            const submitButton = document.getElementById(
                "inquiry-submit"
            );

            if (submitButton) {
                submitButton.disabled = true;

                submitButton.innerHTML = `
                    <span class="material-symbols-outlined">
                        hourglass_top
                    </span>
                    SENDING...
                `;
            }

        });

    }


    // ========================================
    // DJANGO SUCCESS / VALIDATION ERRORS
    // ========================================

    const successMessage = modal.querySelector(
        "[data-inquiry-success]"
    );

    const validationErrors = modal.querySelector(
        ".inquiry-field-error, .inquiry-form-errors"
    );

    // Django redirects back to this page after a
    // successful POST. Reopen to show confirmation.
    if (successMessage || validationErrors) {

        openModal();

        if (validationErrors) {
            const firstInvalidField = modal.querySelector(
                '[aria-invalid="true"], .inquiry-field input, .inquiry-field textarea'
            );

            if (firstInvalidField) {
                firstInvalidField.focus({
                    preventScroll: true
                });
            }
        }

    }

});
