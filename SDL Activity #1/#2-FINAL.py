import tkinter as tk
from PIL import Image, ImageTk


class Student:
    def __init__(self, name, quizzes):
        self.name = name
        self.quizzes = quizzes

    def forda_average(self):
        return sum(self.quizzes) / len(self.quizzes)


class Section:
    def __init__(self):
        self.students = []
        self.student_details_window = None  # To store reference to the student details window
        self.bg_image_main = None
        self.bg_image_detail = None

    def add_student(self, name, quizzes):
        student = Student(name, quizzes)
        self.students.append(student)

    def display_student_details(self):
        top = tk.Toplevel()
        top.title("Student Details")

        # Setting background image for student details window
        bg_label = tk.Label(top, image=self.bg_image_detail)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(top, text=f"Class Record for Every Student")
        title_label.pack()

        for i, student in enumerate(self.students, start=1):
            label_name = tk.Label(top, text=f"Student {i}: {student.name}")
            label_name.pack()

            label_quizzes = tk.Label(top, text=f"Quizzes: {student.quizzes}")
            label_quizzes.pack()

            label_average = tk.Label(top, text=f"Average: {student.forda_average()}")
            label_average.pack()
            label_blank = tk.Label(top, text="")
            label_blank.pack()

    def display_class_averages(self):
        top = tk.Toplevel()
        top.title("Class Averages")

        # Setting background image for class averages window
        bg_label = tk.Label(top, image=self.bg_image_detail)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        num_students = len(self.students)
        num_quizzes = len(self.students[0].quizzes)

        title_label = tk.Label(top, text=f"Class Average for Every Quiz")
        title_label.pack()

        for i in range(num_quizzes):
            quizzes = [student.quizzes[i] for student in self.students]
            ave_quizzes = sum(quizzes) / num_students
            label_average = tk.Label(top, text=f"Quiz {i + 1} Average: {ave_quizzes}")
            label_average.pack()
            label_blank = tk.Label(top, text="")
            label_blank.pack()

    def get_student_names(self, students_total, quizzes_total):
        for i in range(students_total):
            student_name = self.entry_vars[i].get()
            quizzes = []
            for j in range(quizzes_total):
                quiz = int(self.quiz_entries[i][j].get())
                quizzes.append(quiz)
            self.add_student(student_name, quizzes)

        # Open new window after submitting student names
        self.display_student_details()

    def create_student_entries(self, root, students_total, quizzes_total, bg_image_path):
        self.entry_vars = []
        self.quiz_entries = []

        # Create a new window for student details
        self.student_details_window = tk.Toplevel(root)
        self.student_details_window.title("Student Details")

        # Setting background image for student entries window
        self.bg_image_detail = ImageTk.PhotoImage(Image.open(bg_image_path))
        bg_label = tk.Label(self.student_details_window, image=self.bg_image_detail)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        padding_row = 3
        for i in range(students_total):
            quiz_entries_row = []  # Initialize for each student
            label = tk.Label(self.student_details_window, text=f"Student {i + 1} name: ")
            label.grid(row=i * padding_row, column=0, padx=5, pady=5, sticky="e")
            entry_var = tk.StringVar()
            entry = tk.Entry(self.student_details_window, textvariable=entry_var)
            entry.grid(row=i * padding_row, column=1, padx=5, pady=5, sticky="w")
            self.entry_vars.append(entry_var)

            for j in range(quizzes_total):
                label = tk.Label(self.student_details_window, text=f"Quiz {j + 1} grade: ")
                label.grid(row=i * padding_row + j + 1, column=0, padx=5, pady=5, sticky="e")
                entry_var = tk.StringVar()
                entry = tk.Entry(self.student_details_window, textvariable=entry_var)
                entry.grid(row=i * padding_row + j + 1, column=1, padx=5, pady=5, sticky="w")
                quiz_entries_row.append(entry_var)  # Store entry variable
            self.quiz_entries.append(quiz_entries_row)

        label_blank = tk.Label(self.student_details_window, text="")
        label_blank.grid(row=students_total * padding_row + 1, columnspan=2)

        submit_button = tk.Button(self.student_details_window, text="Show Student Scores",
                                  command=lambda: self.get_student_names(students_total, quizzes_total))
        submit_button.grid(row=students_total * padding_row + 2, column=0, columnspan=quizzes_total + 2)

        # Button to display class averages (if needed)
        button_class_averages = tk.Button(self.student_details_window, text="Show Class Averages",
                                          command=lambda: self.display_class_averages())
        button_class_averages.grid(row=students_total * padding_row + 3, column=0, columnspan=quizzes_total + 2)


def create_gui():
    def submit_action():
        num_students_str = entry_students.get()
        num_quizzes_str = entry_quizzes.get()

        # Check if input is not empty
        if num_students_str and num_quizzes_str:
            # Check if input consists of digits only
            if num_students_str.isdigit() and num_quizzes_str.isdigit():
                num_students = int(num_students_str)
                num_quizzes = int(num_quizzes_str)

                # Validate that number of students and quizzes are greater than zero
                if num_students > 0 and num_quizzes > 0:
                    section.create_student_entries(root, num_students, num_quizzes, "bg2.jpg")
                else:
                    tk.messagebox.showerror("Error", "Number of students and quizzes must be greater than zero.")
            else:
                tk.messagebox.showerror("Error", "Please enter valid integer values for students and quizzes.")
        else:
            tk.messagebox.showerror("Error", "Please enter values for students and quizzes.")

    root = tk.Tk()
    root.title("Student Records")

    # Load and display background image for main window
    background_image_main = Image.open("bg1.jpg")
    bg_photo_main = ImageTk.PhotoImage(background_image_main)
    bg_label_main = tk.Label(root, image=bg_photo_main)
    bg_label_main.place(x=0, y=0, relwidth=1, relheight=1)

    label_students = tk.Label(root, text="Enter the number of students: ", bg='white')
    label_students.grid(row=0, column=0)
    entry_students = tk.Entry(root)
    entry_students.grid(row=0, column=1)

    label_quizzes = tk.Label(root, text="Enter the number of quizzes: ", bg='white')
    label_quizzes.grid(row=1, column=0)
    entry_quizzes = tk.Entry(root)
    entry_quizzes.grid(row=1, column=1)

    section = Section()

    submit_button = tk.Button(root, text="Submit", command=submit_action)
    submit_button.grid(row=2, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
