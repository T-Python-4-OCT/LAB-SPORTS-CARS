
document.addEventListener("DOMContentLoaded", () => {

    // ========================================
    // CUSTOM SELECT DROPDOWNS
    // ========================================

    const selects = document.querySelectorAll(
        "select[data-custom-select]"
    );

    const dropdowns = [];

    // ========================================
    // CLOSE ALL DROPDOWNS
    // ========================================

    function closeAll(except = null) {

        dropdowns.forEach(dropdown => {

            if (dropdown === except) {
                return;
            }

            dropdown.close();

        });

    }


    // ========================================
    // CREATE EACH DROPDOWN
    // ========================================

    selects.forEach((select, index) => {

        const field = select.closest(".filter-field");

        if (!field) {
            return;
        }

        const wrapper = document.createElement("div");
        wrapper.className = "custom-select";

        // Trigger button
        const trigger = document.createElement("button");

        trigger.type = "button";
        trigger.className = "custom-select__trigger";
        trigger.setAttribute("aria-haspopup", "listbox");
        trigger.setAttribute("aria-expanded", "false");

        const label = document.createElement("span");
        label.className = "custom-select__value";

        const chevron = document.createElement("span");
        chevron.className = "custom-select__chevron";

        const chevronIcon = document.createElement("span");
        chevronIcon.className = "material-symbols-outlined";
        chevronIcon.textContent = "keyboard_arrow_down";
        chevronIcon.setAttribute("aria-hidden", "true");

        chevron.appendChild(chevronIcon);

        trigger.appendChild(label);
        trigger.appendChild(chevron);

        // Options list
        const menu = document.createElement("div");

        menu.className = "custom-select__menu";
        menu.id = `custom-select-menu-${index}`;
        menu.setAttribute("role", "listbox");
        menu.setAttribute("aria-label", select.name);

        trigger.setAttribute(
            "aria-controls",
            menu.id
        );

        const nativeOptions = Array.from(select.options);
        const optionButtons = [];

        let isOpen = false;

        // ========================================
        // UPDATE VISUAL SELECTION
        // ========================================

        function updateSelected() {

            const selectedOption =
                select.options[select.selectedIndex];

            label.textContent = selectedOption
                ? selectedOption.textContent.trim()
                : "Select option";

            optionButtons.forEach((button, i) => {

                const selected =
                    nativeOptions[i].value === select.value;

                button.classList.toggle(
                    "is-selected",
                    selected
                );

                button.setAttribute(
                    "aria-selected",
                    String(selected)
                );

            });

        }


        // ========================================
        // CLOSE DROPDOWN
        // ========================================

        function close() {

            if (!isOpen) {
                return;
            }

            isOpen = false;

            wrapper.classList.remove("is-open");
            field.classList.remove("dropdown-open");

            trigger.setAttribute(
                "aria-expanded",
                "false"
            );

        }


        // ========================================
        // OPEN DROPDOWN
        // ========================================

        function open(focusSelected = false) {

            closeAll(dropdown);

            isOpen = true;

            wrapper.classList.add("is-open");
            field.classList.add("dropdown-open");

            trigger.setAttribute(
                "aria-expanded",
                "true"
            );

            if (focusSelected) {
                const selectedButton =
                    optionButtons[select.selectedIndex];

                if (selectedButton) {
                    selectedButton.focus();
                }
            }

        }


        // ========================================
        // CHOOSE OPTION
        // ========================================

        function chooseOption(option, button) {

            const oldValue = select.value;

            select.value = option.value;

            updateSelected();
            close();

            trigger.focus();

            if (oldValue !== select.value) {
                select.dispatchEvent(
                    new Event("change", {
                        bubbles: true
                    })
                );
            }

        }


        // ========================================
        // BUILD OPTION BUTTONS
        // ========================================

        nativeOptions.forEach((option, optionIndex) => {

            const button = document.createElement("button");

            button.type = "button";
            button.className = "custom-select__option";
            button.setAttribute("role", "option");
            button.setAttribute("aria-selected", "false");

            const optionLabel =
                document.createElement("span");

            optionLabel.className =
                "custom-select__option-label";

            optionLabel.textContent =
                option.textContent.trim();

            const check = document.createElement("span");

            check.className = "custom-select__check";
            check.setAttribute("aria-hidden", "true");

            const checkIcon = document.createElement("span");
            checkIcon.className = "material-symbols-outlined";
            checkIcon.textContent = "check";

            check.appendChild(checkIcon);

            button.appendChild(optionLabel);
            button.appendChild(check);

            button.addEventListener("click", () => {
                chooseOption(option, button);
            });

            // Keyboard controls
            button.addEventListener("keydown", event => {

                let nextIndex = optionIndex;

                if (event.key === "ArrowDown") {
                    event.preventDefault();

                    nextIndex =
                        (optionIndex + 1) % optionButtons.length;
                }

                else if (event.key === "ArrowUp") {
                    event.preventDefault();

                    nextIndex =
                        (optionIndex - 1 + optionButtons.length)
                        % optionButtons.length;
                }

                else if (event.key === "Home") {
                    event.preventDefault();
                    nextIndex = 0;
                }

                else if (event.key === "End") {
                    event.preventDefault();
                    nextIndex = optionButtons.length - 1;
                }

                else if (event.key === "Escape") {
                    event.preventDefault();

                    close();
                    trigger.focus();
                    return;
                }

                else if (event.key === "Tab") {
                    close();
                    return;
                }

                else {
                    return;
                }

                optionButtons[nextIndex]?.focus();

            });

            optionButtons.push(button);
            menu.appendChild(button);

        });


        // ========================================
        // TRIGGER EVENTS
        // ========================================

        trigger.addEventListener("click", () => {

            if (isOpen) {
                close();
            } else {
                open(false);
            }

        });


        trigger.addEventListener("keydown", event => {

            if (
                event.key === "ArrowDown" ||
                event.key === "ArrowUp"
            ) {
                event.preventDefault();

                open(true);
            }

            if (event.key === "Escape") {
                close();
            }

        });


        // ========================================
        // INSERT ELEMENTS
        // ========================================

        wrapper.appendChild(trigger);
        wrapper.appendChild(menu);

        // Keep original select for Django GET form.
        select.insertAdjacentElement(
            "afterend",
            wrapper
        );

        select.classList.add(
            "native-select-enhanced"
        );

        select.tabIndex = -1;

        // Connect original label to custom button.
        const fieldLabel = field.querySelector("label");

        if (fieldLabel) {
            trigger.setAttribute(
                "aria-label",
                fieldLabel.textContent.trim()
            );

            fieldLabel.addEventListener("click", event => {
                event.preventDefault();

                trigger.focus();

                if (!isOpen) {
                    open();
                }
            });
        }

        // React if original select changes.
        select.addEventListener(
            "change",
            updateSelected
        );

        const dropdown = {
            close,
            open
        };

        dropdowns.push(dropdown);

        updateSelected();

    });


    // ========================================
    // CLOSE WHEN CLICKING OUTSIDE
    // ========================================

    document.addEventListener("pointerdown", event => {

        if (!event.target.closest(".custom-select")) {
            closeAll();
        }

    });


    // ========================================
    // CLOSE ON ESCAPE
    // ========================================

    document.addEventListener("keydown", event => {

        if (event.key === "Escape") {
            closeAll();
        }

    });

});
