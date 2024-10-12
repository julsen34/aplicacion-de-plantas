package controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import model.User;
import java.io.IOException;
import java.sql.SQLException;

import com.example.UserDAO;

/**
 *  implementation class RegisterServlet
 */
@SuppressWarnings("unused")
public class RegisterServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	private UserDAO userDAO = new UserDAO();
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RegisterServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String username = request.getParameter("username");
		String email = request.getParameter("email");
		String password = request.getParameter("password");
		
		User newUser = new User();
		
		newUser.SetUsername(username);
		newUser.SetEmail(email);
		newUser.setPassword(password);
		
		try {
			if(userDAO.registerUser(newUser)) {
				response.sendRedirect("login.jsp");
			}else {
				response.sendRedirect("register.jsp");
			}
		} catch (SQLException | IOException e) {
			e.printStackTrace();
		}
		
	}
}
