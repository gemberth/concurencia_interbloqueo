// Java program to illustrate ConcurrentCollection uses
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.*;
class ConcurrentDemo extends Thread {
    static CopyOnWriteArrayList l =   new CopyOnWriteArrayList();
    
    
    public static void main(String[] args)
        throws InterruptedException
    {
        l.add("A");
        l.add("B");
        l.add("c");
  
        // We create a child thread that is
        // going to modify ArrayList l.
        ConcurrentDemo t = new ConcurrentDemo();
        t.start();
  
        // Now we iterate through the ArrayList
        // and get exception.
        Iterator itr = l.iterator();
        while (itr.hasNext()) {
            String s = (String)itr.next();
            System.out.println(s);
            Thread.sleep(6000);
        }
        System.out.println(l);
    }
}