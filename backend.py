# backend.py

import mysql.connector
from mysql.connector import Error
import bcrypt
from connection import create_connection

def hash_senha(senha):
    """
    Gera o hash da senha utilizando bcrypt.

    Args:
        senha (str): Senha em texto puro.

    Returns:
        str: Hash da senha.
    """
    hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

# --------------------- CRUD para `usuario` ---------------------

def create_usuario(connection, nome, senha, email, cpf, rg):
    """
    Cria um novo registro na tabela `usuario`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        nome (str): Nome do usuário.
        senha (str): Senha do usuário (será hashada).
        email (str): Email do usuário.
        cpf (str): CPF do usuário.
        rg (str): RG do usuário.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        senha_hashed = hash_senha(senha)
        sql = """
        INSERT INTO usuario (nome, senha, email, cpf, rg)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nome, senha_hashed, email, cpf, rg))
        connection.commit()
        return (True, "Usuário criado com sucesso.")
    except Error as e:
        return (False, f"Erro ao criar usuário: {e}")
    finally:
        cursor.close()

def read_usuarios(connection):
    """
    Lê e retorna todos os registros da tabela `usuario`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.

    Returns:
        tuple: (bool, list/str) Indicando sucesso e lista de usuários ou mensagem de erro.
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT id_usuario, nome, email, cpf, rg FROM usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        return (True, resultados)
    except Error as e:
        return (False, f"Erro ao ler usuários: {e}")
    finally:
        cursor.close()

def update_usuario(connection, id_usuario, nome=None, senha=None, email=None, cpf=None, rg=None):
    """
    Atualiza um registro existente na tabela `usuario`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_usuario (int): ID do usuário a ser atualizado.
        nome (str, optional): Novo nome do usuário.
        senha (str, optional): Nova senha do usuário.
        email (str, optional): Novo email do usuário.
        cpf (str, optional): Novo CPF do usuário.
        rg (str, optional): Novo RG do usuário.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        campos = []
        valores = []
        
        if nome:
            campos.append("nome = %s")
            valores.append(nome)
        if senha:
            senha_hashed = hash_senha(senha)
            campos.append("senha = %s")
            valores.append(senha_hashed)
        if email:
            campos.append("email = %s")
            valores.append(email)
        if cpf:
            campos.append("cpf = %s")
            valores.append(cpf)
        if rg:
            campos.append("rg = %s")
            valores.append(rg)
        
        if not campos:
            return (False, "Nenhum campo foi atualizado.")
        
        valores.append(id_usuario)
        sql = f"UPDATE usuario SET {', '.join(campos)} WHERE id_usuario = %s"
        cursor.execute(sql, tuple(valores))
        connection.commit()
        if cursor.rowcount == 0:
            return (False, "Nenhum usuário encontrado com o ID fornecido.")
        else:
            return (True, "Usuário atualizado com sucesso.")
    except Error as e:
        return (False, f"Erro ao atualizar usuário: {e}")
    finally:
        cursor.close()

def delete_usuario(connection, id_usuario):
    """
    Deleta um registro existente na tabela `usuario`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_usuario (int): ID do usuário a ser deletado.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM usuario WHERE id_usuario = %s"
        cursor.execute(sql, (id_usuario,))
        connection.commit()
        if cursor.rowcount == 0:
            return (False, "Nenhum usuário encontrado com o ID fornecido.")
        else:
            return (True, "Usuário deletado com sucesso.")
    except Error as e:
        return (False, f"Erro ao deletar usuário: {e}")
    finally:
        cursor.close()

# --------------------- CRUD para `viagem` ---------------------

def create_viagem(connection, id_usuario, nome, destino, data_ida, data_volta, descricao):
    """
    Cria um novo registro na tabela `viagem`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_usuario (int): ID do usuário associado à viagem.
        nome (str): Nome da viagem.
        destino (str): Destino da viagem.
        data_ida (str): Data de ida no formato YYYY-MM-DD.
        data_volta (str): Data de volta no formato YYYY-MM-DD.
        descricao (str): Descrição da viagem.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO viagem (id_usuario, nome, destino, data_ida, data_volta, descricao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id_usuario, nome, destino, data_ida, data_volta, descricao))
        connection.commit()
        return (True, "Viagem criada com sucesso.")
    except Error as e:
        return (False, f"Erro ao criar viagem: {e}")
    finally:
        cursor.close()

def read_viagens(connection):
    """
    Lê e retorna todos os registros da tabela `viagem`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.

    Returns:
        tuple: (bool, list/str) Indicando sucesso e lista de viagens ou mensagem de erro.
    """
    try:
        cursor = connection.cursor()
        sql = """
        SELECT v.id_viagem, v.nome, v.destino, v.data_ida, v.data_volta, u.nome
        FROM viagem v
        JOIN usuario u ON v.id_usuario = u.id_usuario
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        return (True, resultados)
    except Error as e:
        return (False, f"Erro ao ler viagens: {e}")
    finally:
        cursor.close()

def update_viagem(connection, id_viagem, id_usuario=None, nome=None, destino=None, data_ida=None, data_volta=None, descricao=None):
    """
    Atualiza um registro existente na tabela `viagem`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_viagem (int): ID da viagem a ser atualizada.
        id_usuario (int, optional): Novo ID do usuário associado.
        nome (str, optional): Novo nome da viagem.
        destino (str, optional): Novo destino da viagem.
        data_ida (str, optional): Nova data de ida.
        data_volta (str, optional): Nova data de volta.
        descricao (str, optional): Nova descrição da viagem.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        campos = []
        valores = []
        
        if id_usuario:
            campos.append("id_usuario = %s")
            valores.append(id_usuario)
        if nome:
            campos.append("nome = %s")
            valores.append(nome)
        if destino:
            campos.append("destino = %s")
            valores.append(destino)
        if data_ida:
            campos.append("data_ida = %s")
            valores.append(data_ida)
        if data_volta:
            campos.append("data_volta = %s")
            valores.append(data_volta)
        if descricao:
            campos.append("descricao = %s")
            valores.append(descricao)
        
        if not campos:
            return (False, "Nenhum campo foi atualizado.")
        
        valores.append(id_viagem)
        sql = f"UPDATE viagem SET {', '.join(campos)} WHERE id_viagem = %s"
        cursor.execute(sql, tuple(valores))
        connection.commit()
        if cursor.rowcount == 0:
            return (False, "Nenhuma viagem encontrada com o ID fornecido.")
        else:
            return (True, "Viagem atualizada com sucesso.")
    except Error as e:
        return (False, f"Erro ao atualizar viagem: {e}")
    finally:
        cursor.close()

def delete_viagem(connection, id_viagem):
    """
    Deleta um registro existente na tabela `viagem`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_viagem (int): ID da viagem a ser deletada.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM viagem WHERE id_viagem = %s"
        cursor.execute(sql, (id_viagem,))
        connection.commit()
        if cursor.rowcount == 0:
            return (False, "Nenhuma viagem encontrada com o ID fornecido.")
        else:
            return (True, "Viagem deletada com sucesso.")
    except Error as e:
        return (False, f"Erro ao deletar viagem: {e}")
    finally:
        cursor.close()

# --------------------- CRUD para `transporte` ---------------------

def create_transporte(connection, tipo_transporte, id_viagem, status='confirmado'):
    """
    Cria um novo registro na tabela `transporte`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        tipo_transporte (str): Tipo de transporte (trem, aviao, onibus).
        id_viagem (int): ID da viagem associada.
        status (str, optional): Status do transporte. Default: 'confirmado'.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO transporte (tipo_transporte, id_viagem, status)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (tipo_transporte, id_viagem, status))
        connection.commit()
        id_transporte = cursor.lastrowid
        return (True, f"Transporte criado com sucesso com ID {id_transporte}.")
    except Error as e:
        return (False, f"Erro ao criar transporte: {e}")
    finally:
        cursor.close()

def read_transportes(connection):
    """
    Lê e retorna todos os registros da tabela `transporte`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.

    Returns:
        tuple: (bool, list/str) Indicando sucesso e lista de transportes ou mensagem de erro.
    """
    try:
        cursor = connection.cursor()
        sql = """
        SELECT t.id_transporte, t.tipo_transporte, t.status, v.nome
        FROM transporte t
        JOIN viagem v ON t.id_viagem = v.id_viagem
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        return (True, resultados)
    except Error as e:
        return (False, f"Erro ao ler transportes: {e}")
    finally:
        cursor.close()

def update_transporte(connection, id_transporte, tipo_transporte=None, id_viagem=None, status=None):
    """
    Atualiza um registro existente na tabela `transporte`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_transporte (int): ID do transporte a ser atualizado.
        tipo_transporte (str, optional): Novo tipo de transporte.
        id_viagem (int, optional): Novo ID da viagem associada.
        status (str, optional): Novo status do transporte.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        campos = []
        valores = []
        
        if tipo_transporte:
            campos.append("tipo_transporte = %s")
            valores.append(tipo_transporte)
        if id_viagem:
            campos.append("id_viagem = %s")
            valores.append(id_viagem)
        if status:
            campos.append("status = %s")
            valores.append(status)
        
        if not campos:
            return (False, "Nenhum campo foi atualizado.")
        
        valores.append(id_transporte)
        sql = f"UPDATE transporte SET {', '.join(campos)} WHERE id_transporte = %s"
        cursor.execute(sql, tuple(valores))
        connection.commit()
        if cursor.rowcount == 0:
            return (False, "Nenhum transporte encontrado com o ID fornecido.")
        else:
            return (True, "Transporte atualizado com sucesso.")
    except Error as e:
        return (False, f"Erro ao atualizar transporte: {e}")
    finally:
        cursor.close()

def delete_transporte(connection, id_transporte):
    """
    Deleta um registro existente na tabela `transporte`.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
        id_transporte (int): ID do transporte a ser deletado.

    Returns:
        tuple: (bool, str) Indicando sucesso e mensagem.
    """
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM transporte WHERE id_transporte = %s"
        cursor.execute(sql, (id_transporte,))
        connection.commit()
        if cursor.rowcount == 0:
            return (False, "Nenhum transporte encontrado com o ID fornecido.")
        else:
            return (True, "Transporte deletado com sucesso.")
    except Error as e:
        return (False, f"Erro ao deletar transporte: {e}")
    finally:
        cursor.close()
