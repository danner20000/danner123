// pagination.js

const rowsPerPage = 4; // Set the number of rows per page
let currentPage = 1; // Initialize the current page to 1
let userData = null; // Initialize userData (you'll need to set this when you have the actual data)

function updatePagination() {
  const pagination = document.getElementById("pagination");
  const numPages = Math.ceil(userData.length / rowsPerPage);

  let paginationHTML = "";

  for (let i = 1; i <= numPages; i++) {
    paginationHTML += `<li class="page-item"><a class="page-link" href="javascript:void(0);" onclick="goToPage(${i})">${i}</a></li>`;
  }

  pagination.innerHTML = paginationHTML;
}

function goToPage(page) {
  currentPage = page;
  const start = (currentPage - 1) * rowsPerPage;
  const end = start + rowsPerPage;
  generateTable(userData.slice(start, end));
}

function generateTable(data) {
  // This function will generate the table rows based on the data received
  const tableBody = document.getElementById("userTableBody");
  let tableHTML = "";

  data.forEach((user, index) => {
    tableHTML += `
      <tr>
        <td>${index + 1}</td>
        <td>${user.first_name}</td>
        <td>${user.last_name}</td>
        <td>${user.email}</td>
        <td>
          <a class="btn btn-custom btn-sm edit-user-btn" href="#">Edit</a>
          <button class="btn delete-button custom-delete-btn" data-user-id="${
            user.id
          }">Delete</button>
        </td>
      </tr>
    `;
  });

  tableBody.innerHTML = tableHTML;
}

// Initialize pagination when the DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  updatePagination();
  goToPage(currentPage);
});
