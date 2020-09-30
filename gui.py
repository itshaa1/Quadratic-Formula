import tkinter as tk

from quadratic_functions import standard_to_vertex, num_real_answers,\
     find_answers, find_unfactored, find_factored


def display_results():
    a = ent_a.get()
    b = ent_b.get()
    c = ent_c.get()
    quad_disc = int(b) ** 2 - 4 * int(a) * int(c)
    lbl_num_answers["text"] = f"{num_real_answers(int(quad_disc))}"
    lbl_vertex["text"] = f"The vertex form of the equation is: {standard_to_vertex(int(a), int(b), int(c))}"
    lbl_answers["text"] = f"{find_answers(int(quad_disc), int(a), int(b))}"
    lbl_unfactored["text"] = f"The unfactored equation is: {find_unfactored(int(quad_disc), int(a), int(b))}"
    lbl_factored["text"] = f"The factored equation is: {find_factored(int(quad_disc), int(a), int(b))}"


window = tk.Tk()
window.title("Quadratic Solver")
window.resizable(width=False, height=False)

frm_entry_a = tk.Frame(master=window)
frm_entry_b = tk.Frame(master=window)
frm_entry_c = tk.Frame(master=window)
ent_a = tk.Entry(master=frm_entry_a)
ent_b = tk.Entry(master=frm_entry_b)
ent_c = tk.Entry(master=frm_entry_c)
lbl_a = tk.Label(master=frm_entry_a, text="Enter a:")
lbl_b = tk.Label(master=frm_entry_b, text="Enter b:")
lbl_c = tk.Label(master=frm_entry_c, text="Enter c:")

ent_a.grid(row=0, column=1, sticky="w")
lbl_a.grid(row=0, column=0, stick="e")
ent_b.grid(row=1, column=1, sticky="w")
lbl_b.grid(row=1, column=0, stick="e")
ent_c.grid(row=2, column=1, sticky="w")
lbl_c.grid(row=2, column=0, stick="e")

btn_discrim = tk.Button(
    master=window,
    text="Solve",
    command=display_results
)
lbl_vertex = tk.Label(master=window, text="")
lbl_num_answers = tk.Label(master=window, text="")
lbl_answers = tk.Label(master=window, text="")
lbl_unfactored = tk.Label(master=window, text="")
lbl_factored = tk.Label(master=window, text="")

frm_entry_a.grid(row=0, column=1, padx=10)
frm_entry_b.grid(row=1, column=1, padx=10)
frm_entry_c.grid(row=2, column=1, padx=10)
btn_discrim.grid(row=3, column=1, padx=10)

lbl_num_answers.grid(row=4, column=1, padx=10)
lbl_vertex.grid(row=5, column=1, padx=10)
lbl_answers.grid(row=6, column=1, padx=10)
lbl_unfactored.grid(row=7, column=1, padx=10)
lbl_factored.grid(row=8, column=1, padx=10)


window.mainloop()
