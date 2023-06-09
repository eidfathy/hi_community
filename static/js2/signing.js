// First we get the viewport height and we multiple it by 1% to get a value for a vh unit
let vh = window.innerHeight * 0.0099;
// Then we set the value in the --vh custom property to the root of the document
document.documentElement.style.setProperty('--vh', `${vh}px`);

// We listen to the resize event
window.addEventListener('resize', () => {
  // We execute the same script as before
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);
});

const registerBtn = document.querySelector('.register');
const container = document.querySelector('.container');
const formChoice = document.querySelector('#form-choice');
const form1 = document.querySelector('#form-1');
const form2 = document.querySelector('#form-2');
const form3 = document.querySelector('#form-3');
const form4 = document.querySelector('#form-4');
const btn2 = document.querySelector('#btn-2');
const btn3 = document.querySelector('#btn-3');
const userBtn = document.querySelector('#user');
const placesBtn = document.querySelector('#places');
const image = document.querySelector('.img');

registerBtn.addEventListener('click', (e) => {
  e.preventDefault();

  image.src = './assets/form-5.png';
  container.classList.toggle('reverse');
  form1.style.display = 'none';
  formChoice.style.display = 'flex';
});

// userBtn.addEventListener('click', (e) => {
//   e.preventDefault();

//   image.src = './assets/form-2.png';
//   container.classList.toggle('reverse');
//   formChoice.style.display = 'none';
//   form2.style.display = 'flex';
// });

// placesBtn.addEventListener('click', (e) => {
//   e.preventDefault();

//   image.src = './assets/form-2.png';
//   container.classList.toggle('reverse');
//   formChoice.style.display = 'none';
//   form2.style.display = 'flex';
// });

// registerBtn.addEventListener('click', (e) => {
//   e.preventDefault();

//   image.src = './assets/form-2.png';
//   container.classList.toggle('reverse');
//   form1.style.display = 'none';
//   form2.style.display = 'flex';
// });

btn2.addEventListener('click', (e) => {
  e.preventDefault();

  console.log('lol');
  image.src = './assets/form-3.png';
  container.classList.toggle('reverse');
  form2.style.display = 'none';
  form3.style.display = 'flex';
});
btn3.addEventListener('click', (e) => {
  e.preventDefault();

  image.src = './assets/form-4.png';
  container.classList.toggle('reverse');
  form3.style.display = 'none';
  form4.style.display = 'flex';
});

// The DOM element you wish to replace with Tagify
var input = document.querySelector('input[name=basic]');

// init Tagify script on the above inputs
tagify2 = new Tagify(input, {
  enforeWhitelist: true,
  whitelist: [
    'Accounting',
    'Action adventure films',
    'Adam Driver',
    'Adidas',
    'Adobe',
    'Advertising',
    'Agriculture',
    'Amazon',
    'Android',
    'Angelina Jolie',
    'Animated films',
    'Anna Kendrick',
    'Anthony Martial',
    'Antoine Griezmann',
    'Apple',
    'Archaeology',
    'Architecture',
    'Arduino',
    'Arsenal',
    'Artificial intelligence',
    'Astronauts',
    'Astrophotography',
    'Athletic apparel',
    'Atletico Madrid',
    'Atletico Madridstats',
    'Attack onTitan',
    'Augmented reality',
    'Aviation',
    'BanG Dream',
    'Barbara Palvin',
    'Basketball',
    'Beauty',
    'Beauty influencers',
    'Ben Affleck',
    'Benedict Cumberbatch',
    'Betty White',
    'Bill Hader',
    'Biology',
    'Biotech biomedical',
    'Body building',
    'Bollywood films',
    'Bretman Rock',
    'Brie Larson',
    'Bruno Fernandes',
    'Cambridge University',
    'Cardio',
    'Chainsaw Man',
    'Charlize Theron',
    'Chelsea',
    'Chelsea stats',
    'Chemistry',
    'Chris Evans',
    'Chris Pratt',
    'Christian Pulisic',
    'Cloud computing',
    'Cloud platforms',
    'Clubhouse',
    'Code Geass',
    'Colin Kaepernick',
    'College life',
    'Comedy films',
    'Computer hardware',
    'Construction',
    'Copa Libertadores',
    'Core fitness',
    'Cricket',
    'Crime films',
    'Cristiano Ronaldo',
    'Crossfit',
    'Cult classics',
    'Cybersecurity',
    'Cycling',
    'Daisy Marquez',
    'Dana White',
    'Dance',
    'Dani Alves',
    'Dani Ceballos',
    'Data science',
    'Data visualization',
    'Databases',
    'David Beckham',
    'Deadpool',
    'Demon Slayer',
    'Digital Marketing',
    'Documentary films',
    'Dragon Ball',
    'Drama films',
    'Dune',
    'Dwayne Johnson',
    'Earthquakes',
    'Economics',
    'Eden Hazard',
    'Education',
    'Elizabeth Olsen',
    'Elon Musk',
    'Emilia Clarke',
    'Emily Blunt',
    'Emma Chamberlain',
    'Environmentalism',
    'Everyday style',
    'Exoplanets',
    'FA Cup',
    'FC Barcelona',
    'FC Barcelonastats',
    'Facebook',
    'Farm life',
    'Fashion',
    'Fashion business',
    'Fashion magazines',
    'Fashion models',
    'FinTech',
    'Fire Force',
    'Fist of the North Star',
    'Fitness influencers',
    'Fitness magazines',
    'Futurology',
    'Gal Gadot',
    'Genealogy',
    'Geography',
    'Geology',
    'Georgetown University',
    'Gigi Hadid',
    'Gintama',
    'Godzilla',
    'Golden Kamuy',
    'Google',
    'Graduate school',
    'Gym workouts',
    'HIIT',
    'Haikyu',
    'Hailey Bieber',
    'Hair care',
    'Hair styling',
    'Halloween films',
    'Handbags',
    'Harry Kane',
    'Harry Maguire',
    'Harry Potter',
    'Harvard University',
    'Henry Cavill',
    'Hetalia',
    'History',
    'Holiday films',
    'Homeschooling',
    'Horror films',
    'Huawei',
    'Hugh Jackman',
    'Hulu',
    'Hunter×Hunter',
    'Hypnosismic',
    'IBM',
    'Indie films',
    'Information security',
    'Instagram',
    'Insurance',
    'Intel',
    'Interior design',
    'Internet ofthings',
    'Inuyasha',
    'Ios development',
    'Jackie Aina',
    'Jaclyn Hill',
    'Jadon Sancho',
    'James Bond',
    'James Charles',
    'Jeffree Star',
    'Jennifer Aniston',
    'Jennifer Hudson',
    'Jennifer Lawrence',
    'Jennifer Lopez',
    'Jewelry',
    'Job searching networking',
    'Johnny Depp',
    'Jordi Alba',
    'Joseph Aidoo',
    'Jujutsu Kaisen',
    'Jurgen Klopp',
    'Karim Benzema',
    'Keanu Reeves',
    'Kevin DeBruyne',
    'King Kong',
    'Kristen Stewart',
    'Kylie Skin',
    'LOreal',
    'La Liga',
    'La Ligastats',
    'La Ligatransfers',
    'Language learning',
    'LeBron James',
    'Leeds United',
    'Leicester City',
    'Linux',
    'Lionel Messi',
    'Liverpool FC',
    'London Marathon',
    'Love Live',
    'Lower bodyfitness',
    'Luis Suarez',
    'Luka Modric',
    'Lupin The Third',
    'MAC',
    'Machine learning',
    'Makeup',
    'Manchester City',
    'Manchester United',
    'Manny Gutierrez',
    'Marathon',
    'Marcus Rashford',
    'Margot Robbie',
    'Mark Hamill',
    'Marketing',
    'Mateo Kovacic',
    'Mathematics',
    'Memphis Depay',
    'Mens style',
    'Mens tennis',
    'Microcontrollers',
    'Mindful wellness',
    'Mobile Suit Gundam',
    'Mobile development',
    'Mohamed Salah',
    'Monash University',
    'Musicals',
    'My HeroAcademia',
    'NASA',
    'NBA',
    'NFL',
    'Nacho',
    'Naruto',
    'Netflix',
    'New York Fashion Week',
    'Nike',
    'Nikkie deJager',
    'Novak Djokovic',
    'ONE PIECE',
    'OPPO',
    'Oceanography',
    'OnePlus',
    'Online education',
    'Open source',
    'PUMA',
    'Paleontology',
    'Paul Pogba',
    'Peloton',
    'Pep Guardiola',
    'Perfumes fragrances',
    'Philippe Coutinho',
    'Philosophy',
    'Physics',
    'Pilates',
    'Pokémon',
    'Premier League',
    'Premier Leaguestats',
    'Pretty Cure',
    'Product management',
    'Psychology',
    'Python',
    'Raspberry Pi',
    'Real Betis Balompié',
    'Real Madrid CF stats',
    'Real MadridCF',
    'Real Sociedad',
    'Richard Branson',
    'Romance films',
    'Romcom films',
    'Romelu Lukaku',
    'Running',
    'SEO',
    'Sailor Moon',
    'Saint Seiya',
    'Scarlett Johansson',
    'Science news',
    'Scifi fantasyfilms',
    'Screenwriting',
    'Sergio Aguero',
    'Sergio Busquets',
    'Sevilla FCstats',
    'Shoes',
    'Shopee',
    'Shopping',
    'Simply Nailogical',
    'Skin care',
    'Snapchat',
    'Sneakers',
    'Social media',
    'Solar System',
    'Sony',
    'Space',
    'Space missions',
    'Space telescopes',
    'SpaceX',
    'Spaces YouMightLike',
    'Spas',
    'SpiderMan',
    'Spinning',
    'Sporting goods',
    'Sports technology',
    'Sports themed films',
    'Stanford University',
    'Star Wars',
    'Sunscreen',
    'Superhero films',
    'Supernatural',
    'Tattoos',
    'Tech industry',
    'Tech news',
    'The Lordof the Rings',
    'Thriller films',
    'Tiara Willis',
    'TikTok',
    'Tim Cook',
    'Timo Werner',
    'Tom Cruise',
    'Tom Hanks',
    'Toni Kroos',
    'Tottenham Hotspur',
    'Track cycling',
    'Trail running',
    'Transformers',
    'Twilight Saga',
    'Twitch',
    'Twitter',
    'Twitter Spaces',
    'UEFA ChampionsLeague',
    'UX design',
    'Uber',
    'Ultramarathon',
    'Unai Emery',
    'Valencia CF',
    'Villarreal CF',
    'Virat Kohli',
    'Virtual reality',
    'Vivo',
    'Volcanology',
    'Watches',
    'Weather',
    'Weather videos',
    'Web development',
    'Weight training',
    'West HamUnited',
    'Workout videos',
    'Xiaomi',
    'YUGIOH',
    'Yahoo',
    'Yoga',
    'YouTube',
    'Zinedine Zidane',
    'Zoella',
    'Zoology',
    'eBay',
  ],
  maxTags: 10,

  dropdown: {
    classname: 'color-red',
    enabled: 0, // show the dropdown immediately on focus
    maxItems: 5,
    position: 'text', // place the dropdown near the typed text
    closeOnSelect: true, // keep the dropdown open after selecting a suggestion
    highlightFirst: true,
  },
  texts: {
    empty: 'empty',
    exceed: 'number of tags exceeded',
    pattern: 'pattern mismatch',
    duplicate: 'already exists',
    notAllowed: 'not allowed',
  },
});
