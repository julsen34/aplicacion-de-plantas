// src/components/PlantAnalysis.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Card, Spinner, Alert } from 'react-bootstrap';

const PlantasList = () => {
    const [plantas, setPlantas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPlantas = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/iaplantas');
                setPlantas(response.data);
                setLoading(false);
            } catch (err) {
                setError(err);
                setLoading(false);
            }
        };

        fetchPlantas();
    }, []);

    if (loading) return <Spinner animation="border" />;
    if (error) return <Alert variant="danger">Error: {error.message}</Alert>;

    return (
        <Container>
            <h1>Lista de Plantas</h1>
            {plantas.map(planta => (
                <Card key={planta._id} className="mb-3">
                    <Card.Body>
                        <Card.Title>{planta.nombre}</Card.Title>
                        <Card.Text>Tipo: {planta.tipo}</Card.Text>
                        <Card.Text>Fecha de siembra: {new Date(planta.fechaSiembra).toLocaleDateString()}</Card.Text>
                    </Card.Body>
                </Card>
            ))}
        </Container>
    );
};

export default PlantasList;
