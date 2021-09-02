from pathlib import Path

from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")

def mainMenu():

    window.configure(bg = "#FFFFFF")

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
        file=relative_to_assets("select_menu/image_1.png"))

    image_1 = canvas.create_image(
        719.0,
        511.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("select_menu/image_2.png"))

    image_2 = canvas.create_image(
        366.0,
        511.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("select_menu/button_1.png"))

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("select_menu/button_1 clicked"),
        relief="flat"
    )

    button_1.place(
        x=123.0,
        y=417.0,
        width=481.0,
        height=111.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("select_menu/button_2.png"))

    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("select_menu/button_2 clicked"),
        relief="flat"
    )

    button_2.place(
        x=835.0,
        y=417.0,
        width=481.0,
        height=111.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("select_menu/button_3.png"))

    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("select_menu/button_3 clicked"),
        relief="flat"
    )

    button_3.place(
        x=835.0,
        y=698.0,
        width=481.0,
        height=111.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("select_menu/button_4.png"))

    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("select_menu/button_4 clicked"),
        relief="flat"
    )

    button_4.place(
        x=123.0,
        y=698.0,
        width=481.0,
        height=111.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("select_menu/image_3.png"))

    image_3 = canvas.create_image(
        719.0,
        125.0,
        image=image_image_3
    )

    canvas.create_text(
        360.0,
        100.0,
        anchor="nw",
        text="ESCOLHA UMA OPÇÃO:",
        fill="#FFFFFF",
        font=("Roboto Bold", 68 * -1),
        width=1039.0
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
    text="GPU Pricer",
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
    text="Atualmente apenas usamos os dados da Kabum, Terabyteshop e Pichau.",
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

