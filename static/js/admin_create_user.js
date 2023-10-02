function saveUser() {
  var firstName = $("#firstName").val();
  var lastName = $("#lastName").val();
  var email = $("#email").val();
  var password = $("#password").val();
  var confirmPassword = $("#confirmPassword").val();

  // Check if passwords match
  if (password !== confirmPassword) {
    console.error("Passwords do not match.");
    // You can display an error message or perform other actions
    return;
  }

  // Create a JSON object with the user data
  var userData = {
    first_name: firstName,
    last_name: lastName,
    email: email,
    password: password,
  };

  // Send an AJAX POST request to your Django backend
  $.ajax({
    type: "POST",
    url: "/api/users/",
    contentType: "application/json",
    data: JSON.stringify(userData),
    success: function (response) {
      console.log("User data saved successfully:", response);
      $("#addUserModal").modal("hide");
      // You can add any additional logic here (e.g., updating the table)
    },
    error: function (error) {
      // Handle the error response
      console.error("Error saving user data:", error);
      // You can display an error message or perform other actions
    },
  });
}
