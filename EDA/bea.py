
import numpy as np
from colasecuencial import Cola

class GrafoNoDirigido:
    matriz: list
    
    def __init__(self, nodos):
        self.matriz = [[0 for _ in range(nodos)] for _ in range(nodos)]
        """[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]"""
    
    def arista(self, i, j):
        # No dirigido, se conecta en ambos sentidos
        self.matriz[i][j] = 1
        self.matriz[j][i] = 1

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

    def bea(self,s):
        
        d= np.full(5,999)  ## OR d= [999] * 5

        cola = Cola(5)
        d[s] = 0
        cola.insertar(s)
        while not cola.vacia():
            eliminado = cola.eliminar()    
            x = self.adyacentes(eliminado)  
            for i in x:    
                if d[i] == 999: #### 
                    d[i] = d[eliminado] +1
                    cola.insertar(i)
        print(d)

    def adyacentes(self, u):
        arreAux = []
        for i in range(5):
            if self.matriz[u][i] == 1:
                
                arreAux.append(int(i))
        return arreAux
    

if __name__=='__main__':
    grafo=GrafoNoDirigido(5)
    
    grafo.arista(0,1)
    grafo.arista(1,2)
    grafo.arista(3,2)
    grafo.arista(4,3)
    grafo.arista(0,4)
    grafo.arista(3,1)
    grafo.bea(3)
    