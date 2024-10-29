import subprocess
import time
import os



def iniciar_api():
    print("Iniciando API en Python...")
    
    subprocess.Popen(['py', 'run.py'])  
    time.sleep(2)

def iniciar_app_java():
    print("Compilando y ejecutando App Java Web...")
    os.chdir('userlogin')  
    subprocess.Popen(['javac', 'src/**/*.java'])  # Asegúrate de que los archivos están en src
    time.sleep(2)
    subprocess.Popen(['java', '-cp', 'src', 'com'])  # Cambia por tu clase principal
    time.sleep(2)

def iniciar_app_react():
    print("Iniciando App React...")
    subprocess.Popen(['npm', 'start'], cwd='client')  # Asegúrate de que el directorio sea correcto
    time.sleep(2)

def iniciar_server_node():
    print("Iniciando Server Node.js...")
    subprocess.Popen(['node', 'server'])  # Usa r'...' para evitar problemas de escape
    time.sleep(2)

def abrir_userlogin():
    print("Abriendo UserLogin...")
    subprocess.Popen(['mvn', 'spring-boot:run'], cwd='userlogin\src\main\webapp\register.jsp') 

if __name__ == "__main__":
    iniciar_api()
    iniciar_app_java()
    iniciar_app_react()
    iniciar_server_node()
    abrir_userlogin()