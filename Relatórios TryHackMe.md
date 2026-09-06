<h1>Estudo voltado nas atividades de laboratório do TryHackme <img src="https://github.com/user-attachments/assets/63414096-eaa7-40e7-b733-80347267a6ac" width="80" align="middle" alt="image" /></h1>

<h1>Aprendendo o porquê e não o comando📌</h1>
Percebi que, à medida que anotava a minha evolução nos laboratórios do site TryHackMe, conseguia reter melhor o aprendizado. A seguir, algumas das anotações: evidências de escolhas e...

1) Perguntas Mestres🏷️:

🔍O que esse comando faz?<br>
🔍O que as flags significam?<br>
🔍Quando eu devo usá-lo?<br>
🔍Quais alternativas eu tenho se ele falhar?<br>
🔍Como descobrir algo?<br>
🔍Como evitar de acontecer?


2) O que foi que aprendi mais, como explicar para uma empresa. gerar check-list, mini relatóruio, o que eu vi. o impacto e qual recomendação que dou.
3) É importante equilibrar o ofensivo do defensivo.

<h1>Fica a dica</h1>
<img width="1121" height="537" alt="Captura de tela 2026-06-10 180958" src="https://github.com/user-attachments/assets/11346b64-cfe4-434a-936f-42df2051557e" />

<h3>Analista de Segurança</h3>
São chamados de defensores digitais porque monitoram,investigam e respondem a ameaças,protegendo os ativos da organização.

<h1> Endereço Mac</h1>
É um número hexadecimal de doze caracteres(um sistema de numeração de base dezesseis usado em computação para representar números) dividido em dois e separado por dois pontos. Esses dois pontos são considerados separadosres. Por exemplo:Os seis primeiros caracteres representam a empresa que fabricou a interface de rede e os seis últimos são um número único.<br>
<br>
<p align="center">
<img width="521" height="291" alt="image" src="https://github.com/user-attachments/assets/a22a3100-9dd0-4909-941a-fcc6de4044f2" />
</p>

<h1> DNS</h1>

>Sistema de Nomes de Domínio

É uma maneira simples de nos comunicarmos com dispositivos na internet sem precisarmos memorizar números complexos.Em vez de memorizar 104.26.10.229, se pode memorizar tryhackme.com

<h1>Fica a dica</h1>
<img width="1276" height="800" alt="Captura de tela 2026-06-12 034552" src="https://github.com/user-attachments/assets/92498575-3c4b-49ed-bf63-af6f7245c851" />

<h1>Relembrar é Viver</h1>

```
+------------------------------------+
| APLICAÇÃO   -->   HTTP  /  FTP     |  (Seu código/APIs)
+------------------------------------+
| TRANSPORTE  -->   TCP   /  UDP     |  (Garantia ou velocidade)
+------------------------------------+
| REDE        -->       ICMP         |  (Diagnóstico/Ping)
+------------------------------------+
```
<h1>ICMP (Internet Control Message Protocol)</h1>
<h2>Camada de Rede / Internet (Infraestrutura e Rotas)</h2>

>O que faz: Envia mensagens de status, relatório de erros e diagnósticos de rede.<br>
>Na prática: É o protocolo nativo utilizado pelo comando ping para testar se um servidor está online.<br>
<br>
<h1>TCP (Transmission Control Protocol)</h1>
<h2>Camada de Transporte (Como os dados viajam)</h2>

>O que faz: Protocolo orientado à conexão. Ele garante que todos os pacotes cheguem na ordem correta e sem perdas (se um pacote falhar, ele reenvia).<br>
>Na prática: Usado onde a segurança dos dados é crucial (APIs REST, bancos de dados, carregamento de páginas web).<br>
<br>
<h1>UDP (User Datagram Protocol)</h1>

>O que faz: Protocolo não orientado à conexão. Ele apenas envia os dados o mais rápido possível, sem checar se chegaram ou se estão na ordem.<br>
>Na prática: Usado onde velocidade importa mais que perdas eventuais (Streaming de vídeo, jogos online, chamadas de voz, DNS).<br>
<br>
<h1>HTTP (Hypertext Transfer Protocol)</h1>
<h2>Camada de Aplicação (Onde o Back-end codifica)</h2>

>O que faz: Protocolo de transferência de hipertexto. Base da comunicação da Web, funciona no modelo Cliente-Servidor (Request/Response).<br>
>Na prática: É o que você usa para construir suas APIs (GET, POST, PUT, DELETE). Roda sob o protocolo TCP.<br>
<br>
<h1>FTP (File Transfer Protocol)</h1>

>O que faz: Protocolo específico para a transferência de arquivos de forma direta entre um cliente e um servidor.<br>
>Na prática: Usado para fazer upload de arquivos de configuração, imagens ou backups para um servidor. Também roda sob o TCP.<br>
<br>

<h1>Importante!</h1>
<img width="1442" height="427" alt="Captura de tela 2026-06-16 143717" src="https://github.com/user-attachments/assets/63b9954c-22e4-4005-96fe-4705bb2949ef" /><br>

<img width="1077" height="775" alt="Captura de tela 2026-07-11 084021" src="https://github.com/user-attachments/assets/b28e86ed-724e-4343-9e1b-19233ff5c770" />


<h1>Olha o oculto!</h1>

>Pasta compartilhada oculta

Para achar: Abrir o Gerenciamento do Computador> executar `mkdir` compmgmt.msc> Pastas Compartilhadas> Compartilhamentos

<h1>Resumo da Semana</h1>
<img width="1103" height="775" alt="Captura de tela 2026-07-06 094759" src="https://github.com/user-attachments/assets/dd681fcd-4471-47a9-b40d-77f0fa5f7d67" />

<img width="1227" height="762" alt="Captura de tela 2026-07-06 094825" src="https://github.com/user-attachments/assets/556d8a09-8342-4e29-9c93-0af872750322" />

<img width="1187" height="575" alt="Captura de tela 2026-07-06 095040" src="https://github.com/user-attachments/assets/2e72d912-3ced-4244-bf96-3b17008dd325" />

<h1>Equipe</h1>
<p align="center">
  <img width="1407" height="199" alt="Captura de tela 2026-07-13 111151" src="https://github.com/user-attachments/assets/a9aff94e-725c-406a-92a7-2dff17895dc7" />
<img width="967" height="83" alt="Captura de tela 2026-07-13 112303" src="https://github.com/user-attachments/assets/3b60f908-0c60-473e-a2bb-51be89161c43" />

</p>

<h1>Cenário</h1>
<p align="center">
  <img width="1045" height="661" alt="Captura de tela 2026-07-13 112743" src="https://github.com/user-attachments/assets/f1a044a5-a5d1-4005-9e79-aa277bca90cd" />
</p>

1. SIEM created an alert about FW-NY-01 firewall brute-force.Who should triage the alert?
>R: Lucas | SOC L1 Analyst

2. The HR manager Anna launched a phishing malware.Who should make a deep analysis? 
>R: Susan |SOC L2 Analyst

3. The office in France was somehow hit with ransomware.Immediate response is required!
>R: Robert |CERT Lead

4. Our servers storing the credit cards require PCI DSS audit. Who can help us here?
>R: Nick| GRC Auditor

5. Who can check the new version of tryhackme.thm for vulnerabilities?
>R:Ben | Penetration Tester

6. The SIEM is unavailable due to a storage limit.Who can investigate the issue?
>R: Eugen | SOC Engineer

7. FIN7 threat group actively targets our company.Who can analyze their tactics?
>R: Alice | Threat Researcher

<h1>Suma importância!Por trás dos alertas acionados</h1>
Aprendemos que umSIEMA solução detecta ameaças correlacionando registros de diversas fontes e acionando alertas, mas será que conhecemos o segredo por trás dessas detecções?

Uma solução SIEM possui regras de detecção que identificam ameaças. Essas regras desempenham um papel importante na detecção oportuna de ameaças, permitindo que os analistas ajam em tempo hábil. As regras de detecção são basicamente expressões lógicas definidas para serem acionadas. Alguns exemplos de regras de detecção são:

* Se um usuário tiver cinco tentativas de login falhas em 10 segundos, gere um alerta paraMultiple Failed Login Attempts

* Se o login for bem-sucedido após várias tentativas falhas, gere um alerta paraSuccessful Login After multiple Login Attempts

* Uma regra é configurada para gerar um alerta sempre que um usuário conectar um dispositivo USB (útil se o uso de USB for restrito de acordo com a política da empresa).

* Se o tráfego de saída for superior a 25 MB, gere um alerta para uma possível tentativa de exfiltração de dados (normalmente, isso depende da política da empresa).

<h3>Como é criada uma regra de detecção?</h3>
Para explicar como a regra funciona, considere os seguintes casos de uso do Log de Eventos:

Caso de uso 1:
Os adversários tendem a remover os registros durante a fase pós-exploração para apagar seus rastros. Um ID de evento exclusivo, 104, é registrado sempre que um usuário tenta remover ou limpar os registros de eventos. Para criar uma regra com base nessa atividade, podemos definir a condição da seguinte forma:

>Regra: Se a origem do log for WinEventLog E o ID do evento for 104 - Acione um alerta.Event Log Cleared

Caso de uso 2:
Os adversários usam comandos como esses whoami após a fase de exploração/escalonamento de privilégios. Os seguintes campos serão úteis para incluir na regra.

Fonte de registro: Identifique 🔍 a fonte de registro que captura os logs de eventos.

ID do evento: Qual ID de evento está associado à atividade de execução do processo? Neste caso, o ID de evento 4688 será útil.

NewProcessName: Qual nome de processo será útil incluir na regra?

>Regra: Se a origem do log for WinEventLog E o código do evento for 4688, e o nome do novo processo contiver "whoami", então acione um alerta.WHOAMI command Execution DETECTED

Na tarefa anterior, discutimos a importância dos pares campo-valor. As regras de detecção monitoram os valores de determinados campos para serem acionadas. Por isso, é importante que os logs de entrada estejam normalizados.


<h1>Máquina Windows</h1>
O Windows registra todos os eventos que podem ser visualizados por meio do Visualizador de Eventos. Ele atribui um ID exclusivo a cada tipo de atividade de log, facilitando a análise e o rastreamento por parte do analista. Para visualizar eventos em um ambiente Windows, digite  Event Viewerna barra de pesquisa. Isso o levará à ferramenta onde diferentes logs são armazenados e podem ser visualizados, conforme mostrado abaixo. Esses logs de todos os endpoints Windows são encaminhados para a solução SIEM para monitoramento e maior visibilidade.

<img width="1541" height="842" alt="Captura de tela 2026-08-24 091316" src="https://github.com/user-attachments/assets/5e8cbdbe-be58-45f9-85f0-230549258e8c" />

<img width="1547" height="817" alt="Captura de tela 2026-08-24 091238" src="https://github.com/user-attachments/assets/4837e6a8-44ff-4593-92e7-1def2884443d" />

<img width="1532" height="812" alt="Captura de tela 2026-08-24 091225" src="https://github.com/user-attachments/assets/c3faf4f8-7e0e-45ed-a588-48013943d3e5" />

<img width="1556" height="837" alt="Captura de tela 2026-08-24 091126" src="https://github.com/user-attachments/assets/3b84f184-cbd1-45c1-9c4f-a80be8ad66f9" />


<h1>Continuando a análise</h1>

<h2>Máquina Linux</h2>
O sistema operacional Linux armazena todos os registros relevantes, como eventos, erros, avisos, etc. Esses registros são então integrados ao SIEM para monitoramento contínuo. Alguns dos locais comuns onde o Linux armazena registros são:

/var/log/httpd: Contém os registros de requisição/resposta HTTP e de erros.
/var/log/cron: Os eventos relacionados às tarefas cron são armazenados neste local.
/var/log/auth.log e /var/log/secure: Armazenam registros relacionados à autenticação.
/var/log/kern: Este arquivo armazena eventos relacionados ao kernel.

daí um exemplo na prática de busca
<img width="1542" height="286" alt="image" src="https://github.com/user-attachments/assets/0903ef6a-efe0-4fdf-93ad-a8ee06f3526f" />

É possível descobrir bastante pelas informações que são fornecidas pela ingestão de logs
<img width="1096" height="695" alt="image" src="https://github.com/user-attachments/assets/15f7c385-934b-4311-9244-1a5f8e7722c2" />

Alguns métodos comuns usados ​​por essas soluções SIEM são explicados abaixo:

Agente/Encaminhador
Essas soluções SIEM fornecem uma ferramenta leve chamada agente (encaminhador).Splunk) que é instalado no Endpoint. Ele é configurado para capturar e enviar todos os logs importantes para o servidor SIEM.

Syslog
é um protocolo amplamente utilizado para coletar dados de diversos sistemas, como servidores web, bancos de dados, etc., e enviar dados em tempo real para um destino centralizado.

Carregamento manual
Algumas soluções SIEM, como o Splunk,Alce, etc., permitem que os usuários importem dados offline para análise rápida. Uma vez importados, os dados são normalizados e disponibilizados para análise.

As soluções SIEM de encaminhamento de portas
também podem ser configuradas para escutar em uma determinada porta, e então os endpoints encaminham os dados para a instância SIEM na porta de escuta.

<h1>Como é um alerta</h1>
<img width="922" height="816" alt="Captura de tela 2026-08-25 131052" src="https://github.com/user-attachments/assets/946332da-5c20-40bc-8d12-e051ec496105" />

<img width="945" height="807" alt="Captura de tela 2026-08-25 131041" src="https://github.com/user-attachments/assets/9260ce13-5bf6-4bd8-9b72-70ae2d1f2138" />

<img width="885" height="788" alt="Captura de tela 2026-08-25 131101" src="https://github.com/user-attachments/assets/e9b6f668-f415-4389-9ec6-3101243ee1be" />

<img width="917" height="651" alt="Captura de tela 2026-08-25 131113" src="https://github.com/user-attachments/assets/3f629393-f7a7-4c90-9d4b-7cf344d6b3ce" />

<img width="918" height="642" alt="Captura de tela 2026-08-25 131140" src="https://github.com/user-attachments/assets/e82bce5c-d8b6-4aef-8475-4454239cb5cd" />

<img width="387" height="41" alt="Captura de tela 2026-08-25 131130" src="https://github.com/user-attachments/assets/f31c816d-63ca-4b6c-9050-1f40c8a6cede" />
<img width="870" height="82" alt="Captura de tela 2026-08-25 130740" src="https://github.com/user-attachments/assets/712fee96-ce8f-418c-8116-77c820ca95aa" />

<img width="1022" height="612" alt="Captura de tela 2026-08-25 131147" src="https://github.com/user-attachments/assets/fd3a3d18-5569-4d81-84dc-8878247e5693" />

<img width="1002" height="587" alt="Captura de tela 2026-08-25 131153" src="https://github.com/user-attachments/assets/25198ff2-93f0-4ab7-b107-f0f76c58957f" />

<img width="926" height="546" alt="Captura de tela 2026-08-25 131201" src="https://github.com/user-attachments/assets/df69cfc0-f3ec-4c47-b3ae-899875bbca0f" />


<h1>Minha evolução da semana 😎</h1>
<p align="center">
<img width="322" height="210" alt="image" src="https://github.com/user-attachments/assets/376754cd-d830-42ca-8a56-ab5e30d40e1a" />
</p>
