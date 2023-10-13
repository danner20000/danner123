document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/file/expired_documents/")
    .then((response) => response.json())
    .then((data) => {
      const table = document.getElementById("expired");
      data.forEach((item, index) => {
        const row = document.createElement("tr");
        const cells = [
          "company_name",
          "department_name ",
          "document_type",
          "renewal_date",
          "expiry_date",
          "user_email",
        ];
        cells.forEach((key) => {
          const cell = document.createElement("td");
          cell.innerText = item[key];
          row.appendChild(cell);
        });

        const indexCell = document.createElement("td");
        indexCell.innerText = index + 1;
        row.appendChild(indexCell);
        table.querySelector("tbody").appendChild(row);
      });
    });
});
