import org.graphstream.algorithm.ConnectedComponents;
import org.graphstream.algorithm.generator.*;
import org.graphstream.algorithm.generator.Generator;
import org.graphstream.graph.*;
import org.graphstream.graph.implementations.*;

import java.util.Iterator;

/**
 * Created by backes on 06/11/16.
 */
public class Experiment {

    public static void main(String[] args){

        Utilities util = new Utilities();
        //ToDo: Logging Class
        //ToDo: Debugging graph: 1->2->3->...
        int size = 15;
        //create two similar scale free networks
        System.out.println("Creating Network A");
        Graph graphA = util.scaleFree("A", 4, size);
        System.out.println("Network A created");
        System.out.println("Creating Network B");
        Graph graphB = util.scaleFree("B", 4, size);
        System.out.println("Network B created");
        //combine them into one graph
        System.out.println("Combining Graphs");
        Graph inter = util.combineGraphs(graphA,graphB);
        System.out.println("Graphs combined");
        System.out.println("Connecting Graphs");
        util.connectGraph(inter,"A","B");
        System.out.println("Graphs connected");

        //add color to spice it up ;)
        inter.addAttribute("ui.stylesheet", "node {text-mode: normal;} node.A {fill-color: red;} node.B {fill-color: blue;} edge.ABL {fill-color: green;} node.start {fill-color: grey;} node.found0 {fill-color:orange;} node.found1 {fill-color:purple;}");

        System.out.println("Simulation started");
        System.out.println("Total Edges: " + inter.getEdgeCount());
        System.out.println("Total Nodes: " + inter.getNodeCount());

        ConnectedComponents cc = new ConnectedComponents();
        cc.init(inter);

        //node.addAttribute("ui.style","fill-color: rgb(0,100,255);")


        Agent agent = new Agent();
        agent.init(inter,"A","B");


        //util.specifyClusters(inter.getNode(0),0,"B");
        /*
        util.dfsClustering(inter.getNode(0),0,"A");
        inter.getNode(0).setAttribute("ui.class","start");
        System.out.println("SEED ID: " + inter.getNode(0).getId());
*       */
        //System.out.print("Iterations: [");

        boolean ansA = false, ansB = false;
        do {
            //System.out.print("|");
            ansA = agent.removeSingleClusterLink(inter,"B","A");
            ansB = agent.removeSingleClusterLink(inter,"A","B");
        }while (ansA || ansB);


        //System.out.println("]");
        //System.out.println("Simulation ended");
        System.out.println("Total Edges: " + inter.getEdgeCount());
        System.out.println("Total Nodes: " + inter.getNodeCount());


        /*
        Iterator iterator = cc.iterator();
        for (ConnectedComponents.ConnectedComponent nodes : cc) {
             Iterable<Edge> q = nodes.getEachEdge();
        }
        Object test = null;
        while (iterator.hasNext()){
            test = iterator.next();
        }

        System.out.print("a");
        */


        System.out.printf("%d connected component(s) in this graph, so far.%n",
                cc.getConnectedComponentsCount());



        inter.display();


    }



}
