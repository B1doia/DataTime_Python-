from datetime import date, datetime

# Armazenando os valores
data = datetime.strptime('26/08/2021', '%d/%m/%Y').date()
data_2 = datetime.strptime('20220101',  '%Y%m%d').date()

#convertendo para o formato Dia - Mês -  Ano
dataFormatada = data.strftime('%d/%m/%Y')
dataFormatada_2 = data_2.strftime('%d/%m/%Y')

#Armazenando a maior data
valor1 = data.strftime('%Y')
valor2 = data_2.strftime('%Y')

#mostrando as datas originais e formatadas
print(data_2)
print(data)
print('----------')
print(dataFormatada)
print(dataFormatada_2)
print('----------')

#Comparando a maior!
if valor1 > valor2:
  print('A primeira data ->', data, 'é maior do que a segunda!!')
else:
  print('A segunda data ->',data_2 ,'  é maior do que a primeira')
