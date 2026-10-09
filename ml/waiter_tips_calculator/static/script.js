
"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("tipForm");

    if (!form) {
        return;
    }

    const billInput = document.getElementById("total_bill");
    const sizeInput = document.getElementById("size");
    const predictButton = document.getElementById("predictButton");
    const buttonText = document.getElementById("buttonText");
    const buttonArrow = document.getElementById("buttonArrow");

    form.addEventListener("submit", (event) => {
        const bill = Number(billInput.value);
        const size = Number(sizeInput.value);

        if (!Number.isFinite(bill) || bill <= 0 || bill > 100000) {
            event.preventDefault();
            billInput.setCustomValidity(
                "Enter a bill amount greater than zero and no more than 100000."
            );
            billInput.reportValidity();
            billInput.focus();
            return;
        }

        billInput.setCustomValidity("");

        if (!Number.isInteger(size) || size < 1 || size > 50) {
            event.preventDefault();
            sizeInput.setCustomValidity(
                "Enter a whole number between 1 and 50."
            );
            sizeInput.reportValidity();
            sizeInput.focus();
            return;
        }

        sizeInput.setCustomValidity("");

        if (!form.checkValidity()) {
            event.preventDefault();
            form.reportValidity();
            return;
        }

        // Prevent duplicate submissions and show loading feedback.
        if (predictButton.disabled) {
            event.preventDefault();
            return;
        }

        predictButton.disabled = true;
        buttonText.textContent = "Predicting...";
        buttonArrow.textContent = "⏳";
    });

    billInput.addEventListener("input", () => {
        billInput.setCustomValidity("");
    });

    sizeInput.addEventListener("input", () => {
        sizeInput.setCustomValidity("");
    });
});
