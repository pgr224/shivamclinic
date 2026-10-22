const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#site-nav");

if (menuToggle && navigation) {
  menuToggle.addEventListener("click", () => {
    const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isExpanded));
    menuToggle.setAttribute("aria-label", isExpanded ? "Open navigation" : "Close navigation");
    navigation.classList.toggle("is-open", !isExpanded);
  });

  navigation.querySelectorAll("a").forEach((link) => {
    if (link.pathname === window.location.pathname || (link.pathname.endsWith("/") && window.location.pathname.endsWith("/"))) {
      link.setAttribute("aria-current", "page");
    }
  });
}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = new Date().getFullYear();
});

const dateInput = document.querySelector("#visit-date");
if (dateInput) {
  dateInput.min = new Date().toISOString().split("T")[0];
}

const appointmentForm = document.querySelector("#appointment-form");
if (appointmentForm) {
  appointmentForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!appointmentForm.reportValidity()) return;

    const fields = new FormData(appointmentForm);
    const request = [
      "Hello Shivam Clinic, I would like to request an appointment.",
      `Name: ${fields.get("name")}`,
      `Phone: ${fields.get("phone")}`,
      `Service: ${fields.get("service")}`,
      fields.get("date") ? `Preferred date: ${fields.get("date")}` : "",
      fields.get("message") ? `Message: ${fields.get("message")}` : "",
    ].filter(Boolean).join("\n");

    const whatsappUrl = `https://wa.me/917575826155?text=${encodeURIComponent(request)}`;
    window.open(whatsappUrl, "_blank", "noopener,noreferrer");
  });
}
