package Model;

public class NormalStudents extends Students{
    public NormalStudents() {};

    private int englishScore;
    private int entryTestScore;

    public NormalStudents(String fullName, String doB, String sex, String phoneNumber, String universityName, String gradeLevel, int englishScore, int entryTestScore) {
        super(fullName, doB, sex, phoneNumber, universityName, gradeLevel);
        this.englishScore = englishScore;
        this.entryTestScore = entryTestScore;
    }

    // Setter
    public void setEnglishScore(int englishScore) {
        this.englishScore = englishScore;
    }

    public void setEntryTestScore(int entryTestScore) {
        this.entryTestScore = entryTestScore;
    }

    // Getter
    public int getEnglishScore() {
        return this.englishScore;
    }

    public int getEntryTestScore() {
        return this.entryTestScore;
    }

    @Override
    public void ShowMyInfor() {
        super.ShowMyInfor();
        System.out.printf("English Score: %d\n", getEnglishScore());
        System.out.printf("Entry Test Score: %d\n", getEntryTestScore());
    }
}
