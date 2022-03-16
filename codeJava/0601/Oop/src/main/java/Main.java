import Model.*;

public class Main {
    public static void main(String[] args) {
        // Create new instance for Dog object
        Dog dog = new Dog();
        dog.setName("Dog");
        System.out.printf("Name: %s\n", dog.getName());
        System.out.printf("Sound: %s\n", dog.makeSound());

        // Create new instance for Cat object
        Cat cat = new Cat();
        cat.setName("Cat");
        System.out.printf("Name: %s\n", cat.getName());
        System.out.printf("Sound: %s\n", cat.makeSound());

        // Create new instance for Cat object
        Animals animal = new Animals();
        animal.setName("Animals");
        System.out.printf("Name: %s\n", animal.getName());
        System.out.printf("Sound: %s\n", animal.makeSound());
    }
}
