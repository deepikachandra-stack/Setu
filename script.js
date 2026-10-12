
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

serviceForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const service = serviceInput.value.trim();

  if (!service) {
    formMessage.textContent =
      "Please enter the government service you need help with.";
    serviceInput.focus();
    return;
  }

  formMessage.textContent = "Finding your government service...";

  try {
    const response = await fetch(
      `http://127.0.0.1:5000/process?service=${encodeURIComponent(service)}`
    );

    const data = await response.json();

    if (!response.ok || data.error) {
      formMessage.textContent =
        data.error || "Unable to find the service. Please try again.";
      return;
    }

    sessionStorage.setItem("setuProcessData", JSON.stringify(data));
    sessionStorage.setItem("setuService", service);

    window.location.href =
      "result.html?service=" + encodeURIComponent(service);
  } catch (error) {
    formMessage.textContent =
      "Cannot connect to Setu. Please make sure the backend is running.";
    console.error("Backend connection error:", error);
  }
});
