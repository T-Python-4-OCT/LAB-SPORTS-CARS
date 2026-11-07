(() => {
  let saved;
  try { saved = localStorage.getItem('sportscars-theme'); } catch (_) {  }
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  document.documentElement.dataset.theme = saved === 'light' || saved === 'dark' ? saved : systemDark ? 'dark' : 'light';
})();
