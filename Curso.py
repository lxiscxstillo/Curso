class Curso:
    def __init__(self):
        self.__notas = [3, 4, 1, 2, 0, 0, 1, 2, 5, 4, 3, 4.2]

    def calcularPromedio(self):
        # sum(self.__notas) / len(self.__notas) 
        suma = self.__notas[0] + self.__notas[1] + self.__notas[2] + self.__notas[3] + self.__notas[4] + self.__notas[5] + self.__notas[6] + self.__notas[8] + self.__notas[9] + self.__notas[10] + self.__notas[11] + self.__notas[7]
        return suma / 12

    def calcularPromedio2(self):
        promedio = 0
        indice = 0

        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1
        promedio +=self.__notas[indice]
        indice+=1

        return promedio / indice
    
    def CalcularPromedio3(self):
        promedio = 0
        indice = 0

        while indice < 12:
            promedio+=self.__notas[indice]
            indice+=1

        return promedio/indice 
    
    def calcularCantidadAprobados(self):
        aprobados = 0
        indice = 0
        while indice < 12:
            if self.__notas[indice] >= 3.0 and self.__notas[indice] < 5.0:
                aprobados += 1
            indice += 1
        return aprobados
    
    def calcularCantidadDeAprobados2(self):
        aprobados = 0

        for indice in range(12):
            if self.__notas[indice] >= 3.0 and self.__notas[indice] < 5.0:
                aprobados += 1
        return aprobados
    
    def calcularCantidadAprobados3(self):
        aprobados = 0
        for nota in self.__notas:
            if nota>= 3.0 and nota< 5.0:
                aprobados += 1
        return aprobados
    
    def calcularMayorNota(self):
        notasMasAlta = self.__notas[0]
        for nota in self.__notas:
            if nota > notasMasAlta:
                notasMasAlta = nota
        return notasMasAlta

    def hacerCurva(self):
        incremento = 0

        for i in self.__notas:
            incremento = self.notas * 0.05
            if i + incremento < 5.0:
                i += incremento

    def cambiarNotas(self):
        for nota in self.__notas:
            if nota > 4.0:
                nota = nota - 0.5
            elif nota < 2.0:
                nota = nota + 0.5
        else:
            return nota
        
    def darMenorNota(self):
        notasMasBaja = self.__notas[0]
        for nota in self.__notas:
            if nota < notasMasBaja:
                notasMasBaja = nota
        return notasMasBaja
    
    def darRangoConMasNotas(self):
        rango1 = [0.0, 1.99]
        rango2 = [2.0, 3.49]
        rango3 = [3.5, 5.0]
        for i in range(0, 12):
            if rango1[0] <= i <= rango1[1]:
                return "pertenece a rango 1"
            elif rango2[0] <= i <= rango2[1]:
                return "pertenece a rango 2"
            elif rango3[0] <= i <= rango3[1]:
                return "pertenece a rango 3"
        return "no pertenece a ningun rango"
    
    def HayAlgunCinco(self):
        existe=False
        contador=0

        while contador<len(self.__notas) and not existe:
            if self.__notas[contador] == 5:
                existe = True
            contador +=1
        return existe
    
    def HayAlgunCinco2(self):
        existe = False
        
        for i in range(len(self.__notas)):
            if self.__notas[i] ==5:
                existe = True
                break
        return existe
    
    def HayAlgunCinco3(self):
        existe = False

        for nota in self.__notas:
            if nota == 5:
                existe = True
                break
        return existe
    # encontrar la 3 primeras notas de 1.5 y asignarles 2.5
    #retornar la pocision en la secuencia de la tercera nota con valor 5 si dicha nota no aparece al manos tres veces el metodo debe retornar el valor de -1
    
    def EncontrarNotasyAsignar(self):
        contador = 0

        for i in range(len(self.__notas)):
            if self.__notas[i] == 1.5:
                self.__notas[i] = 2.5
                contador += 1
            if contador == 3:
                break
    
    def EncontrarTerceraNota(self):
        contador = 0

        for i in range(len(self.__notas)):
            if self.__notas[i] == 5.0:
                contador += 1
                if contador == 3:
                    return i
                else:
                    return -1
                
    def ReemplazarNotas(self):

        for i in self.__notas:
            if i <= 3.0:
                self.__notas[i] = 0.0
            else:
                break

    def CalcularNumeroMinimo(self):
        suma = 0
        contador = 0

        for nota in range(len(self.__notas)):
            suma += self.__notas[nota]
            contador += 1
            if suma > 30:
                return contador
            else:
                return -1
            
    def darNotaMasRecurrente(self):
        notaMasRecurrente = 0
        cantidadOcurrencias = 0

        for nota in self.__notas:
            contador=0
            for nota2 in self.__notas:
                if nota == nota2:
                    contador += 1
            if contador > cantidadOcurrencias:
                notaMasRecurrente=nota
                cantidadOcurrencias=contador

        return notaMasRecurrente


    def calcularNota(self): 
        notaMenosMitad = 0

        for i in range(len(self.__notas)):
            contador = 0
            
            for i2 in range(len(self.__notas)): 
                if self.__notas[i] < self.__notas[i2]: 
                    contador += 1
            if contador == len(self.__notas)/2:
                notaMenosMitad = self.__notas[i]
        return(notaMenosMitad)