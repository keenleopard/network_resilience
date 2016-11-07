import com.sun.xml.internal.bind.v2.util.CollisionCheckStack;
import jdk.nashorn.internal.objects.annotations.Constructor;
import org.graphstream.graph.Edge;
import org.graphstream.graph.Graph;
import org.graphstream.graph.Node;

import java.util.*;
import java.util.stream.IntStream;

/**
 * Created by backes on 06/11/16.
 */
public class Agent {
    Utilities utils = new Utilities();

    public Agent(){

    }
    /**
     * Initializes the attack: Removes a node A, all the edges to it, the corresponding node B and all it's edges.
     * @param graph
     * @param identifierA
     * @param identifierB
     */
    protected void init(Graph graph, String identifierA, String identifierB){
        ArrayList<Integer> random = generateUniqueRandomNumber(graph.getNodeCount()/2);
        //remove
        for (int i = 0; i < 10; i++){
            Edge connection = graph.getEdge("ABL"+random.get(i));
            graph.removeNode(connection.getTargetNode().getId());
            graph.removeNode(connection.getSourceNode().getId());
        }
    }

    /**
     * Generation of unique random numbers by filling a list and then shuffling
     * @param size The range of the unique numbers (exclusive)
     * @return ArrayList of unique random numbers in range 0 to size-1
     */
    private ArrayList<Integer> generateUniqueRandomNumber(int size){
        ArrayList<Integer> list = new ArrayList<>();
        for(int k = 0; k < size; k++){
            list.add(k);
        }
        Collections.shuffle(list);
        return list;
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
                    if (e!= null && e.getId().contains("ABL")){
                        //we now check, if the identifierB node has only a single edge
                        Node target = e.getTargetNode();
                        Collection coll = target.getEdgeSet();
                        //if there is only one edge, i.e. the ABL edge
                        if (coll.size() == 1){
                            //we remove all the edges except the ABL edge from the node n, our initial node
                            for (Edge edges:n.getEachEdge()){
                                if (edges != null && !edges.getId().contains("ABL")) {
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
