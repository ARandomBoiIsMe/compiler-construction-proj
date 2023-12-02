import tkinter as tk
from tkinter import filedialog
import subprocess

class VSCodeStyleIDE:
    def __init__(self, root):
        self.root = root
        self.root.title('VSCode-Style IDE')
        self.file_path = ''
        self.create_widgets()

    def create_widgets(self):
        # Configure root background color
        self.root.configure(bg="#1e1e1e")

        # Text editor
        self.text_editor = tk.Text(self.root, wrap="word", undo=True, fg="#d4d4d4", bg="#1e1e1e", insertbackground="#d4d4d4", font=("Courier New", 12))
        self.text_editor.pack(expand="yes", fill="both")

        # Menu Bar
        self.menu_bar = tk.Menu(self.root, fg="#d4d4d4", bg="#333333", font=("Segoe UI", 10))
        self.root.config(menu=self.menu_bar)

        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0, fg="#d4d4d4", bg="#333333", font=("Segoe UI", 10))
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Run Menu
        run_menu = tk.Menu(self.menu_bar, tearoff=0, fg="#d4d4d4", bg="#333333", font=("Segoe UI", 10))
        run_menu.add_command(label="Run", command=self.run_code)
        self.menu_bar.add_cascade(label="Run", menu=run_menu)

        # Output Text
        self.output_text = tk.Text(self.root, height=10, wrap="word", fg="#d4d4d4", bg="#1e1e1e", font=("Courier New", 12))
        self.output_text.pack(expand="yes", fill="both")

    def new_file(self):
        self.text_editor.delete(1.0, tk.END)
        self.file_path = ''

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[('Text Files', '.txt'), ('All Files', '.*')])
        if path:
            with open(path, 'r') as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)
                self.file_path = path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                content = self.text_editor.get(1.0, tk.END)
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text Files', '.txt'), ('All Files', '.*')])
        if path:
            with open(path, 'w') as file:
                content = self.text_editor.get(1.0, tk.END)
                file.write(content)
                self.file_path = path

    def run_code(self):
        code = self.text_editor.get(1.0, tk.END)
        process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        self.output_text.delete(1.0, tk.END)

        if output:
            self.output_text.insert(tk.END, "Output:\n")
            self.output_text.insert(tk.END, output.decode('utf-8'))

        if error:
            self.output_text.insert(tk.END, "Error:\n")
            self.output_text.insert(tk.END, error.decode('utf-8'))

if __name__ == "__main__":
    root = tk.Tk()
    ide = VSCodeStyleIDE(root)
    root.geometry("800x600")
    root.mainloop()