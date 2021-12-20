import sys
import numpy as np
input = sys.stdin.readline

class FindWay:
    def getdata(self):
        self.n, self.m = map(int,input().split())
        self.MAP=list()
        for _ in range(self.n):
            self.MAP.append(list(input().rstrip()))
    
    def findIFT(self):
        for y in range(len(self.MAP)):
            for x in range(len(self.MAP[0])):
                if self.MAP[y][x] == 'I':
                    self.MAP[y][x] = '.'
                    self.I= [y,x]
                    break
        for y in range(len(self.MAP)):
            for x in range(len(self.MAP[0])):
                if self.MAP[y][x] == 'F':
                    self.MAP[y][x] = '.'
                    self.F = [y,x]
                    break
        for y in range(len(self.MAP)):
            for x in range(len(self.MAP[0])):
                if self.MAP[y][x] == 'T':
                    self.T = (y,x)
                    break
        self.state = [self.I, self.F]
    
    def printMAP(self):
        for line in self.MAP:
            print(line)

    def printIFT(self):
        print('I:', self.I)
        print('F:', self.F)
        print('T:', self.T)
    
    def isDifferent(state1, state2):
        return not np.array_equal(np.array(state1), np.array(state2))

    def move(self):
        #return [movingNum, **before it visited reversed]
        stateNow = self.state
        start=0

        def up(stateNow,movingNum): #sort y down
            #이동
            if movingNum == 10:
                return [11]

            while True:
                pass

            stateNew = list()
            if self.isDifferent(stateNow,stateNew):
                return min(down(stateNew,movingNum+1),left(stateNew,movingNum+1),right(stateNew,movingNum+1), key = lambda x: x[0]).append('UP')

        def down(stateNow,movingNum): #sort y up
            #이동
            stateNew = list()
            if self.isDifferent(stateNow,stateNew):
                return min(up(stateNew,movingNum+1),left(stateNew,movingNum+1),right(stateNew,movingNum+1), key= lambda x: x[0]).append('DOWN')


        def left(stateNow,movingNum): #sort x down
            #이동
            stateNew = list()
            if self.isDifferent(stateNow,stateNew):
                return min(up(stateNew,movingNum+1),down(stateNew,movingNum+1),right(stateNew,movingNum+1), key= lambda x: x[0]).append('LEFT')


        def right(stateNow,movingNum): #sort x up
            #이동
            stateNew = list()
            if self.isDifferent(stateNow,stateNew):
                return min(up(stateNew,movingNum+1),down(stateNew,movingNum+1),left(stateNew,movingNum+1), key= lambda x: x[0]).append('RIGHT')

        up(stateNow,start)
        down(stateNow,start)
        left(stateNow,start)
        right(stateNow,start)

findway = FindWay()
findway.getdata()
findway.findIFT()
findway.printMAP()
findway.printIFT()
