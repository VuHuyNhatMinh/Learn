package Model;

public class NormalAccount extends Account {
    /* Default Constructor */
    public NormalAccount() {
    }

    /* Initialise new NormalAccount */
    public NormalAccount(int balance) {
        super(balance);
    }

    @Override
    public boolean withdraw(int money) {
        if (money <= getBalance()) {
            return super.withdraw(money);
        }
        return false;
    }

    @Override
    protected int endMonthCharge() {
        return 10000;
    }
}
