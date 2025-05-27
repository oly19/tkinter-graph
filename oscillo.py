from tkinter import *
from math import sin, pi


class OscilloGraphe(Canvas):
    def __init__(self, boss=None, larg=200, haut=150):
        Canvas.__init__(self)
        self.configure(width=larg, height=haut)
        self.larg, self.haut = larg, haut
        self.create_line(20, haut / 2, larg, haut / 2, arrow=LAST, width=3, fill="white")
        self.create_line(larg / 2, haut - 5, larg / 2, 5, arrow=LAST, width=3, fill="white")

        pas = (larg - 40) / 8.
        for t in range(10):
            stx = 20 + t * pas
            self.create_line(stx, 20, stx, haut - 20, fill="grey")
            # self.create_text(stx - 8, (haut / 2) - 8, text=t, font=("Helvetica", 6))

        pas = (haut - 40) / 10.
        for t in range(11):
            sty = 20 + t * pas
            self.create_line(20, sty, larg - 20, sty, fill="grey")
            # self.create_text(10, sty - 1, text=11 - t - 6, font=("Helvetica", 6))

        self.create_text(30, 10, text="e", anchor=CENTER, fill="red")
        self.create_text(larg - 5, (haut / 2) - 15, text="t", anchor=CENTER, fill="red")

    def traceCourbe(self, freq=1, phase=0, ampl=10, coul='red'):
        curve = []
        pas = (self.larg - 40) / 1000.
        for t in range(0, 1001, 5):
            e = ampl * sin(2 * pi * freq * t / 1000 - phase)
            x = 20 + t * pas
            y = self.haut / 2 - e * self.haut / 25
            curve.append((x, y))
        n = self.create_line(curve, fill=coul, smooth=1)
        return n


if __name__ == '__main__':
    root = Tk()
    gra = OscilloGraphe(root, 1000, 720)
    gra.pack()
    gra.configure(bg='ivory', bd=2, relief=SUNKEN)
    gra.traceCourbe(2, 1.2, 10, 'purple')
    root.mainloop()
