package Model;

public class Experience extends Employee{
    public Experience(){};

    private int ExpInYear;
    private String ProSkill;

    public Experience(String ID, String fullName, String birthDay, String phone, String email, int expInYear, String proSkill) {
        super(ID, fullName, birthDay, phone, email);
        this.ExpInYear = expInYear;
        this.ProSkill = proSkill;
    }

    // Setter
    public void setExplnYear(int explnYear) {
        this.ExpInYear = explnYear;
    }

    public void setProSkill(String proSkill) {
        this.ProSkill = proSkill;
    }

    // Getter
    public int getExplnYear() {
        return this.ExpInYear;
    }

    public String getProSkill() {
        return this.ProSkill;
    }

    @Override
    protected int Employee_type() {
        return 0;
    }

    @Override
    public void ShowInfo() {
        super.ShowInfo();
        System.out.printf("Experience in year: %d\n", getExplnYear());
        System.out.printf("Pro Skill: %s\n", getProSkill());
    }
}
