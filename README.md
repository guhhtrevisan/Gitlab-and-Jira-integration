# BOT: VÍNCULO DE RENOVAÇÃO

Identifiquei que na empresa que trabalho exisita um fluxo exaustivo e complexo que poderia ser automatizado utilizando Python.
Trabalho em uma empresa de tecnologia de seguro, e basicamente o fluxo consiste no ato da renovação de apólices. Como nosso sistema não contempla o caso de renovação atráves de endossos, ou não realiza renovação diretamente pelo portal de apólices que já existem no sistema, tínhamos um fluxo de renovação bastante complexo e manual.

#### Basicamento, esse era o fluxo:
1. Alguém do time de operação identificava uma renovação;
2. Enviava um email para o suporte solicitando a criação do vínculo de renovação (esse email criava um card no Jira);
3. Alguém do suporte avaliava a solicitação fazendo uma série de verificações para validar se o vínculo poderia ser criado;
4. Após validar, criava um arquivo com a query gerando o vínculo na tabela de renovação;
5. Gerava uma nova branch no projeto do gitlab, criava um commit e um Merge Request com o arquivo da query;
6. Após o merge ser aprovado pelo time de produto e engenharia, o sujeito do suporte megeava e o vínculo estava criado!

Entretanto, eu averiguamos que esse fluxo poderia ser automatizado via Python.
Um colega de trabalho desenvolveu uma página utilizando Bubble em que o usuário de operação apenas insere qual o ID renovado e o ID renovação. Esses id's são inputados em uma tabela no banco de dados, e o BOT faz a leitura dessa tabela.

Nos arquivos acima você pode ver:
1. Funcoes_bot: as funções que geram as queries e os nomes do commit e merge request;
2. Vínculo de renovação: o código do BOT em sim, e todo o passo a passo da automação;
3. Merge approval: Script que verifica se o merge foi aprovado no gitlab, faz o merge, fecha o card no Jira e envia email automático para o usuário.
