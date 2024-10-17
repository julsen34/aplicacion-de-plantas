package controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.User;
import java.io.IOException;
import java.sql.SQLException;
import com.example.UserDAO;

public class RegisterServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    
    private UserDAO userDAO = new UserDAO();
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RegisterServlet() {
        super();
    }

    /**
     * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String email = request.getParameter("email");
        String password = request.getParameter("password");
        
        // Creando el nuevo usuario
        User newUser = new User();
        newUser.setUsername(username);  // Cambio a setUsername
        newUser.setEmail(email);        // Cambio a setEmail
        newUser.setPassword(password);
        
        try {
            if(userDAO.registerUser(newUser)) {
                // Redirigir al login en caso de éxito
                response.sendRedirect("login.jsp");
            } else {
                // Si falla, redirigir al registro con un mensaje de error
                request.setAttribute("errorMessage", "No se pudo registrar el usuario. Inténtalo de nuevo.");
                request.getRequestDispatcher("register.jsp").forward(request, response);
            }
        } catch (SQLException e) {
            e.printStackTrace();
            request.setAttribute("errorMessage", "Error en la base de datos: " + e.getMessage());
            request.getRequestDispatcher("register.jsp").forward(request, response);
        }
    }
}
