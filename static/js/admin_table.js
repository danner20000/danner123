document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/file/expired_documents/")
    .then((response) => response.json())
    .then((data) => {
      const table = $("#expired").DataTable({
        lengthMenu: [5, 10, 25, 50, 75, 100],
        searching: true,
      });

      table.clear().draw();

      data.forEach((item, index) => {
        const cells = [
          "company_name",
          "department_name",
          "document_type",
          "renewal_date",
          "expiry_date",
          "user_fullname",
        ];
        const rowData = cells.map((key) =>
          key === "user_fullname"
            ? `${item.user_firstname} ${item.user_lastname}`
            : item[key]
        );

        // Add a row to the table
        table.row.add([index + 1, ...rowData]).draw();
      });
    });
});

document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/file/renewal_documents/")
    .then((response) => response.json())
    .then((data) => {
      const table = $("#renew").DataTable({
        lengthMenu: [5, 10, 25, 50, 75, 100],
        searching: true,
      });

      table.clear().draw();

      data.forEach((item, index) => {
        const cells = [
          "company_name",
          "department_name",
          "document_type",
          "renewal_date",
          "expiry_date",
          "user_fullname",
        ];
        const rowData = cells.map((key) =>
          key === "user_fullname"
            ? `${item.user_firstname} ${item.user_lastname}`
            : item[key]
        );

        // Add a row to the table
        table.row.add([index + 1, ...rowData]).draw();
      });
    });
});

document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/file/valid_documents/")
    .then((response) => response.json())
    .then((data) => {
      const table = $("#valid").DataTable({
        lengthMenu: [5, 10, 25, 50, 75, 100],
        searching: true,
      });

      table.clear().draw();

      data.forEach((item, index) => {
        const cells = [
          "company_name",
          "department_name",
          "document_type",
          "renewal_date",
          "expiry_date",
          "user_fullname",
        ];
        const rowData = cells.map((key) =>
          key === "user_fullname"
            ? `${item.user_firstname} ${item.user_lastname}`
            : item[key]
        );

        // Add a row to the table
        table.row.add([index + 1, ...rowData]).draw();
      });
    });
});
