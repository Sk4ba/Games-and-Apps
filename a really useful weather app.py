import time
from tkinter import*
import random

#THIS IS MY SECOND TIME USING CANVAS IN PYTHON




#I just wanna use define even tho it ain't needed lol
def timer():
    time.sleep(1)


#this one we need
def submit():

    user_input = text_box.get("1.0", END).strip()

    #to add some effect
    timer()

    #deletes the user input in canvas
    text_box.delete("1.0", END)

    #after user input, it does not allow the user to input again.
    text_box.forget()
    button.forget()
    loading_screen.pack(pady=20) #shows loading screen
    window.update()


    #this is the message step by step
    steps = [
        "Loading",
        "Checking Weather",
        "Accessing Satellites",
        f"Checking the Clouds on {user_input}"
    ]


    #printing the loading screen
    for message in steps:
        loading_screen.itemconfig(loading_text, text=message)
        window.update()
        timer()
        for x in range(1,6): #the dots
            dots = ". " * x
            loading_screen.itemconfig(loading_text, text=f"{message}\n{dots:^}")
            window.update()
            timer()

    loading_screen.itemconfig(loading_text, text="Idk bro, go outside")
    window.update()



window = Tk()
window.title("Weather App")
window.resizable(False, False)


#background color
window.configure(bg="light yellow")


#This is the label
label = Label(window, text="Weather App", font=('consolas', 40), bg="light yellow")
label.pack()


#This is the text asking for the location
prompt_label = Label(window, text="Enter location", font=('consolas', 24), bg="light yellow")
prompt_label.pack(pady=(20, 10))


#This is the actual window
text_box = Text(window, font=('consolas', 20),
            height=10, width=30,
            padx=20, pady=20)
text_box.pack()


#submit button
button = Button(window, text="submit", command=submit)
button.pack()

loading_screen = Canvas(window, width=500, height=400, bg="white", highlightthickness=0)
loading_text = loading_screen.create_text(250, 175,
                                  text="",
                                  font=("consolas", 30, "bold"),
                                  fill="black",
                                  justify="center",
                                  width=470)

#end
window.mainloop()