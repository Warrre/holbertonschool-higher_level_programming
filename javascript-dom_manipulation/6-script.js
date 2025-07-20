async function getName() {
	const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
	const response = await fetch(url);
	const data = await response.json();
	const name = data.name;
	document.getElementById("character").textContent = name;
}
getName();
