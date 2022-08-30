# Guia de instalação e utilização deste projeto 

## Requerimentos
- Docker
- Git
- Python 3.9.12

## Deployment
Este projeto também está online na plataforma Heroku em [www]()
- login:
- senha:

## Instalação 
- Para ver o guia rápido de instalação, acesse esse [link]()

## Como utilizar o programa
O acesso ao sistema é feito pelo botão no canto superior direito. Se estiver testando a versão online, o acesso pode ser feito com as credencias disponibilizadas acima. 
Após o login, o usuário é redirecionado para a página inicial do sistema. Nela, já é possível verificar as opções presentes na barra de navegação vertical.
- Na opção 'Meus dados', o analista pode alterar seu nome, sobrenome e email. Neste projeto, a opção de cadastro de novo usuário e alteração de senha foram desabilitadas.
- Em 'Nova comunicação', o usuário pode cadastrar uma comunicação de perda. No formulário, existem validações de email e CPF feitas em JavaScript, assim como uma 
verificação de garantia de veracidade do evento informado, ou seja, caso o analista esteja inserindo uma comunicação de uma lavoura em um raio de 10km de outra já
cadastrada, com a mesma data em ambas, mas com eventos diferentes, um alerta aparecerá na tela.
- No item 'Todas as comunicações', é possível ver as entradas feitas por qualquer analista. No canto superior direito, existe a opção de busca de entradas por 
CPF do produtor.
- Cada comunicação na lista, possui ícones para ver detalhes, editar ou excluir a entrada.
<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/circle-info.svg" width="20" height="20">
<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/5.x/svgs/solid/edit.svg" width="20" height="20">
<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/5.x/svgs/solid/trash.svg" width="20" height="20">
- Na opção 'Exportar dados', o analista ainda pode gerar (com um clique) um arquivo .xlsx com todos os dados de comunicações no banco de dados.
