from Tkinter import *
import threading 
import socket
import sys
import time
import platform  
import cv2
import os

#------------------- END LAYOUT, START FUNCTIONS ----------------------------------


def on_closing():
    root.destroy()
    os._exit(1)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            addLog(data.decode(encoding="utf-8"))

        except Exception:
            print ('\nExit . . .\n')
            break

def camStream():

    while True:
        _, frame = cap.read()
        cv2.imshow('cap', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

def addLog(txt):
    terminalList.insert(0, txt)

def startCam():
    global cap
    sock.sendto('streamon', tello_address)
    cap = cv2.VideoCapture('udp://192.168.10.1:11111')

    camThread = threading.Thread(target=camStream)
    camThread.start()


def startCon():
    addLog('Conectando')
    sock.sendto('command', tello_address)
    label_status_con.config(text='Conectado', fg='green')
    label_status_aircraft.config(text='Pousado')



def takeoff():
    addLog('Decolando')
    sock.sendto('takeoff', tello_address)
    label_status_aircraft.config(text='Voando', fg='green')


def land():
    addLog('Pousando')
    sock.sendto('land', tello_address)
    label_status_aircraft.config(text='Pousado')


def emergency():
    addLog('Parada de emergencia')
    sock.sendto('emergency', tello_address)
    label_status_aircraft.config(text='Pousado')


def move_up():
    addLog('Subindo')
    sock.sendto('up 20', tello_address)

def move_down():
    addLog('Descendo')
    sock.sendto('down 20', tello_address)

def move_cw():
    addLog('Girando para direita')
    sock.sendto('cw 20', tello_address)

def move_ccw():
    addLog('Girando para esquerda')
    sock.sendto('ccw 20', tello_address)

def move_forward():
    addLog('Indo para frente')
    sock.sendto('forward 40', tello_address)
def move_back():
    addLog('Indo para tras')
    sock.sendto('back 40', tello_address)

def move_left():
    addLog('Indo para esquerda')
    sock.sendto('left 40', tello_address)

def move_right():
    addLog('Indo para direita')
    sock.sendto('right 40', tello_address)

def flip_forward():
    addLog('Flip para frente')
    sock.sendto('flip f', tello_address)

def flip_back():
    addLog('Flip para tras')
    sock.sendto('flip b', tello_address)

def flip_left():
    addLog('Flip para esquerda')
    sock.sendto('flip l', tello_address)

def flip_right():
    addLog('Flip para direita')
    sock.sendto('flip r', tello_address)

def battery():
    addLog('Nivel da bateria')
    sock.sendto('battery?', tello_address)

#------------------- PRE CONFIG ----------------------


host = ''
port = 9000
locaddr = (host,port) 

cap = None

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

recvThread = threading.Thread(target=recv)
recvThread.start()

#---------- MAIN FRAME ----------
root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry('600x600+200+200')
root.wm_title("DJI Tello")

#---------- COMMANDS FRAME ----------
commandsFrame = LabelFrame(root, text="Comandos")
commandsFrame.place(rely=0, relx=0, relwidth=1, relheight=0.7)

label_ip = Label(commandsFrame, text="IP Tello", font=("Helvetica", 12))
label_ip.place(rely=0, relwidth=0.2, relheight=0.1, relx=0.05)

entry_ip = Entry(commandsFrame)
entry_ip.place(relx=0.05, relwidth=0.2, relheight=0.1, rely=0.1)
entry_ip.insert(0, '192.168.10.1')

label_port = Label(commandsFrame, text="Command Port", font=("Helvetica", 12))
label_port.place(rely=0, relwidth=0.2, relheight=0.1, relx=0.25)

entry_port = Entry(commandsFrame)
entry_port.place(relx=0.25, relwidth=0.2, relheight=0.1, rely=0.1)
entry_port.insert(0, '8889')

btn_connect = Button(commandsFrame, text="Conectar", command=startCon)
btn_connect.place(relx=0.45, relwidth=0.2, relheight=0.1, rely=0.1)

btn_connect_cam = Button(commandsFrame, text="Camera", command=startCam)
btn_connect_cam.place(relx=0.45, relwidth=0.2, relheight=0.1, rely=0.2)

btn_connect_cam = Button(commandsFrame, text="Bateria", command=battery)
btn_connect_cam.place(relx=0.25, relwidth=0.2, relheight=0.1, rely=0.2)

label_status_con = Label(commandsFrame, text="Desconectado", fg="red", font=("Helvetica", 12))
label_status_con.place(rely=0.1, relwidth=0.2, relheight=0.1, relx=0.7)

btn_takeoff = Button(commandsFrame, text="Decolar", command=takeoff)
btn_takeoff.place(relx=0.05, relwidth=0.2, relheight=0.1, rely=0.3)

btn_land = Button(commandsFrame, text="Pousar", command=land)
btn_land.place(relx=0.25, relwidth=0.2, relheight=0.1, rely=0.3)

btn_emergency = Button(commandsFrame, text="Emergencia", command=emergency)
btn_emergency.place(relx=0.45, relwidth=0.2, relheight=0.1, rely=0.3)

label_status_aircraft = Label(commandsFrame, text="Desconectado", fg="red", font=("Helvetica", 12))
label_status_aircraft.place(rely=0.3, relwidth=0.2, relheight=0.1, relx=0.7)

#------------------ ROTATION -----------------

btn_move_up = Button(commandsFrame, text="Subir", command=move_up)
btn_move_up.place(relx=0.15, relwidth=0.2, relheight=0.1, rely=0.5)

btn_move_cw = Button(commandsFrame, text="Girar", command=move_ccw)
btn_move_cw.place(relx=0.05, relwidth=0.2, relheight=0.1, rely=0.6)

btn_move_down = Button(commandsFrame, text="Descer", command=move_down)
btn_move_down.place(relx=0.15, relwidth=0.2, relheight=0.1, rely=0.7)

btn_move_ccw = Button(commandsFrame, text="Girar", command=move_cw)
btn_move_ccw.place(relx=0.25, relwidth=0.2, relheight=0.1, rely=0.6)

#----------------------- MOVEMENT -------------------

btn_move_up = Button(commandsFrame, text="Frente", command=move_forward)
btn_move_up.place(relx=0.65, relwidth=0.2, relheight=0.1, rely=0.5)

btn_move_cc = Button(commandsFrame, text="Esquerda", command=move_left)
btn_move_cc.place(relx=0.55, relwidth=0.2, relheight=0.1, rely=0.6)

btn_move_down = Button(commandsFrame, text="Tras", command=move_back)
btn_move_down.place(relx=0.65, relwidth=0.2, relheight=0.1, rely=0.7)

btn_move_cc = Button(commandsFrame, text="Direita", command=move_right)
btn_move_cc.place(relx=0.75, relwidth=0.2, relheight=0.1, rely=0.6)

# ------------------------- FLIPS
label_flips = Label(commandsFrame, text="Flips", font=("Helvetica", 12))
label_flips.place(rely=0.8, relwidth=0.2, relheight=0.1, relx=0.05)

btn_flip_front = Button(commandsFrame, text="Frente", command=flip_forward)
btn_flip_front.place(relx=0.05, relwidth=0.2, relheight=0.1, rely=0.9)

btn_flip_back = Button(commandsFrame, text="Tras", command=flip_left)
btn_flip_back.place(relx=0.25, relwidth=0.2, relheight=0.1, rely=0.9)

btn_flip_left = Button(commandsFrame, text="Esquerda", command=flip_back)
btn_flip_left.place(relx=0.45, relwidth=0.2, relheight=0.1, rely=0.9)

btn_flip_right = Button(commandsFrame, text="Direita", command=flip_right)
btn_flip_right.place(relx=0.65, relwidth=0.2, relheight=0.1, rely=0.9)

#---------- TERMINAL FRAME ----------
terminalFrame = LabelFrame(root, text="Terminal")
terminalFrame.place(rely=0.7, relx=0, relwidth=1, relheight=0.3)

terminalList = Listbox(terminalFrame)
terminalList.pack(fill="both", expand=1)

#---------- START APP ----------
root.mainloop()