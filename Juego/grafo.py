class Vertice:
    def __init__(self, clave):
        self.clave = clave
        self.conexiones = {}  # Un diccionario para mantener las aristas y sus ponderaciones

    def agregarArista(self, destino, ponderacion=0):
        self.conexiones[destino] = ponderacion

    def obtenerConexiones(self):
        return self.conexiones.keys()

    def obtenerPonderacion(self, destino):
        return self.conexiones[destino]


class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, clave):
        nuevo_vertice = Vertice(clave)
        self.vertices[clave] = nuevo_vertice
        return nuevo_vertice

    def agregarArista(self, deVertice, aVertice, ponderacion=0):
        if deVertice not in self.vertices:
            self.agregarVertice(deVertice)
        if aVertice not in self.vertices:
            self.agregarVertice(aVertice)
        self.vertices[deVertice].agregarArista(aVertice, ponderacion)

    def obtenerVertice(self, claveVert):
        if claveVert in self.vertices:
            return self.vertices[claveVert]
        else:
            return None

    def obtenerVertices(self):
        return list(self.vertices.keys())

    def __contains__(self, vertice):
        return vertice in self.vertices


# Ejemplo de uso:
grafo = Grafo()

grafo.agregarVertice("A")
grafo.agregarVertice("B")
grafo.agregarVertice("C")

grafo.agregarArista("A", "B", 1)
grafo.agregarArista("B", "C", 2)
grafo.agregarArista("A", "C", 3)

print("Vertices en el grafo:", grafo.obtenerVertices())

print("Aristas de A:", list(grafo.obtenerVertice("A").obtenerConexiones()))
print("Aristas de B:", list(grafo.obtenerVertice("B").obtenerConexiones()))
print("Aristas de C:", list(grafo.obtenerVertice("C").obtenerConexiones()))
