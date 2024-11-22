def calcular_ebitda(ingresos, costos):
    return ingresos - costos




def calcular_eva(ebitda, costo_capital, capital_empleado):
    return ebitda - (costo_capital / 100) * capital_empleado


def calcular_ratios_financieros(utilidad, ingresos, deuda, patrimonio, acciones, dividendos, crecimiento_utilidad):
    ratios = {}
    ratios['RATIO PER (PRECIO SOBRE BENEFICIOS)'] = utilidad / acciones
    ratios['RATIO PRECIO SOBRE VENTAS (PV)'] = ingresos / acciones
    ratios['RATIO PRECIO SOBRE VALOR CONTABLE (PRICE TO BOOK)'] = patrimonio / acciones
    ratios['RATIO  VALOR DE LA EMPRESA SOBRE EL EBITDA'] = deuda / utilidad if utilidad > 0 else 0
    ratios['RATIO PEG'] = (utilidad / acciones) / (crecimiento_utilidad / 100) if crecimiento_utilidad > 0 else 0
    ratios['ROA – RENTABILIDAD SOBRE LOS ACTIVOS'] = (utilidad / ingresos) * 100 if ingresos > 0 else 0
    ratios['ROE – RENTABILIDAD SOBRE PATRIMONIO'] = (utilidad / patrimonio) * 100 if patrimonio > 0 else 0
    ratios['UPA – BENEFICIO POR ACCIÓN'] = utilidad / acciones
    ratios['DIVIDENDO POR ACCIÓN'] = dividendos / acciones
    ratios['YIELD'] = (dividendos / acciones) / ingresos if ingresos > 0 else 0
    return ratios
