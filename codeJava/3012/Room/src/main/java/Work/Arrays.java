package Work;

public class Arrays {
    public void arr() {
        // One - dimensional array
        System.out.println("One - dimensional array example");
        int[] one = {1, 2, 3, 4, 5};
        System.out.println("Length of array: " + one.length);
        System.out.printf("Elements: ");
        for (int i = 0 ; i < one.length ; i = i + 1) {
            System.out.printf("%d ", one[i]);
        }
        System.out.println();

        System.out.println("--------------------------------");

        // Two - dimensional array
        System.out.println("Two - dimensional array example");
        int[][] two = {one, one};
        System.out.println("Length of array: " + two.length);
        for (int i = 0 ; i < two.length ; i = i + 1) {
            System.out.printf("%d one - dimensional array elements: ", i + 1);
            for (int j = 0 ; j < two[i].length ; j = j + 1) {
                System.out.printf("%d ", two[i][j]);
            }
            System.out.println();
        }

        System.out.println("--------------------------------");

        // Multi - dimensional array
        System.out.println("Multi - dimensional array example");
        int[][][] three = {two, two, two};
        System.out.println("Length of array: " + three.length);
        for (int i = 0 ; i < three.length ; i = i + 1) {
            System.out.printf("%d two - dimensional array elements: \n", i + 1);
            for (int j = 0 ; j < three[i].length ; j = j + 1) {
                System.out.printf("%d one - dimensional array elements: ", j + 1);
                for (int k = 0 ; k < three[i][j].length ; k = k + 1) {
                    System.out.printf("%d ", three[i][j][k]);
                }
                System.out.println();
            }
        }

    }
}
