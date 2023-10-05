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
      <td>${file.user.email}</td>
      <td>
      <button class="btn btn-danger btn-sm">Renew</button>
    </td>
    `;
    table.appendChild(tr);
  });
}

function updatePagination(data) {
  const pagination = document.getElementById("pagination");
  const numPages = Math.ceil(data.length / rowsPerPage);

  let paginationHTML = "";

  for (let i = 1; i <= numPages; i++) {
    paginationHTML += `<li class="page-item"><a class="page-link" href="javascript:void(0);" onclick="goToPage(${i}, ${JSON.stringify(
      data
    )})">${i}</a></li>`;
  }

  pagination.innerHTML = paginationHTML;
}

function goToPage(page, data) {
  currentPage = page;
  const start = (currentPage - 1) * rowsPerPage;
  const end = start + rowsPerPage - 1;
  generateTable(data, start, end);
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
