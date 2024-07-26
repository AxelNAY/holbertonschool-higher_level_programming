const UpdateHeader = document.getElementById('update_header');

UpdateHeader.addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
