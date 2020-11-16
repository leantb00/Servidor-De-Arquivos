import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
porta=3000

def autenticacaoDeUsuario(nomeDoUsuario, senha):
    if (nomeDoUsuario == "paulo" and senha == '007'):
        return "Acesso Permitido"
        
    else:
        return "Acesso Negado"

def obterAudio():
    with open("Neo.mp3","rb") as x: #coloquem o nome do arquivo mp3 que vcs forem testar. Nesse caso pus esse nome no arquivo que fiz download na net, prara testar. O arquivo baixado da net, deve ficar na mesma pasta onde foi colocado os scripts do servidor e do cliente. E o arquivo baixado do servidor vai para essa mesma pasta, só que com outro nome.
        return xmlrpc.client.Binary(x.read())



servidor = SimpleXMLRPCServer(("localhost", porta))
print("Servidor escutando na porta...%i." %(porta))
servidor.register_function(obterAudio,"obterAudio")
servidor.register_function(autenticacaoDeUsuario,"autenticacaoDeUsuario")
servidor.serve_forever()
