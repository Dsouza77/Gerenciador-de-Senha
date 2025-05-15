from cryptography.fernet import Fernet
import random
import string
import os

#gerar a chave somente se ela não existir
if not os.path.exists("key.key"):
    #Preciso gerar a chave
    key = Fernet.generate_key()
    #Botei a chave dentro do meu arquivo "key"
    with open("key.key", "wb") as code:
        code.write(key)

    fernet = Fernet(key)

else:
#Coloquei a chave dentro da variável "key"
    with open("key.key", "rb") as code:
        key = code.read()

    fernet = Fernet(key)


#interação com o usuário
print("\n=================KEY MANAGER=================")
print("Gerar nova senha: 1\nConsulta senha: 2\nExcluir senha: 3\n")
opcao = int(input("/: "))

if opcao == 1:
    #gerar nova senha
    digitos = int(input("Quantos digitos terá sua nova senha: "))
    regra_senha = str(string.ascii_letters + string.digits + string.punctuation)
    senha_gerada = str(''.join(random.choice(regra_senha) for _ in range(digitos)))
    print(f'\nNova senha gerada: {senha_gerada}\n')
    
    #criptografa a senha
    senha_bytes = senha_gerada.encode()
    #print(senha_bytes)
    senha_criptografada = fernet.encrypt(senha_bytes)
    #print(senha_criptografada)

    #escrever a senha criptografada no file
    with open("file.txt", "wb") as escreve:
        escreve.write(senha_criptografada)
        print("Senha criptografada com sucesso!\n")

elif opcao == 2:
    try:
        #descriptografar
        #pegar oque está escrito no file (pra descriptografar)
        with open("file.txt", "rb") as descrypt:
            conteudo = descrypt.read()
            print(f"Senha criptografada: {conteudo.decode()}")

        #descriptografa o conteúdo
            senha_descriptografada = fernet.decrypt(conteudo)
            print(f"Senha descriptografada: {senha_descriptografada.decode()}")

    except Exception as e:
        print("Erro ao descriptografar", e)

elif opcao == 3:
    #Pegar oque está escrito no file
    with open("file.txt", "wb") as clear:
        lixo = "Nenhuma senha por aqui..."
        lixo_byte = lixo.encode()
        lixo_encrypt = fernet.encrypt(lixo_byte)
        clear.write(lixo_encrypt)
        print("Senha excluida com sucesso!")

else:
    print("exit...")
