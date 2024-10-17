package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

    private static Connection connection = null;
    private static final String URL = "jdbc:sqlite:C:/sqlite/application.db";
    private static final String DRIVER = "org.sqlite.JDBC";

    public static Connection getConnection() throws SQLException {
        if (connection == null) {
            try {
                Class.forName(DRIVER);
                connection = DriverManager.getConnection(URL);
                System.out.println("Conexión establecida con la base de datos.");
            } catch (ClassNotFoundException e) {
                throw new SQLException("No se encontró el driver JDBC para SQLite.", e);
            }
        }
        return connection;
    }

    public static void closeConnection() {
        if (connection != null) {
            try {
                connection.close();
                connection = null;
                System.out.println("Conexión cerrada.");
            } catch (SQLException e) {
                System.err.println("Error cerrando la conexión: " + e.getMessage());
            }
        }
    }
}
