class pc17 {
 public static void main(String[] args) {
        int [][][] test = {
            {
                {1, -2, 3},
                {2, 3, 4}
            },
            {
                {-4, -5, 6, 9},
                {1},
                {2, 3}
            }
        };

        for (int[][] sub : test) 
        {
            System.out.println(sub.length);
            for(int[] subarray : sub) 
            {
                for (int ele : subarray) 
                {
                    System.out.print(ele + " ");
                }
                System.out.println();
            }
        }

        System.out.println("------------------");

        for (int test3: test[0][0])
        {
            System.out.print(test3 + " ");
        }
        System.out.println();

        System.out.println("------------------");
        System.out.println(test[0][0]);    
    }
}