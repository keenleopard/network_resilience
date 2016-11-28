import org.graphstream.algorithm.generator.*;
import org.graphstream.graph.*;
import org.graphstream.graph.implementations.*;

import java.util.Iterator;
import java.util.Random;

/**
 * Created by backes on 06/11/16.
 */
public class Utilities {
    private Random rand = new Random();

    /**
     * Simultaes random nodes failing. Disconnects num nodes from the Graph G
     * @param G The Graph to work on
     * @param num The number of nodes to disconnect from the graph
     * @param p The probability that a node is removed
     */
    public void randomNodeFailure(Graph G, int num, double p){
        double probability = 0;
        while(num > 0){
            for(Node n:G.getEachNode()) {
                probability = rand.nextDouble();
                if (probability <= p) {
                    G.removeNode(n);
                    num--;
                }
            }
        }
    }
    /**
     * Simultaes random edges failing. Disconnects num edges from the Graph G
     * @param G The Graph to work on
     * @param num The number of edges to disconnect from the graph
     * @param p The probability that an edge is removed
     */
    protected void randomEdgeFailure(Graph G, int num, double p){
        double probability = 0;
        while(num > 0){
            for(Edge e:G.getEachEdge()) {
                probability = rand.nextDouble();
                if (probability <= p) {
                    G.removeEdge(e);
                    num--;
                }
            }
        }
    }

    /**
     * Generate an scale free network based on the Barabasi Albert algorithm
     * @param identifier The name of the graph
     * @param degree the degree
     * @param nodes the additional nodes (there are always 3 more starting nodes!)
     * @return returns the graph
     */
    protected Graph scaleFree(String identifier, int degree, int nodes){
        Graph graph = new SingleGraph(identifier);
        Generator gen = new BarabasiAlbertGenerator(degree);
        gen.addSink(graph);
        gen.begin();
        for(int i=0; i<nodes; i++){
            gen.nextEvents();
        }
        gen.end();
        return graph;
    }

    /**
     * Combines two graphs into one. Nodes of each graph are named as Ai and Bi, and Links as ALi and BLi which i an integer
     * @param graphA The first graph
     * @param graphB The second graph
     * @return Returns a third graph, which contains the two graphs
     */
    protected Graph combineGraphs(Graph graphA, Graph graphB){
        Graph inter = new SingleGraph("graphInter");

        copyNode(graphA,inter,"A");
        copyNode(graphB,inter,"B");
        copyEdge(graphA,inter,"A");
        copyEdge(graphB,inter,"B");


        return inter;
    }

    /**
     * Helper class to copy all the nodes from sourceGraph to targetGraph, and they are identified as identifieri with i a number
     * @param sourceGraph the original graph where the information is taken from
     * @param targetGraph the graph where the nodes are copied to
     * @param identifier the identifier, which is appended with a number
     */
    private void copyNode(Graph sourceGraph, Graph targetGraph, String identifier){
        int i = 0;
        for (Node n:sourceGraph.getEachNode()){
            targetGraph.addNode(identifier+n.getId());
            targetGraph.getNode(identifier+n.getId()).addAttribute("ui.class",identifier);
            targetGraph.getNode(identifier+n.getId()).addAttribute("ui.label",identifier+n.getId());
            //targetGraph.getNode(identifier+n.getId()).addAttribute("ui.style","fill-color: rgb(0,"+ i*37 % 255+ ","+ i*29 % 255+");");
            i++;
        }
    }

    /**
     * Helper class to copy all the edges from sourceGraph to targetGraph, and they are identified as identifieri with i a number
     * @param sourceGraph the original graph where the information is taken from
     * @param targetGraph the graph where the nodes are copied to
     * @param identifier the identifier, which is appended with a number
     */
    private void copyEdge(Graph sourceGraph, Graph targetGraph, String identifier){
        int i = 0;
        for (Edge e:sourceGraph.getEachEdge()){
            Node target = e.getTargetNode();
            Node source = e.getSourceNode();
            targetGraph.addEdge(identifier+"L" + i, identifier+source.getId(),identifier+target.getId());
            targetGraph.getEdge(identifier+"L"+i).addAttribute("ui.class",identifier+"L");
            i++;
        }
    }

    protected void connectGraph(Graph graph, String identifierA, String identifierB){
        String linkIdentifier = "ABL";
        int i = 0;
        for (Node n:graph){
            if (n.getId().contains(identifierA)){
                graph.addEdge(linkIdentifier + i,n.getId(),identifierB+n.getId().replace(identifierA,""));
                graph.getEdge(linkIdentifier+i).addAttribute("ui.class",linkIdentifier);
                i++;
            }
        }
    }


    public void specifyClusters(Node source,int count, String identifier) {
        Iterator<? extends Node> k = source.getDepthFirstIterator();

        while (k.hasNext()) {
            Node next = k.next();
            if (next.getId().contains(identifier) && next.getAttribute("cluster") == null) {
                next.setAttribute("cluster", "found"+count);
                next.setAttribute("ui.class","found"+count);
                System.out.println(next.getId() + " --- " + next.getAttribute("cluster").toString());
            }
            //count++;
        }
    }

    public void dfsClustering(Node source,int count ,String identifier){
        if (source.getId().contains(identifier) && source.getAttribute("cluster") == null) {
            source.setAttribute("cluster","found"+count);
            System.out.print(source.getId() + " (" + source.getAttribute("cluster")+") " );
            for (Edge e : source.getEachEdge()) {
                if (!e.getId().contains("ABL")) {
                    Node target;
                    if (e.getSourceNode() == source)
                        target = e.getTargetNode();
                    else
                        target = e.getSourceNode();
                        dfsClustering(target, count, identifier);
                }
            }
        }
    }

    protected void removeSpecificAttribute(Graph graph, String attr){
        graph.removeAttribute(attr);
    }

    /**
     * Searches the ABL link, connecting subnetwork A to subnetwork B
     * @param node The initial Node where the ABL link is connected to
     * @return returns the ABL edge
     */
    protected Edge getABL(Node node){
        Edge tmp = null;
        for (Edge e:node.getEachEdge()){
            if (e != null && e.getId().contains("ABL")){
                tmp = e;
            }
        }
        if (tmp == null)
            System.out.println("error");
        return tmp;
    }

}