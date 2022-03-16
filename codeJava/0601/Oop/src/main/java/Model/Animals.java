package Model;

public class Animals {
    private String name;
    private int age;

    public String makeSound() {
        return "HAHA";
    };

    private void sleep() {
        System.out.println("I want to sleep!");
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}
