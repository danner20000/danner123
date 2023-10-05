$(document).ready(function () {
  $("#updateUserForm").submit(function (e) {
    e.preventDefault();

    var formData = $(this).serialize();

    var userId = window.location.pathname.split("/").filter(Boolean).pop();

    var csrftoken = $("[name=csrfmiddlewaretoken]").val(); // Get the CSRF token from the page

    $.ajax({
      type: "PATCH",
      url: `/update_user/${userId}/`,
      data: formData,
      dataType: "json",
      headers: {
        "X-CSRFToken": csrftoken, // Include the CSRF token in the request headers
      },
      success: function (data) {
        console.log("User updated successfully:", data);
      },
      error: function (error) {
        console.error("Error updating user:", error);
      },
    });
  });
});
