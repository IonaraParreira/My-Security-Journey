<div align="center">
  <img src="https://github.com/user-attachments/assets/db41a13c-55d7-480c-89ee-581ecc631128" width="400" alt="Sua Imagem">
</div>
<br>
<br>

<h1><img src="https://github.com/user-attachments/assets/7545ba69-4192-417e-aef3-568f2aa14b9d" width="50" height="50" alt="Postman Logo" style="vertical-align: middle; margin-right: 10px;">Postman</h1>

<p>O Postman opera diretamente nas camadas de rede (enviando requisições HTTP/HTTPS, lidando com status codes, cabeçalhos, cookies e payloads).</p>

<h1>Nmap (Network Mapper)</h1>
Varre redes para descobrir quais hosts estão ativos, quais portas estão abertas e quais serviços/sistemas operacionais estão rodando.

>Excelente para entender o protocolo TCP/IP, como funcionam os handshakes e conexões de rede.

Wireshark: Um analisador de protocolos de rede (sniffer). Ele captura e permite que você veja o tráfego que está passando pela rede em tempo real, detalhe por detalhe.

Por que estudar: Para ver na prática a diferença entre tráfego HTTP (texto aberto) e HTTPS (criptografado), além de entender a estrutura dos pacotes de dados.

2. Testes e Análise de APIs e Web (Web Security)
Como desenvolvedora back-end, essas aqui são obrigatórias no seu cinto de utilidades.

OWASP ZAP (Zed Attack Proxy) ou Burp Suite: São proxies de interceptação. Eles ficam no meio do caminho entre o seu navegador e o servidor back-end. Você pode pausar uma requisição HTTP, alterar o corpo dos dados (payload) ou os headers e enviá-la modificada para o servidor para testar falhas.

Por que estudar: Para aprender como os atacantes tentam burlar as validações do seu back-end e para testar suas próprias APIs contra vulnerabilidades como as do OWASP Top 10.

Postman (com foco em Segurança): Você provavelmente já usa para testar rotas, mas ele é ótimo para criar suítes de testes automatizados para validar se suas rotas protegidas realmente bloqueiam requisições sem token JWT válido ou com permissões erradas.

3. Automação e Varredura de Vulnerabilidades
Ferramentas que automatizam testes para encontrar brechas conhecidas.

Nikto: Um scanner de servidor web de código aberto. Ele realiza testes rápidos contra servidores para encontrar arquivos perigosos, softwares desatualizados e problemas de configuração.

Sqlmap: Uma ferramenta automática que detecta e explora falhas de SQL Injection em parâmetros de requisições web e bancos de dados.

Por que estudar: Para entender a importância crucial de usar Prepared Statements e ORMs no seu código back-end.

4. Segurança no Código (SAST/DAST)
Ferramentas que analisam o código-fonte atrás de vulnerabilidades antes do sistema ir para o ar.

SonarQube / Snyk: Analisam seu código (ou suas dependências do npm, pip, maven, etc.) em busca de bugs, vulnerabilidades conhecidas e chaves secretas expostas por acidente.

Por que estudar: Integração de segurança direto na esteira de CI/CD (DevSecOps) é uma habilidade ultra valorizada.

🚀 Como colocar isso no seu GitHub e se destacar?
Como você quer aprender as ferramentas que já existem, o seu GitHub pode se transformar em um Portfólio de Aprendizado e Laboratório (Cybersecurity Lab). Você pode criar um repositório chamado cybersecurity-studies ou my-security-lab e colocar lá:

Relatórios de Testes: Crie uma aplicação back-end simples sua, use o OWASP ZAP ou o Nikto contra ela, e documente no GitHub as vulnerabilidades que a ferramenta achou e como você corrigiu o código para resolver o problema.

Scripts de Automação: Crie scripts (em Python, Bash ou Go) que automatizam o uso dessas ferramentas (ex: um script que roda o Nmap e formata o resultado em um arquivo bonitinho).

Anotações de Cheat Sheets: Crie guias rápidos (Markdown) com os comandos que você mais usou e aprendeu de cada ferramenta. Recrutadores adoram ver engenheiros que sabem documentar processos.
