document.addEventListener("DOMContentLoaded", function () {
  function confirmDelete(event, form) {
    event.preventDefault(); // Evita el envío automático del formulario
    if (confirm("¿Estás seguro de que quieres eliminar este usuario?")) {
      form.submit(); // Envía el formulario si el usuario confirma
    }
  }

  document.querySelectorAll("form[action*='delete_user']").forEach((form) => {
    form.addEventListener("submit", function (event) {
      confirmDelete(event, this);
    });
  });
});
