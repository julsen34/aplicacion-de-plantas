<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css?family=Raleway|Ubuntu" rel="stylesheet">
    <!-- Estilos -->
    <link rel="stylesheet" href="styles.css">
    <title>Insert title here</title>
</head>
<body>
<!-- Formularios -->
    <div class="contenedor-formularios">
      <!-- Links de los formularios -->
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" href="register.jsp">registrarse</a>
            </li>
        </ul>
        <!-- Contenido de los Formularios -->
        <div class="contenido-tab">
            <!-- Iniciar Sesion -->
            <div id="iniciar-sesion">
                <h1>Iniciar Sesión</h1>
                <form>
                    <div class="contenedor-input">
                        <label for="username">
                            Usuario <span class="req">*</span>
                        </label>
                        <input type="text" name="username" required>
                    </div>

                    <div class="contenedor-input">
                        <label for="email"> 
                            Email <span class="req">*</span>
                        </label>
                        <input type="email" name="email" required>
                    </div>

                    <div class="contenedor-input">
                        <label for="password">
                            Contraseña <span class="req">*</span>
                        </label>
                        <input type="password" name="password" required>
                    </div>
                    <p class="forgot"><a href="#">Se te olvidó la contraseña?</a></p>
                    <input type="submit" class="button button-block" value="Iniciar Sesión">
                </form>
            </div> <!-- Cierre del div de iniciar sesión -->
        </div> <!-- Cierre del div de contenido-tab -->
    </div> <!-- Cierre del div de contenedor-formularios -->

</body>
</html>
