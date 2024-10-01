# Solicitar datos al usuario
horas_trabajadas = float(input("Horas trabajadas: "))
tarifa_por_hora = float(input("Tarifa por hora: "))
anios_antiguedad = int(input("Años de antigüedad: "))
total_ventas = float(input("Total de ventas: "))

# Calcular salario base
salario_base = horas_trabajadas * tarifa_por_hora
if horas_trabajadas > 40:
    horas_extras = horas_trabajadas - 40
    salario_base += horas_extras * (tarifa_por_hora * 0.5)  # 150% de la tarifa normal

# Bonificación por antigüedad
bono_antiguedad = 0
if anios_antiguedad >= 5:
    bono_antiguedad = salario_base * 0.05

# Comisión por ventas
comision_ventas = 0
if total_ventas > 1000:
    comision_ventas = (total_ventas - 1000) * 0.02

# Calcular salario bruto
salario_bruto = salario_base + bono_antiguedad + comision_ventas

# Calcular descuentos
if salario_bruto <= 1000:
    descuento = salario_bruto * 0.10
elif salario_bruto <= 2000:
    descuento = 100 + (salario_bruto - 1000) * 0.05
else:
    descuento = 100 + 50 + (salario_bruto - 2000) * 0.03  # 10% + 5% + 3% sobre el resto

# Calcular salario neto
salario_neto = salario_bruto - descuento

# Mostrar resumen
print("\nResumen del salario:")
print("Salario base: $", salario_base)
print("Bono por antigüedad: $", bono_antiguedad)
print("Comisión por ventas: $", comision_ventas)
print("Salario bruto: $", salario_bruto)
print("Descuentos: $", descuento)
print("Salario neto: $", salario_neto)
