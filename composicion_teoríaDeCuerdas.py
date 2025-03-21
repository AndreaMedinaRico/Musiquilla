from music21 import *

# -------- FUNCIONES AUXILIARES --------
def agregar_notas_melodia(melodia, notas):
    """Agrega las notas de la melodía a la parte correspondiente."""
    for nota, duracion in notas:
        melodia.append(note.Note(nota, quarterLength = duracion))

def agregar_acordes_armonia(armonia, acordes):
    """Agrega los acordes a la parte correspondiente."""
    for acorde in acordes:
        acorde_obj = chord.Chord(acorde, quarterLength = 2)
        armonia.append(acorde_obj)

def agregar_notas_armonia(armonia, notas):
    """Agrega las notas de la armonía a la parte correspondiente."""
    for nota in notas:
        armonia.append(note.Note(nota, quarterLength = 0.25))

def agregar_notas_bajo(bajo, notas):
    """Agrega las notas del bajo a la parte correspondiente."""
    for nota in notas:
        bajo.append(note.Note(nota, quarterLength = 1))

def agregar_acordes_bajo(bajo, acordes):
    """Agrega los acordes al bajo."""
    for acorde in acordes:
        acorde_obj = chord.Chord(acorde, quarterLength = 4)
        bajo.append(acorde_obj)



# Declaración de pentagramas y partitura
partitura = stream.Stream()
melodia = stream.Part()
armonia = stream.Part()
bajo = stream.Part()
soprano = stream.Part()

# Armadura de cada pentagrama
melodia.append(key.Key("D", "minor"))
armonia.append(key.Key("D", "minor"))
bajo.append(key.Key("D", "minor"))
soprano.append(key.Key("D", "minor"))

# Instrumentos de cada pentagrama
melodia.append(instrument.Violin())
armonia.append(instrument.Organ())
bajo.append(instrument.Bass())
soprano.append(instrument.Soprano())


# -------- COMPOSICIÓN --------
# PARTE UNO
notas_melodia_uno = [
    ("E4", 0.5), ("F4", 0.5), ("A4", 1), ("G4", 1),
    ("E4", 0.5), ("F4", 0.5), ("D4", 0.5), ("E4", 0.5),
    ("G4", 1), ("F4", 1), ("D4", 0.5), ("E4", 0.5),
    ("C#4", 0.5), ("D4", 0.5), ("F4", 1), ("E4", 1),
    ("C#4", 0.5), ("D4", 0.5), ("B4", 0.5), ("C#4", 0.5),
    ("E4", 1), ("D4", 1), ("B4", 1) 
]

acordes_armonia_uno = [
    ["D4", "F4", "A4"], ["A4", "C#4", "E4"], ["B-4", "D4", "F4"], ["F4", "A4", "C4"],
    ["C4", "E4", "G4"], ["G4", "B4", "D4"], ["B-4", "D4", "F4"], ["A4", "C#4", "E4"]
]

notas_bajo_uno = [
    "D2", "D2", "A2", "D2", "C2", "C2", "G2", "C2",
    "B-2", "B-2", "F2", "B-2", "A2", "A2", "E2", "A2"
]

for i in range(0, 2):
    agregar_notas_melodia(melodia, notas_melodia_uno)
    agregar_acordes_armonia(armonia, acordes_armonia_uno)
    agregar_notas_bajo(bajo, notas_bajo_uno)


# PARTE DOS
notas_bajo_dos = [
    ["D2", "F2", "A2"],
    ["B-2", "D2", "F2"],
    ["F2", "C2", "F2"],
    ["C2", "E2", "G2"],
    ["G2", "B2", "D2"],
    ["D2", "F2", "A2"],
    ["A2", "C#2", "E2"],
    ["D2", "F2", "A2"]
]

notas_melodia_dos = [
    ("A4", 0.5), ("C4", 0.25), ("B-4", 0.25), ("A4", 0.25),
    ("G4", 0.5), ("B-4", 0.25), ("A4", 0.25), ("G4", 0.25),
    ("F4", 0.5), ("A4", 0.25), ("G4", 0.25), ("F4", 0.25),
    ("E4", 0.5), ("G4", 0.25), ("A4", 0.25), ("A4", 0.25),
    ("B-4", 0.5), ("D4", 0.25), ("C4", 0.25), ("B-4", 0.25),
    ("A4", 0.5), ("C4", 0.25), ("B-4", 0.25), ("A4", 0.25),
    ("G4", 0.5), ("B-4", 0.25), ("A4", 0.25), ("G4", 0.25),
    ("F4", 0.5), ("A4", 0.25), ("A4", 0.5), ("C4", 0.25),
    ("B-4", 0.25), ("A4", 0.25), ("G4", 0.5), ("B-4", 0.25),
    ("A4", 0.25), ("G4", 0.25), ("F4", 0.5), ("A4", 0.25),
    ("G4", 0.25), ("F4", 0.25), ("E4", 0.5), ("G4", 0.25),
    ("A4", 0.25), ("A4", 0.25), ("B-4", 0.5), ("D4", 0.25),
    ("C4", 0.25), ("B-4", 0.25), ("A4", 0.5), ("C4", 0.25),
    ("B-4", 0.25), ("A4", 0.25), ("G4", 0.5), ("B-4", 0.25),
    ("A4", 0.25), ("G4", 0.25), ("F4", 0.5), ("A4", 0.25),
    ("A4", 0.5), ("C4", 0.25), ("B-4", 0.25), ("A4", 0.25),
    ("G4", 0.5), ("B-4", 0.25), ("A4", 0.25), ("G4", 0.25),
    ("F4", 0.5), ("A4", 0.25), ("G4", 0.25), ("F4", 0.25),
    ("E4", 0.5), ("G4", 0.25), ("A4", 0.25), ("A4", 0.25),
    ("B-4", 0.5), ("D4", 0.25), ("C4", 0.25), ("B-4", 0.25),
    ("A4", 0.5), ("C4", 0.25), ("B-4", 0.25), ("A4", 0.25),
    ("G4", 0.5), ("B-4", 0.25), ("A4", 0.25), ("G4", 0.25),
    ("F4", 0.5), ("A4", 0.25), ("D4", 3)
]

notas_armonia_dos = [
    "D4", "F4", "A4", "D4",
    "B-4", "D4", "F4", "B-4",
    "F4", "A4", "C4", "F4",
    "C4", "E4", "G4", "C4",
    "G4", "B-4", "D4", "G4",
    "D4", "F4", "A4", "D4",
    "A4", "C#4", "E4", "A4",
    "D4", "F4", "A4", "D4",
    "D4", "F4", "A4", "D4",
    "B-4", "D4", "F4", "B-4",
    "F4", "A4", "C4", "F4",
    "C4", "E4", "G4", "C4",
    "G4", "B-4", "D4", "G4",
    "D4", "F4", "A4", "D4",
    "A4", "C#4", "E4", "A4",
    "D4", "F4", "A4", "D4"
]

acordes_soprano = [
    ["A4", "C#4", "E4", "G4"], 
    ["B3", "F3", "A3"]
]

for i in range(0, 16):
    soprano.append(note.Rest(quarterLength=4))

agregar_notas_armonia(armonia, notas_armonia_dos)
agregar_notas_melodia(melodia, notas_melodia_dos)
agregar_acordes_bajo(bajo, notas_bajo_dos)
bajo.append(note.Rest(quarterLength=4))
bajo.append(chord.Chord(["B2", "F2", "A2"], quarterLength=2))
soprano.append(chord.Chord(acordes_soprano[0], quarterLength=4))

# Volumen
dyn = dynamics.Dynamic('p')  # 'p' = piano (suave)
armonia.insert(0, dyn)

# Unión para formar la partitura
partitura.insert(0, melodia)
partitura.insert(0, armonia)
partitura.insert(0, bajo)
partitura.insert(0, soprano)

partitura.show()