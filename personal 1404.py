import tkinter as tk

# Function triggered when envelope is clicked
def open_message():
    popup = tk.Toplevel(root)
    popup.title("A Message For You 💌")
    popup.geometry("420x320")
    popup.configure(bg="#ffd6e7")

    msg = (
        "Hey Love 💖\n\n"
        "I never really understood what\n"
        "\"mine\" truly meant...\n\n"
        "until YOU walked into my life.\n\n"
        "And now my world feels warmer,\n"
        "happier and complete with you.\n\n"
        "I LOVE YOU, MAYUR ❤️"
    )

    label = tk.Label(
        popup,
        text=msg,
        font=("Arial", 12, "bold"),
        bg="#ffd6e7",
        justify="center"
    )
    label.pack(pady=20)

    close_btn = tk.Button(
        popup,
        text="Close 💕",
        font=("Arial", 12, "bold"),
        command=popup.destroy,
        bg="#ff8fab",
        fg="white",
        padx=10,
        pady=5
    )
    close_btn.pack(pady=10)


# Main window
root = tk.Tk()
root.title("Special Message App")
root.geometry("400x500")
root.configure(bg="#ffc0cb")

# Title
title = tk.Label(
    root,
    text="Tap the Envelope",
    font=("Arial", 18, "bold"),
    bg="#ffc0cb"
)
title.pack(pady=40)

# Envelope button
envelope_btn = tk.Button(
    root,
    text="💌",
    font=("Arial", 80),
    command=open_message,
    bg="white",
    relief="raised",
    bd=5
)
envelope_btn.pack(pady=50)

footer = tk.Label(
    root,
    text="A little surprise inside...",
    font=("Arial", 12),
    bg="#ffc0cb"
)
footer.pack(pady=20)

root.mainloop()
