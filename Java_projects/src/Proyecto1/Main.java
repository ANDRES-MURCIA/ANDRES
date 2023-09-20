import java.util.*;

class Vertice {
    private String clave;
    private Map<Vertice, Integer> conexiones;

    public Vertice(String clave) {
        this.clave = clave;
        this.conexiones = new HashMap<>();
    }

    public void agregarArista(Vertice destino, int ponderacion) {
        conexiones.put(destino, ponderacion);
    }

    public Set<Vertice> obtenerConexiones() {
        return conexiones.keySet();
    }

    public int obtenerPonderacion(Vertice destino) {
        return conexiones.getOrDefault(destino, 0);
    }

    public String obtenerClave() {
        return clave;
    }
}

class Grafo {
    private Map<String, Vertice> vertices;

    public Grafo() {
        vertices = new HashMap<>();
    }

    public void agregarVertice(String clave) {
        if (!vertices.containsKey(clave)) {
            Vertice nuevoVertice = new Vertice(clave);
            vertices.put(clave, nuevoVertice);
        }
    }

    public void agregarArista(String deVertice, String aVertice) {
        agregarArista(deVertice, aVertice, 0);
    }

    public void agregarArista(String deVertice, String aVertice, int ponderacion) {
        if (vertices.containsKey(deVertice) && vertices.containsKey(aVertice)) {
            Vertice origen = vertices.get(deVertice);
            Vertice destino = vertices.get(aVertice);
            origen.agregarArista(destino, ponderacion);
        }
    }

    public Vertice obtenerVertice(String claveVert) {
        return vertices.get(claveVert);
    }

    public List<String> obtenerVertices() {
        return new ArrayList<>(vertices.keySet());
    }

    public boolean contieneVertice(String claveVert) {
        return vertices.containsKey(claveVert);
    }
}
public class Main{
    public static void main(String[] args) {
        Grafo grafo = new Grafo();

        grafo.agregarVertice("A");
        grafo.agregarVertice("B");
        grafo.agregarVertice("C");

        grafo.agregarArista("A", "B", 1);
        grafo.agregarArista("B", "C", 2);
        grafo.agregarArista("A", "C", 3);

        System.out.println("Vertices en el grafo: " + grafo.obtenerVertices());

        System.out.println("Aristas de A: " + grafo.obtenerVertice("A").obtenerConexiones());
        System.out.println("Aristas de B: " + grafo.obtenerVertice("B").obtenerConexiones());
        System.out.println("Aristas de C: " + grafo.obtenerVertice("C").obtenerConexiones());
    }
}