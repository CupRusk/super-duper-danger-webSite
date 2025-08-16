document.getElementById("block").addEventListener("submit", async (e) => {
    e.preventDefault();
    await fetch("http://localhost:3000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            login: e.target.login.value,
            password: e.target.password.value
        })
    });
});
