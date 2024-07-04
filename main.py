import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        self.students = []
        self.load_students()

        self.create_widgets()
        self.display_students()

    def load_students(self):
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as file:
                for line in file:
                    if line.strip():
                        self.students.append(line.strip().split(","))

    def save_students(self):
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(",".join(student) + "\n")

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, height=10, width=50)
        self.listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Student", command=self.add_student)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Student", command=self.edit_student)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search Students", command=self.search_students)
        self.search_button.grid(row=0, column=3, padx=5)

    def display_students(self, students=None):
        self.listbox.delete(0, tk.END)
        for student in students or self.students:
            self.listbox.insert(tk.END, f"{student[0]} ({student[1]} years old) - Class {student[2]}: Grade {student[3]}")

    def add_student(self):
        name = simpledialog.askstring("Input", "Enter student name:")
        age = simpledialog.askstring("Input", "Enter student age:")
        student_class = simpledialog.askstring("Input", "Enter student class:")
        grade = simpledialog.askstring("Input", "Enter student grade:")

        if name and age and student_class and grade:
            self.students.append([name, age, student_class, grade])
            self.save_students()
            self.display_students()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def edit_student(self):
        selected_student_index = self.listbox.curselection()
        if selected_student_index:
            selected_student_index = selected_student_index[0]
            student = self.students[selected_student_index]

            name = simpledialog.askstring("Input", "Enter student name:", initialvalue=student[0])
            age = simpledialog.askstring("Input", "Enter student age:", initialvalue=student[1])
            student_class = simpledialog.askstring("Input", "Enter student class:", initialvalue=student[2])
            grade = simpledialog.askstring("Input", "Enter student grade:", initialvalue=student[3])

            if name and age and student_class and grade:
                self.students[selected_student_index] = [name, age, student_class, grade]
                self.save_students()
                self.display_students()
            else:
                messagebox.showwarning("Input Error", "All fields are required.")
        else:
            messagebox.showwarning("Selection Error", "Please select a student to edit.")

    def delete_student(self):
        selected_student_index = self.listbox.curselection()
        if selected_student_index:
            selected_student_index = selected_student_index[0]
            del self.students[selected_student_index]
            self.save_students()
            self.display_students()
        else:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")

    def search_students(self):
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if search_term:
            search_results = [student for student in self.students if search_term.lower() in " ".join(student).lower()]
            if search_results:
                self.display_students(search_results)
            else:
                messagebox.showinfo("Search Results", "No students found matching the search term.")
        else:
            self.display_students()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
