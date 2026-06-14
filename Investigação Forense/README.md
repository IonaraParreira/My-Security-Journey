<h1>Capturar Dados antes que o computador seja desligado.</h1>(o 🖥️ é a sua testemunha mais importante.)

<br>Seus olhos não focam no corpo, 
nem nas marcas de sangue na parede, mas sim no brilho da tela de um desktop no canto da sala.

Pegando as luvas para manter a máxima  integridade da cena e evidências.

Mas antes de se aproximar do computador,antes de tocar no teclado ou no mouse imediatamente. 
<h2>O que olhar?? Tudo o que importa😅</h2>
<br>

1)Verificação de Energia: Observa se a torre está ligada, se o cooler está girando ou se há luzes de LED acesas, indicando que o sistema está operando.<br>

2)A "Captura Viva": Se o monitor estiver com a imagem ativa, ele fotografa a tela rapidamente, ciente de que qualquer ação pode alterar evidências voláteis na memória RAM.<br>

3)Inspeção Física: Olha por trás da máquina para verificar conexões de rede, pen drives ou dispositivos de armazenamento externo.Com o auxílio de um bloqueador de escrita portátil, e se prepara para isolar o dispositivo da rede e garantir que nenhum dado seja alterado.<br>

4)Anota mentalmente a necessidade de extrair imagens apagadas e logs de internet que podem ter sido gerados naquele exato momento.

A regra é: colete primeiro o que desaparece mais rápido. A RAM é o topo da lista. Se você desliga o servidor, as evidências de um ataque em tempo real (como um malware rodando apenas em memória) somem para sempre.

<h3>Você sabia? Na RAM enquanto seu código roda,armazena</h3>
Credenciais em texto claro: Senhas ou tokens de API que foram descriptografados para uso imediato.
<br>
Conexões de Rede: Endereços IP de onde os usuários estão vindo (mesmo que eles tentem apagar os logs depois).

Processos Ocultos: Scripts maliciosos que não foram salvos no disco para evitar detecção por antivírus comuns.

<h1>Ferramentas de Investigação</h1>

DumpIt ou FTK Imager: Usados para tirar uma "foto" (dump) de tudo o que está na RAM naquele instante.<br>
<br>
Volatility Framework: É o padrão ouro. Ele permite que você pegue esse arquivo de "dump" e pergunte: "Quais processos estavam rodando?" ou "Me mostre o histórico do terminal que o usuário usou".<br>


1. O Primeiro Passo: Captura com o DumpIt
O DumpIt é uma ferramenta de "um clique". Ele é essencial porque, na forense, quanto menos você mexe no sistema alvo, melhor (para não sobrescrever dados na RAM).

Como usar: Você executa o .exe como administrador diretamente de um pendrive (para não instalar nada no HD da vítima).

O que ele faz: Ele lê toda a memória RAM física e gera um arquivo bruto, geralmente com a extensão .raw ou .dmp (ex: MEMORIA.raw).

O resultado: Se o computador tem 16GB de RAM, o arquivo terá exatamente 16GB. É um "espelho" bit a bit de tudo o que estava acontecendo.

2. O Segundo Passo: Análise com o Volatility
Agora que você tem o arquivo .raw no seu computador de trabalho, você usa o Volatility para "interrogar" esse arquivo.

Comandos Essenciais (Volatility 3):
A. Identificar as informações do sistema:
Antes de tudo, você precisa saber qual era o SO para o Volatility entender como a memória estava organizada.

Bash
python3 vol.py -f MEMORIA.raw windows.info
B. Listar Processos (O "Task Manager" do passado):
Isso mostra todos os processos que estavam rodando no momento do dump. É aqui que você procura por nomes estranhos ou processos sem pai.

Bash
python3 vol.py -f MEMORIA.raw windows.pslist
C. Ver Conexões de Rede:
Como programadora backend, isso vai te brilhar os olhos. Você consegue ver sockets abertos, IPs remotos e portas, mesmo que a conexão já tenha sido fechada!

Bash
python3 vol.py -f MEMORIA.raw windows.netscan
D. Extrair Senhas e Hashes:
O comando hashdump tenta extrair os hashes das senhas dos usuários que estavam carregados na memória.

Bash
python3 vol.py -f MEMORIA.raw windows.hashdump
Por que isso é importante para o seu backend?
Imagine que seu servidor sofreu um ataque de Fileless Malware (malware que não salva arquivos no disco, só roda na RAM). Se você apenas reiniciar o servidor, você apaga a única prova do crime. Usar o DumpIt garante que você tenha a "cena do crime" congelada para estudar depois com o Volatility.

Elas são de graça?
Sim! Ambas são ferramentas de código aberto (Open Source) e gratuitas, amplamente utilizadas por profissionais de segurança e perícia digital no mundo todo.

Como "instalar"?
DumpIt (Windows)
Ele não precisa de instalação (é o que chamamos de portable).

Você baixa o executável.

Clica com o botão direito e seleciona "Executar como Administrador".

Ele vai perguntar se você quer confirmar a captura. Digite y (yes).

Ele salva o arquivo na mesma pasta onde o executável está.

Volatility 3 (Multiplataforma)
Como você é dev, vai tirar de letra. Ele é um projeto em Python.

Você faz um git clone do repositório oficial no GitHub.

Instala as dependências (geralmente via pip install -r requirements.txt).

Roda ele direto pelo terminal usando o comando python vol.py.

1. Na Máquina da Vítima (Coleta)
Você não usa o Volatility lá. Você usa apenas a ferramenta de coleta (o DumpIt), que é "standalone" (não precisa de instalação).

Você chega com um Pendrive Pericial (com trava de escrita, se possível).

Roda o DumpIt.exe direto do pendrive.

Salva o arquivo .raw de volta no seu pendrive ou em um HD externo.

Pronto. Você retira o pendrive e deixa o computador da vítima exatamente como estava (ou o desliga, dependendo do protocolo).

2. Na SUA Máquina (Análise)
A análise nunca é feita no computador invadido. Você leva o arquivo .raw para o seu computador de trabalho (o seu laboratório).

É no seu computador que o Python e o Volatility estarão instalados.

Lá, você processa o arquivo com calma, sem pressa e sem medo de alterar a cena do crime original.


<h1>Para não alterar nenhum dado😌☝🏻</h1><br>

>É importante usar os bloqueadore físicos ou montagem via software.<br>

Abaixo estão as práticas essenciais para preparar e conduzir o processo de forma segura😉:
1. Bloqueador de Escrita (Write Blocker)
A forma mais segura e recomendada é o bloqueador de escrita por hardware.
O que faz: Intercepta os comandos do computador, permitindo que você leia o disco de destino sem a possibilidade de enviar dados ou alterar o sistema de arquivos.
Como usar: Conecte o disco suspeito a um Write Blocker (dispositivo de hardware) e conecte-o à sua estação forense via USB/SATA. 

2. Bloqueio por Software (Caso não use hardware)
Se não possuir o bloqueador físico, você deve bloquear a escrita via sistema operacional. 

No Linux:
Identifique o disco (ex: /dev/sdb) e force o modo leitura:
sudo hdparm -r1 /dev/sdb 

No Windows:
Abra o prompt de comando (CMD) como Administrador e digite diskpart: 

Digite list disk e identifique o número do disco alvo.
Selecione o disco: select disk X (substitua pelo número correto).
Ative o atributo de leitura: attributes disk set readonly.<br>

3. Utilização de Sistemas Operacionais Forenses
A melhor prática consiste em iniciar o computador de análise com uma distribuição Linux focada em forense.
O CAINE ou o DEFT são sistemas operacionais inicializáveis (Live USB) que possuem bloqueio automático de escrita nativo em todas as mídias conectadas.
Eles garantem que o sistema operacional de análise não toque ou modifique o disco alvo durante o processo. 
<br>

4. Criação da Imagem Forense
Após montar o disco em modo leitura, nunca analise o disco original diretamente. Você deve criar uma imagem (cópia bit-a-bit). 
Utilize ferramentas de duplicação forense para criar um arquivo de imagem (como .E01 ou .raw).
O FTK Imager (Windows) ou ferramentas de linha de comando como dc3dd são referências no mercado.
<br>

5. Cálculo e Verificação de Hash
Para garantir que a cópia é idêntica ao original:
Calcule o valor de hash (como MD5 ou SHA-256) do disco original antes da cópia e do arquivo de imagem gerado ao final.
Os valores de hash devem ser exatamente iguais, o que prova a integridade da evidência para fins legais. 
A partir desse ponto, você realiza a análise forense utilizando a cópia exata do disco, preservando a mídia original intacta. 

<h1>Logs:Melhores práticas - armazenamento,retenção e exclusão </h1>


* Defina a política de armazenamento,retenção e exclusão com base nas necessidades da empresa e nos requisitos legais.
* Revisar e atualizar regularmente as diretrizes de acordo com as mudanças nas condições e regulamentações.
* Automatize os processos de armazenamento,retenção e exclusão para garantir consistência e evitar erros humanos.
* Criptografe registros confidenciais para proteger os dados.
* É essencial fazer backups regulares,especialmente antes da exclusão de arquivos.

<h1>A prática!</h1>
>Primeiramente a Cadeia de Custódia

Estou com uma folha de papel do lado assinando um documento físico. Escrevendo:

"Eu, Perita Ionara, coletei o log 'auth.log' às 21:50 do dia 14/06/2026, com o Hash X, e guardei no pendrive de etiqueta nº 42." Toda pessoa que encostar nesse pendrive depois de mim tem que assinar esse papel. Se o pendrive mudar de mãos e alguém esquecer de assinar, a cadeia de custódia quebra, e a prova perde o valor no tribunal.

<h2>Como cada acontecimento aconteceu,em detalhes</h2>
O relógio marca 21:42. O prédio corporativo está vazio, exceto pelas luzes piscando na sala do servidor e pelo som constante do ar-condicionado industrial.

🛑 O Cenário: A Chegada à Cena do Crime Digital
Eu recebo o chamado: "Houve um acesso não autorizado na máquina da Diretoria Financeira. O atacante pode ter deixado rastros, mas o computador ainda está ligado."

Entro na sala. Meus olhos não focam nas mesas organizadas, mas sim no brilho da tela de um desktop no canto da sala. A tentação de qualquer leigo seria mexer no mouse, abrir as pastas ou desligar o computador da tomada. Mas sou uma CSI. Sei que a memória RAM apaga quando o computador desliga e que os metadados dos arquivos mudam se clicar em qualquer coisa.

🕵️‍♂️ Passo 1: O Armazenamento (A Coleta das Evidências)
Minha missão agora é extrair os logs de acesso sem contaminar a cena.

Isolamento: Eu desconecto o cabo de rede azul atrás da CPU. Por quê? Para garantir que o hacker, se ainda estiver conectado remotamente, não envie um comando para apagar os logs enquanto trabalho. O computador está isolado do mundo, mas vivo.

O Kit Pericial: Abro a maleta e puxo um Bloqueador de Escrita Hardware (um dispositivo que permite que os dados saiam do computador investigado para o meu drive, mas impede fisicamente que qualquer dado seja gravado de volta na máquina do crime).

A Captura: Eu plugo o meu "Pendrive Forense" através do bloqueador. Com um software automatizado direto de um CD pericial portátil, faço a extração do arquivo de log.

O Momento "Flash" (Integridade): Assim que o arquivo de log cai no meu pendrive seguro, rodo o algoritmo. A tela pisca em verde e gera uma chave única (o Hash SHA-256):

SHA-256=a8f5c2...3d91e0
Tiro uma foto da tela com a câmera do meu celular e anoto essa sequência no meu bloco de notas físico. Esse código é a impressão digital do log. Se o advogado de defesa do hacker disser no tribunal que eu alterei uma linha do arquivo para incriminar o cliente dele,eu recalculo o Hash na frente do juiz. Se bater com o meu bloco de notas, a prova é incontestável.

🗄️ Passo 2: A Retenção (A Linha do Tempo no Laboratório)
Volto para o laboratório de análise forense. Agora, o desafio é entender o padrão do ataque cruzando com as políticas de retenção da empresa.

A Investigação Histórica: Abro o log coletado. O ataque aconteceu hoje, mas eu preciso saber se o hacker já vinha sondando a empresa há semanas.

Buscando no Arquivo Morto: Solicito ao administrador da rede os logs de retenção dos meses anteriores. A empresa guarda os logs compactados em um servidor isolado por 90 dias.

Começo a descompactar os logs antigos (log.tar.gz de 30 dias atrás). Na tela do meu monitor duplo, as linhas de texto rolam rápido em uma sala escura. De repente, eu congelo os olhos em uma linha: exatamente há 22 dias, o mesmo endereço IP suspeito tentou fazer um ataque de SQL Injection na página de login às 03:14 da madrugada. Eles estavam testando as defesas. Você acabou de traçar a linha do tempo do crime.

✂️ Passo 3: A Exclusão (Limpando os Rastros após o Caso Fechado)
O caso foi resolvido, o relatório foi entregue, o invasor foi identificado e o processo judicial foi arquivado. Por lei e proteção de dados (LGPD), eu não posso manter dados confidenciais daquela empresa ou de terceiros flutuando nos meus drives periciais para sempre. Chegou a hora do descarte seguro.

O Perigo do "Deletar" Comum: Eu sei que clicar com o botão direito e ir em "Esvaziar Lixeira" apenas diz ao sistema operacional: "Este espaço está livre para ser gravado por cima", mas o arquivo continua lá, invisível, esperando alguém recuperá-lo.

A Incineração Digital: Eu conecto o drive de evidências em uma máquina isolada.Ativo uma ferramenta de destruição padrão DoD (Departamento de Defesa).

A Execução: Na tela, um gráfico de barras avança enquanto o software escreve sequências aleatórias de 0 e 1 em cima do arquivo de log. Ele faz isso uma, duas, três vezes. É como pegar o documento, passar no triturador de papel, queimar as tiras e jogar as cinzas no oceano. O log desapareceu do universo digital para sempre. Nenhum hacker ou outro perito conseguirá recuperá-lo.

Eu limpei a mesa, guardei as ferramentas na maleta e fechei o meu relatório de investigação. Missão cumprida! O sistema está seguro por hoje. 😎💼

