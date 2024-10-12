// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import ImageUpload from './components/ImageUpload';
import PlantAnalysis from './components/PlantAnalysis';
import PlantasList from './components/PlantasList';
import Footer from './components/Footer.js';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <div className="container mt-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/image-upload" element={<ImageUpload />} />
            <Route path="/plant-analysis" element={<PlantAnalysis />} />
            <Route path="/plantas-list" element={<PlantasList />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
    
  );
}

function Home() {
  return (
    <section>
      <h1>Análisis de Imágenes de Plantas</h1>
      <h2 id="inder">¡HOLA! Nos alegra que estés en nuestra página de implementación de software para el cultivo.</h2>
      <p>Nuestro mundo verde, donde la naturaleza se encuentra con innovación. En nuestra página web de cultivo de plantas, exploraremos juntos el fascinante mundo de la jardinería y agricultura sostenible. Desde la belleza de las flores hasta la producción de alimentos frescos y saludables. ¡PREPÁRATE! ¡PARA INSPIRARTE Y APRENDER A CÓMO CULTIVAR TU PROPIO OASIS VERDE!</p>
      <p><strong>Información sobre nosotros:</strong> Nuestro objetivo y meta de este proyecto es ayudarte a revisar tus plantas de manera sencilla a través de tu teléfono o computadora. Te enviaremos notificaciones sobre la temperatura y la hidratación para que tus plantas crezcan grandes y fuertes.</p>
      </section>
  );
  
}

export default App;