const root = document.documentElement;
const toggle = document.getElementById('theme-toggle');
const icon = toggle.querySelector('span');

function setTheme(theme) {
  root.dataset.theme = theme;
  localStorage.setItem('theme', theme);
  icon.textContent = theme === 'dark' ? 'light_mode' : 'dark_mode';
}
setTheme(root.dataset.theme);
toggle.addEventListener('click', () => setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark'));

document.getElementById('menu-btn').addEventListener('click',
  () => document.getElementById('links').classList.toggle('open'));

const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('show'); io.unobserve(e.target); }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab, .tab-panel').forEach(x => x.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.tab).classList.add('active');
  });
});

document.querySelectorAll('.filters select').forEach(sel =>
  sel.addEventListener('change', () => sel.form.submit()));

const news = document.getElementById('newsletter');
if (news) news.addEventListener('submit', e => {
  e.preventDefault();
  news.hidden = true;
  document.getElementById('thanks').hidden = false;
});