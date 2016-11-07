import org.graphstream.algorithm.generator.*;
import org.graphstream.algorithm.generator.Generator;
import org.graphstream.graph.*;
import org.graphstream.graph.implementations.*;

/**
 * Created by backes on 06/11/16.
 */
public class Experiment {
    public static void main(String[] args){

        Utilities util = new Utilities();

        //create two similar scale free networks
        System.out.println("Creating Network A");
        Graph graphA = util.scaleFree("A", 3, 64000);
        System.out.println("Network A created");
        System.out.println("Creating Network B");
        Graph graphB = util.scaleFree("B", 3, 64000);
        System.out.println("Network B created");
        //combine them into one graph
        System.out.println("Combining Graphs");
        Graph inter = util.combineGraphs(graphA,graphB);
        System.out.println("Graphs combined");
        System.out.println("Connecting Graphs");
        util.connectGraph(inter,"A","B");
        System.out.println("Graphs connected");

        //add color to spice it up ;)
        inter.addAttribute("ui.stylesheet", "node.A {fill-color: red;} node.B {fill-color: blue;} edge.ABL {fill-color: green;} ");
        //display the graph, because we added color...
        //inter.display();

        System.out.println("Simulation started");
        System.out.println("Total Edges: " + inter.getEdgeCount());
        System.out.println("Total Nodes: " + inter.getNodeCount());

        Agent agent = new Agent();
        agent.init(inter,"A","B");
        System.out.print("Iterations: [");
        boolean ansA = false, ansB = false;
        do {
            System.out.print("|");
            ansA = agent.removeSingleClusterLink(inter,"B","A");
            ansB = agent.removeSingleClusterLink(inter,"A","B");
        }while (ansA && ansB);
        System.out.println("]");
        System.out.println("Simulation ended");
        System.out.println("Total Edges: " + inter.getEdgeCount());
        System.out.println("Total Nodes: " + inter.getNodeCount());

    }
}
