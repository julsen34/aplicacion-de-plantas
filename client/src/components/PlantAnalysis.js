// src/components/PlantAnalysis.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Card, Spinner, Alert } from 'react-bootstrap'; 

const PlantAnalysis = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:5000/predict');
                setData(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) return (
        <Container className="text-center mt-5">
            <Spinner animation="border" />
            <p>Loading...</p>
        </Container>
    );

    if (error) return (
        <Container className="mt-5">
            <Alert variant="danger">Error: {error.message}</Alert>
        </Container>
    );

    return (
        <Container className="mt-5">
            <h1 className="mb-4">Plant Analysis Data</h1>
            {data ? (
                <Card>
                    <Card.Body>
                        <pre>{JSON.stringify(data, null, 2)}</pre>
                    </Card.Body>
                </Card>
            ) : (
                <p>No data available.</p>
            )}
        </Container>
    );
};

export default PlantAnalysis;
