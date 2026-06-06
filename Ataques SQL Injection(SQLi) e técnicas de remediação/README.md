<h1> Segurança de APIs e Aplicações Robustas</h1>

>💡um sistema seguro começa na forma como lidamos com os dados vindos do usuário.

📂 Passo 1: O que é SQL Injection (SQLi)?
É um comando que segue ordens 

Curiosidade!
"O ataque de SQL Injection acontece quando um usuário malicioso injeta comandos SQL dentro de um campo de texto comum (como uma barra de pesquisa ou campo de login). Como o código do Back-end junta esse texto direto na consulta do banco, o banco acaba executando o comando malicioso achando que faz parte da ordem original."

Exemplo:
Um código Python que se escreve na consulta colando o texto do usuário direto, usando a formatação de strings(f-string):
<img width="742" height="72" alt="image" src="https://github.com/user-attachments/assets/d9dc81de-0526-4ab3-becc-741b914fd7b4" />

Se uma pessoa digitar João, o banco executa:
SELECT * FROM usuarios WHERE nome = 'João'(Tudo certo)

Mas se um hacker digitar admin' OR '1'='1 O banco vai receber e executar isso:
<img width="643" height="105" alt="image" src="https://github.com/user-attachments/assets/2b222049-5ad6-49c4-b63a-3544e78cef8f" />

Como 1=1 é sempre verdadeiro(True),o banco ignora a checagem do nome e entrega os dados de todos os usuários do sistema,incliuindo o administrador!😱

💻 Passo 2: O Script de Teste Prático em Python

>sqlite3 é um banco de dados leve que já vem embutido no Python

<h1>Ataques SQL Injection (SQLi) e Segurança na Web(mais detalhes)</h1>
<br>

>mas focando na perspectiva de quem defende o código por trás dos panos

Um conceito crucial para o desenvolvimento seguro: Query Parameterization (ou Prepared Statements), que é a principal arma contra o SQL Injection.

<h3>O Problema: SQL Injection Dinâmico</h3>
Quando se construí queries concatenando strings direto com a entrada do usuário, se abre uma brecha

<img width="880" height="77" alt="image" src="https://github.com/user-attachments/assets/63615e97-787a-4a82-8cba-f95df4984fa0" />

Se o atacante digitar ' OR '1'='1, ele quebra a lógica da sua query e consegue logar sem senha. Ele transformou dados em código executável.

<h1>A Solução: Prepared Statements (Parametrização)</h1>
A parametrização resolve isso separando o código SQL dos dados. O banco de dados compila a estrutura da query antes de receber os dados do usuário.

Abaixo, veja como isso funciona na prática usando Node.js (com o driver pg para PostgreSQL), uma realidade muito comum no Back-end:
<img width="783" height="258" alt="image" src="https://github.com/user-attachments/assets/cc16c9cf-38c4-404d-82fb-0fc08aa64696" />

