const rowsPerPage = 5;
let userData = null;

async function generateTable(data) {
  const table = document
    .getElementById("dtBasicExample")
    .querySelector("tbody");
  table.innerHTML = "";

  data.forEach((user, index) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${index + 1}</td>
      <td>${user.first_name}</td>
      <td>${user.last_name}</td>
      <td>${user.email}</td>
    `;
    table.appendChild(tr);
  });
}

async function fetchUserList() {
  try {
    const response = await fetch("/api/file/valid_file/");
    const data = await response.json();
    userData = data;
    await generateTable(data);
  } catch (error) {
    console.error("Error:", error);
  }
}

fetchUserList();
