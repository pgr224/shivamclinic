const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#site-nav");

if (menuToggle && navigation) {
  menuToggle.addEventListener("click", () => {
    const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isExpanded));
    menuToggle.setAttribute("aria-label", isExpanded ? "Open navigation" : "Close navigation");
    navigation.classList.toggle("is-open", !isExpanded);
  });

  function closeNavigation() {
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
    navigation.classList.remove("is-open");
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navigation.classList.contains("is-open")) {
      closeNavigation();
      menuToggle.focus();
    }
  });
  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeNavigation();
  });

}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = new Date().getFullYear();
});

const dateInput = document.querySelector("#visit-date");
if (dateInput) {
  dateInput.min = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Kolkata", year: "numeric", month: "2-digit", day: "2-digit",
  }).format(new Date());
}

const physicianServices = ["General physician", "Fever management", "Diabetes care", "Blood pressure measurement & monitoring", "ECG", "General consultations", "Preventive health checks", "Industrial & occupational health", "Pathology & report review"];
const appointmentForm = document.querySelector("#appointment-form");
if (appointmentForm) {
  const selectedService = new URLSearchParams(window.location.search).get("service");
  const serviceInput = appointmentForm.querySelector('[name="service"]');
  if (selectedService && Array.from(serviceInput.options).some((option) => option.value === selectedService)) {
    serviceInput.value = selectedService;
    if (physicianServices.includes(selectedService)) appointmentForm.elements.doctor.value = "Dr Prashant Rabadia";
    else if (selectedService !== "Not sure — please advise") appointmentForm.elements.doctor.value = "Dr Krishna Kapadiya";
  }

  appointmentForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!appointmentForm.reportValidity()) return;

    const fields = new FormData(appointmentForm);
    const request = [
      "Hello Shivam Clinic, I would like to request an appointment.",
      `Name: ${fields.get("name")}`,
      `Phone: ${fields.get("phone")}`,
      `Service: ${fields.get("service")}`,
      fields.get("doctor") ? `Preferred doctor: ${fields.get("doctor")}` : "",
      fields.get("date") ? `Preferred date: ${fields.get("date")}` : "",
      fields.get("message") ? `Message: ${fields.get("message")}` : "",
    ].filter(Boolean).join("\n");

    const whatsappUrl = `https://wa.me/919824610611?text=${encodeURIComponent(request)}`;
    window.open(whatsappUrl, "_blank", "noopener,noreferrer");
    document.querySelector("#form-status").textContent = "Your WhatsApp draft is ready. Send it in WhatsApp, then wait for our team to confirm your visit.";
  });
}

const galleryFilters = document.querySelector(".gallery-toolbar");
if (galleryFilters) {
  galleryFilters.hidden = false;
  const cards = Array.from(document.querySelectorAll(".gallery-item"));
  galleryFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-gallery-filter]");
    if (!button) return;
    const filter = button.dataset.galleryFilter;
    galleryFilters.querySelectorAll("button").forEach((item) => {
      item.setAttribute("aria-pressed", String(item === button));
    });
    cards.forEach((card) => {
      card.hidden = filter !== "all" && card.dataset.galleryCategory !== filter;
    });
    const count = cards.filter((card) => !card.hidden).length;
    document.querySelector("#gallery-count").textContent = `Showing ${count} care image${count === 1 ? "" : "s"}${filter === "all" ? "" : ` · ${button.textContent}`}`;
  });
}
