$(document).ready(function () {
  $("#updateUserForm").submit(function (e) {
    e.preventDefault();

    var formData = $(this).serialize();

    var userId = window.location.pathname.split("/").filter(Boolean).pop();

    $.ajax({
      type: "PATCH",
      url: `/update_user/${userId}/`,
      data: formData,
      dataType: "json",
      success: function (data) {
        console.log("User updated successfully:", data);
      },
      error: function (error) {
        console.error("Error updating user:", error);
      },
    });
  });
});

$(document).ready(function () {
  $(".delete-button").click(function () {
    var userId = $(this).data("user-id");
  });

  $(".edit-user-btn").click(function (e) {
    e.preventDefault();
    var userId = $(this).data("user-id");
    window.location.href = `/update_user/${userId}/`;
  });
});
