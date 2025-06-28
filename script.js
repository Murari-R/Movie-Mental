function getRecommendations() {
  const actor = document.getElementById("actor").value;
  const genre = document.getElementById("genre").value;

  fetch(`http://127.0.0.1:5000/recommend?actor=${actor}&genre=${genre}`)
    .then(res => res.json())
    .then(data => {
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = "";

      if (!data || data.length === 0) {
        resultsDiv.innerHTML = "<p>No results found.</p>";
        return;
      }

      data.forEach(movie => {
        const m = document.createElement("div");
        m.className = "movie";
        m.innerHTML = `<h3>${movie.title}</h3><p>${movie.overview || "No description available."}</p>`;
        resultsDiv.appendChild(m);
      });
    });
}
