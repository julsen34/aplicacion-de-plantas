// src/components/ImageUpload.js
import React, { useState } from 'react';
import { Form, Button, ProgressBar, Alert, Container } from 'react-bootstrap';
import axios from 'axios';

const ImageUpload = () => {
    const [file, setFile] = useState(null);
    const [uploadProgress, setUploadProgress] = useState(0);
    const [uploadSuccess, setUploadSuccess] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setUploadSuccess(false);
        setErrorMessage('');
    };

    const handleUpload = async () => {
        if (!file) {
            setErrorMessage("Por favor, selecciona una imagen.");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            await axios.post('http://localhost:5000/api/imagenes', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
                onUploadProgress: (progressEvent) => {
                    const percent = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    setUploadProgress(percent);
                },
            });

            setUploadSuccess(true);
            setUploadProgress(100);
            setFile(null);
        } catch (error) {
            console.error('Error al cargar la imagen:', error);
            setErrorMessage(`Error al procesar la imagen: ${error.response?.data?.message || error.message}`);
            setUploadProgress(0);
        }
    };

    return (
        <Container className="mt-5">
            <h2>Procesador de Imágenes</h2>
            <p>En esta sección puedes cargar y procesar imágenes de tus plantas para realizar análisis detallados.</p>
            
            <Form>
                <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>{file ? file.name : "Seleccionar archivo"}</Form.Label>
                    <Form.Control type="file" onChange={handleFileChange} />
                </Form.Group>
                <Button 
                    className="mt-3" 
                    variant="success" 
                    onClick={handleUpload}
                    disabled={!file}
                >
                    Procesar Imagen
                </Button>
            </Form>

            {uploadProgress > 0 && (
                <ProgressBar className="mt-3" now={uploadProgress} label={`${uploadProgress}%`} />
            )}

            {uploadSuccess && (
                <Alert className="mt-3" variant="success">¡Imagen procesada con éxito!</Alert>
            )}
            {errorMessage && (
                <Alert className="mt-3" variant="danger">{errorMessage}</Alert>
            )}
        </Container>
    );
};

export default ImageUpload;
