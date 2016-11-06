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
        Graph graphA = util.scaleFree("A", 3, 10);
        Graph graphB = util.scaleFree("B", 3, 10);
        //combine them into one graph
        Graph inter = util.combineGraphs(graphA,graphB);
        //util.connectGraph(inter,"A","B");

        //add color to spice it up ;)
        inter.addAttribute("ui.stylesheet", "node.A {fill-color: red;} node.B {fill-color: blue;} edge.ABL {fill-color: green;} ");
        //display the graph, because we added color...
        inter.display();
        /*
        Agent agent = new Agent();
        graphA.display();
        graphB.display();
        agent.init(inter,"A","B");
        */
    }
}
