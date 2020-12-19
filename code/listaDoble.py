from graphviz import Digraph
import pickle
from otraLista import *
import os
ldArbol = ListaDobledeArboles()
class Nodo:
    def __init__(self, nombreBase):
        self.nombreBase = nombreBase
        self.tablas = None
        #self.ldArbol = None
        self.siguiente = None
        self.anterior = None
        #self.abajo = None
        
class ListaDOBLE:
    def __init__(self):
        self.primero = None
        self.ultimo = None
         
    #Método que verifica si la lista esta vacía
    def listaVacia(self):
        if self.primero is None:
            return True
        else:
            return False

    #Método agregar MÉTODO FUNCIONAL PARA ENVIAR
    def agregarLista(self, nombreBase):
        nuevoNodo = Nodo(nombreBase)
        #if type(str) != int:
        try:
            if type(nombreBase) != int:
                if self.listaVacia() is True:
                    self.primero = nuevoNodo
                    self.ultimo = nuevoNodo
                    return 0
                else:
                    if self.buscarNodo(nombreBase) == 0:
                        if self.primero != None:
                            self.ultimo.siguiente = nuevoNodo
                            nuevoNodo.anterior = self.ultimo
                            self.ultimo = nuevoNodo
                        else:
                            self.primero = nuevoNodo
                            self.ultimo = nuevoNodo
                        return 0
                    elif self.buscarNodo(nombreBase) == 2:
                        return 2
                    else:
                        return 1
            else:
                return 1
        except:
            return 1
        """
        #print("nodo agregado")
        #if self.buscarNodo(str) == 0:
        if self.primero != None:
            self.ultimo.siguiente = nuevoNodo
            nuevoNodo.anterior = self.ultimo
            self.ultimo = nuevoNodo
            #return 0
        else:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
            #return 0
        #elif self.buscarNodo(str) == 2:
            #return 2
        #else:
            #return 1
        if self.listaVacia() is True:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            nuevoNodo.anterior = self.primero
            self.primero.siguiente = nuevoNodo
            self.primero = nuevoNodo  """

    #Método Buscar
    def buscarNodo(self, dato):
        actual = self.primero
        encontrado = False
        if self.primero != None:
            while actual != None and encontrado != True:
                if actual.nombreBase == dato:
                    encontrado = True
                    return 2
                actual = actual.siguiente
            if not encontrado:
                #print("Dato no encontrado")
                return 0
        else:
            #print("lista vacía")     
            return 1     

    #Método Eliminar MÉTODO FUNCIONAL PARA ENVIAR
    def eliminarNodo(self, dato):
        aux = self.primero
        tmp = None
        encontrado = False
        try:
            if self.listaVacia() is True:
                return 1
            else:
                if self.primero != None:
                    while aux != None and encontrado != True:
                        if aux.nombreBase == dato:
                        #print("Dato encontrado: ", aux.str)
                            if aux == self.primero:
                                self.primero = self.primero.siguiente
                                #self.primero.anterior = None
                            elif aux == self.ultimo:
                                tmp.siguiente = None
                                self.ultimo = tmp
                            else:
                                tmp.siguiente = aux.siguiente
                                aux.siguiente.anterior = tmp
                        #print("Nodo eliminado de la lista")
                            encontrado = True
                            return 0
                        tmp = aux
                        aux = aux.siguiente
                #return False
                    if not encontrado:
                    #print("Dato no encontrado")
                        return 2
        except:
            return 1

    #Método Modificar MÉTODO FUNCIONAL PARA ENVIAR
    def modificarNodo(self, nombreActual, nuevoNombre):
        """
        aux = self.buscarNodo(str)
        aux.str = dato
        print(aux.str)#este print solo es de prueba
        return aux"""
        try:
            if self.buscarNodo(nuevoNombre) == 2:
                #print("nuevo ya se encuentra en la lista, return:3")
                return 3
            else:
                actual = self.primero
                encontrado = False
                if self.primero != None:
                    while actual != None and encontrado != True:
                        if actual.nombreActual == nombreActual:
                            encontrado = True
                            actual.nombreActual = nuevoNombre
                            #return actual.str
                            #print("cambio exitoso, return:0")
                            return 0
                        actual = actual.siguiente
                    if not encontrado:
                        #print("Dato no encontrado return:2")
                        return 2
                else:
                    #print("lista vacía, return:1")     
                    return 1
        except:
            return 1
        
    #Método imprimir MÉTODO FUNCIONAL PARA ENVIAR
    def imprimir(self):
        #print("******")
        lista = []
        tmp = self.primero
        while tmp != None:
            lista.append(tmp.nombreBase)
            #print(tmp.str)
            tmp = tmp.siguiente
        #print(lista)
        return lista
    #imprimir alreves SOLO ES DE PRUEBA NO UTILIZADO
    def imprimir1(self):
        print("******")
        tmp = self.ultimo
        while tmp != None:
            print(tmp.nombreBase)
            tmp = tmp.anterior

    #Método Graficar
    def graficar(self, nombre):
        cadena = ""
        cadena2 = ""
        cadena1 = ""
        cadena3 = ""
        cadena4 = ""
        #g = ""
        #f = open('listadoble.dot', 'wb')
        """
        g = g + "Digraph ListaDoble{\n"
        g = g + "node [shape = record, style=\"rounded,filled\"fillcolor=\"orange:red\",width=0.7,height=0.5]\n"
        """
        g = Digraph('g', 
            node_attr={'shape': 'record', 'style':'rounded,filled','fillcolor': 'orange:red'})
        g.attr(rankdir='LR')
        g.format = 'png'
        #aquí va todo el codigo que recorre la lista
        #1er while crea los nodos a graficar
        aux = self.primero
        while aux != None:
            cadena = cadena + aux.nombreBase
            g.node(cadena,cadena)
                #cadena = cadena + "[label={"+ aux.str+"}];\n"
            cadena = ""
            aux = aux.siguiente
        #2do while crea los apuntadores siguientes entre nodos 
        tmp = self.primero
        while tmp.siguiente != None:
            cadena2 = cadena2 + tmp.nombreBase
            cadena1 = cadena1 + tmp.siguiente.nombreBase
            g.edge(cadena2, cadena1)
            cadena1 = ""
            cadena2 = ""
            tmp = tmp.siguiente
        #3er while crea los apuntadores anteriores entre nodos
        tmp = self.ultimo
        while tmp.anterior != None:
            cadena3 = cadena3 + tmp.nombreBase
            cadena4 = cadena4 + tmp.anterior.nombreBase
            g.edge(cadena3, cadena4)
            cadena3 = ""
            cadena4 = ""
            tmp = tmp.anterior
            #print(cadena2, cadena1)
        """
        g.node('A', 'King Arthur')
        g.node('B', 'Sir Bedevere the Wise')
        g.node('L', 'Sir Lancelot the Brave')

        g.edges(['AB', 'AL'])
        g.edge('B', 'L', constraint='false')"""
        #g = g + apuntadores
        #g = g + nodos
        #f.write(g)
        #f.close()
        #print(g)
        #genera el archivo .Dot y una imagen png
        g.render(nombre+'.gv.png', view=True)
        #g.view() metodo de graphviz para generar pdf con la imagen

     
    def GraficarConArchivo(self):
        f = open("listaDoble.dot", "w")
        f.write("digraph g {\n")
        f.write("node [shape = rect, width=1, height=0.4];\n")     
        f.write("rankdir=LR;\n")

        tmp = self.primero
        while tmp.siguiente != None:
            f.write("\""+str(tmp.nombreBase)+"\"->"+"\""+str(tmp.siguiente.nombreBase)+"\";\n")
            tmp = tmp.siguiente
        aux = self.ultimo
        while aux.anterior != None:
            f.write("\""+str(aux.nombreBase)+"\"->"+"\""+str(aux.anterior.nombreBase)+"\";\n")
            aux = aux.anterior
        f.write("}")
        f.close()
        os.system("dot -Tjpg listaDoble.dot -o listaDoble.png")



    #Método que define los nodos NO UTILIZADO
    def definirNodos(self):
        cadena = ""
        cad=""
        if self.primero == None:
            print("lista vacia")
        else:
            aux = self.primero
            while aux != None:
                cadena = cadena + aux.str + "\n"
                #cadena = cadena + "[label={"+ aux.str+"}];\n"
                cad = cadena
                aux = aux.siguiente
            #print(cad)
        return cad

    #Método que define los apuntadores NO UTILIZADO
    def definirApuntadores(self):
        cadena2 = ""
        cadena1 = ""
        if self.primero == None:
            print("lista vacia")
        else:
            tmp = self.primero
            while tmp.siguiente != None:
                cadena2 = cadena2 + tmp.str+ "\n"
                cadena1 = cadena1 + tmp.siguiente.str + "\n"
                tmp = tmp.siguiente
            cadena2 = ""
            cadena1 = ""
            #print(cadena2, cadena1)
            tmp = self.ultimo
            while tmp.anterior != None:
                cadena2 = cadena2 + tmp.str+ "\n"
                cadena1 = cadena1 + tmp.anterior.str + "\n"
                tmp = tmp.anterior
            print(cadena2, cadena1)
            """
            tmp = self.primero
            while tmp.siguiente != None:
                cadena = cadena + tmp.str
                cadena = cadena + "->"
                cadena = cadena + tmp.siguiente.str+";\n"
                cadena = cadena + tmp.siguiente.str
                cadena = cadena + "->"
                cadena = cadena + tmp.str+";\n"
                tmp = tmp.siguiente
            print(cadena)"""
            
        return cadena1

    #Método para crear archivo binario
def commit( objeto, nombre):
    file = open(nombre+".txt","wb+")
    file.write(pickle.dumps(objeto))
    file.close()
    return ""
    #Método para retornar el archivo binario
def rollback( nombre):
    file = open(nombre+".txt", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)
#init
"""
l = ListaDOBLE()
print(l.agregarLista("Base1"))
#print(l.agregarLista("Base1"))
print(l.agregarLista("Base2"))
print(l.eliminarNodo("Base1"))
print(l.eliminarNodo("Base3"))
print(l.eliminarNodo("Base2"))
l.imprimir()
print(l.eliminarNodo("base4"))
"""
"""
t = ListaDOBLE()

s = ListaDOBLE()
agregar lista 1


"""

print(ldArbol.createTable("", "tabla1",4))
ldArbol.verNodos()

"""
l = ListaDOBLE()

l.agregarLista("DB 2")
l.agregarLista("DB 3")
l.agregarLista("DB 4")
l.agregarLista("DB 5")
l.agregarLista("DB 6")
l.agregarLista("DB 7")
l.agregarLista("DB 8")
l.agregarLista("DB 9")
l.agregarLista("DB 10")
l.agregarLista("DB 11")
print(l.imprimir())
#l.GraficarConArchivo()
#l.graficar("lista")

a = commit(l, "pruebaLista") 
c = rollback("pruebaLista")
#print(c)

print(l.imprimir())
print(l.modificarNodo("DB 3", "DB 1"))
print(l.modificarNodo("DB 13", "DB 12"))
print(l.modificarNodo("DB 8", "DB 1"))
print(l.imprimir())

agregar lista 2
t.agregarLista("Tabla 1")
t.agregarLista("Tabla 2")
t.agregarLista("Tabla 3")
t.agregarLista("Tabla 4")
t.agregarLista("Tabla 5")
t.agregarLista("Tabla 6")
t.agregarLista("Tabla 7")
t.agregarLista("Tabla 8")
t.agregarLista("Tabla 9")
t.agregarLista("Tabla 10")
t.agregarLista("Tabla 11")
agregar lista3
s.agregarLista("BaseDatos1")
imprimir

l.imprimir()

print()
t.imprimir()
print()

print(s.buscarNodo("BaseDatos"))
print()

l.eliminarNodo("cadena")

l.eliminarNodo("seis")

if l.eliminarNodo("base 5") is True:
    print("Eliminado")
else:
    print("no encontrado")
imprimir
l.imprimir()
print()
modificar
l.modificarNodo("cadena", "DB1")
l.modificarNodo("base 6", "DB6")
l.modificarNodo("contiene", "DB4")
imprimir
l.imprimir()

l.graficar("Bases de Datos")
t.graficar("Tablas DB")

l.definirApuntadores()
print()
print(l.definirNodos())
l.definirNodos()
"""