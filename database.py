import psycopg2

class BancoRAD:
	def __init__(self):
		self.conn = None

	def conectar(self):
		try:
			self.conn = psycopg2.connect(host="localhost", database="rad_db", user="postgres", password="postgres")
		except Exception as e:
			print(f"Erro em se conectar: {e}")

	def inserir(self, aluno_nome, matricula, tipo, prioridade, status, descricao, prazo):
		try:
			cursor = self.conn.cursor()
			sql = """INSERT INTO solicitacoes (aluno_nome, matricula, tipo, prioridade, status, descricao, prazo) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
			cursor.execute(sql, (aluno_nome,matricula,tipo,prioridade, status,descricao,prazo))
			self.conn.commit()
			cursor.close()
		except Exception as e:
			print(f"Erro ao inserir: {e}")

	def listar(self):
		try:
			cursor = self.conn.cursor()
			sql = """SELECT * FROM solicitacoes ORDER BY id DESC"""
			cursor.execute(sql)
			resultados = cursor.fetchall()
			cursor.close()
			return resultados
		except Exception as e:
			print(f"Erro ao listar: {e}")
			return []
		
	def pesquisar(self, termo):
		try:
			cursor = self.conn.cursor()
			busca = f"%{termo}%"
			sql = """SELECT * FROM solicitacoes WHERE aluno_nome ILIKE %s OR status ILIKE %s OR prioridade ILIKE %s"""
			cursor.execute(sql, (busca, busca, busca))
			resultados = cursor.fetchall()
			cursor.close()
			return resultados
		except Exception as e:
			print(f"Erro em pesquisar: {e}")
			return []
		
	def atualizar(self, id_registro, aluno_nome, matricula, tipo, prioridade, status, descricao, prazo):
		try:
			cursor = self.conn.cursor()
			sql = """UPDATE solicitacoes SET aluno_nome = %s, matricula = %s, tipo = %s, prioridade = %s, status = %s, descricao = %s, prazo = %s WHERE id = %s"""
			cursor.execute(sql, (aluno_nome, matricula, tipo, prioridade, status, descricao, prazo,id_registro))
			self.conn.commit()
			cursor.close()
		except Exception as e:
			print(f"Erro em atualizar: {e}")

	def excluir(self, id_registro):
		try:
			cursor = self.conn.cursor()
			sql = """DELETE FROM solicitacoes WHERE id = %s"""
			cursor.execute(sql, (id_registro,))
			self.conn.commit()
			cursor.close()
		except Exception as e:
			print(f"Erro em excluir: {e}")
			

