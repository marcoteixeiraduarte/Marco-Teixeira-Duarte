const themeToggle = document.getElementById('theme-toggle');

const applyTheme = (isDark) => {
  document.body.classList.toggle('dark', isDark);
  themeToggle.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
};

const stored = localStorage.getItem('theme');
applyTheme(stored === 'dark');

themeToggle.addEventListener('click', () => {
  const isDark = !document.body.classList.contains('dark');
  applyTheme(isDark);
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});
