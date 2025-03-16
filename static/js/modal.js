document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("userModal");
  const openModalBtn = document.getElementById("addUserBtn");
  const closeModalBtn = document.getElementById("closeModal");

  // Abrir modal
  openModalBtn.addEventListener("click", function () {
    modal.classList.remove("hidden");
    modal.classList.add("flex");
  });

  // Cerrar modal
  closeModalBtn.addEventListener("click", function () {
    modal.classList.remove("flex");
    modal.classList.add("hidden");
  });

  // Recargar la página tras enviar el formulario
  document.getElementById("userForm").addEventListener("submit", function () {
    setTimeout(() => location.reload(), 500);
  });
});
