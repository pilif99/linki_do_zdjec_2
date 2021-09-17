
import os
import pandas as pd, pandas
import re

class Lista_Linkow(pd.DataFrame):

    def __init__(self):

        super().__init__()

        slownik = {}

        os.chdir("Nowy folder (4)")
        lista_marek = os.listdir()

        for marka in lista_marek:

            lista_modeli = os.listdir(marka)
            for model in lista_modeli:
                
                reszta = self.zdobadz_reszte(marka + '\\' + model)
                slownik[model] = reszta

        df =  pd.DataFrame.from_dict(slownik, orient = 'index')
        lista = df.index.tolist()
        for i in range(len(lista)):
            if lista[i] in ['Cubby III', 'Cubby IV', 'Flux', 'Hardy II', 'Hiflow IV', 'Hunter Pro', 'Rebel', 'Vandal']:
                lista[i] = lista[i] + ' (kurtka)'
        
        for i in range(len(lista)):
            if lista[i] == 'Trip ST':
                lista[i] = lista[i] + ' (kurtka)'

        df.index = lista
        self.append(super().__init__(df))
            
    def zdobadz_reszte(self, folder) -> list:

        lista = []

        def dodaj(sciezka):

            if os.path.isdir(sciezka):
                for i in os.listdir(sciezka):
                    return dodaj(sciezka + '\\' + i)
            else:
                return 'https://powerlink.powerbike.pl/AMZPhoto/1mb/' + re.sub('\\\\', '/', sciezka)

        for i in os.listdir(folder):
            lista.append(dodaj(folder + '\\' + i))

        return lista