document.getElementById("block").addEventListener("submit", async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:8000/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: e.target.login.value,
            password: e.target.password.value
        })
    });

    if (response.ok) {
        window.location.href = "Happy.html"; 
    } 
    
    else {
        
        const errorData = await response.json().catch(() => ({}));
        alert(errorData.message || "Ошибка регистрации");
    }
});
