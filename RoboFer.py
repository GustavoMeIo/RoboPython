import PyPDF2
import os
import glob

class pdf:
    @staticmethod
    def ler_penultima_linha(caminho_txt):
        with open(caminho_txt, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()  # lê as linhas do arquivo

            penultima_linha = linhas[-2]  # obtém a penúltima linha
            partes_linha = penultima_linha.split(termo_proucurado)  

            valor = partes_linha[0].strip()  # obtém a primeira parte da linha (antes de 'LUCIENE') e remove espaços em branco

            return valor

    @staticmethod
    def extrair_texto_pdf(caminho_pdf, caminho_txt):
        """
        Extrai o texto do arquivo PDF

        Args:
            caminho_pdf (str): caminho do arquivo pdf que deseja retirar o texto
            caminho_txt (str): caminho do arquivo de texto temporário que será gerado
        """
        with open(caminho_pdf, 'rb') as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            texto = ""

            for pagina in leitor_pdf.pages:
                # Para cada pagina no arquivo a váriavel 'texto' recebe a extração do texto da 'pagina'
                texto += pagina.extract_text()

            with open(caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                # Escreve em uma arquivo temporário o texto extraído
                arquivo_txt.write(texto)

        resposta = pdf.ler_penultima_linha(caminho_txt)
        os.remove(caminho_txt)
        os.rename(caminho_pdf, f'{resposta}.pdf')
        return resposta


# Pasta contendo os arquivos PDF
pasta = 'ARQUIVOS_pdf'

# Padrão de busca de arquivos PDF na pasta
padrao = os.path.join(pasta, '*.pdf')

# Lista de caminhos dos arquivos PDF
arquivos_pdf = glob.glob(padrao)

# Separa a linha pelo termo 'LUCIENE'
termo_proucurado = "LUCIENE"

# Loop para processar cada arquivo PDF
for caminho_pdf in arquivos_pdf:
    caminho_txt = 'arquivo_temp_pdf.txt'

    funcionario = pdf.extrair_texto_pdf(caminho_pdf, caminho_txt)
    print(funcionario)
