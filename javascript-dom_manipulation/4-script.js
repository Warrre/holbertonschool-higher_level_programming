const item = document.querySelector("#add_item");
const list = document.querySelector(".my_list");
item.addEventListener("click", function(){
	const newLi = document.createElement('li');
	newLi.setAttribute('class', 'my_list');
	newLi.innerText = "Item";
	list.appendChild(newLi);
});
