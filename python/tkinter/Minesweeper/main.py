from tkinter import *
import settings
import utils
from cell import Cell

root= Tk()
root.configure(bg= "black")
root.title('minesweeper game')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable('False','False')

top_frame= Frame(
    root,
    bg= 'black',
    width= settings.WIDTH,
    height= utils.height_pct(20)
)
top_frame.place(x=0, y=0)

left_frame= Frame(
    root,
    bg='black',  
    width= utils.width_pct(20),
    height= settings.HEIGHT
)
left_frame.place(x=0, y=utils.height_pct(20))

center_frame= Frame(
    root,
    bg= 'black',
    width= utils.width_pct(80),
    height= utils.height_pct(80)
)
center_frame.place(x= utils.width_pct(20), y= utils.height_pct(20))

cells=[]
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c= Cell(x, y)
        cells.append(c)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column= y, row=x
        )

Cell.randomize_mines()
for c in Cell.all:
    print(c, end='')



# Run the window
root.mainloop()
