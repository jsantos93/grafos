import java.util.List;
import java.util.ArrayList;

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