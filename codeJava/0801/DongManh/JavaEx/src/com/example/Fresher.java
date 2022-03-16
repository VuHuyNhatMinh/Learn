package com.example;

public class Fresher extends Employee{
    private String Graduation_date, Graduation_rank, Education;

    public Fresher(String ID, String fullName, String birthday, String phone, String email,
                   Type employee_Type, String graduation_date, String graduation_rank, String education) {
        super(ID, fullName, birthday, phone, email, employee_Type);
        this.Graduation_date = graduation_date;
        this.Graduation_rank = graduation_rank;
        this.Education = education;
    }



    @Override
    public void ShowInfo() {
        System.out.println("----------------Information-------------------");
        System.out.println("-               Fresher                      -");
        System.out.println("Full Name: " + this.getFullName());
        System.out.println("Birthday: " + this.getBirthday());
        System.out.println("Phone: " + this.getPhone());
        System.out.println("Email: " + this.getEmail());
        System.out.println("Type: Fresher");
        System.out.println("Graduation Date: " + this.Graduation_date);
        System.out.println("Graduation Rank: " + this.Graduation_rank);
        System.out.println("Education: " + this.Education);
        System.out.println("----------------------------------------------");
    }
}
