import bs4
import requests

def getip():
    try:
        step = '0'
        s = requests.get('https://2ip.ua/ua/')
        step = '1'
        b = bs4.BeautifulSoup(s.text, "html.parser")
        step = '2'
        a = b.select(" Ваша IP адреса")[0].getText()
        step = '3'
        a = a.strip()
        print(a)
        a = '0.0.0.0'
    except:
        print('Ошибка определения адреса.....'+step)
    else:
        return a
        print("Текущий адрес " + a)
getip()