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
        for (int i = 0; i < 5; i++){
            Edge connection = graph.getEdge("ABL"+random.get(i));
            System.out.println("REMOVED: " + connection.getTargetNode() + " --- " + connection.getSourceNode());
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

        //remove old cluster classifiers and generate new ones
        utils.removeSpecificAttribute(graph,"cluster");
        for (int i = 0; i < graph.getNodeCount(); i++) {
            //utils.specifyClusters(graph.getNode(i),i,identifierA);
            System.out.print("Cluster: " + i + ": ");
            utils.dfsClustering(graph.getNode(i), i, identifierA);
            System.out.println();
        }


        for (Node n:graph.getEachNode()){
            String clusterA;
            //get every Node B
            if (n.getId().contains(identifierB)){
                //find the ABL link to get the cluster of A
                Edge ABL = utils.getABL(n);
                Node targetA;
                //select the node from the other subnetwork
                if (ABL.getTargetNode() == n)
                   targetA = ABL.getSourceNode();
                else
                    targetA = ABL.getTargetNode();

                clusterA = targetA.getAttribute("cluster");

                System.out.println(n + " is connected to " + targetA + " which is in cluster" + clusterA);

                //get every Node connected to this B node and check if connects to the same cluster
                for (Edge e:n.getEachEdge()){
                    //get every Node, which is in the same subgraph
                    if (e != null && !e.getId().contains("ABL")){
                        Node target; //this node is connected to our node B
                        //System.out.println(identifierB + " - " + n.getId());

                        if (e.getTargetNode() == n)
                            target = e.getSourceNode();
                        else
                            target = e.getTargetNode();
                        //System.out.println("works");
                        //check if this is connected to the same cluster in A
                        //get the corresponding A node
                        Edge ABL2 = utils.getABL(target);
                        Node tmp;
                        if (ABL2.getTargetNode() == target)
                            tmp = ABL2.getSourceNode();
                        else
                            tmp = ABL2.getTargetNode();

                        //System.out.println(n + " is connected to " + target + " which is connected to " + tmp);

                        if (clusterA.compareTo(tmp.getAttribute("cluster")) < 0){
                            working = true;
                            graph.removeEdge(e);
                            System.out.println("Removing edge between " + n + " and " + target + " because cluster " + clusterA + " is not " +  tmp.getAttribute("cluster"));
                            //System.out.println(tmp.getAttribute("cluster") + " --- " + clusterA);
                        }else{
                            System.out.println(" NOT Removing edge between " + n + " and " + target + " because cluster " + clusterA + " is " +  tmp.getAttribute("cluster"));
                        }
                    }
                }
            }
        }
        return working;
    }
}
