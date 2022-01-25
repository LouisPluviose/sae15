import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

df = pd.read_csv(r".\vaccination-covid\data\raw\masterlist.csv", delimiter=";")
df