package com.example;

public class Intern extends Employee{

    private String Majors, semester, university;

    public Intern(String ID, String fullName, String birthday, String phone, String email, Type employee_Type, String majors, String semester, String university) {
        super(ID, fullName, birthday, phone, email, employee_Type);
        Majors = majors;
        this.semester = semester;
        this.university = university;
    }

    @Override
    public void ShowInfo() {
        System.out.println("----------------Information-------------------");
        System.out.println("-               Intern                       -");
        System.out.println("Full Name: " + this.getFullName());
        System.out.println("Birthday: " + this.getBirthday());
        System.out.println("Phone: " + this.getPhone());
        System.out.println("Email: " + this.getEmail());
        System.out.println("Type: Intern");
        System.out.println("Major: " + this.Majors);
        System.out.println("Semester: " + this.semester);
        System.out.println("Education: " + this.university);
        System.out.println("----------------------------------------------");
    }
}
