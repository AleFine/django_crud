import math

def beta_apalancado(beta_d:float, tasa_impuesto:float, wd_pasivo:float):
    beta_a = beta_d * (1+(1-tasa_impuesto/100)*(wd_pasivo/100))
    return beta_a

def calcular_capm(beta_a:float, tasa_libre_riesgo:float, tasa_mercado:float, prima_riesgo:float):
    capm = tasa_libre_riesgo + beta_a * (tasa_mercado - tasa_libre_riesgo) + prima_riesgo
    return capm

def convertir_tea(tasa:float):
    tasa_efectiva = (1+(tasa/100))**(360/30)-1
    return tasa_efectiva * 100

def estructura_capital(pasivo:float, patrimonio:float):
    wd_pasivo = pasivo/(pasivo+patrimonio)
    we_patrimonio = patrimonio/(pasivo+patrimonio)
    return wd_pasivo, we_patrimonio

def tasa_ponderada_pasivo(tasa1:float,tasa_efectiva:float):
    tasa2 = ((100 - tasa1)/100)*(tasa_efectiva/100)
    tasa1 = (tasa1/100) * (tasa1/100)
    tasa_ponderada = tasa1 + tasa2
    return tasa_ponderada * 100

def determinar_wacc(tasa_ponderada:float,prima_riesgo:float,wd_pasivo:float,we_patrimonio:float,capm:float):
    wacc = (tasa_ponderada/100) * (1-(prima_riesgo/100)) * (wd_pasivo/100) + (capm/100) * (we_patrimonio/100)
    return wacc * 100











