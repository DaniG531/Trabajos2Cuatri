import random
Oraciones = []
NuevasOraciones = []
Pronombres = set()
SujetosEl = set()
SujetosLa = set() 
SujetosLos = set() 
SujetosLas = set() 
Verbos = set()
Predicados = set()

while True:
    print("")
    while True:
        print("Escribe una oración con estructura _Pronombre-Sujeto-Verbo-Predicado_:")
        Oracion = input()
        ListaOracion = Oracion.split(" ", 3)
        last_chars2char = ListaOracion[1][-2:]
        last_chars1char = ListaOracion[1][-1]
        if ListaOracion[0] != "El" and ListaOracion[0] != "La" and ListaOracion[0] != "Los" and ListaOracion[0] != "Las":
            print("Pronombres Invalidos. Intentalo de nuevo.")
            continue
        if last_chars2char != "as" and last_chars2char != "os" and last_chars1char != "a" and last_chars1char != "o":
            print("Sujeto Invalido. Intentalo de nuevo.")
            continue
            
        Oraciones.append(Oracion)
        Pronombres.add(ListaOracion[0])
        if last_chars1char == "o":
            SujetosEl.add(ListaOracion[1])
        if last_chars1char == "a":
            SujetosLa.add(ListaOracion[1])
        if last_chars2char == "os":
            SujetosLos.add(ListaOracion[1])
        if last_chars2char == "as":
            SujetosLas.add(ListaOracion[1])
        Verbos.add(ListaOracion[2])
        Predicados.add(ListaOracion[3])
        print("")
        print("Quieres escribir otra oracion?")
        R = input("")
        if R == "no" or R == "NO" or R == "No" or R == "N" or R == "n":
            break
    
    while True:
        print("===============================")
        print("")
        TempNewSentence = []
        TempNewSentence.append(random.choice(list(Pronombres)))
        last_chars2char = TempNewSentence[0][len(TempNewSentence[0])-2:]
        last_chars1char = TempNewSentence[0][len(TempNewSentence[0])-1]
        TempNewSentence.append(str(" "))
        if last_chars1char == "o":
            TempNewSentence.append(random.choice(list(SujetosEl)))
        if last_chars1char == "a":
            TempNewSentence.append(random.choice(list(SujetosLa)))
        if last_chars2char == "os":
            TempNewSentence.append(random.choice(list(SujetosLos)))
        if last_chars2char == "as":
            TempNewSentence.append(random.choice(list(SujetosLas)))
        TempNewSentence.append(str(" "))
        TempNewSentence.append(random.choice(list(Verbos)))
        TempNewSentence.append(str(" "))
        TempNewSentence.append(random.choice(list(Predicados)))
        for i in TempNewSentence:
            print(i, end= "")
        print("")
        print("")
        print("Quieres Generar otra oracion?")
        NuevasOraciones.append(TempNewSentence)
        R = input("")
        if R == "no" or R == "NO" or R == "No" or R == "N" or R == "n":
            break
    print("===============================")
    print("¿Quieres Salir?")
    NuevasOraciones.append(TempNewSentence)
    R = input("")
    if R == "si" or R == "SI" or R == "Si" or R == "S" or R == "s":
        break