listaLogin = ["joao", "maria", "pedro", "ana", "carlos", "beatriz"]
listaSenha = ["123", "456", "789", "abc", "def", "ghi"]

usuarios = {
    "joao": "123",
    "maria": "456",
    "pedro": "789",
    "ana": "abc",
    "carlos": "def",
    "beatriz": "ghi"
}


login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login in usuarios:
    if senha == usuarios[login]:
        print("Login e senha válidos.")
    else:
        print("Senha inválida.")
else:
    print("Login inválido.")