import agent.PowerCascadeAgent;
import protopeer.Experiment;
import protopeer.Peer;
import protopeer.PeerFactory;
import protopeer.SimulatedExperiment;
import protopeer.util.quantities.Time;
import replayer.BenchmarkLogReplayer;

/**
 * Created by backes on 22/10/16.
 */
public class testExperiment extends SimulatedExperiment {
    private static final String expName = "test";
    private static String experimentID = "experiment-test";

    private final static int runDuration = 10;

    private final static int bootstrapTime = 2000;
    private final static int runTime = 1000;
    private final static int N = 1;


    public static void main(String[] args){
        Experiment.initEnvironment();
        testExperiment test = new testExperiment();
        test.init();

        PeerFactory peerFactory = new PeerFactory() {
            @Override
            public Peer createPeer(int peerIndex, Experiment experiment) {
                Peer newPeer = new Peer(peerIndex);
                newPeer.addPeerlet(new PowerCascadeAgent(experimentID, Time.inMilliseconds(bootstrapTime),Time.inMilliseconds(runTime),10.0));
                return newPeer;
            }
        };

        test.initPeers(0,N,peerFactory);
        test.startPeers(0,N);

        test.runSimulation(Time.inSeconds(runDuration));

        BenchmarkLogReplayer replayer = new BenchmarkLogReplayer(expName,0,1000);
    }

}
