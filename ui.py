import tkinter as tk
from steps import (
    step_1_all,
    step_2_all,
    step_3_1,
    step_3_2,
    step_3_3,
    step_3_4,

)
from styles import btn_params, header_font, title_font

        
def make_step_frame(parent, text):
    frame = tk.Frame(
        parent,
        bg="#ffe5ea",  
        bd=2,
        relief="ridge",
        padx=2,
        pady=3
    )
    label = tk.Label(
        frame,
        text=text + " ❤ ",
        font=header_font,
        fg="#064444",  
        bg="#fce7eb"
    )
    label.pack(anchor="w", pady=(0, 1))
    return frame

def create_main_window():
    window = tk.Tk()
    window.title(" Cool Coco 🥥")
    window.geometry("400x480")
    window.configure(bg="#ebfac8")  
    tk.Label(
        window,
        text=" Eccang TP Lite",
        font=title_font,
        fg="#022424",  
        bg="#ebfac8"
    ).pack(pady=6)

    # Step 1
    frame1 = make_step_frame(window, "Eccang Process")
    frame1.pack(padx=25, pady=10, fill="x")
    tk.Button(
    frame1,
    text= "Unzip, Convert, Rename,Copy",
    command=step_1_all,
    **btn_params
    ).pack(padx=4, pady=2)


    # Step 2
    frame2 = make_step_frame(window, "Refresh 1.1")
    frame2.pack(padx=25, pady=10, fill="x")
    tk.Button(
        frame2, 
        text="Open 1.1", 
        command=step_2_all, 
        **btn_params
        ).pack(padx=4, pady=2)

    # Step 2
    frame3 = make_step_frame(window, "TP Upload")
    frame3.pack(padx=25, pady=10, fill="x")
    tk.Button(
        frame3, 
        text="Open 2.1", 
        command=step_3_1, 
        **btn_params
        ).pack(padx=4, pady=2)

    tk.Button(
        frame3, 
        text="Generate & Upload & Copy TP", 
        command=step_3_2, 
        **btn_params
        ).pack(padx=4, pady=2)
    
    tk.Button(
        frame3, 
        text="Open SKUINV", 
        command=step_3_3, 
        **btn_params
        ).pack(padx=4, pady=2)

    tk.Button(
        frame3, 
        text="Copy SKUINV", 
        command=step_3_4, 
        **btn_params
        ).pack(padx=4, pady=2)

    return window
