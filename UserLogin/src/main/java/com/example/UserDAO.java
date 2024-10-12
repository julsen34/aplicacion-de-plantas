package com.example;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import model.User;

public class UserDAO {

	public boolean registerUser(User user) throws SQLException {
		
		Connection conectar = DatabaseConnection.getconnection();
		String consulta = "INSERT INTO users(username,email,passwod) VALUES(?, ?, ?)";
		try ( 	
			PreparedStatement sentencia = conectar.prepareStatement(consulta)){
				sentencia.setString(1, user.getUsername());
				sentencia.setString(2, user.getEmail());
				sentencia.setString(3, user.getPassword());
				
				int resultado = sentencia.executeUpdate();
				
				if (resultado > 0) {
					return true;
			}
		}catch(SQLException e){
				System.out.println(e.getMessage());
				return false;
			}	
		return false;
		}
}