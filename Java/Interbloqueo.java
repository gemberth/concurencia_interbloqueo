package RepositorioGrupo.concurencia_interbloqueo.Java;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import RepositorioGrupo.concurencia_interbloqueo.Java.com.jenkov.java.concurrency.deadlock.Runnable1;
import RepositorioGrupo.concurencia_interbloqueo.Java.com.jenkov.java.concurrency.deadlock.Runnable2;


public class Interbloqueo {

    public static void main(String[] args) {
        
        Lock resource1 = new ReentrantLock();
        Lock resource2 = new ReentrantLock();
        Lock resource3 = new ReentrantLock();
        Lock resource4 = new ReentrantLock();
        Lock resource5 = new ReentrantLock();
        Lock resource6 = new ReentrantLock();

        Runnable runnable1 = new Runnable1(resource1, resource2, 
                                           resource3, resource4);
        Runnable runnable2 = new Runnable2(resource4, resource5, 
                                           resource6, resource1);

        Thread thread1 = new Thread(runnable1);
        Thread thread2 = new Thread(runnable2);

        thread1.start();
        thread2.start();

    }
}