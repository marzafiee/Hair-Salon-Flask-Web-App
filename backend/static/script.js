document.getElementById("book-now").addEventListener("click", () => {
    const message = document.getElementById("message");
    message.textContent = "Thank you for booking! We’ll contact you soon.";
    message.style.color = "green";
});
