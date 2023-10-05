fetch("/api/users/")
  .then((response) => response.json())
  .then((data) => {
    generateTable(data.results);
  })
  .catch((error) => console.error("Error:", error));
