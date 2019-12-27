# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:40:54 2019

@author: ybenson.augustave
"""

import requests
from flask import Flask
app = Flask(__name__)

def consulta1():
    path = 'C:/Users/ybenson.augustave/Desktop/CAPTCHA_V10_20190605/CAPTCHA/'
    file_read = 'IMPUT2_ENR_TICKET_2716.TXT'
    file_write = 'OUTPUT_ENR_TICKET_2716_PJ.txt'
    arquivo = open(path + file_read, 'r',encoding='utf8')
    #meuArquivo = open(path + file_write, 'w')
    nomefantasia = arquivo.readlines()
    nomefantasia
    contador = 0
    total=0
    
    for nome in nomefantasia:
        
        contador=contador+1
        nomefantasia=nome.split(';')
        nome = nome.replace('\n','')
        nome1=nome.replace(';',' ')
        #nome0= (nome.split(';')[0])
        #nome = nome.replace(';',' ')
        #nome = nome.replace(',',' ')
        print(' _________________________________________________')
        print(' Consultando: {} ==> {} '.format(contador, nome))
        response = requests.get('http://192.168.1.11:5000/GB?nomefantasia={}'.format(nome1))
        print(response.text)
        dic=str(response.text)
        dic= dict(eval(dic))
        #type(dic)
        #response1='{}, {}, {}, {}'.format(dic['Empresa'], dic['Phone'],dic['Email'],dic['Site'])
        response1='{};{};{}'.format(dic['Phone'],dic['Email'],dic['Site'])
        #f=dic['Phone']
        #e=dic['Email']
        #s=dic['Site']
        print (str(response1))
        nome= (nome.split(';')[0])
        nome = nome.replace(';',' ')
        #nome = nome.replace(',',' ')
        #nome1 = nome1.replace(';',' ')
        #nome1 = nome.replace(',',' ')
    
        #response2= 'EMPRESA NÃO ENCONTRADA'
        #response1.replace('\\n','')
        
        file = open(path+file_write,'a')
        file.writelines(nome+';'+response1+'\n')
        
        ############################################################################
        ################################### RELATORIO ##############################
        #===========================================================================
        
        telefone=response1.split()
        telefone= (response1.split(',')[0])
        
        if telefone:
            telefone=telefone[0]
            
            total=total+1
        else:
            telefone=''
            total=total+0
        print(' _________________________________________________')    
        file.close()
        print('\033[31m'+' =================>> Relatório <<================='+'\033[0;0m')
        print('|De {} empresas consultadas, encontrou {} telefones|'.format(contador,total))
        print('\033[31m'+' ================================================='+'\033[0;0m')
        print()
consulta1()    
