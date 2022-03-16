import Model.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("-- Normal Account example --");
        NormalAccount nrmacc = new NormalAccount(5000);
        System.out.println("Transfer 3000: " + nrmacc.deposit(3000));
        System.out.println("Withdraw 15000: " + nrmacc.withdraw(15000));
        System.out.println("End month notification");
        nrmacc.endMonth();

        System.out.println("-- NickelNDime --");
        NickelNDime nnd = new NickelNDime(10000);;
        System.out.println("Transfer 4000: " + nnd.deposit(4000));
        System.out.println("Withdraw 20000: " + nnd.withdraw(20000));
        System.out.println("End month notification");
        nnd.endMonth();
    }
}
