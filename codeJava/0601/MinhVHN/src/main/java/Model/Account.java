package Model;

public abstract class Account {
    /* Default Constructor */
    public Account() {
    }

    private int balance;
    private int transactions;
    private int fee;

    public int getBalance() {
        return balance;
    }

    public int getTransactions() {
        return transactions;
    }

    /* Constructor to initialise new account with specific balance */
    public Account(int balance) {
        this.balance = balance;
        transactions = 0;
    }

    /*  */
    public boolean deposit(int money) {
        balance = balance + money;
        cal();
        return true;
    }

    public boolean withdraw(int money) {
        balance = balance - money;
        cal();
        return true;
    }

    private void cal() {
        transactions += 1;
    }

    /*  */
    public void endMonth() {
        fee = endMonthCharge();
        System.out.println("Account information");
        System.out.printf("Balance: %d\n", balance - fee);
        System.out.printf("Transactions: %d\n", transactions);
        System.out.printf("Fee: %d\n", fee);
        transactions = 0;
    }

    /*  */
    protected abstract int endMonthCharge();
}
