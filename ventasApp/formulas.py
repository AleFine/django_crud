import math

def calcular_tasa_equivalente(tasa,c,x):
    tasa = tasa / 100
    potencia = c/x
    tasa_equivalente = (math.pow(1 + tasa, potencia) - 1) * 100
    return tasa_equivalente

def calcular_stock_final(tasa,stock_inicial,periodos):
    tasa = tasa / 100
    stock_final = (math.pow(1+tasa,periodos)) * stock_inicial
    return stock_final

def calcular_stock_inicial(tasa,stock_final,periodos):
    tasa = tasa / 100
    stock_inicial = stock_final / (math.pow(1+tasa, periodos))
    return stock_inicial

def periodo_equivalente(periodos: float,actual:str, final: str):
    actual = actual.upper()
    final = final.upper()
    
    periodos_totales = {
        'ANUAL': 1,
        'SEMESTRAL': 2,
        'TRIMESTRAL': 4,
        'BIMESTRAL': 6,
        'MENSUAL': 12,
        'SEMANAL': 52,
        'DIARIA': 360
    }
    
    if actual not in periodos_totales or final not in periodos_totales:
        raise ValueError("Formato de periodo no encontrado")
    
    periodo_anual = periodos / periodos_totales[actual] #sacamos todo a anual y luego lo convertimos a su equivalente
    
    periodo_final = periodo_anual * periodos_totales[final] 
    
    return periodo_final

def dias_equivalentes(valor: str):
    
    valor = valor.upper()
    
    dias_totales = {
        'ANUAL': 360,
        'SEMESTRAL': 180,
        'TRIMESTRAL': 90,
        'BIMESTRAL': 60,
        'MENSUAL': 30,
        'SEMANAL': 7,
        'DIARIA': 1
    }
    
    if valor not in dias_totales:
        raise ValueError("Formato de periodo no encontrado")
    
    cantidad_dias = dias_totales[valor]
    return cantidad_dias