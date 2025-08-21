document.getElementById("block").addEventListener("submit", async (e) => {
    e.preventDefault();
    await fetch("http://localhost:8000/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: e.target.login.value,
            password: e.target.password.value
        })


    });
});
