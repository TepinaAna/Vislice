import random

# Najprej konstante
STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'A'

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPAČNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Vislice:
    """
    Krovni objekt, ki upravlja z vsemi igrami.
    """
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        return max(self.igre.keys()) + 1

    def nova_igra(self):
        nov_id = self.prost_id_igre()

        sveza = nova_igra(bazen_besed)

        self.igre[nov_id] = (sveza, ZACETEK)

        return nov_id
    
    def ugibaj(self, id_igre, crka):
        igra, stanje = self.igre[id_igre]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() # Pravilno geslo
        # Kar je uporabnik do sedaj ugibal
        self.crke = crke.upper() # Do sedaj ugibane črke
        # Vse stvari v igri so zgolj velike črke

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([i in self.crke for i in self.geslo])
        #['a in self.crke, 'x' in self.crke, ...] -> [True, True,...] -all

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        pravilni_del = ''
        for crka in self.geslo:
            if crka in self.crke:
                pravilni_del += crka
            else:
                pravilni_del += '_'
        return pravilni_del

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    # Uporabnik poskuša 'uganit' črko 'crka'
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke += crka

        if self.zmaga():
            return ZMAGA

        if crka in self.geslo:
            return PRAVILNA_CRKA

        if self.poraz():
            return PORAZ
        return NAPAČNA_CRKA
        
bazen_besed = []
with open('Vislice/besede.txt', encoding='utf8') as input_file:
    bazen_besed = input_file.readlines()

def nova_igra(bazen_besed):
    beseda = random.choice(bazen_besed).strip()
    return Igra(beseda, '')


# i = nova_igra(bazen_besed)
# print(i.geslo)