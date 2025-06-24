import csv

#corregindo texto mal formatado e acentos incorretos
def corrigir_acentos(texto):
    try:
        return texto.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return texto  

# arquivo original separado por tabulações e/ou ;
arquivo_entrada = 'pt_BR1-corrigido.csv'

# o arquivo que será gerado com vírgulas reais
arquivo_saida = 'pt_BR1-final.csv'

# lendo o arquivo original que ta separado por tabulações e ;
with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
    leitor = csv.reader(entrada, delimiter=';')
    dados_corrigidos = []
    for linha in leitor:
        nova_linha = [corrigir_acentos(campo) for campo in linha]
        dados_corrigidos.append(nova_linha)

# salva o arquivo final com vírgulas
with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as saida:
    escritor = csv.writer(saida, delimiter=',')
    escritor.writerows(dados_corrigidos)

print(f'Arquivo corrigido e salvo com sucesso: {arquivo_saida}')
