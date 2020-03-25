import java.util.List;
import java.util.ArrayList;

public class Graph {
    public class Node {
        String nome;
        List<Edge> adj;

        Node(String nome) {
            this.nome = nome;
            this.adj = new ArrayList<Edge>();
        }

        void addAdj(Edge e) {
            adj.add(e);
        }
    }

    public class Edge {
        Node origem;
        Node destino;

        Edge(Node origem, Node destino) {
            this.origem = origem;
            this.destino = destino;
        }
    }

    List<Node> vertices;
    List<Edge> arestas;

    public Graph() {
        vertices = new ArrayList<Node>();
        arestas = new ArrayList<Edge>();
    }

    public static void main(String[] args) {
        Graph g = new Graph();
        System.out.println(g);
    }
}