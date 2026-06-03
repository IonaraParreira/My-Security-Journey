<h1>Nada fica apagado</h1>
TUDO DEIXA RASTRO

1. O Registro do Windows (Windows Registry)
O Registro é o banco de dados central do Windows. Ele guarda configurações do sistema, do hardware e de cada usuário. Para a perícia, ele é uma mina de ouro.

O que ele revela: Quais pendrives já foram plugados na máquina (com número de série e data), quais redes Wi-Fi o computador já se conectou, e quais programas estão configurados para iniciar sozinhos com o sistema (mecanismos de persistência muito usados por malwares).

Chaves famosas para pesquisar: As chaves de Run e RunOnce (onde ficam os programas que iniciam com o Windows) e a chave USBSTOR (que lista todos os dispositivos USB já conectados).

2. Arquivos Prefetch (.pf)
O Windows criou o sistema de Prefetch para fazer os programas abrirem mais rápido. Quando você executa um software pela primeira vez, o Windows cria um arquivo .pf na pasta C:\Windows\Prefetch.

O que ele revela: Se um programa foi executado, quantas vezes ele foi aberto, a data e hora exata da última execução, e quais arquivos e DLLs ele carregou nos primeiros 10 segundos.

Importância forense: Se um atacante usou uma ferramenta hacker (como o Mimikatz para roubar senhas) e depois deletou o executável, o arquivo Prefetch ainda estará lá, provando que a ferramenta rodou naquela máquina.

3. Shellbags
Sabe quando você abre uma pasta no Windows Explorer, muda a visualização para "Ícones Grandes", fecha a pasta e, meses depois, quando abre de novo, ela ainda está em "Ícones Grandes"? O Windows precisa salvar essa preferência em algum lugar. Esse lugar são os Shellbags.

O que ele revela: O nome e o caminho de pastas que existiram no sistema, mesmo que elas tenham sido deletadas ou estivessem em um pendrive que já foi removido. Ele prova que o usuário sabia da existência e acessou aquela pasta específica.

4. Jump Lists e Atalhos (.lnk)
As Jump Lists são aqueles menus que aparecem quando você clica com o botão direito no ícone de um programa na Barra de Tarefas (mostrando os arquivos "Recentes" ou "Fixados").

O que ele revela: Arquivos específicos que o usuário abriu recentemente por meio daquele aplicativo, mesmo que o arquivo original tenha sido apagado ou movido para a nuvem.

5. Amcache.hve
Este é um arquivo de registro especial que o Windows usa para rastrear a compatibilidade de aplicativos.

O que ele revela: Ele guarda o hash SHA-1 dos executáveis instalados ou rodados no sistema, além do caminho do arquivo e a data de criação. É excelente para analistas forenses cruzarem o hash encontrado com bancos de dados de malwares conhecidos (como o VirusTotal).

<h1>🛠️ Como você pode ver isso na prática (Sem instalar quase nada)</h1>
Como você está no Windows, pode explorar isso agora mesmo de duas formas:

Nativamente (Olhar o Prefetch):

Abra o seu menu Iniciar, digite Executar (ou use o atalho Win + R).

Digite prefetch e dê Enter (o Windows vai pedir permissão de administrador, pode clicar em continuar).

Você verá uma lista enorme de arquivos .pf. Cada um representa um programa que rodou na sua máquina.

Usando ferramentas do mestre Eric Zimmerman:
Na comunidade forense, um especialista chamado Eric Zimmerman criou ferramentas gratuitas incríveis (via linha de comando e GUI) para ler esses arquivos, já que eles são binários e difíceis de ler no Bloco de Notas.

Procure por PECmd (para ler arquivos Prefetch).

Procure por ShellBags Explorer (para ver o histórico de pastas de forma visual).
