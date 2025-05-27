from tkinter import *
from math import pi


class ChoixVibra(Frame):
    """Curseurs pour choisir fréquence, phase & amplitude d'une vibration"""

    def __init__(self, boss=None, coul='red'):
        Frame.__init__(self, boss, bd=4, relief="groove")
        self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul
        self.chk = IntVar()

        Checkbutton(
            self, text='Afficher', variable=self.chk,
            fg=self.coul, command=self.setCurve,
        ).pack(side=LEFT)

        Scale(
            self, length=150, orient=HORIZONTAL, sliderlength=25, troughcolor=self.coul,
            label='Fréquence (Hz) :', from_=1., to=9., tickinterval=2,
            resolution=0.25, showvalue=0, command=self.setFrequency
        ).pack(side=LEFT)

        Scale(
            self, length=150, orient=HORIZONTAL, sliderlength=15, troughcolor=self.coul,
            label='Phase (degrés) :', from_=-180, to=180, tickinterval=90,
            showvalue=1, command=self.setPhase
        ).pack(side=LEFT)

        Scale(
            self, length=150, orient=HORIZONTAL, sliderlength=25, troughcolor=self.coul,
            label='Amplitude :', from_=1, to=9, tickinterval=2,
            showvalue=0, command=self.setAmplitude
        ).pack(side=LEFT)

    def setCurve(self):
        self.event_generate('<Control-Z>')

    def setFrequency(self, f):
        self.freq = float(f)
        self.event_generate('<Control-Z>')

    def setPhase(self, p):
        pp = float(p)
        self.phase = pp * 2 * pi / 360
        self.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        self.ampl = float(a)
        self.event_generate('<Control-Z>')


if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text=f"{fra.chk.get()} - {fra.freq} - {fra.phase} - {fra.ampl}")


    root = Tk()
    fra = ChoixVibra(root, 'navy')
    fra.pack(side=TOP)

    lab = Label(root, text='test')
    lab.pack()

    root.bind('<Control-Z>', afficherTout)
    root.mainloop()
