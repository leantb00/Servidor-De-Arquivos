import xmlrpc.client

p0 = xmlrpc.client.ServerProxy("http://localhost:3000/")
p1 = xmlrpc.client.ServerProxy("http://localhost:3000/")
print("Para Acesso Ao Sistema Entre Com Nome E Senha:")
nome=input("Nome Do Usuário:")
senha=input("Senha:") 
x=p0.autenticacaoDeUsuario(nome, senha)
if x == "Permitido Acesso":
    with open ("DownloadDaMusica.mp3", "wb") as b: #Esse arquivo é o nome do arquivo que será baixado no pc de vcs pelo servidor. Vocês tem que colocar o arquivo da musica mp3, na mesma pasta dos scripts de python.Esse é o nome daquele arquivo Neo.mp3, só que com outro nome.É a cópia que o cliente pega do servidor.Então ele escolhe outro nome para aquele arquivo que está no servidor.  
        print("Carregando arquivo...")
        b.write(p1.obterAudio().data)
        print("Arquivo carregado.") 
else:
     print("Acesso Negado")
     print("Você não tem permissão para carregar o arquivo.")
