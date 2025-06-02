from graph import *
from control import *


class ShowVibra(Frame):
    """Démonstration de mouvements vibratoires harmoniques"""

    def __init__(self, boss=None):
        Frame.__init__(self)  # constructeur de la classe parente

        self.couleur = ["green", "yellow", "orange", "blue"]
        self.graph_count = len(self.couleur)
        self.trace = [0] * self.graph_count
        self.controle = [0] * self.graph_count

        self.gra = DrawGraph(self, larg=750, haut=540)
        self.gra.configure(bg='black', bd=2, relief="sunken")
        self.gra.pack(side=TOP, padx=100, pady=5)
        for i in range(self.graph_count):
            self.controle[i] = CreateControl(self, self.couleur[i])
            self.controle[i].pack(pady=5)

        self.master.bind('<Control-Z>', self.montreCourbes)
        self.master.title('Mouvements vibratoires harmoniques')
        self.pack()

    def montreCourbes(self, event):
        """(Ré)Affichage des trois graphiques élongation/temps"""
        for i in range(self.graph_count):
            self.gra.delete(self.trace[i])
            freq, phase, ampl = self.controle[i].get_values()
            if self.controle[i].check.get():
                self.trace[i] = self.gra.traceCourbe(
                    coul=self.couleur[i],
                    freq=freq,
                    phase=phase,
                    ampl=ampl)


#### Code pour tester la classe : ###

if __name__ == '__main__':
    ShowVibra().mainloop()
