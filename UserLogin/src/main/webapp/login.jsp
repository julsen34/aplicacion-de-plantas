<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Enlace a los estilos externos -->
    <link rel="stylesheet" type="text/css" href="css/styles.css">
    <!-- Fuente de Google -->
    <link href="https://fonts.googleapis.com/css?family=Raleway|Ubuntu" rel="stylesheet">
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Iniciar Sesión</title>
</head>
<body>
    <!-- Cabecera -->
    <div class="header">
        <h2>Iniciar Sesión</h2>
    </div>

    <!-- Contenedor de formularios -->
    <div class="contenedor-formularios">
        <!-- Formulario de inicio de sesión -->
        <div id="iniciar-sesion">
            <h1>Iniciar Sesión</h1>
            
            <!-- Mostrar mensaje de error si el login falla -->
            <%
                String errorMessage = (String) request.getAttribute("errorMessage");
                if (errorMessage != null) {
            %>
                <p style="color: red;"><%= errorMessage %></p>
            <%
                }
            %>

            <form action="login" method="post">
                <div class="contenedor-input">
                    <label for="username">Usuario <span class="req">*</span></label>
                    <input type="text" name="username" required>
                </div>

                <div class="contenedor-input">
                    <label for="password">Contraseña <span class="req">*</span></label>
                    <input type="password" name="password" required>
                </div>

                <p class="forgot"><a href="#">¿Olvidaste tu contraseña?</a></p>
                <input type="submit" class="button button-block" value="Iniciar Sesión">
            </form>
            <p>¿Es tu primera vez aquí? <a href="register.jsp">Regístrate</a></p>
        </div>
    </div>
    
    <!-- Pie de página -->
    <div class="footer">
        © 2024 Análisis de Imágenes para el Crecimiento de Plantas
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

