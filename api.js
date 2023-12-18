const express = require("express");
const app = express();

const { pool } = require("mysql2");

const db = pool({
  host: "mariadb",
  port: 3306,
  user: process.env.MARIADB_USERNAME,
  password: process.env.MARIADB_PASSWORD,
  database: "mydb"
});

app.get("/pacientes/:id", (req, res) => {
  const idPaciente = req.params.id;

  // Obtener los datos del paciente de la base de datos
  const paciente = await db.query("SELECT * FROM pacientes WHERE id = ?", [idPaciente]);

  // Devolver los datos del paciente en formato JSON
  res.json(paciente);
});

app.listen(3000, () => {
  console.log("API escuchando en el puerto 3000");
});