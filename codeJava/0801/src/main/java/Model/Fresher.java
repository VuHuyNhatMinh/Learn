package Model;

public class Fresher extends Employee{
    public Fresher(){};

    private int Graduation_date;
    private String Graduation_rank;
    private String Education;

    public Fresher(String ID, String fullName, String birthDay, String phone, String email, int graduation_date, String graduation_rank, String education) {
        super(ID, fullName, birthDay, phone, email);
        this.Graduation_date = graduation_date;
        this.Graduation_rank = graduation_rank;
        this.Education = education;
    }

    // Setter
    public void setGraduation_date(int graduation_date) {
        this.Graduation_date = graduation_date;
    }

    public void setGraduation_rank(String graduation_rank) {
        this.Graduation_rank = graduation_rank;
    }

    public void setEducation(String education) {
        this.Education = education;
    }

    // Getter
    public int getGraduation_date() {
        return Graduation_date;
    }

    public String getGraduation_rank() {
        return Graduation_rank;
    }

    public String getEducation() {
        return Education;
    }

    @Override
    protected int Employee_type() {
        return 1;
    }

    @Override
    public void ShowInfo() {
        super.ShowInfo();
        System.out.printf("Graduation Date: %d\n", getGraduation_date());
        System.out.printf("Graduation Rank: %s\n", getGraduation_rank());
        System.out.printf("Education: %s\n", getEducation());
    }
}
