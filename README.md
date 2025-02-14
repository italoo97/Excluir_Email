# Excluir_Email

1 - Abrir o https://console.cloud.google.com/
2 - Crie um novo projeto ou selecione um existente.
3 - Em "acesso rápido" abra o APIs e serviços
4 - Habilite o "Gmail API"
5 - Crie uma Credencial "ID do cliente OAuth" e faça o dowload dela
6 - Salve ela em uma pasta com o nome "Credentials"
7 - Va em tela de Permissão OAuth > Publico Alvo e adicione um Usuario de Teste
8 - Em acesso a dados adicione o escopo manualmente 'https://www.googleapis.com/auth/gmail.modify'
8 - salve o codigo em Python na mesma pasta do Credentials
9 - Na linha DATA_EXCLUSAO informe a data no formato AAAA/MM/DD
