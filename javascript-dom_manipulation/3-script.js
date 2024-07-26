const ToggleHeader = document.getElementById('toggle_header');

ToggleHeader.addEventListener('click', function () {
  const MyHeader = document.querySelector('header');
  if (MyHeader.className === 'green') {
    MyHeader.classList.toggle('green');
    MyHeader.classList.add('red');
  } else {
    MyHeader.classList.toggle('red');
    MyHeader.classList.add('green');
  }
});
