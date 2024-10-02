const express = require('express');
const router = express.Router();
const Planta = require('../models/Planta');

// GET todas las plantas
router.get('/', async (req, res) => {
    try {
        const plantas = await Planta.find();
        res.json(plantas);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error al obtener plantas' });
    }
});

// POST nueva planta
router.post('/', async (req, res) => {
    try {
        const nuevaPlanta = new Planta(req.body);
        await nuevaPlanta.save();
        res.status(201).json(nuevaPlanta);
    } catch (err) {
        console.error(err);
        res.status(400).json({ message: 'Error al agregar nueva planta' });
    }
});

// DELETE planta por ID
router.delete('/:id', async (req, res) => {
    try {
        const result = await Planta.findByIdAndDelete(req.params.id);
        if (!result) {
            return res.status(404).json({ message: 'Planta no encontrada' });
        }
        res.json({ mensaje: 'Planta eliminada' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error al eliminar planta' });
    }
});

module.exports = router;
