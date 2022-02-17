from operator import truediv
import random
Oraciones = []
NuevasOraciones = []
Pronombres = set()
Sujetos = set()
Verbos = set()
Predicados = set()

class Pronombre:
    def __init__(self, valor):
        self.Masculino = False   # False = Femenino
        self.Plural = False      # False = Singular
        self.Valid = False       # Pronombre invalido
        self.Text = valor
        if valor == "El" or valor == "La" or valor == "Los" or valor == "Las":
            self.Valid = True
        if valor == "El" or valor == "Los":
            self.Masculino = True
        if valor == "Las" or valor == "Los":
            self.Plural = True
        
class Sujeto:
    def __init__(self, valor):
        self.Masculino = False   # False = Femenino
        self.Plural = False      # False = Singular
        self.Valid = False       # Pronombre invalido
        self.Text = valor
        last_chars2char = valor[len(valor)-2:]
        last_chars1char = valor[len(valor)-1]
        if last_chars2char == "as" or last_chars2char == "os" or last_chars1char == "a" or last_chars1char == "o":
            self.Valid = True
        if valor == "o" or valor == "os":
            self.Masculino = True
        if valor == "as" or valor == "os":
            self.Plural = True


class Verbo:
    def __init__(self, valor):
        self.Text = valor
        self.Valid = False       # Pronombre invalido
        if len(valor) >= 2:
            self.Valid = True

class Predicado:
    def __init__(self, valor):
        self.Text = valor
        self.Valid = False       # Pronombre invalido
        if len(valor) >= 2:
            self.Valid = True


class Oracion:
    def __init__(self, Pronombre, Sujeto, Verbo, Predicado):
        self.Valid = True
        if Pronombre.Masculino != Sujeto.Masculino or Pronombre.Plural != Sujeto.Plural:
            self.Valid = False
        

class Manager:
    def __init__():

    def Generador()

    def ObtenerSujeto(Masculino,Plural):
        W = []
        for i in Sujetos:
            if i.Masculino == Masculino and i.Plural == Plural:
                W.append(i)
        return W



    # random.choice(Manage.obtsujet())

while True:
    print("")
    while True:
        print("Escribe una oración con estructura _Pronombre_Sujeto_Verbo_Predicado_:")
        Oracion = input()
        ListaOracion = Oracion.split(" ", 3)
        PalabraP = Pronombre(str(ListaOracion[0]))
        PalabraS = Pronombre(str(ListaOracion[1]))
        PalabraV = Pronombre(str(ListaOracion[2]))
        PalabraP = Pronombre(str(ListaOracion[3]))
        last_chars2char = ListaOracion[1][-2:]
        last_chars1char = ListaOracion[1][-1]
        if PalabraP.Valid == False:
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
        last_chars2char = TempNewSentence[0][-2:]
        last_chars1char = TempNewSentence[0][-1]
        TempNewSentence.append(str(" "))

        if pronombre.masculino == true


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