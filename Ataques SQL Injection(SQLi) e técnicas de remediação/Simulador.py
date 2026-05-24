import sqlite3

# 1. Criando um banco de dados temporário na memória para testar
conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

# 2. Criando a tabela de usuários e inserindo dados de teste
cursor.execute("CREATE TABLE usuarios (id INTEGER, nome TEXT, senha TEXT)")
cursor.execute("INSERT INTO usuarios VALUES (1, 'admin', 'senha_secreta_123')")
cursor.execute("INSERT INTO usuarios VALUES (2, 'ionara', 'python_back_end')")
conexao.commit()

print("--- SIMULANDO SISTEMA DE LOGIN BACK-END ---")

# --- CENÁRIO 1: CÓDIGO INSEGURO (VULNERÁVEL) ---
# Vamos simular o que o hacker digitaria no campo de login
login_hacker = "admin' OR '1'='1"

print(f"\n[Tentativa de Login com]: {login_hacker}")

# Montando a query de forma errada (juntando strings)
query_insegura = f"SELECT * FROM usuarios WHERE nome = '{login_hacker}'"
cursor.execute(query_insegura)
resultado = cursor.fetchall()

if resultado:
    print("❌ VULNERABILIDADE DETECTADA! Hacker conseguiu logar sem saber a senha:")
    print(resultado)
else:
    print("Acesso negado.")


# --- CENÁRIO 2: CÓDIGO SEGURO (PREVENÇÃO) ---
print("\n--- APLICANDO A CORREÇÃO (Prepared Statements) ---")

# O segredo é usar a interrogação '?' no lugar do dado. 
# O Python vai tratar o texto do hacker estritamente como TEXTO, e não como comando SQL!
query_segura = "SELECT * FROM usuarios WHERE nome = ?"

# Passamos o dado dentro de uma tupla no segundo argumento do execute
cursor.execute(query_segura, (login_hacker,))
resultado_seguro = cursor.fetchall()

if resultado_seguro:
    print("Acesso concedido.")
else:
    print("✅ SISTEMA BLINDADO! O banco procurou um usuário com o nome literal \"admin' OR '1'='1\" e não achou nada.")

conexao.close()
