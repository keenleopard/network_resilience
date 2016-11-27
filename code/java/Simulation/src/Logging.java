import java.io.PrintStream;

/**
 * Created by backes on 07/11/16.
 */
public class Logging {
    private PrintStream stream = System.out;

    /**
     * Optional constructor setting the stream
     * @param stream
     */
    public Logging(PrintStream stream){
        this.stream = stream;
    }

}
