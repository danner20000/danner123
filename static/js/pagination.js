function updatePagination(data) {
  const pagination = document.getElementById("pagination");
  const numPages = Math.ceil(data.length / rowsPerPage);

  let paginationHTML = "";

  for (let i = 1; i <= numPages; i++) {
    paginationHTML += `<li class="page-item"><a class="page-link" href="javascript:void(0);" onclick="goToPage(${i}, userData)">${i}</a></li>`;
  }

  pagination.innerHTML = paginationHTML;
}
