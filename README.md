# Excluir_Email

1 - Abrir o https://console.cloud.google.com/
2 - Crie um novo projeto ou selecione um existente.
3 - Em "acesso rápido" abra o APIs e serviços
4 - Habilite o "Gmail API"
5 - Va em tela de Permissão OAuth > Publico Alvo e adicione um Usuario de Teste
6 - Em acesso a dados adicione o escopo manualmente 'https://www.googleapis.com/auth/gmail.modify'
7 - Crie uma Credencial "ID do cliente OAuth" e faça o dowload dela
8 - Salve ela em uma pasta com o nome "Credentials"
9 - salve o codigo em Python na mesma pasta do Credentials
10 - Na linha "date_query" informe a data no formato AAAA/MM/DD
RODE O ARQUIVO NO TERMINAL

# verification.py

- serve para verificar as permissoes do arquivo "token.pickle"
- o arquivo token.pickle é criado na primeira vez que o codigo é rodado
- ele e a autorização do google para rodar a automação no seu email
- caso de algum erro rode ele para ver se as permissoes estão corretas
