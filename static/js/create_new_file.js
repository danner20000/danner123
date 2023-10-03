function saveFile() {
  var select_BU = $("#id_select_BU").val();
  var document_type = $("#id_document_type").val();
  var department = $("#id_department").val();
  var upload_file = $("#id_upload_file")[0].files[0];
  var renewal_date = $("#id_renewal_date").val();
  var expiry_date = $("#id_expiry_date").val();

  var formData = new FormData();
  formData.append("select_BU", select_BU);
  formData.append("document_type", document_type);
  formData.append("department", department);
  formData.append("upload_file", upload_file);
  formData.append("renewal_date", renewal_date);
  formData.append("expiry_date", expiry_date);

  $.ajax({
    type: "POST",
    url: "/api/file/",
    data: formData,
    contentType: false,
    processData: false,
    success: function (response) {
      console.log("File data saved successfully:", response);
    },
    error: function (error) {
      console.error("Error saving file data:", error);
    },
  });
}
