def validar(cpf):
    if len(cpf) != 14:
        print("O formato do CPF é inválido, siga o formato 'xxx.xxx.xxx-xx'.")
        return False
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print("O formato do CPF é inválido, siga o formato 'xxx.xxx.xxx-xx'.")
        return False
    
    rpl = cpf.replace(".", "").replace("-", "")
    if not rpl.isdigit() or len(rpl) != 11:
        print("O CPF deve conter apenas números, traço e número, seguindo o formato 'xxx.xxx.xxx-xx'.")
        return False
    
    numeros = []
    for i in rpl:
        numeros.append(int(i))

# Primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += numeros[i] * (10 - i)
    resto = soma % 11
    if resto < 2:
        d1 = 0
    else:
        d1 = 11 - resto

 # Verificação 1
    if d1 != numeros[9]:
        print("CPF inválido")
        return False

# Segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += numeros[i] * (11 - i)
    resto = soma % 11
    if resto < 2:
        d2 = 0
    else:
        d2 = 11 - resto

# Verificação 2
    if d2 != numeros[10]:
        print("CPF inválido")
        return False
    
    print("CPF válido")
    return True

# void main() {
cpf_input = input("Digite um CPF no formato xxx.xxx.xxx-xx: ")
validar(cpf_input)
# }