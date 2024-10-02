package com.example.controller;

import com.example.dao.UserDAO;
import com.example.model.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Recibir los parámetros del formulario
        String username = request.getParameter("username");
        String email = request.getParameter("email");
        String password = request.getParameter("password");

        // Crear un objeto User con los datos recibidos
        User user = new User(username, email, password);

        // Crear un objeto UserDAO para manejar la lógica de la base de datos
        UserDAO userDAO = new UserDAO();

        // Verificar si el usuario ya existe o registrar un nuevo usuario
        if (userDAO.registerUser(user)) {
            response.sendRedirect("success.jsp"); // Registro exitoso
        } else {
            response.sendRedirect("error.jsp"); // Error en el registro
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Redirigir al formulario de registro si se accede a través de GET
        response.sendRedirect("register.jsp");
    }
}
