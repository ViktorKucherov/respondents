#!/bin/
import pandas as pd
import numpy as np

respondents = "respondents.xlsx" # обозначаем файл
file = pd.ExcelFile(respondents) # вызываем метод загрузки файла в объект
data_frame_survey = file.parse(file.sheet_names[1]) # парсим объект по необходимому нам листу анкета_опрос
print(data_frame_survey.columns) # выводим столбцы

