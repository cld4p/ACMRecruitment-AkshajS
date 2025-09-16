document.addEventListener('DOMContentLoaded', () => {
    const counterValueElement = document.getElementById('counter-value');
    const decrementBtn = document.getElementById('decrement-btn');
    const incrementBtn = document.getElementById('increment-btn');

    let count = 0;

    function updateCounterDisplay() {
        counterValueElement.textContent = count;
    }

    incrementBtn.addEventListener('click', () => {
        count++;
        updateCounterDisplay();
    });

    decrementBtn.addEventListener('click', () => {
        count--;
        updateCounterDisplay();
    });
});
