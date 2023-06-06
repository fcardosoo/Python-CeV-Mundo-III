'''
crie um código em python que teste se o site Pudim
está acessível pelo computador usado
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site <.br> Deu erro')
else:
    print('Site <.br> Tudo OK')
    print(site.read)

try:
    site2 = urllib.request.urlopen('http://www.pudim.com.uk')
except:
    print('Site <.uk> Deu POBLEMA')
else:
    print('Site <.uk>Tudo CERTIN')
    print(site2.read)
