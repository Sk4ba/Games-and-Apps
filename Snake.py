#Snake game
from tkinter import*
import random


#constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 70 #How fast the screen will refresh (lower the faster)
SPACE_SIZE = 50 #How big the tiles are
BODY_PARTS = 1 #How many body parts the snake will start to
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        #Starting position (top left)
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)



class Food:
    def __init__(self):
        #RANDOMIZING WHERE THE FOOD WILL GO
        #Just learned something new. "//" is a floor division which will give u a flat number
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) -1 ) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1 ) * SPACE_SIZE

        #PLACING THE FOOD
        self.coordinates = [x,y]
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")



def next_turn(snake, food):
    #Saving last moves (0 is the head of the snake)
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square)


    #Updates if snake eats food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text = "Score: {}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        #deleting last body part of the snake (trail)
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    #Game over when snake collides with itself or border
    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    #This changes the direction of the snake
    #This also prevents the snake from moving on the back of its head
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction



def check_collisions(snake):

    x, y = snake.coordinates[0]

    #Checking if snake collides with border
    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_HEIGHT:
        print("Game over")
        return True

    #Checking if snake collides with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True


    return False #Returns no collisions



def game_over():
    #Function of game over
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font = ('consolas', 70), text = "GAME OVER", fill = "red", tag = "gameover")



window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down' #starting direction



#The score label
label =Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()



#The game canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()



#Centering the window when it starts
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")



#KEY BINDS
#This also updates the change direction to save the last move
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))



snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()