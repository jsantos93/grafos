import java.util.List;
import java.util.ArrayList;

public class Graph {

    List<Node> vertices;
    List<Edge> arestas;

    public Graph() {
        vertices = new ArrayList<Node>();
        arestas = new ArrayList<Edge>();
    }

    Node addNode(String nome) {
        Node v = new Node(nome);
        vertices.add(v);
        return v;
    }

    Edge addEdge(Node origem, Node destino) {
        Edge e = new Edge(origem, destino);
        origem.addAdj(e);
        arestas.add(e);
        return e;
    }

    public String toString() {
        String r = "";
        for (Node u : vertices) {
            r += u.nome + " -> ";
            for (Edge e : u.adj) {
                Node v = e.destino;
                r += v.nome + ", ";
            }
            r += "\n";
        }
        return r;
    }

    public static void main(String[] args) {
        Graph g = new Graph();
        Node s = g.addNode("s");
        Node t = g.addNode("t");
        Node y = g.addNode("y");
        Edge st = g.addEdge(s, t);
        Edge sy = g.addEdge(s, y);
        Edge ty = g.addEdge(t, y);
        Edge yt = g.addEdge(y, t);
        System.out.println(g);
    }
}