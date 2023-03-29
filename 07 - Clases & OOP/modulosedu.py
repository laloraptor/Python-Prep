class Funmod6:  
    def __init__(self, lisentrada):
       self.lisentrada=lisentrada 
    
    def _esprimo(self):
        for n in self.lisentrada:
            if self.es_primo(n)==True:
                   print (f"El número {n} es primo")
            else:
                 print(f"El número {n} no es primo")
    def _convertirtemp(self, escalainicial, escalafinal):
         for n in self.lisentrada:
              print(f"{n} grados {escalainicial}, equivalen a {self.convertirtem(n,escalainicial,escalafinal)} en grados {escalafinal} ")
            
    def _factorial(self):
         for n in self.lisentrada:
              print(f"El factorial de {n} es: {self.factorial(n)}")

    def es_primo(self, numero):
        primo=True
        for n in range (2,numero):
            if numero%n==0:
                primo=False
                break
        return primo

    def modas(self, mayor=True):
        import random
        listaunicos=[]
        pares=[]
        repeticiones=[]
        varmodas=False
        modasrepeti=[]
        for n in self.lisentrada:
            if n not in listaunicos:
                listaunicos.append(n)
        for a in listaunicos:
            apariciones=self.lisentrada.count(a)
            pares.append((a,apariciones)) #puedes añadir los pares sin necesidad de iterarlos en listas
            #print (f"El número {a} se repite {apariciones} veces")
            repeticiones.append(self.lisentrada.count(a))
        if mayor==True:
            paresdesc = sorted(pares, key=lambda x: x[1], reverse=True)
            #print(repeticiones)
            repeticiones=sorted(repeticiones,reverse=True )
            #print(repeticiones)
            #print(paresdesc)
            valmax=repeticiones[0]
        elif mayor==False:
            paresdesc = sorted(pares, key=lambda x: x[1], reverse=False)
            #print(repeticiones)
            repeticiones=sorted(repeticiones,reverse=False )
            #print(repeticiones)
            #print(paresdesc)
            valmax=repeticiones[0]

        for n in range (1, len(repeticiones)):
                if repeticiones[n]==valmax:
                        varmodas=True
        if varmodas==True:
            return f"La lista tiene varias modas. Te devolveremos cualquier valor: {random.choice(repeticiones)}"
        elif varmodas==False and mayor==True:
                for i in paresdesc:
                        numeromasrep=i[0]
                        break
                #return [numeromasrep,valmax] #este es el que sería operativo para usar la función después
                return f"El valor que más se repite es el {numeromasrep} y lo hace {valmax} veces" #Este es el que serviría para un programa
        elif varmodas==False and mayor==False:
                for i in paresdesc:
                        numeromasrep=i[0]
                        break
                #return [numeromasrep,valmax] #este es el que sería operativo para usar la función después
                return f"El valor que menos se repite (y que es menor que todos los demás números) es el {numeromasrep} y lo hace {valmax} veces" #Este es el que serviría para un programa

    def convertirtem(self, valor,escalainicial,escalafinal):
        if escalainicial=="celsius" and escalafinal=="celsius":
            return valor
        if escalainicial=="celsius" and escalafinal=="farenheit":
            return valor*9/5+32
        elif escalainicial=="celsius" and escalafinal=="kelvin":
            return valor+273.15
        elif escalainicial=="farenheit" and escalafinal=="farenheit":
            return valor
        elif escalainicial=="farenheit" and escalafinal=="celsius":
            return (valor-32)/(9/5)
        elif escalainicial=="farenheit" and escalafinal=="kelvin":
            return ((valor-32)/(9/5))+273.15
        elif escalainicial=="kelvin" and escalafinal=="kelvin":
            return valor
        elif escalainicial=="kelvin" and escalafinal=="celsius":
            return valor-273.15
        elif escalainicial=="kelvin" and escalafinal=="farenheit":
            return ((valor-273.15)*(9/5))+32
    def factorial(self,numero):
        if (type(numero) != int):
            return "Error. El numero debe ser un entero."
        if(numero < 0):
            return "Error. El numero debe ser positivo"
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero