import org.graphstream.graph.Edge;
import org.graphstream.graph.Graph;
import org.graphstream.graph.Node;

import java.util.Collection;
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

    /**
     * For every node identifierA, we check if the corresponding node in the subnetwork of identifierB is single. If yes, then we remove the edges of identifierB, except the ABL edge
     * @param graph the graph to work on
     * @param identifierA the network where the edges are removed from
     * @param identifierB the second, connected network which should have single clusters
     * @return true if edges got removed, else false
     */
    protected boolean removeSingleClusterLink(Graph graph, String identifierA, String identifierB){
        boolean working = false;
        for (Node n:graph.getEachNode()){
            //check if we're part of the subnetwork identifierA
            if (n.getId().contains(identifierA)){
                //get all the edges of this node, and check for the ABL edge, to find the corresponding node in identifierB
                for(Edge e:n.getEachEdge()){
                    //if we found the edge connecting the two subnetworks
                    if (e.getId().contains("ABL")){
                        //we now check, if the identifierB node has only a single edge
                        Node target = e.getTargetNode();
                        Collection coll = target.getEdgeSet();
                        //if there is only one edge, i.e. the ABL edge
                        if (coll.size() == 1){
                            //we remove all the edges except the ABL edge from the node n, our initial node
                            for (Edge edges:n.getEachEdge()){
                                if (!edges.getId().contains("ABL")) {
                                    graph.removeEdge(edges);
                                    working = true;
                                }
                            }
                        }
                    }
                }
            }
        }
        return working;
    }


}
