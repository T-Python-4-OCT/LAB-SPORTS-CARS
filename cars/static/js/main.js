const root = document.documentElement;
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = themeToggle.querySelector('span');

function setTheme(theme) {
  root.dataset.theme = theme;
  localStorage.setItem('theme', theme);
  themeIcon.textContent = theme === 'dark' ? 'light_mode' : 'dark_mode';
}

setTheme(root.dataset.theme);
themeToggle.addEventListener('click', () => {
  setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
});

//mobile menu
document.getElementById('menu-btn').addEventListener('click', () => {
  document.getElementById('links').classList.toggle('open');
});

//reveal elements when they scroll into view
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('show');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

//tabs on the car detail page
document.querySelectorAll('.tab').forEach((tab) => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab, .tab-panel').forEach((el) => el.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.tab).classList.add('active');
  });
});

// submit the filter form as soon as a select changes
document.querySelectorAll('.filters select').forEach((select) => {
  select.addEventListener('change', () => select.form.submit());
});

//newsletter form (demo only)
const newsletter = document.getElementById('newsletter');
if (newsletter) {
  newsletter.addEventListener('submit', (event) => {
    event.preventDefault();
    newsletter.hidden = true;
    document.getElementById('thanks').hidden = false;
  });
}

//wishlist button on the car detail page
const wishlistBtn = document.getElementById('wishlist-btn');
if (wishlistBtn) {
  wishlistBtn.addEventListener('click', () => {
    const saved = wishlistBtn.classList.toggle('saved');
    document.getElementById('wishlist-text').textContent = saved ? 'Saved' : 'Save to Wishlist';
  });
}

//scroll progress bar
const progressBar = document.getElementById('progress');
window.addEventListener('scroll', () => {
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const ratio = maxScroll > 0 ? window.scrollY / maxScroll : 0;
  progressBar.style.width = `${ratio * 100}%`;
});