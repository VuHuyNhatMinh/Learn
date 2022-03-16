class CopyArray {
    public static void main(String[] args)
    {
        int[] numbers = {1, 2, 3, 4, 5, 6};
        int[] positiveNumbers = numbers;    // Copying arrays

        for (int number: positiveNumbers)
        {
            System.out.print(number + " ");
        }
        System.out.println();
    }
}