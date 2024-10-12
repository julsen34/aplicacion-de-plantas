package model;

public class User {
private int id;
private String Username;
private String email;
private String password;

//Getters
public int getId() {
	
	return id;
}

public String getUsername() {
	
	return Username;
   }
public String getEmail() {
	
	return email;
   }

public String getPassword() {
	
	return password;
   }

//Setters

public void SetId(int id) {
	this.id=id;
}
public void SetUsername(String username) {
	this.Username = username;
}

public void SetEmail(String email) {
	this.email = email;
}

public void setPassword(String password) {
	this.password = password;
}
}
