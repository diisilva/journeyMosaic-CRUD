# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from backend import (
    create_usuario, read_usuarios, update_usuario, delete_usuario,
    create_viagem, read_viagens, update_viagem, delete_viagem,
    create_transporte, read_transportes, update_transporte, delete_transporte
)
from connection import create_connection

class UsuarioCRUD:
    def __init__(self, master, connection):
        self.master = master
        self.connection = connection
        master.title("CRUD de Usuário")
        master.geometry("400x400")
        
        # Labels e Entrys
        tk.Label(master, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.nome_entry = tk.Entry(master, width=30)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.senha_entry = tk.Entry(master, width=30, show='*')
        self.senha_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(master, text="CPF:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.cpf_entry = tk.Entry(master, width=30)
        self.cpf_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(master, text="RG:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.rg_entry = tk.Entry(master, width=30)
        self.rg_entry.grid(row=4, column=1, padx=10, pady=5)
        
        # Botões
        tk.Button(master, text="Criar Usuário", command=self.create_usuario_ui).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(master, text="Listar Usuários", command=self.listar_usuarios_ui).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(master, text="Atualizar Usuário", command=self.update_usuario_ui).grid(row=6, column=0, padx=10, pady=10)
        tk.Button(master, text="Deletar Usuário", command=self.delete_usuario_ui).grid(row=6, column=1, padx=10, pady=10)
    
    def create_usuario_ui(self):
        nome = self.nome_entry.get()
        senha = self.senha_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        rg = self.rg_entry.get()
        
        if not (nome and senha and email and cpf and rg):
            messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos.")
            return
        
        success, message = create_usuario(self.connection, nome, senha, email, cpf, rg)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.clear_entries()
        else:
            messagebox.showerror("Erro", message)
    
    def listar_usuarios_ui(self):
        success, usuarios = read_usuarios(self.connection)
        if success:
            list_window = tk.Toplevel(self.master)
            list_window.title("Lista de Usuários")
            list_window.geometry("600x400")
            
            cols = ('ID', 'Nome', 'Email', 'CPF', 'RG')
            tree = ttk.Treeview(list_window, columns=cols, show='headings')
            
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            
            for usuario in usuarios:
                tree.insert("", "end", values=usuario)
            
            tree.pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Erro", usuarios)
    
    def update_usuario_ui(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Atualizar Usuário")
        update_window.geometry("400x300")
        
        tk.Label(update_window, text="ID do Usuário:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        id_entry = tk.Entry(update_window, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Nome:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        nome_entry = tk.Entry(update_window, width=30)
        nome_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Senha:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        senha_entry = tk.Entry(update_window, width=30, show='*')
        senha_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Email:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        email_entry = tk.Entry(update_window, width=30)
        email_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="CPF:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        cpf_entry = tk.Entry(update_window, width=30)
        cpf_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="RG:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        rg_entry = tk.Entry(update_window, width=30)
        rg_entry.grid(row=5, column=1, padx=10, pady=5)
        
        def submit_update():
            id_usuario = id_entry.get()
            nome = nome_entry.get()
            senha = senha_entry.get()
            email = email_entry.get()
            cpf = cpf_entry.get()
            rg = rg_entry.get()
            
            if not id_usuario:
                messagebox.showwarning("Entrada Inválida", "Por favor, insira o ID do usuário.")
                return
            
            success, message = update_usuario(self.connection, id_usuario, nome or None, senha or None, email or None, cpf or None, rg or None)
            if success:
                messagebox.showinfo("Sucesso", message)
                update_window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        tk.Button(update_window, text="Atualizar", command=submit_update).grid(row=6, column=0, columnspan=2, pady=10)
    
    def delete_usuario_ui(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Deletar Usuário")
        delete_window.geometry("300x150")
        
        tk.Label(delete_window, text="ID do Usuário:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        id_entry = tk.Entry(delete_window, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        def submit_delete():
            id_usuario = id_entry.get()
            if not id_usuario:
                messagebox.showwarning("Entrada Inválida", "Por favor, insira o ID do usuário.")
                return
            success, message = delete_usuario(self.connection, id_usuario)
            if success:
                messagebox.showinfo("Sucesso", message)
                delete_window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        tk.Button(delete_window, text="Deletar", command=submit_delete).grid(row=1, column=0, columnspan=2, pady=10)
    
    def clear_entries(self):
        self.nome_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.rg_entry.delete(0, tk.END)

# --------------------- CRUD para `viagem` ---------------------

class ViagemCRUD:
    def __init__(self, master, connection):
        self.master = master
        self.connection = connection
        master.title("CRUD de Viagem")
        master.geometry("500x500")
        
        # Labels e Entrys
        tk.Label(master, text="ID do Usuário:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.id_usuario_entry = tk.Entry(master, width=30)
        self.id_usuario_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Nome da Viagem:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.nome_entry = tk.Entry(master, width=30)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Destino:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.destino_entry = tk.Entry(master, width=30)
        self.destino_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Data de Ida (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.data_ida_entry = tk.Entry(master, width=30)
        self.data_ida_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Data de Volta (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.data_volta_entry = tk.Entry(master, width=30)
        self.data_volta_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Descrição:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.descricao_entry = tk.Entry(master, width=30)
        self.descricao_entry.grid(row=5, column=1, padx=10, pady=5)
        
        # Botões
        tk.Button(master, text="Criar Viagem", command=self.create_viagem_ui).grid(row=6, column=0, padx=10, pady=10)
        tk.Button(master, text="Listar Viagens", command=self.listar_viagens_ui).grid(row=6, column=1, padx=10, pady=10)
        tk.Button(master, text="Atualizar Viagem", command=self.update_viagem_ui).grid(row=7, column=0, padx=10, pady=10)
        tk.Button(master, text="Deletar Viagem", command=self.delete_viagem_ui).grid(row=7, column=1, padx=10, pady=10)
    
    def create_viagem_ui(self):
        id_usuario = self.id_usuario_entry.get()
        nome = self.nome_entry.get()
        destino = self.destino_entry.get()
        data_ida = self.data_ida_entry.get()
        data_volta = self.data_volta_entry.get()
        descricao = self.descricao_entry.get()
        
        if not (id_usuario and nome and destino and data_ida and data_volta and descricao):
            messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos.")
            return
        
        success, message = create_viagem(self.connection, id_usuario, nome, destino, data_ida, data_volta, descricao)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.clear_entries()
        else:
            messagebox.showerror("Erro", message)
    
    def listar_viagens_ui(self):
        success, viagens = read_viagens(self.connection)
        if success:
            list_window = tk.Toplevel(self.master)
            list_window.title("Lista de Viagens")
            list_window.geometry("800x400")
            
            cols = ('ID', 'Nome', 'Destino', 'Data Ida', 'Data Volta', 'Usuário')
            tree = ttk.Treeview(list_window, columns=cols, show='headings')
            
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=120)
            
            for viagem in viagens:
                tree.insert("", "end", values=viagem)
            
            tree.pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Erro", viagens)
    
    def update_viagem_ui(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Atualizar Viagem")
        update_window.geometry("500x400")
        
        tk.Label(update_window, text="ID da Viagem:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        id_entry = tk.Entry(update_window, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="ID do Usuário:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        id_usuario_entry = tk.Entry(update_window, width=30)
        id_usuario_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Nome da Viagem:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        nome_entry = tk.Entry(update_window, width=30)
        nome_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Destino:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        destino_entry = tk.Entry(update_window, width=30)
        destino_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Data de Ida (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        data_ida_entry = tk.Entry(update_window, width=30)
        data_ida_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Data de Volta (YYYY-MM-DD):").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        data_volta_entry = tk.Entry(update_window, width=30)
        data_volta_entry.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Descrição:").grid(row=6, column=0, padx=10, pady=5, sticky='e')
        descricao_entry = tk.Entry(update_window, width=30)
        descricao_entry.grid(row=6, column=1, padx=10, pady=5)
        
        def submit_update():
            id_viagem = id_entry.get()
            id_usuario = id_usuario_entry.get() or None
            nome = nome_entry.get() or None
            destino = destino_entry.get() or None
            data_ida = data_ida_entry.get() or None
            data_volta = data_volta_entry.get() or None
            descricao = descricao_entry.get() or None
            
            if not id_viagem:
                messagebox.showwarning("Entrada Inválida", "Por favor, insira o ID da viagem.")
                return
            
            success, message = update_viagem(self.connection, id_viagem, id_usuario, nome, destino, data_ida, data_volta, descricao)
            if success:
                messagebox.showinfo("Sucesso", message)
                update_window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        tk.Button(update_window, text="Atualizar", command=submit_update).grid(row=7, column=0, columnspan=2, pady=10)
    
    def delete_viagem_ui(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Deletar Viagem")
        delete_window.geometry("300x150")
        
        tk.Label(delete_window, text="ID da Viagem:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        id_entry = tk.Entry(delete_window, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        def submit_delete():
            id_viagem = id_entry.get()
            if not id_viagem:
                messagebox.showwarning("Entrada Inválida", "Por favor, insira o ID da viagem.")
                return
            success, message = delete_viagem(self.connection, id_viagem)
            if success:
                messagebox.showinfo("Sucesso", message)
                delete_window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        tk.Button(delete_window, text="Deletar", command=submit_delete).grid(row=1, column=0, columnspan=2, pady=10)
    
    def clear_entries(self):
        self.id_usuario_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.destino_entry.delete(0, tk.END)
        self.data_ida_entry.delete(0, tk.END)
        self.data_volta_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)

# --------------------- CRUD para `transporte` ---------------------

class TransporteCRUD:
    def __init__(self, master, connection):
        self.master = master
        self.connection = connection
        master.title("CRUD de Transporte")
        master.geometry("400x300")
        
        # Labels e Entrys
        tk.Label(master, text="Tipo de Transporte:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.tipo_transporte_combo = ttk.Combobox(master, values=["trem", "aviao", "onibus"], state="readonly", width=28)
        self.tipo_transporte_combo.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(master, text="ID da Viagem:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.id_viagem_entry = tk.Entry(master, width=30)
        self.id_viagem_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(master, text="Status:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.status_combo = ttk.Combobox(master, values=["confirmado", "cancelado", "pendente"], state="readonly", width=28)
        self.status_combo.current(0)  # Definir 'confirmado' como padrão
        self.status_combo.grid(row=2, column=1, padx=10, pady=5)
        
        # Botões
        tk.Button(master, text="Criar Transporte", command=self.create_transporte_ui).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(master, text="Listar Transportes", command=self.listar_transportes_ui).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(master, text="Atualizar Transporte", command=self.update_transporte_ui).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(master, text="Deletar Transporte", command=self.delete_transporte_ui).grid(row=4, column=1, padx=10, pady=10)
    
    def create_transporte_ui(self):
        tipo_transporte = self.tipo_transporte_combo.get()
        id_viagem = self.id_viagem_entry.get()
        status = self.status_combo.get()
        
        if not (tipo_transporte and id_viagem):
            messagebox.showwarning("Entrada Inválida", "Por favor, preencha os campos obrigatórios.")
            return
        
        success, message = create_transporte(self.connection, tipo_transporte, id_viagem, status)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.clear_entries()
        else:
            messagebox.showerror("Erro", message)
    
    def listar_transportes_ui(self):
        success, transportes = read_transportes(self.connection)
        if success:
            list_window = tk.Toplevel(self.master)
            list_window.title("Lista de Transportes")
            list_window.geometry("600x400")
            
            cols = ('ID', 'Tipo', 'Status', 'Viagem')
            tree = ttk.Treeview(list_window, columns=cols, show='headings')
            
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=150)
            
            for transporte in transportes:
                tree.insert("", "end", values=transporte)
            
            tree.pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Erro", transportes)
    
    def update_transporte_ui(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Atualizar Transporte")
        update_window.geometry("400x250")
        
        tk.Label(update_window, text="ID do Transporte:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        id_entry = tk.Entry(update_window, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Tipo de Transporte:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        tipo_transporte_combo = ttk.Combobox(update_window, values=["trem", "aviao", "onibus"], state="readonly", width=28)
        tipo_transporte_combo.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="ID da Viagem:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        id_viagem_entry = tk.Entry(update_window, width=30)
        id_viagem_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(update_window, text="Status:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        status_combo = ttk.Combobox(update_window, values=["confirmado", "cancelado", "pendente"], state="readonly", width=28)
        status_combo.grid(row=3, column=1, padx=10, pady=5)
        
        def submit_update():
            id_transporte = id_entry.get()
            tipo_transporte = tipo_transporte_combo.get() or None
            id_viagem = id_viagem_entry.get() or None
            status = status_combo.get() or None
            
            if not id_transporte:
                messagebox.showwarning("Entrada Inválida", "Por favor, insira o ID do transporte.")
                return
            
            success, message = update_transporte(self.connection, id_transporte, tipo_transporte, id_viagem, status)
            if success:
                messagebox.showinfo("Sucesso", message)
                update_window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        tk.Button(update_window, text="Atualizar", command=submit_update).grid(row=4, column=0, columnspan=2, pady=10)
    
    def delete_transporte_ui(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Deletar Transporte")
        delete_window.geometry("300x150")
        
        tk.Label(delete_window, text="ID do Transporte:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        id_entry = tk.Entry(delete_window, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        def submit_delete():
            id_transporte = id_entry.get()
            if not id_transporte:
                messagebox.showwarning("Entrada Inválida", "Por favor, insira o ID do transporte.")
                return
            success, message = delete_transporte(self.connection, id_transporte)
            if success:
                messagebox.showinfo("Sucesso", message)
                delete_window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        tk.Button(delete_window, text="Deletar", command=submit_delete).grid(row=1, column=0, columnspan=2, pady=10)
    
    def clear_entries(self):
        self.tipo_transporte_combo.set('')
        self.id_viagem_entry.delete(0, tk.END)
        self.status_combo.current(0)

# --------------------- Interface Principal ---------------------

def main():
    """
    Função principal que inicializa a interface gráfica e permite a navegação entre os módulos CRUD.
    """
    connection = create_connection()
    if not connection:
        messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao banco de dados.")
        return
    
    root = tk.Tk()
    root.title("Journey Mosaic - CRUD Application")
    root.geometry("400x300")
    
    # Botões para acessar os CRUDs
    tk.Button(root, text="CRUD de Usuário", width=30, command=lambda: open_crud_window("usuario", connection)).pack(pady=20)
    tk.Button(root, text="CRUD de Viagem", width=30, command=lambda: open_crud_window("viagem", connection)).pack(pady=20)
    tk.Button(root, text="CRUD de Transporte", width=30, command=lambda: open_crud_window("transporte", connection)).pack(pady=20)
    
    tk.Button(root, text="Sair", width=30, command=root.quit).pack(pady=20)
    
    root.mainloop()
    connection.close()

def open_crud_window(entidade, connection):
    """
    Abre a janela correspondente ao CRUD da entidade selecionada.

    Args:
        entidade (str): Nome da entidade ('usuario', 'viagem', 'transporte').
        connection (mysql.connector.connection.MySQLConnection): Objeto de conexão.
    """
    if entidade == "usuario":
        crud_window = tk.Toplevel()
        UsuarioCRUD(crud_window, connection)
    elif entidade == "viagem":
        crud_window = tk.Toplevel()
        ViagemCRUD(crud_window, connection)
    elif entidade == "transporte":
        crud_window = tk.Toplevel()
        TransporteCRUD(crud_window, connection)
    else:
        messagebox.showerror("Erro", "Entidade desconhecida.")

if __name__ == "__main__":
    main()
