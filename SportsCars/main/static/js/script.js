document.addEventListener("DOMContentLoaded", () => {


  const btn = document.getElementById("menuBtn");
  const links = document.getElementById("navLinks");

  if (btn && links) {
    const icon = btn.querySelector(".material-symbols-outlined");

    btn.addEventListener("click", () => {
      const open = links.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
      icon.textContent = open ? "close" : "menu";
    });

   
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        links.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
        icon.textContent = "menu";
      })
    );
  }

 
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.15 });
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

 
  document.querySelectorAll(".wish").forEach((b) =>
    b.addEventListener("click", () => b.classList.toggle("on"))
  );

 
  document.querySelectorAll(".wish-btn").forEach((b) =>
    b.addEventListener("click", () => b.classList.toggle("on"))
  );

 
  const mainImg = document.getElementById("mainImg");
  if (mainImg) {
    const thumbs = document.querySelectorAll(".thumb");
    thumbs.forEach((t) =>
      t.addEventListener("click", () => {
        thumbs.forEach((x) => x.classList.remove("active"));
        t.classList.add("active");
        mainImg.classList.add("fade");
        setTimeout(() => {
          mainImg.src = t.dataset.src;
          mainImg.classList.remove("fade");
        }, 200);
      })
    );
  }

});
