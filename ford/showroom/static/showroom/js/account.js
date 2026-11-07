
(() => {
  const form = document.querySelector(".account-form");
  if (!form) return;
  form.addEventListener("submit", () => {
    const submit = form.querySelector('button[type="submit"]');
    submit.disabled = true;
    submit.setAttribute("aria-busy", "true");
    submit.textContent = document.documentElement.lang.startsWith("ar") ? "جارٍ المتابعة…" : "Continuing…";
  });
  window.addEventListener("pageshow", event => {
    if (event.persisted) window.location.reload();
  });
  const rtl = document.documentElement.lang.startsWith("ar");
  const first = form.querySelector('[name="password1"]');
  const confirmation = form.querySelector('[name="password2"]');
  const username = form.querySelector('[name="username"]');
  if (username) {
    username.autocomplete = "username";
    username.autocapitalize = "none";
    username.spellcheck = false;
  }
  form.querySelectorAll('input[type="password"]').forEach(input => {
    input.autocomplete = first ? "new-password" : "current-password";
    const warning = input.closest(".account-field").querySelector("[data-caps-lock]");
    const updateCaps = event => {
      warning.hidden = !event.getModifierState || !event.getModifierState("CapsLock");
    };
    input.addEventListener("keydown", updateCaps);
    input.addEventListener("keyup", updateCaps);
    input.addEventListener("blur", () => { warning.hidden = true; });
  });
  form.querySelectorAll("[data-password-toggle]").forEach(button => {
    button.addEventListener("click", () => {
      const input = document.getElementById(button.getAttribute("aria-controls"));
      const show = input.type === "password";
      input.type = show ? "text" : "password";
      button.setAttribute("aria-pressed", String(show));
      button.setAttribute("aria-label", rtl ? (show ? "إخفاء كلمة المرور" : "إظهار كلمة المرور") : (show ? "Hide password" : "Show password"));
      button.querySelector(".password-eye-slash").toggleAttribute("hidden", !show);
    });
  });
  function updateGuidance() {
    form.querySelector("[data-length-check]").classList.toggle("is-met", first.value.length >= 8);
    form.querySelector("[data-number-check]").classList.toggle("is-met", /[^0-9]/.test(first.value));
    const status = form.querySelector("[data-password-match]");
    status.textContent = !confirmation.value ? "" : first.value === confirmation.value
      ? (rtl ? "كلمتا المرور متطابقتان" : "Passwords match")
      : (rtl ? "كلمتا المرور غير متطابقتين" : "Passwords do not match");
  }
  if (first && confirmation) {
    first.addEventListener("input", updateGuidance);
    confirmation.addEventListener("input", updateGuidance);
  }
  const invalid = form.querySelector('[aria-invalid="true"]');
  const errors = form.querySelector(".errorlist");
  if (invalid) invalid.focus();
  else if (errors && username) username.focus();
})();
