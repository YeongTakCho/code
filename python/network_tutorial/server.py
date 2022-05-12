from multiprocessing.dummy import current_process
import socket 
from _thread import * 

server= "192.168.56.1" # !!!!!!!!!!!!!!!!! must be deleted when upload git !!!!!!!!!!!!!!!!!!!!!!!!!!
port = 5555

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)
    
s.listen(2)
print("waitng for connection, Server Started")

def read_pos(str): # "45,67" -> (45,67)
    str= str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup): # (45,67) -> "45,67"
    return str(tup[0]) + "," + str(tup[1])

pos= [(0,0), (100,100)]
def threaded_client(conn :socket, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply= ''
    while True:
        try:
            # print('start receiving') # test how socket works
            # data= conn.recv(2048) # recv:  waiting conn send the data but if conn end, it finish and return none
            # print('receive compeleted') # test how socket works
            
            pos_data= read_pos(conn.recv(2048).decode())
            
            
            if not pos_data:
                print("disconnected")
                break

            else:
                pos[player] = pos_data
                
                if player ==0:
                    reply = pos[1]
                else:
                    reply = pos[0]
                    
                print("sending: ", reply)
                
                

            conn.sendall(str.encode(make_pos(reply)))
            
        except:
            break
        
    print('Lost connection')
    conn.close()
    


current_player =0
while True:
    conn,addr = s.accept() # waiting the accept
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn, current_player))
    current_player +=1