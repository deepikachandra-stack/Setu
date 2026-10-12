const serviceInput = document.getElementById("serviceInput");
const serviceForm = document.getElementById("serviceForm");
const formMessage = document.getElementById("formMessage");

function selectService(service) {
  serviceInput.value = service;
  serviceInput.focus();
  formMessage.textContent = "";
}

document.querySelectorAll("[data-service]").forEach((button) => {
  button.addEventListener("click", () => {
    selectService(button.dataset.service);
  });
});

serviceForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const service = serviceInput.value.trim();

  if (!service) {
    formMessage.textContent = "Please enter the government service you need help with.";
    serviceInput.focus();
    return;
  }

  // Frontend demo only: this does not yet connect to an AI/backend.
  const destination = "result.html?service=" + encodeURIComponent(service);
  window.location.href = destination;
});
