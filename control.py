from tkinter import *
from math import pi


class CreateControl(Frame):
    """Control window in order to set values for different curve parameters"""

    def __init__(self, boss=None, coul: str = "red"):
        Frame.__init__(self, boss, bd=4, relief="groove")

        self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul
        self.check = IntVar()

        Checkbutton(
            self, text="Display", variable=self.check, font=("Helvetica", 9),
            fg=self.coul, command=self.set_curve,
        ).pack(side=LEFT)

        Scale(
            self, length=200, orient=HORIZONTAL, sliderlength=25, troughcolor=self.coul,
            label='Fréquence (Hz) :', from_=1.0, to=9.0, tickinterval=2.0, font=("Helvetica", 9),
            resolution=0.25, showvalue=False, command=self.set_frequency,
        ).pack(side=LEFT, padx=10)

        Scale(
            self, length=200, orient=HORIZONTAL, sliderlength=15, troughcolor=self.coul,
            label='Phase (degrés) :', from_=-180, to=180, tickinterval=90, font=("Helvetica", 9),
            showvalue=0, command=self.set_phase
        ).pack(side=LEFT, padx=10)

        Scale(
            self, length=200, orient=HORIZONTAL, sliderlength=25, troughcolor=self.coul,
            label='Amplitude :', from_=2, to=10, tickinterval=2, font=("Helvetica", 9),
            showvalue=0, command=self.set_amplitude
        ).pack(side=LEFT, padx=10)

    def set_curve(self):
        self.event_generate('<Control-Z>')

    def set_frequency(self, frequency: int | float):
        self.freq = float(frequency)
        self.event_generate('<Control-Z>')

    def set_phase(self, phase: int | float):
        self.phase = float(phase) * 2 * pi / 360
        self.event_generate('<Control-Z>')

    def set_amplitude(self, amplitude: int | float):
        self.ampl = float(amplitude)
        self.event_generate('<Control-Z>')

    def get_values(self):
        return self.freq, self.phase, self.ampl

if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text=f"{fra.check.get()} - {fra.freq} - {fra.phase} - {fra.ampl}")


    root = Tk()
    fra = CreateControl(root, 'navy')
    fra.pack(side=TOP)

    lab = Label(root, text='test')
    lab.pack()

    root.bind('<Control-Z>', afficherTout)
    root.mainloop()
