import turtle
import pandas

from tkinter import * 
from tkinter import messagebox


screen = turtle.Screen()
screen.title("Turkey Game")
image = "unnamed_turkey_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("81_states_coordinate.csv")
all_states = data.state.to_list()
guessed_states = []
counter = 0

# Define a function to close the window
def close():
    messagebox.showinfo("Alert!", "There is no city try again!") # The alert.

Button(text= "Close the Window", font=("Calibri",14,"bold"), command=close).pack(pady=20)



while counter < 81:
    

    answer_state = screen.textinput(title=f"{counter}/81 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state not in all_states:
        messagebox.showinfo("Alert!", "There is no city try again!") # The alert.

    elif  answer_state in guessed_states:
        messagebox.showinfo("showinfo", "Same city try again!") # The alert.

    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        counter += 1
        t.write(answer_state)
    
