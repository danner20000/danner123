const rowsPerPage = 5;
let userData = null;

function generateTable(data) {
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
      <td>
      <button class="btn btn-custom btn-sm" onclick="editUser(${
        user.id
      })">Edit</button>
        <button class="btn btn-danger btn-sm" onclick="deleteUser(${
          user.id
        })">Delete</button>
      </td>
    `;
    table.appendChild(tr);
  });
}

function deleteUser(userId) {
  const csrftoken = $("[name=csrfmiddlewaretoken]").val();

  fetch(`http://127.0.0.1:8000/api/users/${userId}/`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log("User deleted successfully:", data);
      fetchUserList(); // Refresh the user list after deletion
    })
    .catch((error) => {
      console.error("Error deleting user:", error);
    });
}

function fetchUserList() {
  fetch("/api/users/")
    .then((response) => response.json())
    .then((data) => {
      userData = data;
      generateTable(data);
    })
    .catch((error) => console.error("Error:", error));
}

fetchUserList();
