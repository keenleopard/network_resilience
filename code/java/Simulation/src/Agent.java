import org.graphstream.graph.Edge;
import org.graphstream.graph.Graph;

import java.util.Random;

/**
 * Created by backes on 06/11/16.
 */
public class Agent {
    Utilities utils = new Utilities();

    /**
     * Initializes the attack: Removes a node A, all the edges to it, the corresponding node B and all it's edges.
     * @param graph
     * @param identifierA
     * @param identifierB
     */
    protected void init(Graph graph, String identifierA, String identifierB){
        Random rand = new Random();
        int num = rand.nextInt(graph.getNodeCount()/2+1);
        Edge connection = graph.getEdge("ABL"+num);
        graph.removeNode(connection.getTargetNode().getId());
        graph.removeNode(connection.getSourceNode().getId());
    }
}
