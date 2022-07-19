import PyPDF2

arquivo = r"C:\Users\leand\Documents\pdf\intranet-crim-DeveloperWorkbook.pdf"
lerpdf = PyPDF2.PdfFileReader(arquivo)
with open('testeResultado.txt', 'w',encoding="utf-8") as arquivo:
    for i in range(2448, 3202):
        pagina =lerpdf.getPage(i)
        conteudo = pagina.extractText()
        print(conteudo, file=arquivo)
