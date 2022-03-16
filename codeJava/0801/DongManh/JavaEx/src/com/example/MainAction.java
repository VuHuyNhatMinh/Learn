package com.example;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class MainAction {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        List employees = new LinkedList();
        int key = -1;
        boolean run = true;
        while(run) {
            System.out.println("--------------------------------------");
            System.out.println("----------------MENU------------------");
            System.out.println("- 1.Add                              -");
            System.out.println("- 2.Edit                             -");
            System.out.println("- 3.Delete                           -");
            System.out.println("- 4.Show Information                 -");
            System.out.println("- 5.Quit                             -");
            System.out.println("--------------------------------------");
            System.out.println("Enter option: ");
            key = sc.nextInt();
            System.out.println("Choose option: " + key);
            switch (key) {
                case 1: {
                    Add(employees);
                    break;
                }

                case 2: {
                    String ID;
                    System.out.print("Enter ID: ");
                    ID = sc.next();
                    Edit(ID, employees);
                    break;
                }

                case 3: {
                    String ID;
                    System.out.print("Enter ID: ");
                    ID = sc.next();
                    Delete(ID, employees);
                    break;
                }

                case 4: {
                    for (Iterator i = employees.iterator(); i.hasNext();) {
                        Employee employee = (Employee) i.next();
                        employee.ShowInfo();
                    }
                    break;
                }

                case 5: {
                    run = false;
                    System.out.println("Closing Program ...");
                    break;
                }

                default:
                    break;
            }

            if (key > 5) {
                run = false;
            }
        }
    }

    private static void Add(List employees) {
        String ID, FullName, Birthday, Phone, Email;
        System.out.println("-------------Employee Type-------------");
        System.out.println("-            0. Experience            -");
        System.out.println("-            1. Fresher               -");
        System.out.println("-            2. Intern                -");
        System.out.println("---------------------------------------");
        System.out.print("Enter option: ");
        int key = sc.nextInt();
        System.out.print("Enter ID: ");
        ID = sc.next();
        System.out.print("Enter full name: ");
        FullName = sc.next();
        System.out.print("Enter birthday: ");
        Birthday = sc.next();
        System.out.print("Enter phone number: ");
        Phone = sc.next();
        System.out.print("Enter email: ");
        Email = sc.next();
        switch (key) {
            case 0: {
                String expInYear, ProSkill;
                System.out.print("Enter Exp in year: ");
                expInYear = sc.next();
                System.out.print("Enter Pro Skill: ");
                ProSkill = sc.next();
                Employee experience = new Experience(ID, FullName, Birthday, Phone, Email, Type.EXPERIENCE, expInYear, ProSkill);
                employees.add(experience);
                break;
            }

            case 1: {
                String graduation_date, graduation_rank, education;
                System.out.print("Enter Graduation Date: ");
                graduation_date = sc.next();
                System.out.print("Enter graduation rank: ");
                graduation_rank = sc.next();
                System.out.print("Enter Education: ");
                education = sc.next();
                Employee fresher = new Fresher(ID, FullName, Birthday, Phone,
                        Email, Type.FRESHER, graduation_date, graduation_rank, education);
                employees.add(fresher);
                break;
            }

            case 2: {
                String Majors, semester, university;
                System.out.print("Enter Majors: ");
                Majors = sc.next();
                System.out.print("Enter semester: ");
                semester = sc.next();
                System.out.print("Enter university: ");
                university = sc.next();
                Employee intern = new Intern(ID, FullName, Birthday, Phone, Email, Type.INTERN, Majors, semester, university);
                employees.add(intern);
                break;
            }

            default:
                break;
        }
    }

    private static Employee Edit(String ID, List employees) {
        int key = -1;
        for (Iterator i = employees.iterator(); i.hasNext();) {
            Employee employee = (Employee) i.next();
            if (!ID.equals(employee.getID())) continue;

            System.out.println("-------------------------------");
            System.out.println("-           EDIT              -");
            System.out.println("-    1. Name                  -");
            System.out.println("-    2. Birthday              -");
            System.out.println("-    3. Phone                 -");
            System.out.println("-    4. Email                 -");
            System.out.println("-    5. Type                  -");
            System.out.println("-------------------------------");
            System.out.print("Enter option: ");
            key = sc.nextInt();
            switch (key) {
                case 1: {
                    System.out.print("Enter Name: ");
                    String name = sc.next();
                    employee.setFullName(name);
                }

                case 2: {
                    System.out.print("Enter birthday");
                    String birthday = sc.next();
                    employee.setBirthday(birthday);
                }

                case 3: {
                    System.out.print("Enter phone number: ");
                    String phone = sc.next();
                    employee.setPhone(phone);
                }

                case 4: {
                    System.out.print("Enter email: ");
                    String email = sc.next();
                    employee.setEmail(email);
                }

                case 5: {
                    String FullName, Birthday, Phone, Email;
                    System.out.println("-------------Employee Type-------------");
                    System.out.println("-            0. Experience            -");
                    System.out.println("-            1. Fresher               -");
                    System.out.println("-            2. Intern                -");
                    System.out.println("---------------------------------------");
                    System.out.print("Enter option: ");
                    int key_Type = sc.nextInt();

                    switch (key_Type) {
                        case 0: {
                            if (Type.EXPERIENCE == employee.getEmployee_Type()) {
                                System.out.println("No need to change");
                                break;
                            }
                            String expInYear, proSkill;
                            FullName = employee.getFullName();
                            Birthday = employee.getBirthday();
                            Phone = employee.getPhone();
                            Email = employee.getEmail();
                            System.out.print("Enter Exp in year: ");
                            expInYear = sc.next();
                            System.out.print("Enter Pro Skill: ");
                            proSkill = sc.next();
                            Employee newEmployee = new Experience(ID, FullName, Birthday, Phone, Email, Type.EXPERIENCE, expInYear, proSkill);
                            employees.remove(employee);
                            employees.add(newEmployee);
                            break;
                        }

                        case 1: {
                            if (Type.FRESHER == employee.getEmployee_Type()) {
                                System.out.println("No need to change");
                                break;
                            }
                            String Graduation_date, Graduation_rank, Education;
                            System.out.print("Enter Graduation Date: ");
                            Graduation_date = sc.next();
                            System.out.print("Enter graduation rank: ");
                            Graduation_rank = sc.next();
                            System.out.print("Enter Education: ");
                            Education = sc.next();
                            Employee newEmployee = new Fresher(ID, employee.getFullName(), employee.getBirthday(), employee.getPhone(),
                                    employee.getEmail(), Type.FRESHER, Graduation_date, Graduation_rank, Education);
                            employees.remove(employee);
                            employees.add(newEmployee);
                            break;
                        }

                        case 2: {
                            if (Type.INTERN == employee.getEmployee_Type()) {
                                System.out.println("No need to change");
                                break;
                            }
                            String Majors, semester, university;
                            System.out.print("Enter Majors: ");
                            Majors = sc.next();
                            System.out.print("Enter semester: ");
                            semester = sc.next();
                            System.out.print("Enter university: ");
                            university = sc.next();
                            Employee newEmployee = new Intern(ID, employee.getFullName(), employee.getBirthday(), employee.getPhone(), employee.getEmail(),
                                    Type.INTERN, Majors, semester, university);
                            employees.remove(employee);
                            employees.add(newEmployee);
                        }
                        default: break;
                    }
                }
                default:
                    break;
            }
            return employee;
        }
        return null;
    }

    private static Employee Delete(String id, List employees) {
        for (Iterator i = employees.iterator(); i.hasNext();) {
            Employee employee = (Employee) i.next();
            if (!id.equals(employee.getID())) continue;
            employees.remove(employee);
            return employee;
        }
        System.out.println("ID is invalid or not found in List");
        return null;
    }
}
