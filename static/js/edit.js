document.addEventListener("DOMContentLoaded", function () {
  const editModal = document.getElementById("editUserModal");
  const closeEditModalBtn = document.getElementById("closeEditModal");

  // Abrir modal y llenar los datos del usuario
  document.querySelectorAll(".modifyUserBtn").forEach((button) => {
    button.addEventListener("click", function () {
      document.getElementById("editUserId").value = this.dataset.id;
      document.getElementById("editUserName").value = this.dataset.nombre;
      document.getElementById("editUserEmail").value = this.dataset.correo;
      document.getElementById("editUserPassword").value = ""; // Se deja vacío para cambiar solo si es necesario

      editModal.classList.remove("hidden");
      editModal.classList.add("flex");
    });
  });

  // Cerrar modal de edición
  closeEditModalBtn.addEventListener("click", function () {
    editModal.classList.remove("flex");
    editModal.classList.add("hidden");
  });

  // Recargar la página tras enviar el formulario de edición
  document
    .getElementById("editUserForm")
    .addEventListener("submit", function () {
      setTimeout(() => location.reload(), 500);
    });
});
