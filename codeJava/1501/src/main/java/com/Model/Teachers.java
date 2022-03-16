package com.Model;

import java.util.List;

public class Teachers extends Human{
    public Teachers() {};

    private int salary;
    private int reward;
    private int penalty;
    private int fieldSalary;

    public Teachers(String name, String homeTown, String teacherID, int salary, int reward, int penalty) {
        super(name, homeTown, teacherID);
        this.salary = salary;
        this.reward = reward;
        this.penalty = penalty;
    }

    // Setter
    public void setSalary(int salary) {
        this.salary = salary;
    }

    public void setReward(int reward) {
        this.reward = reward;
    }

    public void setPenalty(int penalty) {
        this.penalty = penalty;
    }

    public void setFieldSalary(int fieldSalary) {
        this.fieldSalary = fieldSalary;
    }

    // Getter
    public int getSalary() {
        return this.salary;
    }

    public int getReward() {
        return this.reward;
    }

    public int getPenalty() {
        return this.penalty;
    }

    public int getFieldSalary() {
        return this.fieldSalary;
    }

    public void calSalary() {
        fieldSalary = salary + reward - penalty;
        System.out.printf("Salary: %d\n", fieldSalary);
    }

    @Override
    public void setTeacherID(String teacherID) throws InvalidTeacherIDException{
        for(List<Teachers> lst: listTe)
            super.setTeacherID(teacherID);
        }
    }
}
