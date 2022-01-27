from itertools import groupby
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

df = pd.read_csv(r".\vaccination-covid\src\data\masterlist.csv", delimiter=";")

#4. Déterminer pour chaque région (*src/model/model.py*) quand la vaccination à débuté.
#y = df.sort_values(by=["semaine_injection", "effectif_1_inj", "region_residence"])



#compression_opts = dict(method='zip', archive_name='out.csv')  
#y.to_csv('out.zip', sep=";", index=False, compression=compression_opts) 

def debutVaccination():
    numRegion = []
    date = []
    s = range(0,100)
    for s in df.semaine_injection.iteritems():
        if s == numRegion:
            pass
        else:
            numRegion.append(df.region_residence)
            date.append(df.semaine_injection)
    return(numRegion, date)

def ComputeMean():
    mean = 0
    return (mean)

def ComputeMedian():
    median = df.groupby(by=["effectif_cumu_termine", "libelle_region = Haut-Rhin"]).median()
    return (median)    

ComputeMedian
    