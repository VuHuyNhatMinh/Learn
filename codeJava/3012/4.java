class pc21 {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6};
        int[] positiveNumbers = numbers;     // Copying arrays: shadow copy, copy address of numbers
        // deep copy: not copy address, have to use for

        numbers[0] = -1;

        for (int number: positiveNumbers) {
            System.out.print(number + " ");
        }
        System.out.println();
    }
}