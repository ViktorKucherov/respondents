#!/bin/
import pandas as pd
import numpy as np
import re

respondents = "respondents.xlsx"  # обозначаем файл
file = pd.ExcelFile(respondents)  # вызываем метод загрузки файла в объект
data_frame_survey = file.parse(file.sheet_names[1])  # парсим объект по необходимому нам листу анкета_опрос
# print(data_frame_survey.columns) # выводим столбцы
# data_frame_survey['№ Анкеты']=data_frame_survey['№ Анкеты'].astype('str')
# print(data_frame_survey.iterrows())
# parser_dict = {year_key: [f"MONTHS:{m}:{year_key}" for m in months] for year_key in years}


dictionary = {"Респондент": [], "Вопрос": [], "Варианты ответов": [], "Ответ": [], "Населенный пункт": [], "Код субъекта": [], "Телефон": []}

indices = list()
keys = list()

for index, row in data_frame_survey.iterrows():
    if re.search(r"^\S+", str(row[0])) and (str(row[0]) != "nan"):
        print(index, ":", row[0])
        indices.append(index)
        keys.append(row[0])
indices.append(indices[-1]+1)

# print(indices, keys)
# print({"Вопрос": [key for key in keys]})
questions = [[key] * i for i, key in zip(np.diff(indices), keys)]
questions = [every_question for sublist in questions for every_question in sublist]


variants = data_frame_survey[data_frame_survey.columns[1]].values

byte_code = b"\xa0"


for variant in variants:
    print(str(variant))
    for e in str(variant):
        print(e)
        e = re.sub(r'\S+', '', str(e))
print(variants)
for column in data_frame_survey.columns[2:]:
    answers = data_frame_survey[column].values


result_df = pd.DataFrame(data=dictionary)
result_df.to_excel("output.xlsx")
