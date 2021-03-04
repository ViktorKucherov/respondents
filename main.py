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


dictionary = {"Респондент": [], "Вопрос": [], "Варианты ответов": [], "Ответ": []}

indices = list()
keys = list()

for index, row in data_frame_survey.iterrows():
    if re.search(r"^\S+", str(row[0])) and (str(row[0]) != "nan"):
        print(index, ":", row[0])
        indices.append(index)
        keys.append(row[0])
indices.append(indices[-1]+1)

questions_block = [[key] * i for i, key in zip(np.diff(indices), keys)]
questions_block = [every_question for sublist in questions_block for every_question in sublist]
count_of_repeatitions = len(questions_block)

variants_block = data_frame_survey[data_frame_survey.columns[1]].values
print(variants_block)
#variants_block = [re.sub(r'(?:\\xa0)+', '', str(i)) for i in variants_block]
variants_block = [re.sub(r" +"," ",ud.normalize("NFKD",str(i))) for i in variants_block]
print(variants_block)

# формирование колонки с повторяющимися названиями респондентов
respondents = list()
answers = list()
respondents_names = data_frame_survey.columns[2:]
#print(respondents_names)
for respondent_name in respondents_names:
    respondents = respondents + [respondent_name] * count_of_repeatitions
    #print(data_frame_survey[respondent_name].values)
    #answers = answers + data_frame_survey[respondent_name].values



# формирование колонки с повторяющимися блоками вопросов, исходя из количества респондентов
questions = list()
questions = questions_block * len(respondents_names)

# формирование колонки с повторяющимися блоками вариантов ответов, исходя из количества респондентов
variants = list()
variants = variants_block * len(respondents_names)

print(len(respondents))
dictionary["Респондент"] = respondents
dictionary["Вопрос"] = questions
dictionary["Варианты ответов"] = variants
dictionary["Ответ"] = variants

#result_df = pd.DataFrame(data=dictionary)
#result_df.to_excel("output.xlsx")
print("END_OF_STRING")
