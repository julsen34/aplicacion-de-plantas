<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" >
    <link href="https://fonts.googleapis.com/css?family=Raleway|Ubuntu" rel="stylesheet">
    <title>Nuevo Usuario</title>
</head>
<body>
    <div class="container mt-5">

        <!-- Registrarse -->
        <div id="registrarse" class="mt-4">
            <h1>Registrarse</h1>
            <form>
                <div class="mb-3">
                    <label for="username" class="form-label"><span class="text-danger"></span></label>
                    <input type="text" name="username" id="username" class="form-control" placeholder="nombre completo" required>
                </div>
                <div class="mb-3">
                    <label for="email" class="form-label"><span class="text-danger"></span></label>
                    <input type="email" name="email" id="email" class="form-control" placeholder="email" required>
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label"><span class="text-danger"></span></label>
                    <input type="password" name="password" id="password" class="form-control" placeholder="Contraseña" required>
                </div>
                <div class="mb-3">
                    <label for="confirm_password" class="form-label"><span class="text-danger"></span></label>
                    <input type="password" name="confirm_password" id="confirm_password" class="form-control" placeholder="Repetir contraseña" required>
                </div>
                <button type="submit" value="Registrarse">Registrarse</button>
            </form>
        </div>
    </div>

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
</body>
</html>
