
const countElement = document.getElementById('count-value');
const addBtn = document.getElementById('add-btn');


let count = 0;

addBtn.addEventListener('click', () => {
    count++;
    countElement.textContent = count;
});