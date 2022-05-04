package RepositorioGrupo.concurencia_interbloqueo.Java.com.jenkov.java.concurrency.deadlock;
import java.util.concurrent.locks.Lock;

public class Runnable1 implements Runnable{

    private Lock resource1 = null;
    private Lock resource2 = null;
    private Lock resource3 = null;
    private Lock resource4 = null;


    public Runnable1(Lock resource1, Lock resource2, 
                     Lock resource3, Lock resource4) 
    {
        this.resource1 = resource1;
        this.resource2 = resource2;   
        this.resource3 = resource3;
        this.resource4 = resource4;

    }

    public void run() {
        String threadName = Thread.currentThread().getName() + ": ";

        System.out.println(threadName +
            "Intentando Bloquear recurso 1");
        resource1.lock();
        System.out.println(threadName + 
            "Recurso 1 bloqueado");

            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                //Nada
            }
    
        System.out.println(threadName +
            "Intentando Bloquear recurso 2");
        resource2.lock();
        System.out.println(threadName + 
            "Recurso 2 bloqueado");

            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                //Nada
            }
    
        System.out.println(threadName +
            "Intentando Bloquear recurso 3");
        resource3.lock();
        System.out.println(threadName + 
            "Recurso 3 bloqueado");
            



        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            //Nada
        }



        System.out.println(threadName + 
        "Intentando Bloquear recurso 4");
        resource4.lock();
        System.out.println(threadName + 
        "Recurso 4 bloqueado");


        System.out.println(threadName +
            "Desbloqueando el recurso 1");
        resource1.unlock();
        System.out.println(threadName +
            "Desbloqueando el recurso 2");
        resource2.unlock();
        System.out.println(threadName +
            "Desbloqueando el recurso 3");
        resource3.unlock();
        System.out.println(threadName +
            "Desbloqueando el recurso 4");
        resource4.unlock();
        
    }

}