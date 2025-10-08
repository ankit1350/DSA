import java.util.*;
import java.io.*;

class AttendanceSystem {
    static HashMap<String, String> students = new HashMap<>();
    static HashMap<String, String> attendance = new HashMap<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int choice;
        do {
            System.out.println("\n===== ATTENDANCE MANAGEMENT SYSTEM =====");
            System.out.println("1. Add Student");
            System.out.println("2. Mark Attendance");
            System.out.println("3. View Attendance");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // clear buffer

            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    markAttendance();
                    break;
                case 3:
                    viewAttendance();
                    break;
                case 4:
                    System.out.println("Exiting... Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        } while (choice != 4);
    }

    static void addStudent() {
        System.out.print("Enter Student ID: ");
        String id = sc.nextLine();
        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();
        students.put(id, name);
        System.out.println("Student Added Successfully!");
    }

    static void markAttendance() {
        if (students.isEmpty()) {
            System.out.println("No students found! Please add students first.");
            return;
        }

        System.out.println("Mark Attendance (P/A):");
        for (String id : students.keySet()) {
            String status;
            while (true) {
            System.out.print(students.get(id) + " (" + id + "): ");//
            status = sc.nextLine().trim().toUpperCase();
            if (status.equals("P") || status.equals("A")) {
                attendance.put(id, status);
                break;
            } else {
                System.out.println("Invalid input! Please enter 'P' for Present or 'A' for Absent.");
            }
            }
        }
        System.out.println("Attendance Marked Successfully!");
    }

    static void viewAttendance() {
        if (attendance.isEmpty()) {
            System.out.println("No attendance data available!");
            return;
        }

        System.out.println("\n--- Attendance Report ---");
        for (String id : attendance.keySet()) {
            System.out.println(students.get(id) + " (" + id + "): " + attendance.get(id));
        }
    }
}
