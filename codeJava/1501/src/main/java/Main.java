import com.Model.Teachers;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Teachers> listTeacher = new ArrayList<>();
        Teachers tc = new Teachers("Minh", "HP", "20191973", 300, 100, 10);
        Teachers tc1 = new Teachers("M", "HP", "20191811", 300, 100, 10);
        Teachers tc2 = new Teachers("I", "HP", "20192031", 300, 100, 10);
        listTeacher.add(tc);
        listTeacher.add(tc1);
        listTeacher.add(tc2);
        for(int i = 0; i < listTeacher.size() ; i = i + 1) {
            System.out.println(listTeacher.get(i).getName());
        };

        System.out.println();
        // Remove
        for(int i = 0 ; i < listTeacher.size() ; i = i + 1) {
            if (listTeacher.get(i).getTeacherID() == "20191973") {
                listTeacher.remove(i);
            }
        }

        for(int i = 0; i < listTeacher.size() ; i = i + 1) {
            System.out.println(listTeacher.get(i).getName());
        };

    }
}
