#pyuic5.exe -x p1.ui -o p1.py
import os
from PyQt5 import QtGui, QtCore
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time as t
import serial
from MP32 import *
import pygame
import eyed3
import pyrebase
#Imiportamos todas las librearias que utilizaremos

#seteamos la configuracion para la base de datos
config = {
    "apiKey": "AIzaSyAYHUhONVse4aLsBPpbSN1URs8KxTNdNgQ",
    "authDomain": "pryecto1-b58cc.firebaseapp.com",
    "projectId": "pryecto1-b58cc",
    "storageBucket": "pryecto1-b58cc.appspot.com",
    "messagingSenderId": "122195239233",
    "appId": "1:122195239233:web:e1c9df21ca906a405801c0",
    "measurementId": "G-5ZYYV4L122",
    "databaseURL": "https://pryecto1-b58cc-default-rtdb.firebaseio.com",
    }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#seamos los parametors para el ambiente de nuestra interfaz
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
j = 1

#creamos la clase que contendra todo nuestro codigo principal
class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #conectamos lo botones de la interfaz con las funciones que cada uno va a realizar
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.PlayButton.clicked.connect(self.P)
        self.PauseButton.clicked.connect(self.Pa)
        self.StopButton_3.clicked.connect(self.S)
        self.arriba_button.clicked.connect(self.adelante)
        self.abajo_button.clicked.connect(self.atras)
        self.izquierda_button.clicked.connect(self.izquierda)
        self.derecha_button.clicked.connect(self.derecha)
        self.detener_button.clicked.connect(self.detener)
        
        #leemos las 100 canciones guardadas
        for i in range (1,101):
            audiofile = eyed3.load("100 canciones/track"+ str(i) +".mp3")
            title = str(audiofile.tag.title)
            artist = str(audiofile.tag.artist)
            album = str(audiofile.tag.album)
            numi = str(i)
            tex = numi +" | "+ title +" | "+ artist +" | "+ album  
            self.textBrowser.append(tex)
            
    #inisializamos pygame mixer para la musica
    pygame.mixer.init() 

    #funcion si el sensor de colider es acctivado
    def stream_handler1(message):
        #mandamos a llamar el dato collicion de la firebase
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        c = db.child("Collision").get()
        co = c.val()
        
        #verificamos que el sensor fue activado, en estecaso nos debe de dar una lectura de 3
        if co == 3:
            #llamamos el dato de cancion de firebase
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            m = db.child("Cancion").get()
            NC = m.val()
            #le restamos uno al numero de cancion actual
            NC = NC - 1
            #actualizamos la firabase con el numero de cancion actualizado
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            upload= db.child("Cancion").set(NC)
            #cargamos la cancion deceada en el pygame mixer
            pygame.mixer.music.load("100 canciones/track"+ str(NC) +".mp3")
            audiofile = eyed3.load("100 canciones/track"+ str(NC) +".mp3")
            pygame.mixer.init()
            #y le damo play
            pygame.mixer.music.play()
            
            # obtenemos los datos de la cancion actual de la metadata
            title = str(audiofile.tag.title)
            artist = str(audiofile.tag.artist)
            album = str(audiofile.tag.album)
            
            #creamos una nueva imagen para el display
            image = Image.new('1', (128, 64))
            width = disp.width
            height = disp.height
            image = Image.new('1', (width, height))
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            draw.rectangle((100,100,width,height), outline=100, fill=255)
            # Mandamos los datos de la cancion
            draw.text((15, 16), "Suena "+ title + "\nPor " + artist + "\nDel album " + album, font=font, fill=255)
            # Muestra Texto
            disp.image(image)
            disp.show()
            t.sleep(2)
            
    # funcion si el sensor de barrier es activado
    def stream_handler2(message):
        # llamamos el dato de barrier de la firebase
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        b = db.child("Barrier").get()
        ba = b.val()
        
        #coroboramos que el sensor ha sido activado, en este caso es un 1
        if ba == 1:
            #llamams el dato del numero de cancion de la firebase
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            m = db.child("Cancion").get()
            NC = m.val()
            #le sumamos 1
            NC = NC + 1
            #actualizamos el dato en la firebase
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            upload= db.child("Cancion").set(NC)
            
            #cargamos la cancion en el mixer
            pygame.mixer.music.load("100 canciones/track"+ str(NC) +".mp3")
            audiofile = eyed3.load("100 canciones/track"+ str(NC) +".mp3")
            pygame.mixer.init()
            #y le damos play
            pygame.mixer.music.play()
            
            #obtenemos los datos de la cancion actual
            title = str(audiofile.tag.title)
            artist = str(audiofile.tag.artist)
            album = str(audiofile.tag.album)
            
            #creamos una nueva imagen para el display
            image = Image.new('1', (128, 64))
            width = disp.width
            height = disp.height
            image = Image.new('1', (width, height))
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            draw.rectangle((100,100,width,height), outline=100, fill=255)
            #mandamos la cancion
            draw.text((15, 16), "Suena "+ title + "\nPor " + artist + "\nDel album " + album, font=font, fill=255)
            # Muestra Texto
            disp.image(image)
            disp.show()
            t.sleep(2)
    
    #estas son las encargadas de checar constante mente por cambios de los detos de los sensores de barrier y collision
    my_stream1 = db.child("Collision").stream(stream_handler1)
    my_stream2 = db.child("Barrier").stream(stream_handler2)
    
    #funcion para el boton de play    
    def P(self):
        #obtenemos el numero de nuestra casilla de numero de cancion de la interfaz
        NC = int (self.NumC.text())
        #si el dato en nuestra casilla de la interfaz es mayor a cero cargamos la cancion con el numero ingresado
        if NC > 0:
            #caragamos la cancion al mixer
            pygame.mixer.music.load("100 canciones/track"+ str(NC) +".mp3")
            audiofile = eyed3.load("100 canciones/track"+ str(NC) +".mp3")
            #actualizamo el numero de cancion en la firebase
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            upload= db.child("Cancion").set(NC)
        #si el numero de nuestra casilla de la interfas es 0 descargamos el numero que tengamos en la firebase
        else:
            #llamamos el dato canion de la firebase
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            m= db.child("Cancion").get()
            mc= m.val()
            #acualizamos el dato en la interfaz
            self.NumC.setText(str(mc))
            #cargamos la cancion en la mixer
            pygame.mixer.music.load("100 canciones/track"+ str(mc) +".mp3")
            audiofile = eyed3.load("100 canciones/track"+ str(mc) +".mp3")
        
        #le damos play
        pygame.mixer.music.play()
        
        #obtenemos los datos de la cancion por su metadata
        title = str(audiofile.tag.title)
        artist = str(audiofile.tag.artist)
        album = str(audiofile.tag.album)
        
        #creamos una nueva imagen para el display
        image = Image.new('1', (128, 64))
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.rectangle((100,100,width,height), outline=100, fill=255)
        #mandamos los datos de la cancion
        draw.text((15, 16), "Suena "+ title + "\nPor " + artist + "\nDel album " + album, font=font, fill=255)
        # Muestra Texto
        disp.image(image)
        disp.show()
        t.sleep(2)
        
        #tambien mandamos las datos de la cancion a la interfaz
        self.lineEdit.setText("Suena "+ title + " por " + artist + " del album " + album)
        
    #funcion para el boton de pausa
    def Pa(self):
        #si hay una cancion tocando ponemos pause
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
        #pero si no hay una cancion toando ponemos unpause
        else:
            pygame.mixer.music.unpause()
    
    #funcion para el boton de stop
    def S(self):
        #paramos la cancion
        pygame.mixer.music.stop()
        
    #funcion para el bonton de adlante del mbot
    def adelante(self):
        #actualizamos el dato direccion de la firebase con una f
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        upload= db.child("Direction").set("f")

    #funcion para el bonton de atras del mbot
    def atras(self):
        #actualizamos el dato direccion de la firebase con una b
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        upload= db.child("Direction").set("b")
    
    #funcion para el bonton de izquierda del mbot
    def izquierda(self):
        #actualizamos el dato direccion de la firebase con una l
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        upload= db.child("Direction").set("l")

    #funcion para el bonton de derecha del mbot
    def derecha(self):
        #actualizamos el dato direccion de la firebase con una r
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        upload= db.child("Direction").set("r")

    #funcion para el bonton de detener del mbot
    def detener(self):
        #actualizamos el dato direccion de la firebase con una s
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        upload= db.child("Direction").set("s")
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()
