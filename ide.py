from frontend import lexer, parser
from backend import interpreter
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.filedialog as filedialog
import subprocess

process = None

def exec():
    code = text_widget.get("1.0", tk.END)
    
    try:
        process = subprocess.Popen(
            ["python", "main.py", code],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(input=None)

        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, stdout)

        if stderr:
            output_text.insert(tk.END, stderr, "error")

        output_text.config(state=tk.DISABLED)
    except Exception as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")
        output_text.config(state=tk.DISABLED)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", ".py"),("All Files", ".*")])
    if file_path:
        current_file_path = file_path
        with open(file_path, 'r') as file:
            code = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, code)

root = tk.Tk()
root.title("Compiler Construction Group 6")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

run_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Execute", command=exec)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label= "Open", command=open_file)

text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_widget.pack(expand=True, fill='both')
text_widget.configure(font=("TkDefaultFont", 10))

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
output_text.pack(expand=True, fill='both')
output_text.tag_configure("error", foreground="red")
output_text.config(state=tk.DISABLED)

root.mainloop()