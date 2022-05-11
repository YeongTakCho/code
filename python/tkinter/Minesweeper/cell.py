from tkinter import Button, PhotoImage
import random
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
            bg= 'gray',
            text=f""
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object= btn
    
    def left_click_actions(self, event):
        print("click left")
        if self.is_open:
            return
        
        self.is_open =True
        
        if self.is_mine:
            self.cell_btn_object["bg"]= 'red'

        else:
            near_mine= self.near_mine()
            self.cell_btn_object["text"] = f'{near_mine}'
            self.cell_btn_object["bg"]= 'white'
            
            if near_mine ==0:
                for cell in self.surrounded_cells():
                    cell.left_click_actions(None)
    
    
            
    def right_click_actions(self, event):

        print("right click - flag")
        if self.is_open:
            return
            
        if self.cell_btn_object["bg"] == 'purple':
            self.cell_btn_object["bg"] = 'gray'
            
        else: self.cell_btn_object["bg"] = 'purple'


    def near_mine(self):
        n_mines =0
        for cell in  self.surrounded_cells():
            if cell.is_mine:
                n_mines+=1
        return n_mines
    
    
    def surrounded_cells(self):
        cells= []
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if x==0 and y ==0:
                    continue
                nx = self.x +x 
                ny = self.y +y
                cells.append(self.get_cell_by_axis(nx,ny))
                
        return [cell for cell in cells if cell is not None]
    
            
    def get_cell_by_axis(self, x ,y):
        for cell_object in self.all:
            if cell_object.x == x and cell_object.y == y:
                return cell_object

   
         
    @staticmethod
    def randomize_mines():
        mine_objects= random.sample(Cell.all, settings.MINE_COUNT)
        for mine_object in mine_objects:
            mine_object.is_mine = True
            mine_object.cell_btn_object["text"]= text=f"{mine_object.x}, {mine_object.y}\n MINE!!"

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"       
            
            