from tkinter import *
import requests
from bs4 import BeautifulSoup

coins = []
prise_coins = []
page = 1

while True:
    r = requests.get('https://www.coingecko.com/?page=' + str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    if(page<6):
        for row in soup.select('tbody tr'):
            row_prise = [x.text for x in row.find_all('td', class_="td-price")]
            row_coin = [y.text for y in row.find_all('span', class_="font-normal")]

            Coin = (', '.join(row_coin))
            Prise = (', '.join(row_prise))

            coins.append(Coin.strip())
            prise_coins.append(Prise.strip())
        page += 1
    else:
        break
dict = dict(zip(coins, prise_coins))


window = Tk()
window.geometry('350x200')
window.title('Парсер')
window.resizable(width=False, height=False)
window['bg'] = 'Gray70'


value = StringVar()


def test():
    get = value.get().upper()
    l['text'] = dict.get(get)


def frame():
    frame1 = Label(text='', background='Gray70', pady=10)
    frame1.pack()

frame_top = Frame(window, bg='gold', bd=1)
frame_top.place(relx=0.15, rely=0.15, relheight=0.25, relwidth=0.7)

frame_button = Frame(window, bg='gold', bd=1)
frame_button.place(relx=0.40, rely=0.15, relheight=0.4, relwidth=0.2)


e = Entry(frame(), textvariable=value, bg='gray90',font=('Arial', 15))
e.pack()
b = Button(command=test, text='Поиск', bd=3, font=0.2)
b.pack()
l = Label(frame(), text='Prise $$$', bg='gold', font=50, bd=3)
l.pack()



window.mainloop()



