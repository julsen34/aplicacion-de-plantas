package controller;

import com.example.UserDAO;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;
import java.sql.SQLException;
import model.User;


public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        UserDAO userDAO = new UserDAO();
        User user = null;
		try {
			user = userDAO.validateLogin(username, password);
		} catch (SQLException e) {
			e.printStackTrace();
		}

        if (user != null) {
            // Si el login es exitoso, guardar el usuario en la sesión
            HttpSession session = request.getSession();
            session.setAttribute("user", user);

            // Redirigir a la página de inicio
            response.sendRedirect("aplicacion-de-plantas/client/src/App.js");
        } else {
            // Si el login falla, redirigir a la página de login con un mensaje de error
            request.setAttribute("errorMessage", "Usuario o contraseña incorrectos");
            request.getRequestDispatcher("login.jsp").forward(request, response);
        }
    }
}