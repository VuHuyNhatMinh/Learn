class LiteralExample {
    public static void main(String[] args) {
        // Error! Literal 42332200000 of type int is out of range
        // long myVariable1 = 42332200000;
        long myVariable1 = 4233;
        
        // 4233200000L is of type long, and it's not out of range
        long myVariable2 = 42332200000L;

    }
}