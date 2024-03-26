import sqlite3

def adicionar_jogador(conn, name, team_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Players (name, team_id) VALUES (?, ?)", (name, team_id))
    conn.commit()

def consultar_jogador(conn, player_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Players WHERE id=?", (player_id,))
    return cursor.fetchone()

def atualizar_jogador(conn, player_id, name, team_id):
    cursor = conn.cursor()
    cursor.execute("UPDATE Players SET name=?, team_id=? WHERE id=?", (name, team_id, player_id))
    conn.commit()

def apagar_jogador(conn, player_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Players WHERE id=?", (player_id,))
    conn.commit()

def listar_jogadores(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Players")
    return cursor.fetchall()

def adicionar_time(conn, name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Teams (name) VALUES (?)", (name,))
    conn.commit()

def atualizar_time(conn, team_id, name):
    cursor = conn.cursor()
    cursor.execute("UPDATE Teams SET name=? WHERE id=?", (name, team_id))
    conn.commit()

def listar_times(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Teams")
    return cursor.fetchall()
