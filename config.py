import pymysql


#Función conexión
def get_db_connection():
    return pymysql.connect(
        host="10.3.29.20",
        port=33060,
        user="user_gr5",
        password="Grupo5_listat",
        database="gr5_db",
    )