
import os
import pandas as pd
from lista_linkow import Lista_Linkow

class Linki_Do_Zdjec_2:

    def __init__(self):

        df = Lista_Linkow()
        os.chdir("..")
        writer = pd.ExcelWriter('lista_linkow.xlsx', engine = 'xlsxwriter')
        df.to_excel(writer, header = None)
        writer.save()

a = Linki_Do_Zdjec_2()