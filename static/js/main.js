const checkbox = document.querySelector('.switch');
let localTheme = localStorage.getItem('theme');

function enabeleDarkMode() {
  localStorage.setItem('theme', 'dark');
  document.documentElement.setAttribute('data-theme', 'dark');
  checkbox.checked = true;
}

function disableDarkMode() {
  localStorage.setItem('theme', 'light');
  document.documentElement.setAttribute('data-theme', 'light');
  checkbox.checked = false;
}

checkbox.addEventListener('change', function () {
  if (this.checked) {
    enabeleDarkMode();
  } else {
    disableDarkMode();
  }
});

if (localTheme === 'dark') enabeleDarkMode();

const prefersDarkScheme = window.matchMedia(
  '(prefers-color-scheme: dark)'
);

localTheme === 'dark' && prefersDarkScheme.matches
  ? (checkbox.checked = true)
  : (checkbox.checked = false);

prefersDarkScheme.matches && !localStorage.hasOwnProperty('theme')
  ? enabeleDarkMode()
  : disableDarkMode;

const linkItems = document.querySelectorAll('.nav__item');
document
  .querySelector('.nav__links')
  .addEventListener('click', function (e) {
    e.preventDefault();
    // Matching strategy
    if (e.target.classList.contains('nav__link')) {
      linkItems.forEach((e) => e.classList.remove('current'));
      const id = e.target.getAttribute('href');
      document
        .querySelector(id)
        .scrollIntoView({ behavior: 'smooth' });
      e.target.closest('.nav__item').classList.add('current');
    }
  });

document.querySelector('.scroll').addEventListener('click', (e) => {
  document
    .querySelector('#features')
    .scrollIntoView({ behavior: 'smooth' });
});

const header = document.querySelector('.start');
const sections = document.querySelectorAll('.section');
const nav = document.querySelector('.navigation');
const navHeight = nav.getBoundingClientRect().height;

const stickyNav = function (entries) {
  const [entry] = entries;

  if (!entry.isIntersecting) nav.classList.add('sticky');
  else nav.classList.remove('sticky');
};

const headerObserver = new IntersectionObserver(stickyNav, {
  root: null,
  threshold: 0,
  rootMargin: `-${navHeight}px`,
});

headerObserver.observe(header);

/*
const featuresF = function (entries) {
    const [entry] = entries;
  
    linkItems.forEach((e) => e.classList.remove('current'));
  
    if (entry.isIntersecting) {
      const id = entry.target.id;
  
      linkItems.forEach((e) => {
        if (e.dataset.id === id) {
          e.classList.add('current');
        }
        //   e.closest('.nav__link').getAttribute('href');
      });
    }
  
    //   else nav.classList.remove('sticky');
  };
  */
