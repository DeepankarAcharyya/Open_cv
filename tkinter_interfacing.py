import tkinter as tk
import cv2
from PIL import Image,ImageTk
import threading 
import imutils
from imutils.video import VideoStream
import os
import datetime
import time

#We’ll also need Python’s threading  package to spawn a thread (separate from Tkinter’s mainloop ), used to handle polling of new frames from our video stream.

class boothapp:
    def __init__(self, video_stream):
        self.vs=video_stream
        self.frame=None
        self.thread=None
        self.stopEvent=None

        self.root=tk.Tk()
        self.panel=None 

        btn=tk.Button(self.root,text="Exit",command=self.onClose)
        btn.pack(side="bottom",fill="both", expand="yes")

        self.stopEvent=threading.Event()
        self.thread=threading.Thread(target=self.VideoLoop,args=())
        self.thread.start()

        self.root.title("Tkinter+OpenCV")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

    def VideoLoop(self):
        try:
            while not self.stopEvent.is_set():
                self.frame=self.vs.read()
                self.frame=imutils.resize(self.frame, width=300)
                
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)
                
                if self.panel is None:
                    self.panel = tk.Label(image = image)
                    self.panel.image = image
                    self.panel.pack(side="left", padx=10, pady=10)
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image
        
        except RuntimeError as e:
            print("[INFO] caught a RuntimeError")

    def onClose(self):
            print("[INFO] closing...")
            self.stopEvent.set()
            self.vs.stop()
            self.root.quit()

vs=VideoStream(src=0).start()
time.sleep(2.0)

pba=boothapp(vs)
pba.root.mainloop()