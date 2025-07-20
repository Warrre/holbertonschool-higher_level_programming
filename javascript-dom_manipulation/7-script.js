fetch("https://swapi-api.hbtn.io/api/films/?format=json")
	.then(response => response.json())
	.then(data => {
		const ul = document.getElementById("list_movies");
		data.results.forEach(film => {
			ul.innerHTML += `<li>${film.title}</li>`;
		});
	});
    