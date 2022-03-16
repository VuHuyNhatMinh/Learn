package Model;

public class Intern extends Employee{
    public Intern(){};

    private String Majors;
    private int Semester;
    private String University_name;

    public Intern(String ID, String fullName, String birthDay, String phone, String email, String majors, int semester, String university_name) {
        super(ID, fullName, birthDay, phone, email);
        this.Majors = majors;
        this.Semester = semester;
        this.University_name = university_name;
    }

    // Setter
    public void setMajors(String majors) {
        this.Majors = majors;
    }

    public void setSemester(int semester) {
        this.Semester = semester;
    }

    public void setUniversity_name(String university_name) {
        this.University_name = university_name;
    }

    // Getter
    public String getMajors() {
        return this.Majors;
    }

    public int getSemester() {
        return this.Semester;
    }

    public String getUniversity_name() {
        return this.University_name;
    }

    @Override
    protected int Employee_type() {
        return 2;
    }

    @Override
    public void ShowInfo() {
        super.ShowInfo();
        System.out.printf("Major: %s\n", getMajors());
        System.out.printf("Semester: %d\n", getMajors());
        System.out.printf("University: %s\n", getUniversity_name());
    }
}
