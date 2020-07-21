from readability.readability import Document
import requests
import sys
import time
import re


def getPage(url):
    while True:
        espera = 0
        try:
            response = requests.get(url)
            return response
        except Exception:
            print("Nao Rolou")
            time.sleep(2 ** espera)
            espera += 1

def main():
    novels = {'cbi': 'https://boxnovel.com/novel/castle-of-black-iron/chapter-', 'sgg': 'https://boxnovel.com/novel/super-gene-webnovel/chapter-',
              'sas': 'https://boxnovel.com/novel/strongest-abandoned-son/chapter-', 'atg': 'https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-',
              'vm' : 'https://boxnovel.com/novel/versatile-mage/chapter-'}
    total = []
    if len(sys.argv) < 4:
        inicio = int(sys.argv[2])
        fim = int(sys.argv[2]) + 1
    else:
        inicio = int(sys.argv[2])
        fim = int(sys.argv[3]) + 1

    url = novels[sys.argv[1]]
    for i in range(inicio, fim):
        response = getPage(f"{url}{i}") # f"" e a funcao de template literal onde coloca a experessao entre {} e ela e substituida na string ex print(f"{1+1} vs {nomeVariavel}")
        doc = Document(response.text)
        fileName = re.sub(r'[^a-zA-Z0-9]+', ' ', doc.title())
        total.append(doc.summary())
        print(i)

    f = open(f"{fileName}{fim-1}.html", 'w')
    for i in total:
        f.write(i)
    f.close()

main()
