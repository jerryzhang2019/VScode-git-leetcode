public class DeadLock_demo01 {

    private static String s1 = "chopstiks_left";
    private static String s2 = "chopstiks_right";

    public static void main(final String[] args){
        //Deadlock In multi-thread synchronization, if the synchronization code is nested and the same lock is used, 
        //a deadlock may occur
        new Thread(){  
            public void run(){
                while(true){
                    synchronized(s1){
                        System.out.println("Thread A: get" + s1 + " waiting for" + s2);
    
                        synchronized(s2){
                            System.out.println("Thread A: get" + s2 + "starting lunch...");
                        }
                    }
                }

            };
        }.start();
        new Thread(){
            public void run(){
                while(true){
                    synchronized(s2){
                        System.err.println("Thread B: get" + s2 + " waiting for" + s1);

                        synchronized(s1){
                            System.err.println("Thread B: get" + s1 + "starting lunch...");
                        }
                    }
                }
            };
        }.start();
    }
}