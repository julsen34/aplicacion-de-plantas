// server/models/Planta.js
const mongoose = require('mongoose');

const PlantaSchema = new mongoose.Schema({
    nombre: String,
    tipo: String,
    fechaSiembra: Date,
});

module.exports = mongoose.model('Planta', PlantaSchema);
