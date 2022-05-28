
from tkinter import*
#Creating two global variables
current_x,current_y = 0,0
color = 'black'
#Creating our function
def locate_xy(event):
    global current_x,current_y
    current_x,current_y=event.x,event.y
#When u click on the canvas u get the x,y cords 
#print(current_x,current_y)


def addLine(event):
    global current_x,current_y
##The begining of the line to wherever the user drags the line 
    canvas.create_line((current_x,current_y,event.x,event.y),fill= color)
#Setting current(x,y) to the last location
    current_x,current_y = event.x,event.y


def show_color(new_color):
  global color
  color = new_color

def new_canvas():
    canvas.delete("all")
    display_pallete()

window = Tk()
window.title('PAINTZX')
window.state('zoomed')#It means the window should open to its full size.
#window.config(bg='red')# Config is used for changing bg colors
window.rowconfigure(0,weight=1)#TO make sure when we expand the size of the window the row expands too.
window.columnconfigure(0,weight=1)

menubar = Menu(window)
window.config(menu = menubar)
submenu = Menu(menubar,tearoff = 0)

#Adding submenu to the menubar using the cascade method
#Cascade is the list of options on the menubar

menubar.add_cascade(label='FILE',menu=submenu)
submenu.add_command(label='New Canvas',command=new_canvas)

## Creating a canvas and placing it ontop our window
canvas = Canvas(window, bg ='white')
#"nsew" north,south,east,west making the canvas expand in all directions and expanding to the size of the window.
canvas.grid(row=0,column=0,sticky='nsew')

##Creating a line in our canvas
# x and y coordinates they represent were i want the lines to end.
# also u need the x and y coordinates to begin and end a line.

#CREATING a function to give us x&y coordinates of where we are in the screen
#Bind would be acivated when the user clicks on the screen.
#
canvas.bind('<Button-1>',locate_xy)
#The second bind is for when a user drags a mouse on the canvas
canvas.bind('<B1-Motion>',addLine)
#Creating our pallete.
# we need to attch a bind to them by storing them with unique id's

# In order for our pallete not to be destroyed by the("all") keyword
# we need to create a function.

def display_pallete():
    id = canvas.create_rectangle((10,10,30,30),fill='black')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('black'))

    id= canvas.create_rectangle((10,40,30,60),fill='gray')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('gray'))

    id = canvas.create_rectangle((10,70,30,90),fill='brown4')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('brown4'))

    id = canvas.create_rectangle((10,100,30,120),fill='red')# every canvas object has a unique integer id
    # also used to return the identity of the object.
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('red'))

    id = canvas.create_rectangle((10,130,30,150),fill='orange')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('orange'))#shorthand for defining functions to show colors

    id = canvas.create_rectangle((10,160,30,180),fill='yellow')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('yellow'))

    id = canvas.create_rectangle((10,190,30,210),fill= 'green')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('green'))

    id = canvas.create_rectangle((10,220,30,240),fill='blue')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('blue'))

    id = canvas.create_rectangle((10,250,30,270),fill='purple')
    canvas.tag_bind(id,'<Button-1>',lambda x:show_color('purple'))

display_pallete()

window.mainloop()