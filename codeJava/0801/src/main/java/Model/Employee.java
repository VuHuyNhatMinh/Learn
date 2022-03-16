package Model;

public abstract class Employee {
    public Employee(){};

    private String ID;
    private String FullName;
    private String BirthDay;
    private String Phone;
    private String Email;
    private int cnt = 0;

    public Employee(String ID, String fullName, String birthDay, String phone, String email) {
        this.ID = ID;
        this.FullName = fullName;
        this.BirthDay = birthDay;
        this.Phone = phone;
        this.Email = email;
    }


    protected abstract int Employee_type();

    protected void Employee_count() {
        cnt = cnt + 1;
    }

    public void ShowInfo() {
        System.out.printf("ID: %s\n", getID());
        System.out.printf("Full Name: %s\n", getFullName());
        System.out.printf("Brith Day: %s\n", getBirthDay());
        System.out.printf("Phone: %s\n", getPhone());
        System.out.printf("Email: %s\n", getEmail());
    }

    // Setter
    public void setID(String ID) {
        this.ID = ID;
    }

    public void setFullName(String fullName) {
        this.FullName = fullName;
    }

    public void setBirthDay(String birthDay) {
        this.BirthDay = birthDay;
    }

    public void setPhone(String phone) {
        this.Phone = phone;
    }

    public void setEmail(String email) {
        this.Email = email;
    }

    // Getter
    public String getID() {
        return this.ID;
    }

    public String getFullName() {
        return this.FullName;
    }

    public String getBirthDay() {
        return this.BirthDay;
    }

    public String getPhone() {
        return this.Phone;
    }

    public String getEmail() {
        return this.Email;
    }
}
