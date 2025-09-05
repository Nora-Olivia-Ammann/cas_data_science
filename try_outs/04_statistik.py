import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import scipy.stats as stats

def aufgabe_2_3_1_frequency():
    """
    Aufgabe 2.3.1. Der folgende Datensatz stellt die Schalld ̈ammzahl [in db] von 10 cm starken
    Gibsdielenw ̈anden bei 400 Hz dar.
    25 24 27 24 24 23 23 28 26
    Erstellen Sie eine H ̈aufigkeitstabelle und ein Histogramm
    """
    nums = [25, 24, 27, 24, 24, 23, 23, 28, 26]
    values, counts = np.unique(nums, return_counts=True)
    frequency_dict = dict(zip(values, counts))
    ic(frequency_dict)


def aufgabe_2_3_1_bar_plot():
    """
    Aufgabe 2.3.1. Der folgende Datensatz stellt die Schalld ̈ammzahl [in db] von 10 cm starken
    Gibsdielenw ̈anden bei 400 Hz dar.
    25 24 27 24 24 23 23 28 26
    Erstellen Sie eine H ̈aufigkeitstabelle und ein Histogramm
    """
    nums = [25, 24, 27, 24, 24, 23, 23, 28, 26]
    n = len(nums)

    def get_anzahl_klassen():
        # root of n
        return int(np.sqrt(n))

    number_of_bins = get_anzahl_klassen()
    ic(number_of_bins)

    def get_klassenbreite() -> int:
        # (max - min) / k
        zaehler = max(nums) - min(nums)
        return int(zaehler / number_of_bins)

    d = get_klassenbreite()
    ic(d)

    plt.hist(nums, bins=number_of_bins, edgecolor="black")
    ic("Histogram")
    # plt.show()
    data = np.array(nums)

    np_hist = np.histogram(data, bins=number_of_bins)
    ic(np_hist)

    plt.hist(data, bins=number_of_bins)
    plt.show()


def aufgabe_5_1_4():
    anzahl_schiessen = 3
    summe = sum([0.5*10, 0.3*5, 0.2*1])
    ic(summe / 3)


def aufgabe_6_1_1():
    anzahl_schiessen = 3
    summe = sum([15*0.08, 16*0.28, 17*0.52, 18*0.12]) * 100
    ic(summe)

def aufgabe_9_1_1():
    pass

aufgabe_9_1_1()