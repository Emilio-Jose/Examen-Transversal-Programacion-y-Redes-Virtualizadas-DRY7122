# vlan.py
# Pide al usuario un número de VLAN e indica su tipo

vlan = input("Ingresa el número de VLAN: ")

if vlan.isdigit():
    vlan_num = int(vlan)
    if 1 <= vlan_num <= 1005:
        print("La VLAN ingresada está en el rango NORMAL.")
    elif 1006 <= vlan_num <= 4094:
        print("La VLAN ingresada está en el rango EXTENDIDO.")
    else:
        print("El número ingresado no corresponde a una VLAN válida (1-4094).")
else:
    print("Por favor, ingresa un número válido.")
