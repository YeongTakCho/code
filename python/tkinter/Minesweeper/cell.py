from tkinter import Button
import random
from typing import overload
import settings

class Cell:
    all=[]
    
    def __init__(self, x, y, is_mine= False, is_open = False):
        self.is_mine = is_mine
        self.is_open = is_open
        self.cell_btn_object= None
        self.x= x
        self.y= y
        
        #Append the object to the Cell.all list
        Cell.all.append(self)
        
    def create_btn_object(self,location):
        btn = Button(
            location,
            width= 12,
            height= 4,
            bg= 'white',
            text=f"{self.x}, {self.y}"
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object= btn
    
    def left_click_actions(self, event):
        print("click left")
        if self.is_open:
            pass
        if self.is_mine:
            # finish the game
            self.cell_btn_object["location"]["bg"] = 'red'
        
        self.cell_btn_object['text']=f'{self.get_near_mine(self,self.x,self.y)}'        
            
    def get_near_mine(self,x,y):
        from main import cells
        near_mine=0        
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                ny= y+i
                nx= x+i
                if ny>= 0 and ny< settings.GRID_SIZE and nx>=0 and nx< settings.GRID_SIZE:
                    state = ny * settings.GRID_SIZE + nx
                    print(f'{state} is mine')
                    if cells[state].is_mine:
                        near_mine+=1            
        return near_mine
                
        
               
    def right_click_actions(self, event):
        print("right click - flag")
        if self.is_open:
            pass
        if self.cell_btn_object["bg"] == 'purple':
            self.cell_btn_object["bg"] = 'white'
        else:
            self.cell_btn_object["bg"] = 'purple'
         
    @staticmethod
    def randomize_mines():
        mine_objects= random.sample(Cell.all, settings.MINE_COUNT)
        for mine_object in mine_objects:
            mine_object.is_mine = True
            mine_object.cell_btn_object["text"]= text=f"{mine_object.x}, {mine_object.y}\n MINE!!"

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"       
            
            