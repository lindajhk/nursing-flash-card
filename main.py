from tkinter import *
import pandas
import requests
import random

BASE_URL = "https://www.dictionaryapi.com/api/v3/references/medical/json/"
BACKGROUND_COLOR = "#B1DDC6"
current_card = []
to_learn = []
orig_title_coords = None

try:
    csv_data = pandas.read_csv("data/words_list.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/word_list.csv")
    to_learn = original_data
else:
    to_learn = csv_data


def next_card():
    global current_card, flip_timer, orig_title_coords
    window.after_cancel(flip_timer)
    # Reset title position to original coordinates
    canvas.coords(card_title, orig_title_coords)
    try:
        current_card = random.choice(to_learn.iloc[:, 0].tolist())
    except IndexError:
        canvas.itemconfig(card_title, text="Congrats!\nYou've learned all the cards!")
        canvas.itemconfig(front_card_word, text="", fill="white")
        unknown_button.grid_forget()
        known_button.grid_forget()
        return

    current_card = random.choice(to_learn.iloc[:, 0].tolist())
    if 30 < len(current_card) < 20:
        font_size = 40
    elif len(current_card) > 29:
        font_size = 30
    else:
        font_size = 60
    canvas.itemconfig(card_title, text="Word", fill="black")
    canvas.itemconfig(front_card_word, text=current_card, fill="black", font=("Ariel", font_size, "bold"))
    canvas.itemconfig(def_card_word, text="", fill="white")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global orig_title_coords
    request_url = f"{BASE_URL}{current_card}?key={API_KEY}"
    response = requests.get(request_url)
    response.raise_for_status()
    data = response.json()
    definition = data[0]['shortdef'][0]
    print(definition)

    # Store original title coordinates
    orig_title_coords = canvas.coords(card_title)

    # Move title up if definition is too long
    canvas.itemconfig(card_title, text="Definition", fill="white")
    title_coords = canvas.coords(card_title)
    if len(definition) > 199:
        canvas.coords(card_title, title_coords[0], title_coords[1] - 30)

    if 50 < len(definition) < 120:
        font_size = 30
        print(font_size)
    elif 200 > len(definition) > 119:
        font_size = 25
        print(font_size)
    elif 380 > len(definition) > 199:
        font_size = 20
        print(font_size)
    elif len(definition) > 379:
        font_size = 15
        print(font_size)
    else:
        font_size = 40
        print(font_size)
    canvas.itemconfig(front_card_word, text="", fill="white")
    canvas.itemconfig(def_card_word, text=definition, fill="white", font=("Ariel", font_size, "bold"))
    canvas.itemconfig(card_background, image=card_back_img)




def is_known():
    global to_learn
    to_learn = to_learn[to_learn.iloc[:, 0] != current_card]
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def restart_program():
    # Reload the original words from the CSV and start over
    global to_learn
    to_learn = original_data
    next_card()
    known_button.grid(row=1, column=2)
    unknown_button.grid(row=1, column=0)


def close_program():
    window.destroy()


window = Tk()
window.title("Premed Flash Focus")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(300, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
completed_card_word = canvas.create_text(400, 263, text="", width=700)
front_card_word = canvas.create_text(400, 263, text="", width=700)
def_card_word = canvas.create_text(400, 263, text="", width=700)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=2)

restart_image = PhotoImage(file="images/restart.png")
restart_button = Button(image=restart_image, highlightthickness=0, command=restart_program)
restart_button.grid(row=1, column=1)

next_card()

window.mainloop()
