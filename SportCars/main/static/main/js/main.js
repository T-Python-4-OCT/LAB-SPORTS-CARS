// ===== Safe localStorage helpers =====
function getSaved(key) {
  try { return localStorage.getItem(key); } catch (e) { return null; }
}
function save(key, value) {
  try { localStorage.setItem(key, value); } catch (e) {}
}

// ===== Dark mode =====
const root = document.documentElement;
const themeIcon = document.getElementById('themeIcon');

function updateThemeIcon() {
  themeIcon.textContent = root.dataset.theme === 'dark' ? 'dark_mode' : 'light_mode';
}
updateThemeIcon();

document.getElementById('themeToggle').addEventListener('click', () => {
  const isDark = root.dataset.theme === 'dark';
  if (isDark) delete root.dataset.theme;
  else root.dataset.theme = 'dark';
  save('theme', isDark ? 'light' : 'dark');
  updateThemeIcon();
});

// ===== Mobile menu =====
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');

menuToggle.addEventListener('click', () => {
  const open = navLinks.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', open);
  menuToggle.querySelector('span').textContent = open ? 'close' : 'menu';
});

// ===== Reveal on scroll =====
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

// ===== Wishlist =====
let wishlist = [];
try { wishlist = JSON.parse(getSaved('wishlist')) || []; } catch (e) {}

document.querySelectorAll('[data-wishlist]').forEach((button) => {
  const slug = button.dataset.wishlist;
  button.setAttribute('aria-pressed', wishlist.includes(slug));

  button.addEventListener('click', () => {
    if (wishlist.includes(slug)) wishlist = wishlist.filter((item) => item !== slug);
    else wishlist.push(slug);
    button.setAttribute('aria-pressed', wishlist.includes(slug));
    save('wishlist', JSON.stringify(wishlist));
  });
});

// ===== Filters (All Cars page) =====
const carGrid = document.getElementById('carGrid');

if (carGrid) {
  const brandFilter = document.getElementById('brandFilter');
  const priceFilter = document.getElementById('priceFilter');
  const yearFilter = document.getElementById('yearFilter');
  const cards = carGrid.querySelectorAll('.car-card');

  function applyFilters() {
    let count = 0;
    cards.forEach((card) => {
      const show =
        (!brandFilter.value || card.dataset.brand === brandFilter.value) &&
        (!priceFilter.value || Number(card.dataset.price) < Number(priceFilter.value)) &&
        (!yearFilter.value || card.dataset.year === yearFilter.value);
      card.hidden = !show;
      if (show) count++;
    });
    document.getElementById('carCount').textContent = count;
    document.getElementById('noResults').hidden = count > 0;
  }

  [brandFilter, priceFilter, yearFilter].forEach((select) => select.addEventListener('change', applyFilters));

  document.getElementById('resetFilters').addEventListener('click', () => {
    brandFilter.value = priceFilter.value = yearFilter.value = '';
    applyFilters();
  });
}

// ===== Image gallery (Detail page) =====
const galleryImage = document.getElementById('galleryImage');

if (galleryImage) {
  const thumbs = [...document.querySelectorAll('.thumb')];
  let current = 0;

  function showImage(index) {
    current = (index + thumbs.length) % thumbs.length;
    galleryImage.style.opacity = 0;
    setTimeout(() => {
      galleryImage.src = thumbs[current].querySelector('img').src;
      galleryImage.style.opacity = 1;
    }, 200);
    thumbs.forEach((thumb, i) => thumb.classList.toggle('active', i === current));
  }

  thumbs.forEach((thumb, i) => thumb.addEventListener('click', () => showImage(i)));
  document.getElementById('galleryPrev').addEventListener('click', () => showImage(current - 1));
  document.getElementById('galleryNext').addEventListener('click', () => showImage(current + 1));
}

// ===== Tabs (Detail page) =====
document.querySelectorAll('.tab').forEach((tab) => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab, .tab-panel').forEach((el) => el.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.tab).classList.add('active');
  });
});