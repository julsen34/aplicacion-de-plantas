// server/routes/imagenes.js
const express = require('express');
const multer = require('multer');
const path = require('path');
const router = express.Router();
const Imagen = require('../models/Image');

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + '-' + file.originalname);
    }
});

const upload = multer({ storage: storage });

// GET todas las imágenes
router.get('/', async (req, res) => {
    const imagenes = await Imagen.find();
    res.json(imagenes);
});

// POST nueva imagen
router.post('/', upload.single('file'), async (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).json({ message: 'No se ha subido ningún archivo' });
        }

        const nuevaImagen = new Imagen({
            url: req.file.path,
            descripcion: req.body.descripcion || '',
        });

        await nuevaImagen.save();
        res.status(201).json({ message: 'Imagen cargada con éxito', imagen: nuevaImagen });
    } catch (error) {
        console.error('Error al procesar la imagen:', error);
        res.status(500).json({ message: 'Error al procesar la imagen', error: error.message });
    }
});

// eliminar imagen por ID
router.delete('/:id', async (req, res) => {
    await Imagen.findByIdAndDelete(req.params.id);
    res.json({ mensaje: 'Imagen eliminada' });
});

module.exports = router;
