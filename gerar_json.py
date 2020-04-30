from decrypt import result_json
import json

def arquivoJson():
    arquivo = open('answer.json', 'w')
    json.dump(result_json, arquivo, indent=4, sort_keys=False)
    arquivo.close()
    print('Arquivo json gerado com sucesso!')
