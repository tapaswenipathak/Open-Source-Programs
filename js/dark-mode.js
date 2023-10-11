//Switch to dark mode and update dark mode const
function switchMode() {
  document.body.classList.toggle('dark');
  const isDarkMode = document.body.classList.contains('dark');
    document.cookie = `darkMode=${isDarkMode ? 1 : 0}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/`;
}

// Function to get the value of a cookie by name
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// Check for the dark mode preference in the cookie
const darkModeCookie = getCookie('darkMode');

// Apply dark mode if the cookie value is '1' (for dark mode)
if (darkModeCookie === '1') {
  document.body.classList.add('dark');
}