from tkinter import*
import pickle
from PIL import ImageTk,Image  
import socket
import cv2
import numpy as np
import time
import datetime
import sys
import threading
import os


#Global variables
ipr='192.168.0.106'  #enter IP of this laptop
ipc='192.168.0.106' #enter IP of other laptop
filter_flag=0 #filter flag
stop_flag=0 #stop command flag


#----------------------------N/W----------------------------#


def receive():
  
  global stop_flag
  global flag
  
  HOST = ipr
  PORT = 5050
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('Socket created')
  s.bind((HOST, PORT))
  print('Socket bind complete')
  s.listen(10)
  print('Socket now listening')
  conn, addr = s.accept()

  while True:
      data = conn.recv(100000) #receive max 100k bytes
      #check if data received is credible
      if(sys.getsizeof(data)>5000 and sys.getsizeof(data)<20000):
          enc_img = np.fromstring(data, np.uint8)
          frame = cv2.imdecode(enc_img, 1)
          try:
              cv2.imshow('frame', frame)
              cv2.waitKey(5) & 0XFF
          except:
              print(datetime.datetime.now()," Check connection")
      else:
          print(datetime.datetime.now()," Error: data too small/large  bytes:",sys.getsizeof(data))
      data=''
      if stop_flag:
        s.close()
        cv2.destroyAllWindows()
        break



def send():
  
  global stop_flag

  print("Starting video stream...")
  cap = cv2.VideoCapture(0)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((ipc, 5050))

  while(True):
      #capture frame-by-frame
      ret, frame = cap.read()
      #operations on the frame done here
      if(filter_flag==1):
      	frame=cv2.bitwise_not(frame)
      #encode image to send on network
      encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
      data = cv2.imencode('.jpg', frame, encode_param)[1].tostring()

      #uncomment to check size of processed image
      #print(sys.getsizeof(data))
    
      sock.sendall(data)
      
      if(stop_flag):
        sock.close()
        break

  # When everything done, release the capture
  print("Stopping video stream.")
  cap.release()
  cv2.destroyAllWindows()


#----------------------------GUI----------------------------#


def register_user():
 
  with open(r'''C:\Users\hegde\Desktop\CN\users.txt''', "rb") as myFile:
    users = pickle.load(myFile)
  username_info = usernamer.get()
  password_info = passwordr.get()
  users[username_info]=password_info
  with open(r'''C:\Users\hegde\Desktop\CN\users.txt''', "wb") as myFile:
    pickle.dump(users, myFile) 
  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()


 
def log_user():
 
  username_info1 = usernamel.get()
  password_info1 = passwordl.get()
  with open(r'''C:\Users\hegde\Desktop\CN\users.txt''', "rb") as myFile:
    users = pickle.load(myFile)
  print(username_info1,password_info1)
  try:
    (users[username_info1])
  except:
    screen2.destroy()
  if users[username_info1]!=password_info1:
    Label(screen2, text = "Wrong password", fg = "green" ,font = ("calibri", 11)).pack()    
  else:
    screen.destroy()
    video_screen()

    
 
def register():
  
  global screen1
  global usernamer
  global passwordr
  
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  usernamer = StringVar()
  passwordr = StringVar()
 
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = usernamer)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = passwordr)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()


 
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  global usernamel
  global passwordl
  usernamel = StringVar()
  passwordl = StringVar()
 
  Label(screen2, text = "Please enter details below").pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Username * ").pack()
  username_entry = Entry(screen2, textvariable = usernamel)
  username_entry.pack()
  Label(screen2, text = "Password * ").pack()
  password_entry =  Entry(screen2, textvariable = passwordl)
  password_entry.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = log_user).pack()
  print("Login session started")
  
  
 
def main_screen():
  
  global username
  global password
  global screen
  global d
  
  d={} 
  screen = Tk()
  screen.configure(background='grey38')
  screen.geometry("1600x900")
  screen.title("WHO ARE YOU")
  Label(text = "Video Streaming Service", bg = "grey21", fg='white',width = "300", height = "2", font = ("Calibri", 13)).pack()
  canvas = Canvas(screen, width = 1000, height = 400, bg='grey33',  highlightthickness=0,relief='ridge')  
  canvas.pack()  
  img = ImageTk.PhotoImage(Image.open('C:\\Users\\hegde\\Desktop\\CN\\2peeps.jpg'))  
  canvas.create_image(0,-100, image=img, anchor='nw')  
  Button(text = "Login", height = "2", width = "30", command = login).place(x=500,y=500)
  Button(text = "Register",height = "2", width = "30", command = register).place(x=500,y=600)
  screen.mainloop()


 
def video_screen():
  
    global flag
    
    s=Tk()
    s.configure(background='grey38')
    s.geometry("1600x900")
    s.title("Choose")
    Label(text = "Video Streaming Service", bg = "grey21", fg='white',width = "300", height = "2", font = ("Calibri", 13)).pack()
    canvas = Canvas(s, width = 1000, height = 400, bg='grey33',  highlightthickness=0,relief='ridge') 
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\hegde\\Desktop\\CN\\2peeps.jpg'))  
    canvas.create_image(0,-100, image=img, anchor='nw')  
    Button(text = "Send", height = "2", width = "30", command = sen).place(x=150,y=500)
    Button(text = "Receive",height = "2", width = "30", command = rec).place(x=150,y=580)
    Button(text = "Conference", height = "2", width = "30", command = both).place(x=420,y=500)
    Button(text = "Activate filter", height = "2", width = "30", command = apply_filter).place(x=680,y=500)
    Button(text = "Stop", height = "2", width = "30", command = stop).place(x=920,y=580)
    s.mainloop()
    

#----------------------------<>----------------------------#


def both():
  
  global stop_flag
  global t2
  global t1
  
  stop_flag=0
  t1 = threading.Thread(target=send, name='t1') 
  t2 = threading.Thread(target=receive, name='t2')   

  # starting threads 
  t2.start()
  time.sleep(3)  
  t1.start() 


def apply_filter():
  
  global filter_flag
  print("Toggle filter")
  filter_flag=not(filter_flag)
  

def sen():
  
  global stop_flag
  global f
  stop_flag=0
  t3 = threading.Thread(target=send, name='t3') 
  t3.start()
  

def rec():
  
  global stop_flag
  global f1
  stop_flag=0
  t4 = threading.Thread(target=receive, name='t4') 
  t4.start()

   
def stop():
  global stop_flag
  print("STOP")
  stop_flag=1

 
#----------------------------<>----------------------------#

 
main_screen()
  
