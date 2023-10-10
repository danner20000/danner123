$(document).ready(function () {
  $(".delete-button").click(function () {
    var userId = $(this).data("user-id");
    var confirmation = confirm("Are you sure you want to delete this user?");

    if (confirmation) {
      $.ajax({
        type: "DELETE",
        url: "/api/users/" + userId + "/",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
        success: function () {
          $(this).closest("tr").remove();
        },
        error: function () {
          alert("Error deleting user");
        },
      });
    }
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
