const mongoose = require('mongoose');

const ImagenSchema = new mongoose.Schema({
    url: { type: String, required: true },
    descripcion: { type: String, default: '' },
    fechaSubida: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Imagen', ImagenSchema);
