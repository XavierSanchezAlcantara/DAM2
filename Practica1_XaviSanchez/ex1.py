class EquacioPrimerGrau:
    

    def __init__(self,eq):
        self.eq = eq
        
        split=eq.split()
        a,self.operacio,b,igual,c=eq.split()
        x=a[:-1]
        z=a[-1]
        try:
            self.aa=float(x)
            self.bb=float(b)
            self.cc=float(c)
        except:
            return "l'equacio conte caracter no calculables: "
        if type(x)==float and x=='x':
            return ("hola")

        print("Part12= "+x)
        print("Part1 = "+a)
        print("Part2 = "+b)
        print("Operador= "+ self.operacio)
        print("Part3 = "+c)
    def calcula(self):    

        if self.operacio=="+":
            resultat=(self.cc-self.bb)/self.aa
            return resultat
        elif self.operacio=="-":
            resultat=(self.cc+self.bb)/self.aa
            return resultat
        else:
            return ("Operador incorrecte!!!!")
        print(resultat)




#extreuPart1asasda2()

#extreuPart1()

##ExtreuPart2()

#ExtreuOperador()

#ExtreuPart3()