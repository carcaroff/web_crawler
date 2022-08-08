from pathlib import Path
from tkinter import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
from re import sub
from decimal import Decimal
sns.set()

df = pd.read_json('https://raw.githubusercontent.com/carcaroff/web_crawler/main/hardware_scraper/placas_de_video.json')
# print(data)
# df = pd.json_normalize(data)

df['preco_a_vista'] = df['preco_a_vista'].str.replace(' ', '')
df['preco_a_vista'] = df['preco_a_vista'].str.replace('.', '')
df['preco_a_vista'] = df['preco_a_vista'].str.replace(',', '.')
df['preco_a_vista'] = df['preco_a_vista'].str.replace('R', '')
df['preco_a_vista'] = df['preco_a_vista'].str.replace('$', '')

df['preco_parcelado'] = df['preco_parcelado'].str.replace(' ', '')
df['preco_parcelado'] = df['preco_parcelado'].str.replace('.', '')
df['preco_parcelado'] = df['preco_parcelado'].str.replace(',', '.')
df['preco_parcelado'] = df['preco_parcelado'].str.replace('R', '')
df['preco_parcelado'] = df['preco_parcelado'].str.replace('$', '')

df['nome'] = df['nome'].str.replace(' ', '')

df['preco_a_vista'] = pd.to_numeric(df['preco_a_vista'])
df['preco_parcelado'] = pd.to_numeric(df['preco_parcelado'])

def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

models = [
          'GTX1050TI',
          'GTX1650',
          'GTX1660TI',
          'GTX1660',
          'RTX3060TI',
          'RTX2060',
          'RTX3060',
          'RTX3070TI',
          'RTX3070',
          'RTX3080TI',
          'RTX3080',
          'RTX3090',
          'RX6900XT',
          'RX6800XT',
          'RX6800',
          'RX6700XT',
]

for index, value in enumerate(df['nome']):
  is_pv = False
  for model in models:
    if model in value.upper():
      df['nome'] = df['nome'].str.replace(value, insert_str(model, '-', 2))
      is_pv = True
  if not is_pv:
    df = df.drop(index=index)

df['nome'] = df['nome'].str.replace('-', '')

lojas = {
    'https://www.pichau.com.br/hardware/placa-de-video': 'Pichau',
    'https://www.amazon.com.br/b?node=16364811011&ref=lp_16364750011_nr_n_9': 'Amazon',
    'https://www.chipart.com.br/placa-de-video': 'Chipart',
}

def _get_loja(url):
  return lojas[url]


df['loja'] = df['url'].apply(_get_loja)
df['data'] = pd.to_datetime(df['data'], dayfirst=True)

df_pichau = df[df['loja'] == 'Pichau']
df_amazon = df[df['loja'] == 'Amazon']
df_chipart = df[df['loja'] == 'Chipart']

#Pichau
df_pichau = df_pichau.groupby(['nome', 'data']).aggregate(
        {'nome': 'first', 'preco_a_vista': 'min', 'preco_parcelado': 'min', 'data': 'first'}).reset_index(drop=True)
df_pichau.set_index('data', inplace=True)

#Amazon
df_amazon = df_amazon.groupby(['nome', 'data']).aggregate({'nome': 'first', 'preco_a_vista': 'min', 'preco_parcelado': 'min', 'data': 'first'}).reset_index(drop=True)
df_amazon.set_index('data', inplace=True)

#Chipart
df_chipart = df_chipart.groupby(['nome', 'data']).aggregate({'nome': 'first', 'preco_a_vista': 'min', 'preco_parcelado': 'min', 'data': 'first'}).reset_index(drop=True)
df_chipart.set_index('data', inplace=True)

#3060TI
df_3060ti = df[df['nome'] == 'RTX3060TI']
df_3060ti = df_3060ti.groupby(['loja', 'data']).aggregate({'loja': 'first', 'preco_a_vista': 'min', 'preco_parcelado': 'min', 'data': 'first'}).reset_index(drop=True)
df_3060ti.set_index('data', inplace=True)

#3070
df_3070 = df[df['nome'] == 'RTX3070']
df_3070 = df_3070.groupby(['loja', 'data']).aggregate({'loja': 'first', 'preco_a_vista': 'min', 'preco_parcelado': 'min', 'data': 'first'}).reset_index(drop=True)
df_3070.set_index('data', inplace=True)

#3080TI
df_3080ti = df[df['nome'] == 'RTX3080TI']
df_3080ti = df_3080ti.groupby(['loja', 'data']).aggregate({'loja': 'first', 'preco_a_vista': 'min', 'preco_parcelado': 'min', 'data': 'first'}).reset_index(drop=True)
df_3080ti.set_index('data', inplace=True)

def pichauMenor():
    df_pichau.groupby(['nome'])['preco_a_vista'].plot(title="Pichau", figsize=(20, 10), legend=True)
    plt.show()

def amazonMenor():
    df_amazon.groupby(['nome'])['preco_a_vista'].plot(title="Amazon", figsize=(20, 10), legend=True)
    plt.show()

def chipartMenor():
    df_chipart.groupby(['nome'])['preco_a_vista'].plot(title="Chipart", figsize=(20, 10), legend=True)
    plt.show()

def compara3060ti():
    df_3060ti.groupby(['loja'])['preco_a_vista'].plot(title="RTX 3060TI", figsize=(20, 10), legend=True)
    plt.show()

def compara3070():
    df_3070.groupby(['loja'])['preco_a_vista'].plot(title="RTX 3070", figsize=(20, 10), legend=True)
    plt.show()

def compara3080ti():
    df_3080ti.groupby(['loja'])['preco_a_vista'].plot(title="RTX 3080TI", figsize=(20, 10), legend=True)
    plt.show()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")

def comparacao():
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=1024,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        1024.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("comparacao/image_1.png"))
    image_1 = canvas.create_image(
        719.0,
        511.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("comparacao/button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=compara3060ti,
        relief="flat"
    )
    button_1.place(
        x=479.0,
        y=376.0,
        width=481.0,
        height=111.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("comparacao/button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=compara3070,
        relief="flat"
    )
    button_2.place(
        x=479.0,
        y=551.0,
        width=481.0,
        height=111.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("comparacao/button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=compara3080ti,
        relief="flat"
    )
    button_3.place(
        x=479.0,
        y=726.0,
        width=481.0,
        height=111.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("comparacao/image_2.png"))
    image_2 = canvas.create_image(
        719.0,
        125.0,
        image=image_image_2
    )

    canvas.create_text(
        200.0,
        55.0,
        anchor="nw",
        text="Placa para comparar:",
        fill="#FFFFFF",
        font=("Roboto Bold", 96 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def menorPreco():
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=1024,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        1024.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("mais_barato/image_1.png"))
    image_1 = canvas.create_image(
        719.0,
        511.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("mais_barato/button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=pichauMenor,
        relief="flat"
    )
    button_1.place(
        x=479.0,
        y=376.0,
        width=481.0,
        height=111.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("mais_barato/button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=amazonMenor,
        relief="flat"
    )
    button_2.place(
        x=479.0,
        y=551.0,
        width=481.0,
        height=111.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("mais_barato/button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=chipartMenor,
        relief="flat"
    )
    button_3.place(
        x=479.0,
        y=726.0,
        width=481.0,
        height=111.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("mais_barato/image_2.png"))
    image_2 = canvas.create_image(
        719.0,
        125.0,
        image=image_image_2
    )

    canvas.create_text(
        200.0,
        55.0,
        anchor="nw",
        text="Flutuação na:",
        fill="#FFFFFF",
        font=("Roboto Bold", 96 * -1)
    )

    window.resizable(False, False)
    window.mainloop()


def mainMenu():

    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=1024,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        1024.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("select_menu/image_1.png"))
    image_1 = canvas.create_image(
        719.0,
        511.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("select_menu/button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=comparacao,
        relief="flat"
    )
    button_1.place(
        x=479.0,
        y=376.0,
        width=481.0,
        height=111.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("select_menu/button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=menorPreco,
        relief="flat"
    )
    button_2.place(
        x=479.0,
        y=551.0,
        width=481.0,
        height=111.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("select_menu/image_2.png"))
    image_2 = canvas.create_image(
        719.0,
        125.0,
        image=image_image_2
    )

    canvas.create_text(
        200.0,
        55.0,
        anchor="nw",
        text="ESCOLHA UMA OPÇÃO:",
        fill="#FFFFFF",
        font=("Roboto Bold", 96 * -1)
    )

    window.resizable(False, False)
    window.mainloop()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    1024.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    719.0,
    511.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    935.0,
    281.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    366.0,
    511.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= mainMenu,
    relief="flat"
)

button_1.place(
    x=825.0,
    y=672.0,
    width=481.0,
    height=111.0
)

canvas.create_text(
    67.0,
    219.0,
    anchor="nw",
    text="PAPAPRICE",
    fill="#FFFFFF",
    font=("Roboto Bold", 96 * -1),
    width=559.0
)

canvas.create_text(
    67.0,
    343.0,
    anchor="nw",
    text="A sua ferramenta para acompanhar os preços das placas de video no mercado brasileiro.",
    fill="#FFFFFF",
    font=("Roboto Bold", 48 * -1),
    width=561.0
)

canvas.create_text(
    67.0,
    682.0,
    anchor="nw",
    text="Atualmente apenas usamos os dados da Amazon, Chipart e Pichau.",
    fill="#FFFFFF",
    font=("Roboto Bold", 24 * -1),
    width=561.0
)

canvas.create_rectangle(
    75.0,
    337.0,
    261.0,
    350.0,
    fill="#FFFFFF",
    outline="")

window.resizable(False, False)

window.mainloop()

