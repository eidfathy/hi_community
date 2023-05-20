const spans = document.querySelectorAll('span');

const array1 = [];
spans.forEach((e) => console.log(array1.push(e.textContent)));

console.log(array1);
