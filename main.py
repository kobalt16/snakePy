from tkinter import *
import time
import random

game_width = 500
game_height = 500
snake_item = 10
snake_color1 = 'yellow'
snake_color2 = 'red'
snake_x = 24
snake_y = 24
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 3

virt_game_x = game_width / snake_item
virt_game_y = game_height / snake_item

tk = Tk()
tk.title("S   N   A   K   E")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

gift_list = []
gift_size = 5
gift_color1 = 'green'
gift_color2 = 'red'

for i in range(gift_size):
    x = random.randrange(virt_game_x)
    y = random.randrange(virt_game_y)
    id1 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                  y * snake_item + snake_item, fill=gift_color1)
    id2 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                  y * snake_item + snake_item - 2, fill=gift_color2)

    gift_list.append([x,y,id1,id2])

# print(gift_list)

def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x*snake_item, y*snake_item, x*snake_item+snake_item, y*snake_item+snake_item, fill=snake_color2)
    id2 = canvas.create_rectangle(x*snake_item+2, y*snake_item+2, x*snake_item+snake_item-2, y*snake_item+snake_item-2, fill=snake_color1)
    snake_list.append([x,y,id1,id2])
    # print(snake_list)

snake_paint_item(canvas, snake_x, snake_y)

def delete_snake_item():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        # print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])

def check_found():
    global snake_size
    for i in range(len(gift_list)):
        if gift_list [i][0] == snake_x and gift_list[i][1] == snake_y:
            # print("+++++++++++++YESSS!!!+++++++++++++++++++++++")
            snake_size += 1
            canvas.delete(gift_list[i][2])
            canvas.delete(gift_list[i][3])
    # print('x:',snake_x, 'y:',snake_y)

def snake_move(event):
    global snake_x
    global snake_y
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        delete_snake_item()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        delete_snake_item()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        delete_snake_item()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        delete_snake_item()

    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    check_found()

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)


tk.mainloop()