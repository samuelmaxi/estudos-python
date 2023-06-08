"""
Validação de nome de usuário Codeland
Faça com que a função CodelandUsernameValidation(str) pegue o parâmetro str sendo passado e determine se a string é um nome de usuário válido de acordo com as seguintes regras:

1. O nome de usuário tem entre 4 e 25 caracteres.
2. Deve começar com uma letra.
3. Pode conter apenas letras, números e o caractere de sublinhado.
4. Não pode terminar com um caractere de sublinhado.

Se o nome de usuário for válido, seu programa deve retornar a string true, caso contrário, retornar a string false.
"""

def verificador(nome):
    for letra in nome:
        ...