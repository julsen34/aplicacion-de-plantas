<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Enlace a los estilos externos -->
    <link rel="stylesheet" type="text/css" href="css/register.css">
    <!-- Fuente de Google -->
    <link href="https://fonts.googleapis.com/css?family=Raleway|Ubuntu" rel="stylesheet">
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Registrarse</title>
</head>
<body>
    <!-- Cabecera -->
    <div class="header">
        <h2>Registrarse</h2>
    </div>

    <!-- Contenedor de formularios -->
    <div class="register-container">
        <!-- Formulario de registro -->
        <div id="registrarse">
            <h1>Registrarse</h1>

            <!-- Mostrar mensaje de error si el registro falla -->
            <%
                String errorMessage = (String) request.getAttribute("errorMessage");
                if (errorMessage != null) {
            %>
                <p style="color: red;"><%= errorMessage %></p>
            <%
                }
            %>

            <form action="register" method="post">
                <div class="mb-3">
                    <label for="username" class="form-label">Nombre Completo</label>
                    <input type="text" name="username" id="username" class="form-control" placeholder="Nombre Completo" required>
                </div>

                <div class="mb-3">
                    <label for="email" class="form-label">Email</label>
                    <input type="email" name="email" id="email" class="form-control" placeholder="Correo Electrónico" required>
                </div>

                <div class="mb-3">
                    <label for="password" class="form-label">Contraseña</label>
                    <input type="password" name="password" id="password" class="form-control" placeholder="Contraseña" required>
                </div>

                <div class="mb-3">
                    <label for="confirm_password" class="form-label">Repetir Contraseña</label>
                    <input type="password" name="confirm_password" id="confirm_password" class="form-control" placeholder="Repetir Contraseña" required>
                </div>

                <button type="submit" class="btn btn-success w-100">Registrarse</button>
            </form>
            <p>¿Ya tienes un usuario? <a href="login.jsp">Iniciar sesión</a></p>
        </div>
    </div>

    <!-- Verificación de contraseñas -->
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const registerForm = document.querySelector('#registrarse form');
            const password = registerForm.querySelector('input[name="password"]');
            const confirmPassword = registerForm.querySelector('input[name="confirm_password"]');

            registerForm.addEventListener('submit', function (event) {
                if (password.value !== confirmPassword.value) {
                    alert('Las contraseñas no coinciden');
                    event.preventDefault();  // Evitar el envío del formulario
                }
            });
        });
    </script>

    <!-- Pie de página -->
    <div class="footer">
        © 2024 Análisis de Imágenes para el Crecimiento de Plantas
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

