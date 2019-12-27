# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:29:42 2019

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
    arquivo_linhas = arquivo.readlines()
    contador = 0
    total=0
    
    for linha in arquivo_linhas :
        nome = linha.split(';')[1]
        cnpj = linha.split(';')[0]
        
        contador=contador+1
        nome = nome.replace(';',' ')
    
        print(' _________________________________________________')
        print(' Consultando: {} ==> {} '.format(contador, nome))
        response = requests.get('http://192.168.1.11:5000/GB?nomefantasia={}'.format(nome))
        print(response.text)
        dic=str(response.text)
        dic= dict(eval(dic))
        #response='{}'.format(dic['Phone'])
        response='{};{};{}'.format(dic['Phone'],dic['Email'],dic['Site'])
        print (str(response)) 
        nome = nome.replace(';',' ')
        file = open(path+file_write,'a')
       
        file.writelines(cnpj+';'+nome+';'+response+'\n')
        
        ############################################################################
        ################################### RELATORIO ##############################
        #===========================================================================
        telefone=response.split(';')
        telefone= (response.split(';')[0])
        
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

    

    
    
    
    
    
    
    
    
    
