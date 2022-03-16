package com.Model;

public class Human {
    public Human() {};

    private String name;
    private String homeTown;
    private String teacherID;

    public Human(String name, String homeTown, String teacherID) {
        this.name = name;
        this.homeTown = homeTown;
        this.teacherID = teacherID;
    }

    // Setter
    public void setName(String name) {
        this.name = name;
    }

    public void setHomeTown(String homeTown) {
        this.homeTown = homeTown;
    }

    public void setTeacherID(String teacherID) {
        this.teacherID = teacherID;
    }

    // Getter
    public String getName() {
        return this.name;
    }

    public String getHomeTown() {
        return this.homeTown;
    }

    public String getTeacherID() {
        return this.teacherID;
    }
}
