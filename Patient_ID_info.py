
# coding: utf-8


import os
import re

def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)
#1
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD ADOS"):
    alist.append(fullname)
file_ADOS=[(i,item) for i, item in enumerate(alist)]
#2
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD IEP"):
    alist.append(fullname)
file_IEP=[(i,item) for i, item in enumerate(alist)]
#3
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD Parent Form"):
    alist.append(fullname)
file_Parent_Form=[(i,item) for i, item in enumerate(alist)]
#4
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD Parent Questionnaire"):
    alist.append(fullname)
file_Parent_Questionnaire=[(i,item) for i, item in enumerate(alist)]
#5
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD PCP"):
    alist.append(fullname)
file_PCP=[(i,item) for i, item in enumerate(alist)]
#6
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD School"):
    alist.append(fullname)
file_School=[(i,item) for i, item in enumerate(alist)]
#7
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD School Questionnaire"):
    alist.append(fullname)     
file_School_Questionnaire=[(i,item) for i, item in enumerate(alist)]
#8
alist=[]
for fullname in iterbrowse("/scratch/tsmith8_lab/xye6/data/KDD Testing and Psych"):
    alist.append(fullname)    
file_Testing_and_Psych=[(i,item) for i, item in enumerate(alist)]


def extract_info(catalog_info):
    patient_info=[]

    for i in range(len(catalog_info)):

        test_word=catalog_info[i][1]
        
        if 'MRN' not in test_word:
            continue
        else:

            names =[''.join(re.findall(r'[A-Z]*[,][ ]*[A-Z]*', test_word))]

            Encounter=re.findall(r'\d+',re.findall(r'(?<=Encounter)(.*?)(?=\--)',test_word)[0])
            if len(Encounter)==0:
                    Encounter.append('')

            MRN=re.findall(r'E\d{3,12}',test_word)
            if len(MRN)==0:
                    MRN.append('')

            if len(re.findall(r'(?<=--Vi)(.*?)(?=\.)',test_word))==0:
                    Visit=[]
            else:
                    Visit=re.findall(r'\d{3,12}',re.findall(r'(?<=--Vi)(.*?)(?=\.)',test_word)[0])
            if len(Visit)==0:
                    Visit.append('')

            a=[names,Encounter,MRN,Visit]

            patient_info.append(a)

    temp2=[]
    
    for i in range(len(patient_info)):
        temp1=[]
        for j in range(len(patient_info[i])):
            temp1.append(patient_info[i][j][0])
        temp2.append(temp1)
        
    return temp2


KDD_ADOS = extract_info(file_ADOS)
KDD_IEP = extract_info(file_IEP)
KDD_Parent_Form = extract_info(file_Parent_Form)
KDD_Parent_Questionnaire = extract_info(file_Parent_Questionnaire)
KDD_PCP = extract_info(file_PCP)
KDD_School = extract_info(file_School)
KDD_School_Questionnaire = extract_info(file_School_Questionnaire)
KDD_Testing_and_Psych = extract_info(file_Testing_and_Psych)
