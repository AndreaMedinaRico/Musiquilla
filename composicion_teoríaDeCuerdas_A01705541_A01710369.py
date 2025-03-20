from music21 import *

pentragrama = stream.Stream()
#poner en el pentragrama con la armura de re menor


melodia = stream.Part()
armonia = stream.Part()
bajo = stream.Part()

#Agregar armadura a las partes
melodia.append(key.Key("D", "minor"))
armonia.append(key.Key("D", "minor"))
bajo.append(key.Key("D", "minor"))

#Agregar instrumentos a las partes
melodia.append(instrument.Violin())
armonia.append(instrument.Organ())
bajo.append(instrument.Bass())

notas = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

D_minor = chord.Chord(["D4", "F4", "A4"])
C_major = chord.Chord(["C4", "E4", "G4"])
B_b_major = chord.Chord(["B-4", "D4", "F4"])
A_major = chord.Chord(["A4", "C#4", "E4"])
G_major = chord.Chord(["G4", "B4", "D4"])


#Primera parte
for i in range(0,2):
    #Parte de bajos
    #| D - D - A - D | C - C - G - C | Bb - Bb - F - Bb | A - A - E - A |
    bajo.append(note.Note("D2"))
    bajo.append(note.Note("D2"))
    bajo.append(note.Note("A2"))
    bajo.append(note.Note("D2"))
    bajo.append(note.Note("C2"))
    bajo.append(note.Note("C2"))
    bajo.append(note.Note("G2"))
    bajo.append(note.Note("C2"))
    bajo.append(note.Note("B-2"))
    bajo.append(note.Note("B-2"))
    bajo.append(note.Note("F2"))
    bajo.append(note.Note("B-2"))
    bajo.append(note.Note("A2"))
    bajo.append(note.Note("A2"))
    bajo.append(note.Note("E2"))
    bajo.append(note.Note("A2"))

    #Parte de la melodia
    #| (E→)F - A - G - (E→)F | (D→)E - G - F - (D→)E | (C#→)D - F - E - (C#→)D | (B→)C# - E - D - (B→)C# |
    melodia.append(note.Note("E4", quarterLength=0.5))
    melodia.append(note.Note("F4", quarterLength=0.5))
    melodia.append(note.Note("A4", quarterLength=1))
    melodia.append(note.Note("G4", quarterLength=1))
    melodia.append(note.Note("E4", quarterLength=0.5))
    melodia.append(note.Note("F4", quarterLength=0.5))
    melodia.append(note.Note("D4", quarterLength=0.5))
    melodia.append(note.Note("E4", quarterLength=0.5))
    melodia.append(note.Note("G4", quarterLength=1))
    melodia.append(note.Note("F4", quarterLength=1))
    melodia.append(note.Note("D4", quarterLength=0.5))
    melodia.append(note.Note("E4", quarterLength=0.5))
    melodia.append(note.Note("C#4", quarterLength=0.5))
    melodia.append(note.Note("D4", quarterLength=0.5))
    melodia.append(note.Note("F4", quarterLength=1))
    melodia.append(note.Note("E4", quarterLength=1))
    melodia.append(note.Note("C#4", quarterLength=0.5))
    melodia.append(note.Note("D4", quarterLength=0.5))
    melodia.append(note.Note("B4", quarterLength=0.5))
    melodia.append(note.Note("C#4", quarterLength=0.5))
    melodia.append(note.Note("E4", quarterLength=1))
    melodia.append(note.Note("D4", quarterLength=1))
    melodia.append(note.Note("B4", quarterLength=1))

    #Parte de la armonia
    #Acordes: | Dm - A - Bb - F | C - G - Bb - A |
    armonia.append(chord.Chord(["D4", "F4", "A4"], quarterLength=2))
    armonia.append(chord.Chord(["A4", "C#4", "E4"], quarterLength=2))
    armonia.append(chord.Chord(["B-4", "D4", "F4"], quarterLength=2))
    armonia.append(chord.Chord(["F4", "A4", "C4"], quarterLength=2))
    armonia.append(chord.Chord(["C4", "E4", "G4"], quarterLength=2))
    armonia.append(chord.Chord(["G4", "B4", "D4"], quarterLength=2))
    armonia.append(chord.Chord(["B-4", "D4", "F4"], quarterLength=2))
    armonia.append(chord.Chord(["A4", "C#4", "E4"], quarterLength=2))


#Segunda parte

#Parte de bajos
#| 4D(D-F-A-D) | 4Bb(Bb-D-F-Bb) |
#| 4F(F-C-F-A) | 4C(C-E-G-C) |
#| 4G(G-Bb-D-G) | 4D(D-F-A-D) |
#| 4A(A-C#-E-A) | 4D(D-F-A-D) |

bajo.append(chord.Chord(["D2", "F2", "A2", "D2"], quarterLength=4))
bajo.append(chord.Chord(["B-2", "D2", "F2", "B-2"], quarterLength=4))
bajo.append(chord.Chord(["F2", "C2", "F2", "A2"], quarterLength=4))
bajo.append(chord.Chord(["C2", "E2", "G2", "C2"], quarterLength=4))
bajo.append(chord.Chord(["G2", "B2", "D2", "G2"], quarterLength=4))
bajo.append(chord.Chord(["D2", "F2", "A2", "D2"], quarterLength=4))
bajo.append(chord.Chord(["A2", "C#2", "E2", "A2"], quarterLength=4))
bajo.append(chord.Chord(["D2", "F2", "A2", "D2"], quarterLength=8))


#Parte de la melodia
#| A/2 - C/4 - Bb/4 - A/4 | G/2 - Bb/4 - A/4 - G/4 | F/2 - A/4 - G/4 - F/4 | E/2 - G/4 - A/4 - A/4 |
#| Bb/2 - D/4 - C/4 - Bb/4 | A/2 - C/4 - Bb/4 - A/4 | G/2 - Bb/4 - A/4 - G/4 | F/2 - A/4 - G/4 - F/4 |

melodia.append(note.Note("A4", quarterLength=0.5))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.5))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.5))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.25))
melodia.append(note.Note("E4", quarterLength=0.5))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.5))
melodia.append(note.Note("D4", quarterLength=0.25))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.5))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.5))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.5))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.5))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.5))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.5))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.25))
melodia.append(note.Note("E4", quarterLength=0.5))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.5))
melodia.append(note.Note("D4", quarterLength=0.25))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.5))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.5))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.5))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.5))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.5))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.5))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.25))
melodia.append(note.Note("E4", quarterLength=0.5))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.5))
melodia.append(note.Note("D4", quarterLength=0.25))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.5))
melodia.append(note.Note("C4", quarterLength=0.25))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.5))
melodia.append(note.Note("B-4", quarterLength=0.25))
melodia.append(note.Note("A4", quarterLength=0.25))
melodia.append(note.Note("G4", quarterLength=0.25))
melodia.append(note.Note("F4", quarterLength=0.5))
melodia.append(note.Note("A4", quarterLength=0.25))

#Parte de la armonia
#| D/4 - F/4 - A/4 - D/4 | Bb/4 - D/4 - F/4 - Bb/4 | F/4 - A/4 - C/4 - F/4 | C/4 - E/4 - G/4 - C/4 |
#| G/4 - Bb/4 - D/4 - G/4 | D/4 - F/4 - A/4 - D/4 | A/4 - C#/4 - E/4 - A/4 | D/4 - F/4 - A/4 - D/4 |

armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("B-4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("B-4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("C4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("C4", quarterLength=0.25))
armonia.append(note.Note("E4", quarterLength=0.25))
armonia.append(note.Note("G4", quarterLength=0.25))
armonia.append(note.Note("C4", quarterLength=0.25))
armonia.append(note.Note("G4", quarterLength=0.25))
armonia.append(note.Note("B-4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("G4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("C#4", quarterLength=0.25))
armonia.append(note.Note("E4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("B-4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("B-4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("C4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("C4", quarterLength=0.25))
armonia.append(note.Note("E4", quarterLength=0.25))
armonia.append(note.Note("G4", quarterLength=0.25))
armonia.append(note.Note("C4", quarterLength=0.25))
armonia.append(note.Note("G4", quarterLength=0.25))
armonia.append(note.Note("B-4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("G4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("C#4", quarterLength=0.25))
armonia.append(note.Note("E4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))
armonia.append(note.Note("F4", quarterLength=0.25))
armonia.append(note.Note("A4", quarterLength=0.25))
armonia.append(note.Note("D4", quarterLength=0.25))

#Agregar bateria en semicorcheas
bateria = stream.Part()
bateria.append(key.Key("D", "minor"))

for i in range(0, 8):
    bateria.append(note.Rest(quarterLength=4))


#Agregar bateria al pentragrama en el compas 9 (despues de la primera parte)
pentragrama.insert(9, bateria)

#Tercera parte




#Corregir volumen
dyn = dynamics.Dynamic('p')  # 'p' = piano (suave)
armonia.insert(0, dyn)

#Agregar melodia, armonia y bajo a pentragrama
pentragrama.insert(0, melodia)
pentragrama.insert(0, armonia)
pentragrama.insert(0, bajo)

pentragrama.show()
pentragrama.write("midi", "pentagrama.mid")