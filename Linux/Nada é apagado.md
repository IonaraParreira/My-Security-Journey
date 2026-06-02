No Linux, "Tudo é um arquivo" (Everything is a file). Não existe um "Registro" centralizado como no Windows. Em vez disso, as evidências ficam espalhadas em arquivos de configuração de texto puro, logs estruturados e metadados do próprio sistema de arquivos (como o Ext4).

Aqui estão os equivalentes e os artefatos forenses mais importantes para se estudar no Linux hoje:

<h1>1. Histórico do Shell (.bash_history / .zsh_history)</h1>
O equivalente mais direto (embora mais simples) ao Prefetch/Amcache do Windows para comandos executados. Cada usuário tem um arquivo oculto em sua pasta Home que guarda os últimos comandos digitados no terminal.

O que ele revela: Quais comandos o suspeito executou, scripts que ele rodou ou ferramentas que baixou.

Ponto de atenção forense: Um atacante experiente pode limpar esse arquivo usando history -c ou alterando a variável HISTSIZE=0. Por isso, peritos olham o timestamp do arquivo e buscam por fragmentos desses comandos que ainda possam estar isolados na memória RAM.<br>
<br>
<h1>2. Os Quatro Timestamps (Metadados do Ext4)</h1>
No Windows, costumamos olhar a data de criação, modificação e acesso. No Linux (usando sistemas de arquivos modernos como Ext4), existem quatro timestamps críticos armazenados no Inode de cada arquivo, conhecidos como MACB:

M (Modified): Quando o conteúdo do arquivo foi alterado.

A (Accessed): Quando o arquivo foi lido ou aberto.

C (Changed): Quando os metadados do arquivo (como permissões chmod ou dono chown) foram alterados.

B (Birth/Created): A data de criação original do arquivo (suportada nos sistemas de arquivos mais recentes).

Ferramenta para ver isso: O comando stat nome_do_arquivo.

3. O Diretório /var/log (A Mina de Ouro)
É aqui que o Linux centraliza as atividades do sistema. Para um perito, este diretório é o primeiro lugar a ser analisado após coletar a imagem do disco.

/var/log/auth.log (ou /var/log/secure no RedHat/CentOS): Registra todas as tentativas de login (sucessos e falhas) e o uso do comando sudo. Essencial para rastrear ataques de força bruta.

/var/log/syslog (ou /var/log/messages): O log geral do sistema, onde serviços reportam erros, inicializações e alertas.

/var/log/wtmp e /var/log/utmp: Arquivos binários (não abrem no bloco de notas) que registram quem está logado no momento e o histórico de conexões/reboots do sistema.

Como ler: Você usa os comandos last e lastb no terminal para interpretar esses arquivos.

4. Persistência e Agendamento (Crontab e Systemd)
Assim como os malwares no Windows usam chaves de Registro para iniciar com o sistema, no Linux eles usam serviços ou tarefas agendadas para garantir que continuem rodando mesmo após um reboot.

Cron Jobs: Arquivos em /etc/crontab e nos diretórios /etc/cron.*. Eles agendam tarefas para rodar repetidamente (ex: "execute este script oculto toda meia-noite").

Systemd Services: Arquivos de configuração em /etc/systemd/system/. Um atacante pode criar um serviço falso (ex: nginx-update.service) que na verdade executa um artefato malicioso em segundo plano.

5. Arquivos de Configuração de Rede (/etc)
Para entender se o sistema foi modificado para redirecionar tráfego ou aceitar conexões estranhas:

/etc/hosts: Pode ser adulterado para fazer técnicas de "DNS Spoofing" local (ex: apontar o domínio de um banco para o IP do atacante).

/etc/resolv.conf: Mostra quais servidores DNS a máquina está usando. Atacantes costumam alterar isso para servidores DNS maliciosos controlados por eles.

🛠️ Como praticar isso agora (No Terminal Linux)
Se você estiver em um terminal Linux (ou usando o WSL - Windows Subsystem for Linux no seu Windows), você pode rodar esses comandos para ver a forense acontecer:

Investigar as propriedades de um arquivo (Timestamps):

Bash<br>
stat /etc/passwd<br>
Isso vai te mostrar detalhadamente os tempos de Acesso, Modificação e Alteração do arquivo mais importante de usuários do sistema.

Ver quem logou recentemente no sistema:

Bash<br>
last<br>
Este comando lê o arquivo binário /var/log/wtmp e te dá uma tabela limpa de quais usuários logaram, por onde (terminal local ou SSH) e quanto tempo ficaram conectados.

Ver os logs de autenticação em tempo real (Simulação de Monitoramento):

Bash<br>
tail -f /var/log/auth.log<br>
(Nota: Em algumas distribuições modernas que usam apenas o systemd-journald, você usaria o comando journalctl -u ssh ou journalctl _AUDIT_TYPE=1006).
