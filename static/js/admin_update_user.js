function updateUserPassword(userId, newPassword) {
  const csrftoken = $("[name=csrfmiddlewaretoken]").val();

  fetch(`http://127.0.0.1:8000/api/users/${userId}/`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      password: newPassword,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log("Password updated successfully:", data);
    })
    .catch((error) => {
      console.error("Error updating password:", error);
    });
}
