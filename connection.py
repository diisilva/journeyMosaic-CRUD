import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Estabelece uma conexão com o banco de dados MySQL.

    Retorna:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',            # Endereço do servidor MySQL
            port=3308,                   # Porta do MySQL no Docker
            user='user',                 # Usuário do MySQL
            password='userpassword',     # Senha do MySQL
            database='journey_mosaic'    # Nome do banco de dados
        )
        if connection.is_connected():
            print("Conexão com o MySQL estabelecida com sucesso.")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
