// server/index.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path'); 
const fs = require('fs');
require('dotenv').config(); 

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Configurar la carpeta de uploads
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

app.get('/', (req, res) => {
    res.send('Servidor funcionando');
});

// Definir rutas de plantas
const plantasRoute = require('./routes/plantas');
app.use('/api/plantas', plantasRoute);

// Definir la ruta para las imágenes
const imagenesRoute = require('./routes/images');
app.use('/api/imagenes', imagenesRoute);

// Conectar a MongoDB
mongoose.connect(process.env.MONGODB_URI)
    .then(() => {
        console.log('Conectado a MongoDB');
        const PORT = process.env.PORT || 5000;
        app.listen(PORT, () => {
            console.log(`Servidor corriendo en el puerto ${PORT}`);
        });
    })
    .catch(err => console.error('Error de conexión a MongoDB:', err));

// Después de definir todas tus rutas
app._router.stack.forEach(function(r){
    if (r.route && r.route.path){
        console.log(r.route.path);
    }
});
