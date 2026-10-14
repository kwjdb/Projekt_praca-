
class Ekspres:
    def __init__(self,marka):
        self.marka = marka
        self.woda =0
        self.ziarna = 0

    def dolej_wode(self,ilosc):
        print("dodaje składniki")
        self.woda += ilosc
    def dosyp_ziarna(self,iosc):
        print("dodaje składniki")
        self.ziarna += iosc
    def zrob_espreso(self):
        if (self.woda >= 30 and self.ziarna >= 15):
            print("pssss")

            print("twoje espresso z maszyny", self.marka , "jest gotowe")
            self.dolej_wode(-30)
            self.dosyp_ziarna(-15)


        else:
            print("Błąd! Brak składników.")

if __name__ == '__main__':
    philips = Ekspres("Philips")


    philips.zrob_espreso()



    philips.dolej_wode(30)
    philips.dosyp_ziarna(15)


    philips.zrob_espreso()

