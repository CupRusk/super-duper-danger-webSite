const express = require("express");
const app = express();
app.use(express.json());

app.post("/register", (req, res) => {
    console.log("Данные пришли:", req.body);
    res.json({ status: "ok", received: req.body });
});

app.listen(3000, () => console.log("Сервер запущен: http://localhost:3000"));

