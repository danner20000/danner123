document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/file/expired_documents/")
    .then((response) => response.json())
    .then((data) => {
      const numberOfExpiredFile = data.length;
      const numberOfExpiredFileElement = document.getElementById("expired");
      numberOfExpiredFileElement.innerText = `${numberOfExpiredFile}`;
    });

  fetch("/api/file/valid_documents/")
    .then((response) => response.json())
    .then((data) => {
      const numberOfValidFile = data.length;
      const numberOfValidFileElement = document.getElementById("valid");
      numberOfValidFileElement.innerText = `${numberOfValidFile}`;
    });

  fetch("/api/file/due_for_renewal_documents/")
    .then((response) => response.json())
    .then((data) => {
      const numberofToRenewFile = data.length;
      const numberofToRenewFileElement = document.getElementById("to_be_renew");
      numberofToRenewFileElement.innerText = `${numberofToRenewFile}`;
    });
});
