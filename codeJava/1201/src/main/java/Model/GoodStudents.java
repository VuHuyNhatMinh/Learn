package Model;

public class GoodStudents extends Students{
    public GoodStudents() {};

    private int gpa;
    private String bestRewardName;

    public GoodStudents(String fullName, String doB, String sex, String phoneNumber, String universityName, String gradeLevel, int gpa, String bestRewardName) {
        super(fullName, doB, sex, phoneNumber, universityName, gradeLevel);
        this.gpa = gpa;
        this.bestRewardName = bestRewardName;
    }

    // Setter
    public void setGpa(int gpa) {
        this.gpa = gpa;
    }

    public void setBestRewardName(String bestRewardName) {
        this.bestRewardName = bestRewardName;
    }

    // Getter
    public int getGpa() {
        return this.gpa;
    }

    public String getBestRewardName() {
        return this.bestRewardName;
    }

    @Override
    public void ShowMyInfor() {
        super.ShowMyInfor();
        System.out.printf("GPA: %d\n", getGpa());
        System.out.printf("Best Reward Name: %s\n", getBestRewardName());
    }
}
