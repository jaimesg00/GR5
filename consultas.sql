USE gr5_db;
#usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,      
    name VARCHAR(100) NOT NULL,             
    surnames VARCHAR(100) NOT NULL,         
    email VARCHAR(255) UNIQUE NOT NULL,     
    password VARCHAR(255) NOT NULL          
);
#Tareas
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,     
    email VARCHAR(255) NOT NULL,            
    title VARCHAR(255) NOT NULL,            
    description TEXT NOT NULL,              
    date_task DATETIME NOT NULL,            
    FOREIGN KEY (email) REFERENCES users(email) 
);
#fecha de inicio y fin de la tarea
ALTER TABLE tasks  
ADD COLUMN start_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN end_datetime DATETIME NULL,      

#Seguridad
ALTER TABLE users CHANGE password password_hash VARCHAR(255);

