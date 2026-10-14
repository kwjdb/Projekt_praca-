
class KontoBankowe:
    def __init__(self, wlasciceil):
        self.wlasciceil = wlasciceil
        self.konto = 0
    def wplac(self,kwota):
        self.konto = self.konto + kwota
    def wyplac(self,kwota):

        self.konto = self.konto - kwota


kontohuberta = KontoBankowe("Hubert")
kontokornela = KontoBankowe("Kornel")

kontokornela.wyplac(1000)
kontohuberta.wplac(1000)

print(kontohuberta.konto)
print(kontokornela.konto)
