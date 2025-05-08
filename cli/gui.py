import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from algorithms.basic_lsb_steganography import encode, decode
import os

# Main Window
root = tk.Tk()
root.title("Audio Steganography")
root.geometry("800x600")
root.config(bg="#F0F4F8")

# Global paths
input_file_path = ""
output_file_path = ""

# Style
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TEntry", font=("Segoe UI", 10))

# ---- FUNCTIONS ----

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    input_file_label.config(text=os.path.basename(input_file_path))

def select_output_file():
    global output_file_path
    output_file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    output_file_label.config(text=os.path.basename(output_file_path))

def encode_message():
    message = secret_entry.get()
    if not input_file_path:
        messagebox.showerror("Error", "Select input file")
        return
    if not message:
        messagebox.showerror("Error", "Enter a secret message")
        return
    try:
        save_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if not save_path:
            return
        encode(input_file_path, save_path, message)
        messagebox.showinfo("Success", f"Message encoded and saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decode_message():
    if not output_file_path:
        messagebox.showerror("Error", "Select a file to decode")
        return
    try:
        decoded = decode(output_file_path)
        if decoded:
            decoded_msg_label.config(text=f"Decoded: {decoded}")
        else:
            messagebox.showerror("Error", "No message found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def check_accuracy():
    original = original_msg_entry.get().strip()
    decoded = decoded_msg_label.cget("text").replace("Decoded: ", "").strip()
    if not original:
        messagebox.showerror("Error", "Enter original message")
        return
    if original == decoded:
        accuracy_result.config(text="Accuracy: Matched✅", fg="green")
    else:
        accuracy_result.config(text="Accuracy: Not Matched❌", fg="red")

# ---- LAYOUT ----

# Header
tk.Label(root, text="Audio Steganography Tool", bg="#4CAF50", fg="white", font=("Segoe UI", 18, "bold")).pack(fill="x", pady=10)

main_frame = tk.Frame(root, bg="#F0F4F8")
main_frame.pack(expand=True, fill="both", padx=20, pady=10)

# Left (Encode)
encode_frame = tk.LabelFrame(main_frame, text="Encode", font=("Segoe UI", 12, "bold"), bg="#E8F5E9", width=400, height=300, bd=2, relief="groove")
encode_frame.pack(side="left", fill="y", padx=20, pady=10)
encode_frame.pack_propagate(False)  # Prevent shrinking

ttk.Button(encode_frame, text="Select Input File", command=select_input_file).pack(pady=8)
input_file_label = tk.Label(encode_frame, text="No file selected", bg="#E8F5E9", anchor="w", wraplength=360)
input_file_label.pack(pady=4, fill="x", padx=10)

tk.Label(encode_frame, text="Secret Message", bg="#E8F5E9").pack(pady=(10, 0))
secret_entry = ttk.Entry(encode_frame, width=45)
secret_entry.pack(pady=5)

ttk.Button(encode_frame, text="Encode Message", command=encode_message).pack(pady=10)

# Right (Decode)
decode_frame = tk.LabelFrame(main_frame, text="Decode", font=("Segoe UI", 12, "bold"), bg="#E3F2FD", width=400, height=300, bd=2, relief="groove")
decode_frame.pack(side="right", fill="y", padx=20, pady=10)
decode_frame.pack_propagate(False)  # Prevent shrinking

ttk.Button(decode_frame, text="Select Encoded File", command=select_output_file).pack(pady=8)
output_file_label = tk.Label(decode_frame, text="No file selected", bg="#E3F2FD", anchor="w", wraplength=360)
output_file_label.pack(pady=4, fill="x", padx=10)

ttk.Button(decode_frame, text="Decode Message", command=decode_message).pack(pady=10)
decoded_msg_label = tk.Label(decode_frame, text="Decoded: ", bg="#E3F2FD", fg="black", wraplength=360)
decoded_msg_label.pack(pady=5, padx=10)


# Center-Bottom (Accuracy Check)
accuracy_frame = tk.Frame(root, bg="#F0F4F8")
accuracy_frame.pack(pady=15)

tk.Label(accuracy_frame, text="Enter Original Secret Message:", bg="#F0F4F8").pack()
original_msg_entry = ttk.Entry(accuracy_frame, width=50)
original_msg_entry.pack(pady=5)

ttk.Button(accuracy_frame, text="Check Accuracy", command=check_accuracy).pack(pady=8)

accuracy_result = tk.Label(accuracy_frame, text="Accuracy: ", bg="#F0F4F8", font=("Segoe UI", 12))
accuracy_result.pack(pady=5)

# Run loop
root.mainloop()
