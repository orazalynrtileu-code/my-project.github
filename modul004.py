from abc import ABC, abstractmethod


class Qūjat(ABC):
    @abstractmethod
    def ashu(self):
        pass


class Esap(Qūjat):
    def __init__(self, ataýy, kezeń):
        self.ataýy = ataýy
        self.kezeń = kezeń

    def ashu(self):
        print(f"«{self.ataýy}» есебі {self.kezeń} кезеңі бойынша ашылды.")


class Tüyindeme(Qūjat):
    def __init__(self, aty_zhoni, lauazym):
        self.aty_zhoni = aty_zhoni
        self.lauazym = lauazym

    def ashu(self):
        print(f"{self.aty_zhoni} — {self.lauazym} түйіндемесі ашылды.")


class Hat(Qūjat):
    def __init__(self, alushy, taqyryp):
        self.alushy = alushy
        self.taqyryp = taqyryp

    def ashu(self):
        print(f"Хат ашылды: алушы {self.alushy}, тақырыбы «{self.taqyryp}».")


class Shott(Qūjat):
    def __init__(self, nomer, soma, klient):
        self.nomer = nomer
        self.soma = soma
        self.klient = klient

    def ashu(self):
        print(f"№{self.nomer} шоты {self.soma} ₸ сомасына {self.klient} үшін ашылды.")


class QūjatZhasaushy(ABC):
    @abstractmethod
    def qūjat_zhasau(self) -> Qūjat:
        pass

    def oryndau(self):
        print("Құжат дайындалуда...")
        qūjat = self.qūjat_zhasau()
        qūjat.ashu()
        print("Құжат сәтті өңделді.\n")


class EsapZhasaushy(QūjatZhasaushy):
    def __init__(self, ataýy, kezeń):
        self.ataýy = ataýy
        self.kezeń = kezeń

    def qūjat_zhasau(self) -> Qūjat:
        return Esap(self.ataýy, self.kezeń)


class TüyindemeZhasaushy(QūjatZhasaushy):
    def __init__(self, aty_zhoni, lauazym):
        self.aty_zhoni = aty_zhoni
        self.lauazym = lauazym

    def qūjat_zhasau(self) -> Qūjat:
        return Tüyindeme(self.aty_zhoni, self.lauazym)


class HatZhasaushy(QūjatZhasaushy):
    def __init__(self, alushy, taqyryp):
        self.alushy = alushy
        self.taqyryp = taqyryp

    def qūjat_zhasau(self) -> Qūjat:
        return Hat(self.alushy, self.taqyryp)


class ShottZhasaushy(QūjatZhasaushy):
    def __init__(self, nomer, soma, klient):
        self.nomer = nomer
        self.soma = soma
        self.klient = klient

    def qūjat_zhasau(self) -> Qūjat:
        return Shott(self.nomer, self.soma, self.klient)


FABRIKA_KARTASY = {
    "esap": EsapZhasaushy,
    "tuyindeme": TüyindemeZhasaushy,
    "hat": HatZhasaushy,
    "shott": ShottZhasaushy
}


def main():
    print("Құжат жасау жүйесі\n")
    print("Қолжетімді түрлер: esap, tuyindeme, hat, shott")
    print("Шығу үшін 'exit' енгізіңіз\n")

    while True:
        qūjat_turi = input("Қандай құжат жасау керек? ").strip().lower()

        if qūjat_turi == "exit":
            print("Бағдарлама аяқталды.")
            break

        if qūjat_turi not in FABRIKA_KARTASY:
            print("Белгісіз құжат түрі.\n")
            continue

        zhasaushy_klass = FABRIKA_KARTASY[qūjat_turi]

        try:
            if qūjat_turi == "esap":
                ataýy = input("Есеп атауы: ")
                kezeń = input("Кезеңі: ")
                zhasaushy = zhasaushy_klass(ataýy, kezeń)

            elif qūjat_turi == "tuyindeme":
                aty_zhoni = input("Аты-жөні: ")
                lauazym = input("Лауазымы: ")
                zhasaushy = zhasaushy_klass(aty_zhoni, lauazym)

            elif qūjat_turi == "hat":
                alushy = input("Алушы: ")
                taqyryp = input("Тақырыбы: ")
                zhasaushy = zhasaushy_klass(alushy, taqyryp)

            elif qūjat_turi == "shott":
                nomer = input("Шот нөмірі: ")
                soma = input("Сомасы (₸): ")
                klient = input("Клиент: ")
                zhasaushy = zhasaushy_klass(nomer, soma, klient)

            zhasaushy.oryndau()

        except Exception as e:
            print(f"Қате: {e}\n")


if __name__ == "__main__":
    main()
