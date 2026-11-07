(() => {
  'use strict';
  const root = document.documentElement;
  if (document.fonts) document.fonts.load('24px "Material Symbols Outlined"').then(fonts => {
    if (fonts.length) root.classList.add('google-icons-ready');
  }).catch(() => {  });
  const themeToggle = document.querySelector('.theme-toggle');
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  const preference = matchMedia('(prefers-color-scheme: dark)');
  const readStorage = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } };
  const writeStorage = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); } catch {  } };
  function syncTheme() {
    const dark = root.dataset.theme === 'dark';
    themeToggle?.setAttribute('aria-pressed', String(dark));
    themeToggle?.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
    themeMeta?.setAttribute('content', dark ? '#151515' : '#fbf9f8');
  }
  syncTheme();
  themeToggle?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('sportscars-theme', root.dataset.theme); } catch {  }
    syncTheme();
  });
  preference.addEventListener('change', () => {
    let saved; try { saved = localStorage.getItem('sportscars-theme'); } catch {  }
    if (!['dark', 'light'].includes(saved)) { root.dataset.theme = preference.matches ? 'dark' : 'light'; syncTheme(); }
  });
  window.addEventListener('storage', event => {
    if (event.key === 'sportscars-theme') { root.dataset.theme = ['dark', 'light'].includes(event.newValue) ? event.newValue : preference.matches ? 'dark' : 'light'; syncTheme(); }
  });

  const menuButton = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#mobile-nav');
  function closeMenu(focus = false) {
    if (!menu || !menuButton) return;
    menu.hidden = true; menuButton.setAttribute('aria-expanded', 'false'); menuButton.setAttribute('aria-label', 'Open navigation');
    if (focus) menuButton.focus();
  }
  menuButton?.addEventListener('click', () => {
    const open = menu.hidden; menu.hidden = !open; menuButton.setAttribute('aria-expanded', String(open)); menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  });
  menu?.querySelectorAll('a,button').forEach(link => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu && !menu.hidden) closeMenu(true); });
  matchMedia('(min-width:561px)').addEventListener('change', event => { if (event.matches) closeMenu(); });

  let toastTimer;
  function notify(message) {
    const toast = document.querySelector('.toast'); if (!toast) return;
    clearTimeout(toastTimer); toast.textContent = message; toast.hidden = false;
    toastTimer = setTimeout(() => { toast.hidden = true; }, 3500);
  }
  const storedWishlist = readStorage('sportscars-wishlist', []);
  let wishlist = new Set(Array.isArray(storedWishlist) ? storedWishlist.filter(slug => typeof slug === 'string') : []);
  function syncWishlist() {
    document.querySelectorAll('[data-wishlist]').forEach(button => {
      const saved = wishlist.has(button.dataset.wishlist);
      button.setAttribute('aria-pressed', String(saved));
      const label = button.querySelector('[data-wishlist-label]');
      if (label) label.textContent = saved ? 'Saved to Wishlist' : 'Save to Wishlist';
      else { const name = button.closest('[data-car-card]')?.dataset.name || 'car'; button.setAttribute('aria-label', `${saved ? 'Remove' : 'Save'} ${name} ${saved ? 'from' : 'to'} wishlist`); }
    });
  }
  syncWishlist();
  document.querySelectorAll('[data-wishlist]').forEach(button => button.addEventListener('click', () => {
    const slug = button.dataset.wishlist; const saved = wishlist.has(slug);
    if (saved) wishlist.delete(slug); else wishlist.add(slug);
    writeStorage('sportscars-wishlist', [...wishlist]); syncWishlist(); applyFilters();
    notify(saved ? 'Removed from your wishlist.' : 'Saved to your wishlist.');
  }));

  const filters = document.querySelector('#collection-filters');
  const cards = [...document.querySelectorAll('.collection-grid [data-car-card]')];
  const brand = document.querySelector('#brand-filter');
  const model = document.querySelector('#model-filter');
  const price = document.querySelector('#price-filter');
  const year = document.querySelector('#year-filter');
  const search = document.querySelector('#car-search');
  const savedOnly = document.querySelector('#saved-filter');
  const filterToggle = document.querySelector('.filter-toggle');
  const extraFilters = document.querySelector('#extra-filters');
  function expandFilters(open) {
    if (!filters) return;
    filters.classList.toggle('is-expanded', open); extraFilters.hidden = !open; filterToggle.setAttribute('aria-expanded', String(open));
  }
  function applyFilters() {
    if (!filters) return;
    let visible = 0;
    const term = search.value.trim().toLocaleLowerCase();
    cards.forEach(card => {
      const amount = Number(card.dataset.price);
      const matches = (!brand.value || brand.value === card.dataset.brand) && (!model.value || model.value === card.dataset.model) && (!year.value || year.value === card.dataset.year) && (!price.value || (price.value === 'low' ? amount < 125000 : amount >= 125000)) && (!term || card.dataset.name.toLocaleLowerCase().includes(term)) && (!savedOnly.checked || wishlist.has(card.dataset.slug));
      card.hidden = !matches; if (matches) visible++;
    });
    document.querySelector('[data-result-count]').textContent = `${visible} ${visible === 1 ? 'Car' : 'Cars'} Found`;
    document.querySelector('.empty-state').hidden = visible > 0;
    document.querySelector('.pagination').hidden = visible === 0;
  }
  if (filters) {
    const params = new URLSearchParams(location.search);
    for (const [name, control] of [['brand',brand],['model',model],['year',year]]) { const value = params.get(name); if (value && [...control.options].some(option => option.value === value)) control.value = value; }
    search.value = params.get('q') || ''; savedOnly.checked = params.get('wishlist') === '1';
    if (params.has('search') || savedOnly.checked || search.value) expandFilters(true);
    if (params.has('search')) search.focus({ preventScroll: true });
    filterToggle.addEventListener('click', () => expandFilters(extraFilters.hidden));
    filters.addEventListener('input', applyFilters); filters.addEventListener('change', applyFilters);
    filters.addEventListener('submit', event => { event.preventDefault(); applyFilters(); });
    filters.addEventListener('reset', () => requestAnimationFrame(applyFilters));
    document.querySelector('[data-clear-filters]')?.addEventListener('click', () => { filters.reset(); history.replaceState(null, '', location.pathname + '#collection'); });
    applyFilters();
  }

  const gallery = document.querySelector('[data-gallery]');
  if (gallery) {
    const primary = gallery.querySelector('#primary-photo');
    const thumbs = [...gallery.querySelectorAll('[data-gallery-thumb]')]; let current = 0;
    function showPhoto(index) {
      current = (index + thumbs.length) % thumbs.length;
      primary.src = thumbs[current].dataset.image; primary.alt = thumbs[current].dataset.alt;
      thumbs.forEach((thumb, i) => { thumb.classList.toggle('selected', i === current); if (i === current) thumb.setAttribute('aria-current', 'true'); else thumb.removeAttribute('aria-current'); });
      gallery.querySelector('[data-gallery-count]').textContent = `${current + 1} / ${thumbs.length}`;
    }
    thumbs.forEach((thumb, i) => thumb.addEventListener('click', () => showPhoto(i)));
    gallery.querySelector('[data-gallery-prev]').addEventListener('click', () => showPhoto(current - 1));
    gallery.querySelector('[data-gallery-next]').addEventListener('click', () => showPhoto(current + 1));
    gallery.addEventListener('keydown', event => { if (['ArrowLeft','ArrowRight'].includes(event.key)) { event.preventDefault(); showPhoto(current + (event.key === 'ArrowRight' ? 1 : -1)); } });
    let startX = 0; let startY = 0;
    primary.addEventListener('touchstart', event => { startX = event.changedTouches[0].clientX; startY = event.changedTouches[0].clientY; }, { passive: true });
    primary.addEventListener('touchend', event => { const dx = event.changedTouches[0].clientX - startX; const dy = event.changedTouches[0].clientY - startY; if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) showPhoto(current + (dx < 0 ? 1 : -1)); }, { passive: true });
  }
  const tabs = [...document.querySelectorAll('.detail-tabs [role=tab]')];
  function selectTab(tab, focus = false) {
    tabs.forEach(item => { const selected = tab === item; item.setAttribute('aria-selected', String(selected)); item.tabIndex = selected ? 0 : -1; document.getElementById(item.getAttribute('aria-controls')).hidden = !selected; });
    if (focus) tab.focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', event => {
      let next = index;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      else if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      else if (event.key === 'Home') next = 0; else if (event.key === 'End') next = tabs.length - 1; else return;
      event.preventDefault(); selectTab(tabs[next], true);
    });
  });

  const heroVideo = document.querySelector('#home-hero-video');
  if (heroVideo) {
    heroVideo.muted = true;
    heroVideo.loop = true;
    heroVideo.autoplay = true;
    const playHeroVideo = () => {
      heroVideo.play().catch(() => {  });
    };
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) heroVideo.pause();
      else playHeroVideo();
    });
    if (!document.hidden) playHeroVideo();
  }

  const inquiryDialog = document.querySelector('#inquiry-dialog');
  document.querySelectorAll('[data-inquire]').forEach(button => button.addEventListener('click', () => {
    const name = button.dataset.inquire;
    inquiryDialog.querySelector('[data-inquiry-model]').textContent = name ? `Interested in the ${name}? Let’s start a conversation.` : 'Tell us which car caught your eye.';
    inquiryDialog.querySelector('textarea').value = name ? `I would like to know more about the ${name}.` : '';
    inquiryDialog.showModal();
  }));
  document.querySelector('#inquiry-form')?.addEventListener('submit', event => {
    event.preventDefault(); if (!event.target.reportValidity()) return;
    inquiryDialog.close(); event.target.reset(); notify('Demo inquiry complete. No message was sent.');
  });
  document.querySelectorAll('[data-close-dialog]').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
  document.querySelectorAll('dialog').forEach(dialog => dialog.addEventListener('click', event => {
    if (event.target !== dialog) return; const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  }));
  const information = {
    faqs: ['Frequently Asked Questions', 'Browse the collection, compare specifications, and save your favorites. Three models have full detail pages. SportsCars is a fictional dealership created for this lab.'],
    financing: ['Financing', 'Financing is a demonstration link. This site does not offer credit or accept payments. Contact your preferred dealership for real financing options.'],
    warranty: ['Warranty', 'Warranty details depend on the vehicle and dealer. The cars and prices displayed here are examples for this project.'],
    'after-sales': ['After-Sales', 'For servicing, maintenance, and ownership support, contact an authorized dealer. This demo does not book appointments.'],
    privacy: ['Privacy Policy', 'Your theme and saved cars are stored on this device. Forms are demonstrations and do not send your information to a server. Google Fonts loads typography from Google.'],
    terms: ['Terms of Service', 'SportsCars is an educational demonstration. Images, prices, and vehicle specifications are illustrative. No vehicle purchase, reservation, or other transaction can be made through this site.'],
  };
  const infoDialog = document.querySelector('#info-dialog');
  document.querySelectorAll('[data-info]').forEach(button => button.addEventListener('click', () => {
    const info = information[button.dataset.info];
    infoDialog.querySelector('#info-title').textContent = info[0]; infoDialog.querySelector('#info-content').textContent = info[1]; infoDialog.showModal();
  }));
  document.querySelector('.newsletter-form')?.addEventListener('submit', event => {
    event.preventDefault(); if (!event.target.reportValidity()) return;
    document.querySelector('.newsletter-status').textContent = 'Thank you! This is a demo subscription.'; event.target.reset();
  });
})();
