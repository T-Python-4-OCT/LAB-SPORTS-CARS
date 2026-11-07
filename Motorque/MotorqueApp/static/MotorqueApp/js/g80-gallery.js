
document.addEventListener("DOMContentLoaded", function () {

    const mainImage = document.getElementById("g80-car-image");
    const thumbnails = document.querySelectorAll(".g80-thumb");
    const thumbnailContainer = document.querySelector(".g80-thumbnails");

    const previousButton = document.querySelector(".g80-prev");
    const nextButton = document.querySelector(".g80-next");
    const counter = document.getElementById("g80-image-counter");

    let currentIndex = 0;

    const images = Array.from(thumbnails).map(button => {
        return button.dataset.image;
    });

    // عرض الصورة المختارة
    function showImage(index) {

        currentIndex = (index + images.length) % images.length;

        mainImage.style.opacity = "0";

        setTimeout(() => {
            mainImage.src = images[currentIndex];
            mainImage.style.opacity = "1";
        }, 120);

        // تحديث الصورة النشطة
        thumbnails.forEach((thumbnail, i) => {
            thumbnail.classList.toggle("active", i === currentIndex);
        });

        // تحديث عداد الصور
        counter.textContent =
            String(currentIndex + 1).padStart(2, "0") +
            " / " +
            String(images.length).padStart(2, "0");

        // تحريك شريط الصور لإظهار الصورة المختارة
        thumbnails[currentIndex].scrollIntoView({
            behavior: "smooth",
            block: "nearest",
            inline: "nearest"
        });
    }

    // التنقل عند المرور أو الضغط على الصور المصغرة
    thumbnails.forEach((thumbnail, index) => {

        thumbnail.addEventListener("mouseenter", () => {
            showImage(index);
        });

        thumbnail.addEventListener("click", () => {
            showImage(index);
        });

    });

    // زر الصورة السابقة
    previousButton.addEventListener("click", () => {
        showImage(currentIndex - 1);
    });

    // زر الصورة التالية
    nextButton.addEventListener("click", () => {
        showImage(currentIndex + 1);
    });

    // تحويل عجلة الماوس إلى تمرير أفقي
    thumbnailContainer.addEventListener("wheel", function (event) {

        if (Math.abs(event.deltaY) > Math.abs(event.deltaX)) {
            event.preventDefault();

            thumbnailContainer.scrollBy({
                left: event.deltaY,
                behavior: "auto"
            });
        }

    }, { passive: false });

    // إظهار الصورة الأولى عند تحميل الصفحة
    showImage(0);

});
