document.querySelectorAll("[data-toggle]").forEach((button) => {
  const target = document.getElementById(button.dataset.toggle);
  button.addEventListener("click", () => {
    const open = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!open));
    if (target.id === "primary-nav") {
      target.classList.toggle("is-open", !open);
    } else {
      target.hidden = open;
      if (!open) target.querySelector("input").focus();
    }
  });
});

const hero = document.querySelector("[data-hero]");
if (hero) {
  const photos = [...hero.querySelectorAll(".hero-image")];
  const dots = [...hero.querySelectorAll(".hero-dots button")];
  const video = hero.querySelector("[data-hero-video]");
  const toggle = hero.querySelector("[data-hero-playback]");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let pausedByUser = navigator.connection?.saveData === true;
  let heroVisible = true;

  function updateControl() {
    toggle.dataset.playing = String(!video.paused);
    toggle.setAttribute("aria-label", video.paused ? toggle.dataset.play : toggle.dataset.pause);
  }

  function syncVideo() {
    if (!video) return;
    const enabled = video.classList.contains("is-active") && !reducedMotion.matches && heroVisible && !document.hidden;
    toggle.hidden = !enabled;
    if (!enabled || pausedByUser) {
      video.pause();
      return;
    }
    if (!video.hasAttribute("src")) {
      const mobile = window.matchMedia("(max-width: 680px)").matches;
      video.src = mobile ? video.dataset.mobile : video.dataset.desktop;
    }
    video.play().catch(updateControl);
  }

  dots.forEach((dot, index) => {
    dot.addEventListener("click", () => {
      photos.forEach((photo, number) => photo.classList.toggle("is-active", index === number));
      dots.forEach((item, number) => item.setAttribute("aria-pressed", String(index === number)));
      syncVideo();
    });
  });

  if (video) {
    toggle.addEventListener("click", () => {
      pausedByUser = !video.paused;
      syncVideo();
    });
    video.addEventListener("play", updateControl);
    video.addEventListener("pause", updateControl);
    reducedMotion.addEventListener("change", syncVideo);
    document.addEventListener("visibilitychange", syncVideo);
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(entries => {
        heroVisible = entries[0].isIntersecting;
        syncVideo();
      });
      observer.observe(hero);
    }
    syncVideo();
  }
}

const gallery = document.querySelector("[data-gallery]");
if (gallery) {
  const image = gallery.querySelector("[data-gallery-image]");
  const photos = [...gallery.querySelectorAll("[data-gallery-photo]")];
  const status = gallery.querySelector("[data-gallery-status]");
  const dialog = gallery.querySelector("[data-gallery-dialog]");
  const expand = gallery.querySelector("[data-gallery-open]");
  const fullImage = dialog.querySelector("[data-full-image]");
  const caption = dialog.querySelector("[data-full-caption]");
  let current = 0;

  function syncDialog() {
    fullImage.src = image.src;
    fullImage.alt = image.alt;
    caption.textContent = (current + 1) + " / " + photos.length + " · " + image.alt;
  }

  expand.addEventListener("click", () => {
    syncDialog();
    dialog.showModal();
  });

  dialog.addEventListener("keydown", (event) => {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
    event.preventDefault();
    showPhoto(current + (event.key === "ArrowLeft" ? -1 : 1));
  });

  let touchStart;
  fullImage.addEventListener("touchstart", (event) => {
    touchStart = event.changedTouches[0].clientX;
  }, {passive: true});
  fullImage.addEventListener("touchend", (event) => {
    if (touchStart === undefined) return;
    const distance = event.changedTouches[0].clientX - touchStart;
    touchStart = undefined;
    if (Math.abs(distance) > 45) showPhoto(current + (distance > 0 ? -1 : 1));
  }, {passive: true});
  fullImage.addEventListener("touchcancel", () => { touchStart = undefined; });

  function showPhoto(index) {
    current = (index + photos.length) % photos.length;
    const photo = photos[current];
    image.src = photo.dataset.galleryPhoto;
    image.alt = photo.getAttribute("aria-label");
    if (dialog.open) syncDialog();
    status.textContent = (current + 1) + " / " + photos.length + " · " + image.alt;
    photos.forEach((item, number) => item.setAttribute("aria-pressed", String(current === number)));
  }

  photos.forEach((photo, index) => photo.addEventListener("click", () => showPhoto(index)));
  gallery.querySelectorAll("[data-gallery-step]").forEach((button) => {
    button.addEventListener("click", () => showPhoto(current + Number(button.dataset.galleryStep)));
  });
}

const wishlistKey = "ford-wishlist";
const accountFavorites = JSON.parse(document.getElementById("account-favorites").textContent);
let savedCars = new Set(accountFavorites || []);
if (accountFavorites === null) {
  try {
    const saved = JSON.parse(localStorage.getItem(wishlistKey) || "[]");
    if (Array.isArray(saved)) savedCars = new Set(saved.filter(slug => typeof slug === "string"));
  } catch { /* Browser storage is optional. */ }
}
function renderWishlist() {
  document.querySelectorAll("[data-wishlist]").forEach(button => {
    const saved = savedCars.has(button.dataset.wishlist);
    button.setAttribute("aria-pressed", String(saved));
    const label = button.querySelector("[data-wishlist-label]");
    if (label) label.textContent = saved ? document.body.dataset.wishlistSaved : document.body.dataset.wishlistSave;
  });
}
renderWishlist();
document.querySelectorAll("[data-wishlist]").forEach(button => {
  button.addEventListener("click", async () => {
    const slug = button.dataset.wishlist;
    const saved = !savedCars.has(slug);
    if (accountFavorites !== null) {
      document.querySelectorAll("[data-wishlist]").forEach(item => { item.disabled = true; });
      try {
        const endpoint = document.querySelector("[data-favorite-endpoint]");
        const response = await fetch(endpoint.dataset.favoriteEndpoint, {
          method: "POST",
          headers: {"X-CSRFToken": endpoint.querySelector("[name=csrfmiddlewaretoken]").value},
          body: new URLSearchParams({car: slug, saved: String(saved)}),
        });
        if (!response.ok) throw new Error("Favorite save failed");
        if (saved) savedCars.add(slug);
        else savedCars.delete(slug);
      } catch {
        window.alert(document.documentElement.lang === "ar"
          ? "تعذر حفظ المفضلة. حاول مجددًا." : "Unable to save your favorite. Please try again.");
      } finally {
        document.querySelectorAll("[data-wishlist]").forEach(item => { item.disabled = false; });
      }
    } else {
      if (saved) savedCars.add(slug);
      else savedCars.delete(slug);
      try { localStorage.setItem(wishlistKey, JSON.stringify([...savedCars])); } catch { /* Optional storage. */ }
    }
    renderWishlist();
  });
});

const newsletter = document.querySelector("[data-demo-newsletter]");
if (newsletter) {
  newsletter.addEventListener("submit", (event) => {
    event.preventDefault();
    newsletter.parentElement.querySelector("[role=status]").textContent = newsletter.dataset.success;
    newsletter.reset();
  });
}


const installments = document.querySelector("[data-installments]");
if (installments) {
  const fields = installments.elements;
  const price = Number(installments.dataset.price);
  const output = installments.querySelector("output");
  const arabic = document.documentElement.lang === "ar";
  const currency = new Intl.NumberFormat(arabic ? "ar-SA-u-nu-latn" : "en-SA", {
    style: "currency", currency: "SAR", currencyDisplay: arabic ? "symbol" : "code",
  });

  function updateEstimate() {
    if (!installments.checkValidity()) {
      output.textContent = installments.dataset.invalid;
      return;
    }
    const financed = price - fields.down.valueAsNumber;
    const months = Number(fields.months.value);
    const monthlyRate = fields.rate.valueAsNumber / 1200;
    const payment = monthlyRate === 0
      ? financed / months
      : financed * monthlyRate / (1 - (1 + monthlyRate) ** -months);
    output.textContent = installments.dataset.monthly.replace("{amount}", currency.format(payment));
  }

  installments.addEventListener("submit", (event) => {
    event.preventDefault();
    updateEstimate();
  });
  installments.addEventListener("input", updateEstimate);
  updateEstimate();
}


const actionLinks = [...document.querySelectorAll("[data-action-link]")];
if (actionLinks.length) {
  function syncActions() {
    const selected = actionLinks.find((link) => link.hash === window.location.hash);
    if (selected) {
      const panel = document.getElementById(selected.getAttribute("aria-controls"));
      requestAnimationFrame(() => {
        panel.scrollIntoView({
          block: "start",
          behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth",
        });
        panel.focus({preventScroll: true});
      });
    }
    actionLinks.forEach((link) => {
      const panel = document.getElementById(link.getAttribute("aria-controls"));
      if (window.location.hash) panel.classList.remove("is-active");
      link.setAttribute("aria-expanded", String(
        link.hash === window.location.hash || panel.classList.contains("is-active")
      ));
    });
  }
  syncActions();
  window.addEventListener("hashchange", syncActions);
}

document.querySelectorAll("[data-preserve-hash]").forEach((form) => {
  form.addEventListener("submit", () => {
    const next = form.elements.namedItem("next");
    next.value = next.value.split("#")[0] + window.location.hash;
  });
});

const inventoryFilters = document.querySelector("[data-inventory-filters]");
if (inventoryFilters) {
  try {
    const params = new URLSearchParams(location.search);
    const names = ["q", "brand", "model", "price", "year"];
    const explicit = names.some(name => params.has(name)) || params.has("reset");
    if (!explicit && !params.size) {
      const saved = sessionStorage.getItem("ford-filters");
      if (saved) location.replace(location.pathname + "?" + saved + location.hash);
    } else {
      const remembered = new URLSearchParams();
      names.forEach(name => { if (params.get(name)) remembered.set(name, params.get(name)); });
      sessionStorage.setItem("ford-filters", remembered.toString());
    }
  } catch { /* Filters continue to work without storage. */ }
  inventoryFilters.addEventListener("change", (event) => {
    if (event.target.matches("select")) inventoryFilters.requestSubmit();
  });
}

const compareTray = document.querySelector("[data-compare-tray]");
if (compareTray) {
  const compareForm = document.querySelector("#compare form");
  const fields = [...compareForm.querySelectorAll('select[name="compare"]')];
  const choices = new Map([...fields[0].options].filter(option => option.value)
    .map(option => [option.value, option.textContent.trim()]));
  const buttons = [...document.querySelectorAll("[data-compare-card]")];
  const list = compareTray.querySelector("[data-compare-selection]");
  const status = compareTray.querySelector("[data-compare-status]");
  const submit = compareTray.querySelector("[data-compare-submit]");
  const storageKey = "ford-compare";
  let selectedCars = [];
  try {
    const stored = JSON.parse(localStorage.getItem(storageKey) || "null");
    const saved = stored && stored.expires > Date.now() && Array.isArray(stored.cars) ? stored.cars : [];
    if (!saved.length) localStorage.removeItem(storageKey);
    sessionStorage.removeItem(storageKey);
    if (Array.isArray(saved)) selectedCars = [...new Set(saved.filter(slug => choices.has(slug)))].slice(0, 2);
  } catch {
    // The selection still works on this page.
  }
  const compared = fields.map(field => field.value);
  if (compared.every(slug => choices.has(slug)) && compared[0] !== compared[1]) {
    selectedCars = compared;
  }

  function renderComparison() {
    compareTray.hidden = selectedCars.length === 0;
    submit.disabled = selectedCars.length !== 2;
    list.replaceChildren(...selectedCars.map(slug => {
      const item = document.createElement("li");
      const name = document.createElement("bdi");
      name.textContent = choices.get(slug);
      const remove = document.createElement("button");
      remove.type = "button";
      remove.textContent = "×";
      remove.setAttribute("aria-label", compareTray.dataset.remove + " — " + choices.get(slug));
      remove.addEventListener("click", () => {
        selectedCars = selectedCars.filter(car => car !== slug);
        renderComparison();
      });
      item.append(name, remove);
      return item;
    }));
    status.textContent = selectedCars.map(slug => choices.get(slug)).join(" · ");
    buttons.forEach(button => {
      const slug = button.dataset.compareCard;
      const selected = selectedCars.includes(slug);
      const label = selected ? button.dataset.remove : button.dataset.add;
      button.hidden = false;
      button.disabled = !selected && selectedCars.length === 2;
      button.setAttribute("aria-pressed", String(selected));
      button.setAttribute("aria-label", label + " — " + choices.get(slug));
      button.querySelector("span").textContent = label;
    });
    try {
      const stored = JSON.parse(localStorage.getItem(storageKey) || "null");
      const expires = stored && stored.expires > Date.now() ? stored.expires : Date.now() + 172800000;
      localStorage.setItem(storageKey, JSON.stringify({cars: selectedCars, expires}));
    } catch {
      // Storage is optional.
    }
  }

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const slug = button.dataset.compareCard;
      if (selectedCars.includes(slug)) selectedCars = selectedCars.filter(item => item !== slug);
      else if (selectedCars.length < 2) selectedCars.push(slug);
      renderComparison();
    });
  });
  compareTray.querySelector("[data-compare-clear]").addEventListener("click", () => {
    selectedCars = [];
    renderComparison();
  });
  submit.addEventListener("click", () => {
    fields.forEach((field, index) => { field.value = selectedCars[index]; });
    compareForm.requestSubmit();
  });
  renderComparison();
}

const generations = document.querySelector("[data-generations]");
if (generations) {
  const links = [...generations.querySelectorAll("[data-generation-link]")];
  const panels = [...generations.querySelectorAll("[data-generation-panel]")];
  function showGeneration(link) {
    links.forEach(item => {
      if (item === link) item.setAttribute("aria-current", "true");
      else item.removeAttribute("aria-current");
    });
    panels.forEach(panel => { panel.hidden = "#" + panel.id !== link.hash; });
  }
  const initial = links.find(link => link.hash === window.location.hash)
    || links.find(link => link.hasAttribute("aria-current")) || links[0];
  showGeneration(initial);
  links.forEach(link => link.addEventListener("click", event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    showGeneration(link);
  }));
}

const differences = document.querySelector("[data-differences-only]");
if (differences) {
  const rows = [...document.querySelectorAll(".comparison-table tbody tr")];
  const matching = rows.filter(row => {
    const cells = [...row.querySelectorAll("td")];
    return cells.length === 2 && cells[0].textContent.trim() === cells[1].textContent.trim();
  });
  document.querySelector("[data-difference-control]").hidden = false;
  function showDifferences() {
    matching.forEach(row => { row.hidden = differences.checked; });
    document.querySelector("[data-no-differences]").hidden = !differences.checked || matching.length !== rows.length;
  }
  differences.addEventListener("change", showDifferences);
  showDifferences();
}

const recentSection = document.querySelector("[data-recent-cars]");
if (recentSection) {
  try {
    const now = Date.now();
    const stored = JSON.parse(localStorage.getItem("ford-recent") || "[]");
    const current = recentSection.dataset.currentCar;
    const candidates = new Map([...recentSection.querySelectorAll("[data-recent-slug]")]
      .map(card => [card.dataset.recentSlug, card]));
    const recent = Array.isArray(stored) ? stored.filter(item =>
      item && typeof item.slug === "string" && item.expires > now && item.slug !== current) : [];
    const visible = recent.filter(item => candidates.has(item.slug)).slice(0, 3);
    visible.forEach(item => {
      const card = candidates.get(item.slug);
      card.hidden = false;
      recentSection.querySelector(".recent-grid").append(card);
    });
    recentSection.hidden = visible.length === 0;
    localStorage.setItem("ford-recent", JSON.stringify([
      {slug: current, expires: now + 604800000}, ...recent,
    ].slice(0, 10)));
  } catch { /* Recent history is optional. */ }
}

const themeForm = document.querySelector("[data-theme-form]");
if (themeForm && window.fetch) {
  const button = themeForm.querySelector('[name="theme"]');
  let themeTimer;
  themeForm.addEventListener("submit", async event => {
    event.preventDefault();
    if (button.disabled) return;
    const theme = button.value;
    const data = new FormData(themeForm);
    data.set("theme", theme);
    button.disabled = true;
    button.setAttribute("aria-busy", "true");
    try {
      const response = await fetch(themeForm.action, {
        method: "POST",
        headers: {"Accept": "application/json"},
        body: data,
      });
      if (!response.ok) throw new Error("Unable to save theme");
      const result = await response.json();
      if (result.theme !== theme) throw new Error("Unexpected theme");
      clearTimeout(themeTimer);
      document.documentElement.classList.add("theme-changing");
      // Commit the initial colors before applying the next theme.
      getComputedStyle(document.body).backgroundColor;
      document.documentElement.dataset.theme = theme;
      button.value = theme === "dark" ? "light" : "dark";
      button.setAttribute("aria-label", theme === "dark" ? themeForm.dataset.light : themeForm.dataset.dark);
      themeTimer = setTimeout(() => document.documentElement.classList.remove("theme-changing"), 240);
    } catch {
      // Preserve the original form flow if the enhanced request fails.
      const fallback = document.createElement("input");
      fallback.type = "hidden";
      fallback.name = "theme";
      fallback.value = theme;
      themeForm.append(fallback);
      HTMLFormElement.prototype.submit.call(themeForm);
    } finally {
      button.disabled = false;
      button.removeAttribute("aria-busy");
    }
  });
}
