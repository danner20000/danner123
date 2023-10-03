const rowsPerPage = 5;
let fileData = null;

async function generateTable(data) {
  const table = document
    .getElementById("dtBasicExample")
    .querySelector("tbody");
  table.innerHTML = "";

  data.forEach((file, index) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${index + 1}</td>
      <td>${file.select_BU}</td>
      <td>${file.document_type}</td>
      <td>${file.department}</td>
      <td>${file.renewal_date}</td>
      <td>${file.expiry_date}</td>
      <td>
      <button class="btn btn-danger btn-sm">Renew</button>
    </td>
    `;
    table.appendChild(tr);
  });
}

async function fetchFileList() {
  try {
    const response = await fetch("/api/file/expired/");
    const data = await response.json();
    fileData = data;
    console.log(data);
    await generateTable(data);
  } catch (error) {
    console.error("Error:", error);
  }
}

fetchFileList();
