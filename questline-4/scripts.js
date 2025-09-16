
document.querySelectorAll('nav a').forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const target = link.getAttribute('data-section');

    document.querySelectorAll('.content-section').forEach(section => {
      section.classList.add('hidden');
    });

    document.getElementById(target).classList.remove('hidden');
  });
});