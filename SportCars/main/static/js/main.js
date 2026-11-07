// Small enhancements for SportCars. The site still works without JavaScript.
document.documentElement.classList.add("js");

const header = document.getElementById("site-header");

// Mobile menu
document.getElementById("menu-btn")?.addEventListener("click", () => {
    header.classList.toggle("menu-open");
});

// Search bar toggle
document.getElementById("search-btn")?.addEventListener("click", () => {
    header.classList.toggle("search-open");
    if (header.classList.contains("search-open")) {
        header.querySelector("#search-bar input").focus();
    }
});

// Reveal elements when they scroll into view
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll(".reveal").forEach((el, i) => {
    el.style.transitionDelay = `${(i % 4) * 80}ms`;
    revealObserver.observe(el);
});

// Count-up numbers (About page)
const countObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = Number(el.dataset.count);
        const start = performance.now();
        const step = (now) => {
            const progress = Math.min((now - start) / 1500, 1);
            el.textContent = Math.round(target * (1 - Math.pow(1 - progress, 3))).toLocaleString();
            if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        countObserver.unobserve(el);
    });
});
document.querySelectorAll("[data-count]").forEach((el) => countObserver.observe(el));

// Car detail gallery
document.querySelectorAll("[data-gallery]").forEach((gallery) => {
    const main = gallery.querySelector("[data-gallery-main]");
    const thumbs = [...gallery.querySelectorAll("[data-gallery-thumb]")];
    let current = 0;

    const show = (index) => {
        current = (index + thumbs.length) % thumbs.length;
        main.classList.add("switching");
        setTimeout(() => {
            main.src = thumbs[current].dataset.galleryThumb;
            main.classList.remove("switching");
        }, 200);
        thumbs.forEach((t, i) => t.classList.toggle("active", i === current));
    };

    thumbs.forEach((thumb, i) => thumb.addEventListener("click", () => show(i)));
    gallery.querySelector("[data-gallery-prev]")?.addEventListener("click", () => show(current - 1));
    gallery.querySelector("[data-gallery-next]")?.addEventListener("click", () => show(current + 1));
});

// Highlight the active tab while scrolling the car detail page
const tabLinks = [...document.querySelectorAll(".tabs a")];
if (tabLinks.length) {
    const tabObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                tabLinks.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === `#${entry.target.id}`));
            }
        });
    }, { rootMargin: "-40% 0px -55% 0px" });
    tabLinks.forEach((a) => {
        const section = document.querySelector(a.getAttribute("href"));
        if (section) tabObserver.observe(section);
    });
}

// Give the header a shadow once the page is scrolled
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 10);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Scroll progress bar + back-to-top button
const progress = document.getElementById("scroll-progress");
const toTop = document.getElementById("back-to-top");
const onScrollProgress = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.transform = `scaleX(${max > 0 ? window.scrollY / max : 0})`;
    toTop.classList.toggle("show", window.scrollY > 600);
};
window.addEventListener("scroll", onScrollProgress, { passive: true });
onScrollProgress();
toTop.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Hero slider: fades between the car photos every 5 seconds (dots switch manually)
document.querySelectorAll("[data-hero-slider]").forEach((slider) => {
    const slides = [...slider.querySelectorAll("img")];
    const dots = [...slider.querySelectorAll(".hero-dots button")];
    let current = 0;
    const show = (index) => {
        current = (index + slides.length) % slides.length;
        slides.forEach((img, i) => img.classList.toggle("active", i === current));
        dots.forEach((dot, i) => dot.classList.toggle("active", i === current));
    };
    dots.forEach((dot, i) => dot.addEventListener("click", () => { show(i); restart(); }));
    let timer;
    const restart = () => { clearInterval(timer); timer = setInterval(() => show(current + 1), 5000); };
    restart();
});
