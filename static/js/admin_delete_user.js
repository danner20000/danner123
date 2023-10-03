function deleteUser(userId) {
  fetch(`/api/users/${userId}/`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log("User deleted successfully:", data);
    })
    .catch((error) => {
      console.error("Error deleting user:", error);
    });
}
