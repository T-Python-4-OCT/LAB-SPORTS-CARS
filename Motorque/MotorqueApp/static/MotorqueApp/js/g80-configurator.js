
const g80Images = {
    Glossy: {
        Sport: {
            UyuniWhite: "G80-GlossyUyuniWhiteSP.avif",
            VikBlack: "G80-GlossyVikBlackSP.avif"
        },
        Standard: {
            UyuniWhite: "G80-GlossyUyuniWhiteST.avif",
            VikBlack: "G80-GlossyVikBlackST.avif"
        }
    },

    Matte: {
        Sport: {
            MakaluGray: "G80-MatteMakaluGraySP.avif",
            VerbierWhite: "G80-MatteVerbierWhiteSP.avif"
        },
        Standard: {
            MakaluGray: "G80-MatteMakaluGrayST.avif",
            VerbierWhite: "G80-MatteVerbierWhiteST.avif"
        }
    }
};

let selectedTrim = "Standard";
let selectedFinish = "Glossy";
let selectedColor = "UyuniWhite";

const carImage = document.getElementById("g80-car-image");

function updateG80Configurator() {
    const availableColors =
        g80Images[selectedFinish][selectedTrim];

    // If the selected color is unavailable, choose the first available color.
    if (!availableColors[selectedColor]) {
        selectedColor = Object.keys(availableColors)[0];
    }

    // Update the car image.
    carImage.src =
        `/static/MotorqueApp/images/G80/${selectedFinish}/${selectedTrim}/${availableColors[selectedColor]}`;

    carImage.alt =
        `Genesis G80 ${selectedTrim} ${selectedFinish} ${selectedColor}`;

    // Update button appearance and availability.
    document.querySelectorAll("[data-trim]").forEach(button => {
        button.classList.toggle(
            "active",
            button.dataset.trim === selectedTrim
        );
    });

    document.querySelectorAll("[data-finish]").forEach(button => {
        button.classList.toggle(
            "active",
            button.dataset.finish === selectedFinish
        );
    });

    document.querySelectorAll("[data-color]").forEach(button => {
        const color = button.dataset.color;
        const isAvailable = Boolean(availableColors[color]);

        button.disabled = !isAvailable;
        button.classList.toggle(
            "active",
            color === selectedColor
        );
    });
}

// Trim selection.
document.querySelectorAll("[data-trim]").forEach(button => {
    button.addEventListener("click", () => {
        selectedTrim = button.dataset.trim;
        updateG80Configurator();
    });
});

// Finish selection.
document.querySelectorAll("[data-finish]").forEach(button => {
    button.addEventListener("click", () => {
        selectedFinish = button.dataset.finish;
        updateG80Configurator();
    });
});

// Color selection.
document.querySelectorAll("[data-color]").forEach(button => {
    button.addEventListener("click", () => {
        if (!button.disabled) {
            selectedColor = button.dataset.color;
            updateG80Configurator();
        }
    });
});

// Initialize configurator.
updateG80Configurator();
