import sqlite3

def conectar_banco():
    conn = sqlite3.connect('campeonato.db')
    return conn

def criar_tabelas(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Players (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        team_id INTEGER,
                        FOREIGN KEY (team_id) REFERENCES Teams(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Teams (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    )''')
    conn.commit()

def fechar_conexao(conn):
    conn.close()
