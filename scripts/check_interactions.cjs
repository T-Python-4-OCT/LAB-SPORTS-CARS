const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

class Element {
  constructor(options = {}) {
    Object.assign(this, { hidden: false, value: '', checked: false, dataset: {}, attrs: {}, handlers: {}, textContent: '', options: [] }, options);
    this.classes = new Set();
    this.classList = { add: name => this.classes.add(name), toggle: (name, state) => state ? this.classes.add(name) : this.classes.delete(name) };
  }
  addEventListener(name, callback) { (this.handlers[name] ||= []).push(callback); }
  emit(name, detail = {}) { for (const callback of this.handlers[name] || []) callback({ target: this, preventDefault() {}, ...detail }); }
  setAttribute(name, value) { this.attrs[name] = value; }
  getAttribute(name) { return this.attrs[name] ?? null; }
  removeAttribute(name) { delete this.attrs[name]; }
  querySelector(selector) { return this.children?.[selector] || null; }
  querySelectorAll(selector) { return this.groups?.[selector] || []; }
  closest(selector) { return this.closestMap?.[selector] || null; }
  focus() { this.focused = true; }
}

const element = options => new Element(options);
const root = element({ dataset: { theme: 'light' } });
const theme = element(), meta = element(), menuButton = element(), menu = element({ hidden: true }), toast = element({ hidden: true });
const heroVideo = element({ paused: true, muted: false, loop: false, autoplay: false });
heroVideo.play = function () { this.paused = false; this.emit('play'); return Promise.resolve(); };
heroVideo.pause = function () { this.paused = true; this.emit('pause'); };
const controls = Object.fromEntries(['brand','model','price','year','car-search','saved'].map(name => [name,element()]));
for (const [name, value] of [['brand','Hyundai'],['model','Elantra N'],['year','2025']]) controls[name].options = [{ value: '' },{ value }];
const filterForm = element(), filterToggle = element(), extras = element({ hidden: true }), result = element(), empty = element(), pagination = element();
const cars = [
  element({ dataset: { slug: 'hyundai-genesis-coupe', name: 'Hyundai Genesis Coupe', brand: 'Hyundai', model: 'Genesis Coupe', year: '2013', price: '65000' } }),
  element({ dataset: { slug: 'hyundai-elantra-n-2025', name: 'Hyundai Elantra N 2025', brand: 'Hyundai', model: 'Elantra N', year: '2025', price: '125000' } }),
  element({ dataset: { slug: 'hyundai-sonata-n-line', name: 'Hyundai Sonata N Line', brand: 'Hyundai', model: 'Sonata N Line', year: '2024', price: '165000' } }),
];
const saved = element({ dataset: { wishlist: cars[0].dataset.slug }, closestMap: { '[data-car-card]': cars[0] } });
const image = element(), prev = element(), next = element(), count = element();
const thumbs = [0,1,2].map(i => element({ dataset: { image: `photo-${i}.webp`, alt: `Photo ${i}` } }));
const gallery = element({ children: { '#primary-photo': image, '[data-gallery-prev]': prev, '[data-gallery-next]': next, '[data-gallery-count]': count }, groups: { '[data-gallery-thumb]': thumbs } });
const tabs = ['overview','specifications','features','gallery'].map(name => element({ attrs: { 'aria-controls': `panel-${name}` } }));
const panels = Object.fromEntries(tabs.map(tab => [tab.attrs['aria-controls'],element()]));
const nodes = {
  '.theme-toggle': theme, 'meta[name="theme-color"]': meta, '.menu-toggle': menuButton, '#mobile-nav': menu,
  '.toast': toast, '#collection-filters': filterForm, '#brand-filter': controls.brand, '#model-filter': controls.model,
  '#price-filter': controls.price, '#year-filter': controls.year, '#car-search': controls['car-search'],
  '#saved-filter': controls.saved, '.filter-toggle': filterToggle, '#extra-filters': extras,
  '[data-result-count]': result, '.empty-state': empty, '.pagination': pagination, '[data-gallery]': gallery,
  '#home-hero-video': heroVideo,
};
const groups = { '[data-wishlist]': [saved], '.collection-grid [data-car-card]': cars, '.detail-tabs [role=tab]': tabs };
const storage = new Map();
const document = element({ documentElement: root, querySelector: selector => nodes[selector] || null, querySelectorAll: selector => groups[selector] || [], getElementById: id => panels[id] });
const window = { addEventListener() {} };
const localStorage = { getItem: key => storage.get(key) ?? null, setItem: (key,value) => storage.set(key,value) };
const mediaQueries = new Map();
const matchMedia = query => {
  if (!mediaQueries.has(query)) mediaQueries.set(query, element({ matches: false }));
  return mediaQueries.get(query);
};
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
reducedMotion.matches = true;
const context = vm.createContext({ document, window, localStorage, location: { search: '', pathname: '/cars/' }, history: { replaceState() {} }, matchMedia, URLSearchParams, setTimeout: () => 1, clearTimeout() {}, requestAnimationFrame: callback => callback(), console });
vm.runInContext(fs.readFileSync(path.join(__dirname,'../static/js/site.js'),'utf8'), context);

assert.equal(result.textContent,'3 Cars Found');
controls.brand.value = 'Hyundai'; filterForm.emit('change');
assert.equal(result.textContent,'3 Cars Found');
controls.model.value = 'Elantra N'; filterForm.emit('change');
assert.equal(result.textContent,'1 Car Found'); assert.deepEqual(cars.map(car => car.hidden),[true,false,true]);
controls.brand.value = ''; controls.model.value = ''; controls.price.value = 'low'; filterForm.emit('change');
assert.deepEqual(cars.map(car => car.hidden),[false,true,true]);
controls.price.value = ''; controls['car-search'].value = 'SONATA'; filterForm.emit('input');
assert.deepEqual(cars.map(car => car.hidden),[true,true,false]);
controls['car-search'].value = 'nonexistent'; filterForm.emit('input');
assert.equal(result.textContent,'0 Cars Found'); assert.equal(empty.hidden,false); assert.equal(pagination.hidden,true);
controls['car-search'].value = ''; controls.saved.checked = true; filterForm.emit('change');
assert.equal(result.textContent,'0 Cars Found');
saved.emit('click'); assert.equal(saved.attrs['aria-pressed'],'true'); assert.equal(result.textContent,'1 Car Found');
assert.deepEqual(JSON.parse(storage.get('sportscars-wishlist')),['hyundai-genesis-coupe']);
saved.emit('click'); assert.equal(result.textContent,'0 Cars Found'); assert.equal(saved.attrs['aria-pressed'],'false');
theme.emit('click'); assert.equal(root.dataset.theme,'dark'); assert.equal(storage.get('sportscars-theme'),'dark');
theme.emit('click'); assert.equal(root.dataset.theme,'light');
menuButton.emit('click'); assert.equal(menu.hidden,false); assert.equal(menuButton.attrs['aria-expanded'],'true');
menuButton.emit('click'); assert.equal(menu.hidden,true);
filterToggle.emit('click'); assert.equal(extras.hidden,false); assert.equal(filterForm.classes.has('is-expanded'),true);
next.emit('click'); assert.equal(image.src,'photo-1.webp'); assert.equal(count.textContent,'2 / 3');
prev.emit('click'); prev.emit('click'); assert.equal(image.src,'photo-2.webp'); assert.equal(count.textContent,'3 / 3');
thumbs[2].emit('click'); assert.equal(image.src,'photo-2.webp'); assert.equal(image.alt,'Photo 2');
tabs[1].emit('click'); assert.equal(panels['panel-overview'].hidden,true); assert.equal(panels['panel-specifications'].hidden,false);
tabs[1].emit('keydown',{ key:'ArrowRight' }); assert.equal(panels['panel-features'].hidden,false); assert.equal(tabs[2].focused,true);

assert.equal(heroVideo.muted, true); assert.equal(heroVideo.loop, true); assert.equal(heroVideo.autoplay, true);
assert.equal(heroVideo.paused, false, 'The requested hero video should autoplay even when reduced motion is enabled.');
reducedMotion.matches = false; reducedMotion.emit('change');
reducedMotion.matches = true; reducedMotion.emit('change');
assert.equal(heroVideo.paused, false, 'Motion preference changes should not interrupt the requested autoplay.');
document.hidden = true; document.emit('visibilitychange');
assert.equal(heroVideo.paused, true, 'An invisible page should suspend video playback.');
document.hidden = false; document.emit('visibilitychange');
assert.equal(heroVideo.paused, false, 'Returning to the page should resume video playback.');
console.log('Passed: filters, empty state, saved-car persistence, theme, mobile menu, gallery wraparound, tabs, keyboard navigation, and muted looping hero autoplay with visibility handling.');
