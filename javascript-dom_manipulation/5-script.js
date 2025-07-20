const header = document.querySelector("header");
const handler = document.querySelector("#update_header");
handler.addEventListener("click", function(){
	header.innerHTML = "New Header!!!";
});
