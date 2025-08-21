document.getElementById("block").addEventListener("submit", async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: e.target.login.value,
            password: e.target.password.value
        })


    });
    const data = await res.json();
    console.log(data);
});
