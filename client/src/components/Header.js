// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';

const Header = () => {
    return (
        <Navbar bg="success" variant="dark" expand="lg">
            <Navbar.Brand as={Link} to="/">Análisis de Imágenes para el Crecimiento de Plantas</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link as={Link} to="/image-upload">Procesador de Imágenes</Nav.Link>
                    <Nav.Link as={Link} to="/plant-analysis">Respuestas IA</Nav.Link>
                    <Nav.Link as={Link} to="/plantas-list">Historial de Imágenes</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
};

export default Header;
