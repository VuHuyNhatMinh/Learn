package com.example;

public abstract class Employee {
    private String ID, FullName, Birthday, Phone, Email;
    private Type Employee_Type;

    public Employee(String ID, String fullName, String birthday, String phone, String email, Type employee_Type) {
        this.ID = ID;
        this.FullName = fullName;
        this.Birthday = birthday;
        this.Phone = phone;
        this.Email = email;
        this.Employee_Type = employee_Type;
    }

    public String getID() {
        return ID;
    }

    public String getFullName() {
        return FullName;
    }

    public String getBirthday() {
        return Birthday;
    }

    public String getPhone() {
        return Phone;
    }

    public String getEmail() {
        return Email;
    }

    public Type getEmployee_Type() {
        return Employee_Type;
    }

    public void setFullName(String fullName) {
        FullName = fullName;
    }

    public void setBirthday(String birthday) {
        Birthday = birthday;
    }

    public void setPhone(String phone) {
        Phone = phone;
    }

    public void setEmail(String email) {
        Email = email;
    }

    public abstract void ShowInfo();
}
