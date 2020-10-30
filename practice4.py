# -*- coding: utf-8 -*-
"""Practice4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WfK5y09L9E6-fJik9MNtNNQjOM37ZGvS
"""

import numpy as np

url="https://github.com/hajdeger/AOP_PUB/blob/master/heart.dat"

import pandas as pd

"""# 4. Vezba
4.1 Ucitavanje realnih podataka sa spoljasnih repozitorijuma

4.2 Formiranje data framea

4.3 Elementarni uvid u prirodu podataka
"""

df=pd.read_csv(url, delimiter=" ", names=['age', 'sex', 'chest_pain_type', 'resting_blood_preassure', 'serum_cholesterol_mg_per_dl', 'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results', 'max_heart_rate_achieved', 'exercise_induced_angina', 'oldpeak_eg_st_depression', 'slope_of_peak_exercise_st_segment', 'num_major_vessels', 'thal', 'heart_disease_present'])

!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

file_id = '1NNd3fjy9rhpefDlXoKaRJATKbA_1ta-W'
downloaded = drive.CreateFile({'id': file_id})

# Download the file to a local disk as 'exported.xlsx'.
downloaded.GetContentFile('exported.xlsx')

!pip install -q xlrd

import pandas as pd
df = pd.read_excel('exported.xlsx')
df

