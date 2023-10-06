let messages = "{{ messages }}";
if (messages.trim()) {
  Toastify({
    text: messages,
    duration: 3000,
    close: true,
    gravity: "top",
    position: "center",
    backgroundColor: "#4caf50",
    stopOnFocus: true,
  }).showToast();
}
