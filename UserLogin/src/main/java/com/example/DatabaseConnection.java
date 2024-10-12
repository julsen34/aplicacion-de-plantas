package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

	public static  Connection connection = null;
	
	public static Connection getconnection() throws SQLException {
		if (connection == null) {
    try {
    	String url = "jdbc:sqlite: c:/sqlite/application.db";
    	connection = DriverManager.getConnection(url);
    	}catch(SQLException e) {
    		throw new SQLException("ha habido un error al conectar con la base de datos", e);
    	}
    }
		return connection;
	}
	
}

