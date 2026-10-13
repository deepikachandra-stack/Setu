const serviceInput = document.getElementById("serviceInput");
const serviceForm = document.getElementById("serviceForm");
const formMessage = document.getElementById("formMessage");
const submitButton = serviceForm.querySelector('button[type="submit"]');

function selectService(service) {
  serviceInput.value = service;
  formMessage.textContent = "";
  serviceInput.focus();
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
    formMessage.textContent =
      "Please enter the government service you need help with.";
    serviceInput.focus();
    return;
  }

  if (service.length > 200) {
    formMessage.textContent =
      "Please describe the service in 200 characters or fewer.";
    serviceInput.focus();
    return;
  }

  formMessage.textContent = "Preparing your service guide…";
  submitButton.disabled = true;
  submitButton.setAttribute("aria-busy", "true");

  const destination =
    "result.html?service=" + encodeURIComponent(service);

  window.location.href = destination;
});
