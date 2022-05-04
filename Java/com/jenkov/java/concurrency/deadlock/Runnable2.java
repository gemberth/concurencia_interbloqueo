package RepositorioGrupo.concurencia_interbloqueo.Java.com.jenkov.java.concurrency.deadlock;
import java.util.concurrent.locks.Lock;

public class Runnable2 implements Runnable{

    private Lock resource4 = null;
    private Lock resource5 = null;
    private Lock resource6 = null;
    private Lock resource1 = null;

    public Runnable2(Lock resource4, Lock resource5, 
                     Lock resource6, Lock resource1) 
    {
        this.resource4 = resource4;
        this.resource5 = resource5;   
        this.resource6 = resource6;
        this.resource1 = resource1;  
    }

    public void run() {
        
        String threadName = Thread.currentThread().getName()+ ": ";

        System.out.println(threadName + 
        "Intentando Bloquear recurso 4");
        resource4.lock();
        System.out.println(threadName + 
        "Recurso 4 bloqueado");

        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            //Nada
        }

        System.out.println(threadName + 
        "Intentando Bloquear recurso 5");
        resource5.lock();
        System.out.println(threadName + 
        "Recurso 5 bloqueado");

        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            //Nada
        }

        System.out.println(threadName + 
        "Intentando Bloquear recurso 6");
        resource6.lock();
        System.out.println(threadName + 
        "Recurso 6 bloqueado");



        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            //Nada
        }


        System.out.println(threadName +
            "Intentando Bloquear recurso 1");
        resource1.lock();
        System.out.println(threadName + 
            "Recurso 1 bloqueado");




        System.out.println(threadName +
            "Desbloqueando el recurso 4");
        resource4.unlock();
        System.out.println(threadName +
            "Desbloqueando el recurso 5");
        resource5.unlock();
        System.out.println(threadName +
            "Desbloqueando el recurso 6");
        resource6.unlock();
        System.out.println(threadName +
            "Desbloqueando el recurso 1");
        resource1.unlock();
        
    }

}