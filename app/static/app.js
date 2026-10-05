// Task Manager — client-side enhancements

// Prevent accidental double-submit on create-task form
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    forms.forEach((form) => {
        form.addEventListener("submit", (e) => {
            const btn = form.querySelector("button[type='submit']");
            if (btn) {
                btn.disabled = true;
                setTimeout(() => { btn.disabled = false; }, 3000);
            }
        });
    });
});
