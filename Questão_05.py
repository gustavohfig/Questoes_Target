def inverter_string(string):
    # Inicialização de uma string vazia para armazenar a string invertida
    string_invertida = ""
    
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    # Retornar a string invertida
    return string_invertida

string_original = "Hello, world!"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
