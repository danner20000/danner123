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
      <td>
      <a class="btn btn-custom btn-sm edit-user-btn" href="update_user" data-user-id="{{ user.id }}">Edit</a>
        <button class="btn btn-danger btn-sm" onclick="deleteUser(${
          user.id
        })">Delete</button>
      </td>
    `;
    table.appendChild(tr);
  });
}

document.addEventListener("click", function (event) {
  if (event.target.classList.contains("edit-user-btn")) {
    var userId = event.target.dataset.userId;
    window.location.href = `update_user/${userId}/`;
  }
});

async function deleteUser(userId) {
  const csrftoken = $("[name=csrfmiddlewaretoken]").val();

  try {
    const response = await fetch(`http://127.0.0.1:8000/api/users/${userId}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("User deleted successfully:", data);
    await fetchUserList(); // Refresh the user list after deletion
  } catch (error) {
    console.error("Error deleting user:", error);
  }
}

async function fetchUserList() {
  try {
    const response = await fetch("/api/users/");
    const data = await response.json();
    userData = data;
    await generateTable(data);
  } catch (error) {
    console.error("Error:", error);
  }
}

fetchUserList();
