# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
import fft

#----------------------------------------------------------------------

class MainWindow():

    #----------------

    def __init__(self, main):

        # Nos variables
        lst = ["jazz_1", "jazz_2", "metal_1", "metal_2", "blues_1", "blues_2", "classical_1", "classical_2", "country_1", "country_2", "disco_1", "disco_2", "hiphop_1", "hiphop_2", "pop_1", "pop_2", "rock_1", "rock_2"]
        music1 = StringVar()
        music1.set("jazz_1")
        music2 = StringVar()
        music2.set("hiphop_1")

        # Initialisation de nos graphes
        tabplot1 = fft.plot("jazz_1", 1)
        tabplot2 = fft.plot("hiphop_1", 2)
        self.joinPlot()
        self.myPlot = self.returnPicture("myplots.jpg")

        # Creation de nos frames
        self.l1 = LabelFrame(main, text="Selection des fichiers", pady=15, padx=15)
        self.l2 = LabelFrame(main, text="Graphes", pady=15)
        self.l3 = LabelFrame(main, text="Analyse", pady=15)

        # Frame 1
        Label(self.l1, text="Selectionnez le fichier audio à analyser").grid(row=0, columnspan=2)

        self.m1 = OptionMenu(self.l1, music1, *lst, command=self.onSelect)
        self.m1.grid(row=1, column=0)
        self.m2 = OptionMenu(self.l1, music2, *lst, command=self.onSelect2)
        self.m2.grid(row=1, column=1)

        self.l1.pack(fill="both", expand="yes")

        # Frame 2
        self.plot1 = Canvas(self.l2, width=500, height=400, bg="white")
        self.plot1.pack()

        self.plot1_on_canvas = self.plot1.create_image(0, 0, anchor=NW, image=self.myPlot)

        self.l2.pack(fill="both", expand="yes")

        # Frame 3
        Label(self.l3, text=self.compare(tabplot1, tabplot2)).pack()
        Label(self.l3, text="% de similitude").pack()


        self.l3.pack(fill="both", expand="yes")

    #----------------

    def onSelect(self, choix):
        fft.plot(choix, 1)

        self.joinPlot()
        self.plot1.itemconfig(self.plot1_on_canvas, image=self.returnPicture("myplots.jpg"))

    def onSelect2(self, choix):
        fft.plot(choix, 2)

        self.joinPlot()
        self.plot1.itemconfig(self.plot1_on_canvas, image=self.returnPicture("myplots.jpg"))

    def returnPicture(self, path):
        self.img = Image.open(path)
        self.photo = ImageTk.PhotoImage(self.img)
        return self.photo

    def compare(self, tabplot1, tabplot2):
        var = 0
        tabLen = len(tabplot1)
        for i in range(0, tabLen):
            if tabplot1[i] == tabplot2[i]:
                var = var + 1

        var = var / len(tabplot1) * 100

        return var

    def joinPlot(self):
        self.myPlot1 = Image.open("myplot1.jpg")
        self.myPlot2 = Image.open("myplot2.jpg")
        self.width, self.height = self.myPlot1.size
        new_img = Image.new('RGB', (self.width, self.height * 2))
        y_offset = 0
        new_img.paste(self.myPlot1, (0, y_offset))
        y_offset += self.height
        new_img.paste(self.myPlot2, (0, y_offset))
        new_img.save('myplots.jpg')

#----------------------------------------------------------------------

root = Tk()
root.title("MusicIA")
MainWindow(root)
root.mainloop()