package Work;

public class Room {
    int roomno;
    String roomtype;
    int roomarea;
    String ACmachine;

    // Constructor: Initialize default values for Room object attributes
    public Room() {
        this.roomno = 5;
        this.roomtype = "Family";
        this.roomarea = 400;
        this.ACmachine = "ACmachine";
    }

    // Setter
    public void setData(int roomno, String roomtype, int roomarea, String ACmachine) {
        this.roomno = roomno;
        this.roomtype = roomtype;
        this.roomarea = roomarea;
        this.ACmachine = ACmachine;
    }

    // Getter
    public void getData() {
        System.out.printf("Numbers of rooms: %d\n", this.roomno);
        System.out.printf("Room type: %s\n", this.roomtype);
        System.out.printf("Area of rooms: %d\n", this.roomarea);
        System.out.printf("ACmachine: %s\n", this.ACmachine);
    }
}
