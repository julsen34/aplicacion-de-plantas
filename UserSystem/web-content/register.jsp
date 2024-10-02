<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Raleway|Ubuntu" rel="stylesheet">

    <!-- Estilos -->
    <link rel="stylesheet" href="css/styles.css">

    <title>Formulario Login y Registro de Usuarios</title>
</head>
<body>

   <!-- Formularios -->
    <div class="contenedor-formularios">
        <!-- Links de los formularios -->
        <ul class="contenedor-tabs">
            <li class="tab tab-segunda active"><a href="#iniciar-sesion">Iniciar Sesión</a></li>
            <li class="tab tab-primera"><a href="#registrarse">Registrarse</a></li>
        </ul>

        <!-- Contenido de los Formularios -->
        <div class="contenido-tab">
            <!-- Iniciar Sesion -->
            <div id="iniciar-sesion">
                <h1>Iniciar Sesión</h1>
                <form action="login" method="post">
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
            </div>

            <!-- Registrarse -->
            <div id="registrarse">
                <h1>Registrarse</h1>
                <form action="register" method="post">
                    <div class="fila-arriba">
                        <div class="contenedor-input">
                            <label for="name">
                                Nombre <span class="req">*</span>
                            </label>
                            <input type="text" name="name" required >
                        </div>

                        <div class="contenedor-input">
                            <label for="lastname">
                                Apellido <span class="req">*</span>
                            </label>
                            <input type="text" name="lastname" required>
                        </div>
                    </div>
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

                    <div class="contenedor-input">
                        <label for="confirm_password">
                            Repetir Contraseña <span class="req">*</span>
                        </label>
                        <input type="password" name="confirm_password" required>
                    </div>

                    <input type="submit" class="button button-block" value="Registrarse">
                </form>
            </div>
        </div>
    </div>
<script>document.addEventListener("DOMContentLoaded", function () {
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
   <script src="js/main.js"></script>

</body>
</html>
