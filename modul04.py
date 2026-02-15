from abc import ABC, abstractmethod

class Koliq(ABC):
    @abstractmethod
    def juru(self):
        pass

    @abstractmethod
    def zhanarmai_quyu(self):
        pass


class Kolik(Koliq):
    def __init__(self, marka, model, zhanarmai_turi):
        self.marka = marka
        self.model = model
        self.zhanarmai_turi = zhanarmai_turi

    def juru(self):
        print(f"{self.marka} {self.model} көлігі {self.zhanarmai_turi} отынымен жүріп жатыр.")

    def zhanarmai_quyu(self):
        print(f"{self.marka} {self.model} көлігіне {self.zhanarmai_turi} отыны құйылуда.")


class Motocikl(Koliq):
    def __init__(self, turi, qozgaltqysh_kolemi):
        self.turi = turi
        self.qozgaltqysh_kolemi = qozgaltqysh_kolemi

    def juru(self):
        print(f"{self.qozgaltqysh_kolemi}cc қозғалтқышы бар {self.turi} мотоцикл жүріп жатыр.")

    def zhanarmai_quyu(self):
        print(f"{self.turi} мотоцикліне жанармай құйылуда.")


class ZhukKoligi(Koliq):
    def __init__(self, juk_koterimi, oster_sany):
        self.juk_koterimi = juk_koterimi
        self.oster_sany = oster_sany

    def juru(self):
        print(f"{self.juk_koterimi} тонна жүк көтеретін, {self.oster_sany} осьті жүк көлігі жүріп жатыр.")

    def zhanarmai_quyu(self):
        print(f"{self.juk_koterimi} тонна жүк көлігіне жанармай құйылуда.")


class Avtobus(Koliq):
    def __init__(self, oryn_sany, bagyt):
        self.oryn_sany = oryn_sany
        self.bagyt = bagyt

    def juru(self):
        print(f"{self.oryn_sany} орындық автобус {self.bagyt} бағыты бойынша жүріп жатыр.")

    def zhanarmai_quyu(self):
        print(f"{self.bagyt} бағытына шығатын автобусқа жанармай құйылуда.")


class Elektrosamokat(Koliq):
    def __init__(self, batareya_siyimdilygy, max_zhyldamdyq):
        self.batareya_siyimdilygy = batareya_siyimdilygy
        self.max_zhyldamdyq = max_zhyldamdyq

    def juru(self):
        print(f"{self.batareya_siyimdilygy}Wh батареясы бар электросамокат {self.max_zhyldamdyq} км/сағ жылдамдыққа дейін жүре алады.")

    def zhanarmai_quyu(self):
        print(f"{self.batareya_siyimdilygy}Wh батареялы электросамокат зарядталуда.")


class KoliqFabrikasy(ABC):
    @abstractmethod
    def koliq_zhasau(self, **kwargs) -> Koliq:
        pass


class KolikFabrikasy(KoliqFabrikasy):
    def koliq_zhasau(self, **kwargs) -> Koliq:
        marka = kwargs.get('marka')
        model = kwargs.get('model')
        zhanarmai_turi = kwargs.get('zhanarmai_turi')
        if not (marka and model and zhanarmai_turi):
            raise ValueError("Көлік үшін параметрлер жетіспейді: marka, model, zhanarmai_turi")
        return Kolik(marka, model, zhanarmai_turi)


class MotociklFabrikasy(KoliqFabrikasy):
    def koliq_zhasau(self, **kwargs) -> Koliq:
        turi = kwargs.get('turi')
        qozgaltqysh_kolemi = kwargs.get('qozgaltqysh_kolemi')
        if not (turi and qozgaltqysh_kolemi):
            raise ValueError("Мотоцикл үшін параметрлер жетіспейді: turi, qozgaltqysh_kolemi")
        return Motocikl(turi, qozgaltqysh_kolemi)


class ZhukKoligiFabrikasy(KoliqFabrikasy):
    def koliq_zhasau(self, **kwargs) -> Koliq:
        juk_koterimi = kwargs.get('juk_koterimi')
        oster_sany = kwargs.get('oster_sany')
        if not (juk_koterimi and oster_sany):
            raise ValueError("Жүк көлігі үшін параметрлер жетіспейді: juk_koterimi, oster_sany")
        return ZhukKoligi(juk_koterimi, oster_sany)


class AvtobusFabrikasy(KoliqFabrikasy):
    def koliq_zhasau(self, **kwargs) -> Koliq:
        oryn_sany = kwargs.get('oryn_sany')
        bagyt = kwargs.get('bagyt')
        if not (oryn_sany and bagyt):
            raise ValueError("Автобус үшін параметрлер жетіспейді: oryn_sany, bagyt")
        return Avtobus(oryn_sany, bagyt)


class ElektrosamokatFabrikasy(KoliqFabrikasy):
    def koliq_zhasau(self, **kwargs) -> Koliq:
        batareya_siyimdilygy = kwargs.get('batareya_siyimdilygy')
        max_zhyldamdyq = kwargs.get('max_zhyldamdyq')
        if not (batareya_siyimdilygy and max_zhyldamdyq):
            raise ValueError("Электросамокат үшін параметрлер жетіспейді: batareya_siyimdilygy, max_zhyldamdyq")
        return Elektrosamokat(batareya_siyimdilygy, max_zhyldamdyq)


def fabrikany_alu(kolik_turi: str) -> KoliqFabrikasy:
    fabrikalar = {
        'kolik': KolikFabrikasy(),
        'motocikl': MotociklFabrikasy(),
        'zhuk': ZhukKoligiFabrikasy(),
        'avtobus': AvtobusFabrikasy(),
        'elektrosamokat': ElektrosamokatFabrikasy()
    }
    fabrika = fabrikalar.get(kolik_turi.lower())
    if not fabrika:
        raise ValueError(f"Белгісіз көлік түрі: {kolik_turi}")
    return fabrika


def main():
    while True:
        kolik_turi = input("Көлік түрін енгізіңіз (kolik, motocikl, zhuk, avtobus, elektrosamokat) немесе 'exit' деп жазыңыз: ").strip().lower()
        if kolik_turi == 'exit':
            break

        try:
            fabrika = fabrikany_alu(kolik_turi)

            kwargs = {}
            if kolik_turi == 'kolik':
                kwargs['marka'] = input("Маркасын енгізіңіз: ")
                kwargs['model'] = input("Моделін енгізіңіз: ")
                kwargs['zhanarmai_turi'] = input("Жанармай түрін енгізіңіз: ")
            elif kolik_turi == 'motocikl':
                kwargs['turi'] = input("Мотоцикл түрін енгізіңіз: ")
                kwargs['qozgaltqysh_kolemi'] = int(input("Қозғалтқыш көлемін енгізіңіз (cc): "))
            elif kolik_turi == 'zhuk':
                kwargs['juk_koterimi'] = float(input("Жүк көтерімділігін енгізіңіз (тонна): "))
                kwargs['oster_sany'] = int(input("Ось санын енгізіңіз: "))
            elif kolik_turi == 'avtobus':
                kwargs['oryn_sany'] = int(input("Орын санын енгізіңіз: "))
                kwargs['bagyt'] = input("Бағытын енгізіңіз: ")
            elif kolik_turi == 'elektrosamokat':
                kwargs['batareya_siyimdilygy'] = int(input("Батарея сыйымдылығын енгізіңіз (Wh): "))
                kwargs['max_zhyldamdyq'] = int(input("Максималды жылдамдықты енгізіңіз (км/сағ): "))

            kolik = fabrika.koliq_zhasau(**kwargs)
            kolik.juru()
            kolik.zhanarmai_quyu()
            print("\n")

        except ValueError as e:
            print(f"Қате: {e}")


if __name__ == "__main__":
    main()
