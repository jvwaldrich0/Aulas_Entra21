from sqlite3 import connect


class DatabaseUtils:
    def __init__(self, database):
        # Conectar ao SQLite3
        self.bd = connect(database)
        self.sql = self.bd.cursor()

    def listar(self, tabela: str):
        # Selecionar tabela
        self.sql.execute(f'SELECT nome FROM {tabela}')
        # Recolher dados
        dados = self.sql.fetchall()
        # Loop para print de tudo
        for i in range(len(dados)):
            print(f'{i+1} - {dados[i]}')

    def listar_dados(self, tabela: str, id: int) -> list:
        self.sql.execute(f'SELECT * FROM {tabela} WHERE id = {id} ')
        return self.sql.fetchall()

    def rem(self, tabela, colum: int):
        self.sql.execute(f'''
DELETE FROM {tabela}
WHERE id = {colum}''')
        self.bd.commit()


