const AddItem = document.getElementById('add_item');

AddItem.addEventListener('click', function () {
  const Newlist = document.createElement('li');
  Newlist.textContent = 'Item';
  document.querySelector('.my_list').appendChild(Newlist);
});
