import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_cor(X, Y):
    print(X, Y)


turtle.onscreenclick(get_mouse_click_cor)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_guesses = []
remaining_states = []
new_x_list = []
new_y_list = []

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.color("blue")

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states guessed",
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        for st in states_list:
            if st not in correct_guesses:
                remaining_states.append(st)
        print(remaining_states)
        print(new_x_list)
        print(new_y_list)

        df = pandas.DataFrame(remaining_states)
        df.to_csv("remaining_states.csv")

        break

    if answer_state in states_list:
        state = data[data.state == answer_state]
        x_location = int(state.x)
        y_location = int(state.y)

        text.goto(x_location, y_location)
        text.write(f"{answer_state}", align="center", font=('Courier', 8, 'normal'))

        correct_guesses.append(answer_state)

turtle.mainloop()
