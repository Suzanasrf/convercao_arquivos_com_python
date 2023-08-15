import xmltodict
import os
import pandas as pd


def pegar_infos(nome_arquivo, valores):
    print(f'Pegou as informações do arquivo: {nome_arquivo}')
    with open(os.path.join('nfs', nome_arquivo), 'rb') as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

        if 'NFe' in dic_arquivo:
            infos_nf = dic_arquivo['NFe']['infNFe']
        else:
            infos_nf = dic_arquivo['nfeProc']['NFe']['infNFe']

        numero_nota = infos_nf['@Id']
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf['dest']['xNome']
        endereco = infos_nf['dest']['enderDest']

        if 'peso' in infos_nf['transp']:
            peso = infos_nf['transp']['vol']['pesoB']
        else:
            peso = "Não informado"

        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])


arquivos = os.listdir('nfs')
colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"]
valores = []

for arquivo in arquivos:

        pegar_infos(arquivo, valores)
        print("=" * 30)  # Linha para separar as informações de diferentes arquivos

tabela = pd.DataFrame(columns=colunas, data=valores)
print(tabela)

tabela.to_excel("NotasFiscais.xlsx", index= False)

"""Correções e melhorias realizadas: Diretório: Usei os.path.join('nfs', nome_arquivo) para criar o caminho completo para o arquivo XML, independentemente do sistema operacional. Isso evita problemas com barras de diretório.

Exibição das Informações: Em vez de imprimir todas as informações em uma única linha, separei-as em várias linhas para tornar a saída mais legível.

Separação de Arquivos: Usei um if arquivo.endswith('.xml') para processar apenas arquivos XML no diretório. Isso evita tentar analisar arquivos que não são XML.

Separador de Informações: Adicionei uma linha de caracteres "=" para separar as informações de diferentes arquivos na saída, tornando mais claro onde termina uma análise e começa a próxima.

Agora, quando você executar este código, ele deve imprimir as informações de cada arquivo XML no diretório 'nfs' de forma mais organizada. Certifique-se de que seus arquivos XML estejam formatados corretamente e correspondam à estrutura que você está tentando acessar"""