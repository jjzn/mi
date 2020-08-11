#!/usr/bin/python3

import sys

notes = ["do", "re", "mi", "fa", "sol", "la", "si", "do'"]
tones = { 2: 1, 3: 2, 4: 2.5, 5: 3.5, 6: 4.5, 7: 5.5, 8: 6 }

start = input("Inicio: ")
end = input("Fin: ")

if (start not in notes) or (end not in notes):
    print("\nNota inválida")
    sys.exit(1)

start_mod = input("Modificador 1: ")
end_mod = input("Modificador 2: ")

if (start_mod not in ["#", "b", ""]) or (end_mod not in ["#", "b", ""]):
    print("\nModificador inválido")
    sys.exit(1)

print(f"\n{start} {start_mod}  --  {end} {end_mod}")

start_mod = { "#": 0.5, "b": 0.5, "": 0 }[start_mod]
end_mod = { "#": 0.5, "b": 0.5, "": 0 }[end_mod]

print()

diff = notes.index(end) - notes.index(start) + 1
print(f"Intervalo: {diff}")

count = tones[diff] + start_mod + end_mod
print(f"Tonos: {count}")
