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
<h1>Minha evolução da semana 😁</h1>
<p align="center">
<img width="596" height="342" alt="Captura de tela 2026-06-12 064250" src="https://github.com/user-attachments/assets/6d78cb56-9c68-4896-8741-a436bd5616c2" />
</p>



