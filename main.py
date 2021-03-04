#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re
import unicodedata as ud


respondents_file = "respondents.xlsx"  # обозначаем файл
file = pd.ExcelFile(respondents_file)  # вызываем метод загрузки файла в объект
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

questions = [[key] * i for i, key in zip(np.diff(indices), keys)]
questions = [every_question for sublist in questions for every_question in sublist]
count_of_repeatitions = len(questions)
print(count_of_repeatitions)

variants = data_frame_survey[data_frame_survey.columns[1]].values
variants = re.sub(r'(?:\\xa0)+', '', str(variants))
print(f"ОТФОРМАТИРОВАННЫЙ ВАРИАНТ! {variants}")

respondents = list()
respondents_names = data_frame_survey.columns[2:]
respondents = []

for respondent_name in respondents_names:
    respondents = respondents + [respondent_name]*count_of_repeatitions
    #for e in range(count_of_repeatitions):
    #    respondents.append(respondent_name)

print(len(respondents))


result_df = pd.DataFrame(data=dictionary)
result_df.to_excel("output.xlsx")
