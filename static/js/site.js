(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  const savedTheme = localStorage.getItem('sportscars-theme');
  if (savedTheme === 'dark') root.dataset.theme = 'dark';
  const updateThemeIcon = () => {
    if (!themeButton) return;
    const icon = themeButton.querySelector('.material-symbols-rounded');
    icon.textContent = root.dataset.theme === 'dark' ? 'light_mode' : 'dark_mode';
  };
  updateThemeIcon();
  themeButton?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('sportscars-theme', root.dataset.theme);
    updateThemeIcon();
  });
  menuButton?.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
    menuButton.querySelector('.material-symbols-rounded').textContent = open ? 'close' : 'menu';
  });
  const backToTop = document.querySelector('.back-to-top');
  const updateBackToTop = () => backToTop?.classList.toggle('is-visible', window.scrollY > 360);
  updateBackToTop();
  window.addEventListener('scroll', updateBackToTop, { passive: true });
  backToTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  const favoriteKey = 'sportscars-favorites';
  const readFavorites = () => { try { return JSON.parse(localStorage.getItem(favoriteKey) || '[]'); } catch { return []; } };
  let favorites = readFavorites();
  const favoriteButtons = [...document.querySelectorAll('.favorite[data-favorite]')];
  const syncFavoriteButtons = () => favoriteButtons.forEach(button => {
    const saved = favorites.includes(button.dataset.favorite);
    button.classList.toggle('is-favorite', saved);
    button.setAttribute('aria-pressed', String(saved));
  });
  syncFavoriteButtons();
  favoriteButtons.forEach(button => button.addEventListener('click', () => {
    const slug = button.dataset.favorite;
    favorites = favorites.includes(slug) ? favorites.filter(item => item !== slug) : [...favorites, slug];
    localStorage.setItem(favoriteKey, JSON.stringify(favorites));
    syncFavoriteButtons();
    applyCarFilters();
  }));

  const heroImage = document.querySelector('[data-hero-image]');
  const heroSlides = [...document.querySelectorAll('[data-hero-slide]')];
  if (heroImage && heroSlides.length > 1) {
    const heroName = document.querySelector('[data-hero-name]');
    const heroCount = document.querySelector('[data-hero-count]');
    const heroLink = document.querySelector('[data-hero-link]');
    const hero = heroImage.closest('.hero');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let activeSlide = heroSlides.findIndex(slide => slide.getAttribute('aria-pressed') === 'true');
    let autoplay;
    const showHeroSlide = index => {
      activeSlide = (index + heroSlides.length) % heroSlides.length;
      const slide = heroSlides[activeSlide];
      heroImage.classList.add('is-changing');
      window.setTimeout(() => {
        heroImage.style.backgroundImage = `url("${slide.dataset.image}")`;
        heroImage.setAttribute('aria-label', `${slide.dataset.name} driving on the road`);
        heroName.textContent = slide.dataset.name;
        heroCount.textContent = String(activeSlide + 1).padStart(2, '0');
        heroLink.href = slide.dataset.url;
        heroSlides.forEach((item, itemIndex) => {
          const selected = itemIndex === activeSlide;
          item.classList.toggle('is-active', selected);
          item.setAttribute('aria-pressed', String(selected));
        });
        heroImage.classList.remove('is-changing');
      }, 180);
    };
    const stopAutoplay = () => window.clearInterval(autoplay);
    const startAutoplay = () => {
      stopAutoplay();
      if (!reducedMotion.matches && !document.hidden && !hero?.matches(':hover') && !hero?.contains(document.activeElement)) {
        autoplay = window.setInterval(() => showHeroSlide(activeSlide + 1), 5000);
      }
    };
    document.querySelector('[data-hero-prev]')?.addEventListener('click', () => { showHeroSlide(activeSlide - 1); startAutoplay(); });
    document.querySelector('[data-hero-next]')?.addEventListener('click', () => { showHeroSlide(activeSlide + 1); startAutoplay(); });
    heroSlides.forEach((slide, index) => slide.addEventListener('click', () => { showHeroSlide(index); startAutoplay(); }));
    hero?.addEventListener('mouseenter', stopAutoplay);
    hero?.addEventListener('mouseleave', startAutoplay);
    hero?.addEventListener('focusin', stopAutoplay);
    hero?.addEventListener('focusout', event => { if (!hero.contains(event.relatedTarget)) startAutoplay(); });
    document.addEventListener('visibilitychange', startAutoplay);
    reducedMotion.addEventListener?.('change', startAutoplay);
    startAutoplay();
  }

  const searchInput = document.querySelector('#car-search');
  const brandFilter = document.querySelector('#brand-filter');
  const sortSelect = document.querySelector('#car-sort');
  const favoritesFilter = document.querySelector('.favorites-filter');
  const carGrid = document.querySelector('#cars-grid');
  const resultCount = document.querySelector('.result-count');
  let onlyFavorites = false;
  function applyCarFilters() {
    if (!carGrid) return;
    const query = (searchInput?.value || '').trim().toLocaleLowerCase();
    const brand = brandFilter?.value || '';
    const cards = [...carGrid.querySelectorAll('.car-card')];
    cards.forEach(card => {
      const slug = card.querySelector('[data-favorite]')?.dataset.favorite;
      card.hidden = !(card.dataset.name.includes(query) && (!brand || card.dataset.brand === brand) && (!onlyFavorites || favorites.includes(slug)));
    });
    const visible = cards.filter(card => !card.hidden);
    if (resultCount) resultCount.textContent = `(${visible.length})`;
    const empty = document.querySelector('.no-cars');
    if (empty) empty.hidden = visible.length > 0;
    const mode = sortSelect?.value || 'default';
    const key = mode.startsWith('price') ? 'price' : mode === 'power-high' ? 'power' : '';
    if (key) visible.sort((a, b) => (Number(a.dataset[key]) - Number(b.dataset[key])) * (mode === 'price-low' ? 1 : -1));
    (key ? visible : cards).forEach(card => carGrid.append(card));
  }
  searchInput?.addEventListener('input', applyCarFilters);
  brandFilter?.addEventListener('change', applyCarFilters);
  sortSelect?.addEventListener('change', applyCarFilters);
  favoritesFilter?.addEventListener('click', () => {
    onlyFavorites = !onlyFavorites;
    favoritesFilter.setAttribute('aria-pressed', String(onlyFavorites));
    favoritesFilter.classList.toggle('is-active', onlyFavorites);
    favoritesFilter.lastChild.textContent = onlyFavorites ? ' Show all cars' : ' Show favorites';
    applyCarFilters();
  });
  applyCarFilters();  document.querySelectorAll('[data-gallery]').forEach(gallery => {
    const image = gallery.querySelector('[data-gallery-image]');
    const thumbs = [...gallery.parentElement.querySelectorAll('[data-gallery-thumb]')];
    const counter = gallery.querySelector('[data-gallery-counter]');
    let index = 0;
    const showImage = nextIndex => {
      index = (nextIndex + thumbs.length) % thumbs.length;
      const thumb = thumbs[index];
      image.src = thumb.dataset.image;
      image.alt = image.alt.split(' - ')[0] + ' - ' + thumb.dataset.caption;
      counter.textContent = `${index + 1} / ${thumbs.length}`;
      thumbs.forEach((item, i) => {
        item.classList.toggle('is-active', i === index);
        item.setAttribute('aria-pressed', String(i === index));
      });
    };
    thumbs.forEach((thumb, i) => thumb.addEventListener('click', () => showImage(i)));
    gallery.querySelector('[data-gallery-prev]')?.addEventListener('click', () => showImage(index - 1));
    gallery.querySelector('[data-gallery-next]')?.addEventListener('click', () => showImage(index + 1));
    gallery.addEventListener('keydown', event => {
      if (event.key === 'ArrowLeft') showImage(index - 1);
      if (event.key === 'ArrowRight') showImage(index + 1);
    });
  });
  const revealObserver = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('in-view'); revealObserver.unobserve(entry.target); }
  }), { threshold: 0.12 });
  document.querySelectorAll('.section, .benefits, .story-content, .contact-strip').forEach(el => revealObserver.observe(el));
})();
