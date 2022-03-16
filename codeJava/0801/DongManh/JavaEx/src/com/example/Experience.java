package com.example;

public class Experience extends Employee{
    private String ExpInYear;
    private String ProSkill;

    public Experience(String ID, String fullName, String birthday, String phone, String email, Type employee_Type, String expInYear, String proSkill) {
        super(ID, fullName, birthday, phone, email, employee_Type);
        ExpInYear = expInYear;
        ProSkill = proSkill;
    }

    @Override
    public void ShowInfo() {
        System.out.println("----------------Information-------------------");
        System.out.println("-               Experience                   -");
        System.out.println("Full Name: " + this.getFullName());
        System.out.println("Birthday: " + this.getBirthday());
        System.out.println("Phone: " + this.getPhone());
        System.out.println("Email: " + this.getEmail());
        System.out.println("Type: Experience");
        System.out.println("Exp in year: " + this.ExpInYear);
        System.out.println("Pro Skill: " + this.ProSkill);
        System.out.println("----------------------------------------------");
    }
}
