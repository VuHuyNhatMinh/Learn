package Work;

public class SimpleObject {
    String message;

    // Constructor
    public SimpleObject(String mes) {
        System.out.println("Message display: " + mes);
    }

    // Setter
    public void setMessage(String message) {
        this.message = message;
    }

    // Getter
    public String getMessage() {
        return this.message;
    }
}
