package Model;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Students {
    public Students() {};

    private String fullName;
    private Date doB;
    private String sex;
    private String phoneNumber;
    private String universityName;
    private String gradeLevel;

    public Students(String fullName, Date doB, String sex, String phoneNumber, String universityName, String gradeLevel) {
        this.fullName = fullName;
        this.doB = doB;
        this.sex = sex;
        this.phoneNumber = phoneNumber;
        this.universityName = universityName;
        this.gradeLevel = gradeLevel;
    }

    // Setter
    public void setFullName(String fullName) {
        if (fullName.length() < 50 && fullName.length() >= 10) {
            this.fullName = fullName;
        } else {
            try {
                throw new InvalidFullNameException();
            } catch (InvalidFullNameException e) {
                System.out.println("Invalid Full Name");
            }
        }
    }

    public void setDoB(String doB) {
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
        try {
            Date date = formatter.parse(doB);
            this.doB = date;
        } catch (ParseException e) {
            System.out.println("Invalid Date of Birth");
        }
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setUniversityName(String universityName) {
        this.universityName = universityName;
    }

    public void setGradeLevel(String gradeLevel) {
        this.gradeLevel = gradeLevel;
    }

    // Getter
    public String getFullName() {
        return this.fullName;
    }

    public Date getDoB() {
        return this.doB;
    }

    public String getSex() {
        return this.sex;
    }

    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public String getUniversityName() {
        return this.universityName;
    }

    public String getGradeLevel() {
        return this.gradeLevel;
    }

    public void ShowMyInfor() {
        System.out.printf("Full Name: %s\n", getFullName());
        System.out.printf("Date of Birth: %s\n", getDoB());
        System.out.printf("Sex: %s\n", getSex());
        System.out.printf("Phone Number: %s\n", getPhoneNumber());
        System.out.printf("University: %s\n", getUniversityName());
        System.out.printf("Grade Level: %s\n", getGradeLevel());
    }
}
