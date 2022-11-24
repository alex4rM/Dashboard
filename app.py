import pandas as pd
import openpyxl

exc = pd.read_excel('BD_Dash_Entrega.xlsx')
#print(exc[['Empleado','Ventas', 'Cliente']])

tabla_pivote = exc.pivot_table(index='Empleado',columns='Cliente', values='Ventas', aggfunc='sum').round(0)
print(tabla_pivote)