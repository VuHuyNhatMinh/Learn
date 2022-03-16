package Model;

public class NickelNDime extends Account{
    /* Default Constructor */
    public NickelNDime() {
    }

  /* Initialise new NickelNDime */
    public NickelNDime(int balance) {
        super(balance);
    }

    @Override
    public boolean withdraw(int money) {
        if (getTransactions() <= 9 && money <= getBalance()) {
            return super.withdraw(money);
        }
        return false;
    }

    @Override
    protected int endMonthCharge() {
        return 2000 * getTransactions();
    }
}
