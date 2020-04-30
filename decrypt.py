from string import ascii_lowercase as alfabeto
import requests
import hashlib

token = "21ec6c3bd0c77efcc05e041db0620192f5976cce"
url = f"https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={token}"

res = requests.get(url)
responseJson = res.json()
numero_casas = int(responseJson["numero_casas"])
encrypted = responseJson["cifrado"]
decrypted = responseJson["decifrado"]
resumo_criptografico = responseJson["resumo_criptografico"]

def decrypt():
    result = ''
    for letra in encrypted:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            result += alfabeto[posicao - numero_casas]
        else:
            result += letra
    return result

new_decrypt = decrypt()
resumo_criptografico = hashlib.sha1(str(new_decrypt).encode('utf-8')).hexdigest()

result_json = {
    "numero_casas": numero_casas,
    "token": token,
    "cifrado": encrypted,
    "decifrado": new_decrypt,
    "resumo_criptografico": resumo_criptografico
}

def postJson():
    url = f"https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={token}"
    file = {"answer": open("answer.json", "rb")}
    requests.post(url, files=file)
    print('Enviado com sucesso!!!')
