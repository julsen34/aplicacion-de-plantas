package com.example;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import model.User;

public class UserDAO {

    // Registrar nuevo usuario
    public boolean registerUser(User user) throws SQLException {
        Connection conectar = DatabaseConnection.getConnection();
        String consulta = "INSERT INTO users(username, email, password) VALUES(?, ?, ?)";
        
        try (PreparedStatement sentencia = conectar.prepareStatement(consulta)) {
            sentencia.setString(1, user.getUsername());
            sentencia.setString(2, user.getEmail());
            
            // Aquí deberías aplicar hash a la contraseña antes de almacenarla
            // Ejemplo: String hashedPassword = BCrypt.hashpw(user.getPassword(), BCrypt.gensalt());
            sentencia.setString(3, user.getPassword());

            int resultado = sentencia.executeUpdate();
            return resultado > 0;
        } catch (SQLException e) {
            System.out.println("Error al registrar el usuario: " + e.getMessage());
            throw new SQLException("Error al registrar el usuario", e);  // Lanza una excepción con más información
        }
    }

    // Validar login
    public User validateLogin(String username, String password) throws SQLException {
        Connection conectar = DatabaseConnection.getConnection();
        String consulta = "SELECT * FROM users WHERE username = ? AND password = ?";

        try (PreparedStatement sentencia = conectar.prepareStatement(consulta)) {
            sentencia.setString(1, username);

            // Aquí también deberías verificar la contraseña hash almacenada
            // Ejemplo: if (BCrypt.checkpw(password, storedPassword)) { ... }
            sentencia.setString(2, password);

            ResultSet rs = sentencia.executeQuery();

            if (rs.next()) {
                // Crear un objeto User con los datos obtenidos de la consulta
                User user = new User();
                user.setId(rs.getInt("id"));
                user.setUsername(rs.getString("username"));
                user.setEmail(rs.getString("email"));
                user.setPassword(rs.getString("password"));

                return user;  // Si las credenciales son válidas, retornar el objeto User
            }
        } catch (SQLException e) {
            System.out.println("Error al validar el login: " + e.getMessage());
        }

        return null;  // Si las credenciales no son válidas, retornar null
    }
}
