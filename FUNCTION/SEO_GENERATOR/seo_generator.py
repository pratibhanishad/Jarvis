def seo_app():
    import tkinter as tk
    from tkinter import scrolledtext
    from g4f.client import Client

    # LLM Function
    def llm2(text):
        client = Client()
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",   # ✅ Supported model
                messages=[{"role": "user", "content": f"{text}"}],
                ignore_working=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ Error: {e}"

    # Function to generate title and description
    def generate_title_and_description():
        loading_label.config(text="Generating...", fg="blue")
        root.update()

        topic = topic_entry.get()

        title_text = f"Write the best SEO-based YouTube title (under 80 words) for topic: {topic}"
        title_result.set(llm2(title_text))

        description_text = f"Write the best SEO-based YouTube description with exactly 50 keywords for topic: {topic}"
        description_result.set(llm2(description_text))

        loading_label.config(text="")
        root.update()

    # Tkinter setup
    root = tk.Tk()
    root.title("SEO Title and Description Generator")
    root.geometry("900x700")
    root.configure(bg="#282c34")  # Dark theme

    # Topic Entry
    topic_label = tk.Label(root, text="Enter the topic:", fg="white", bg="#282c34", font=("Helvetica", 12))
    topic_label.pack(pady=5)

    topic_entry = tk.Entry(root, bg="#D3D3D3", font=("Helvetica", 12))
    topic_entry.pack(pady=5)

    # Generate Button
    generate_button = tk.Button(root, text="Generate", command=lambda: (generate_title_and_description(), check_completion()),
                                bg="#61dafb", fg="white", font=("Helvetica", 12, "bold"))
    generate_button.pack(pady=10)

    # Loading Label
    loading_label = tk.Label(root, text="", fg="blue", bg="#282c34", font=("Helvetica", 12, "italic"))
    loading_label.pack()

    # Title Output
    title_result = tk.StringVar()
    title_label = tk.Label(root, text="Generated Title:", font=("Helvetica", 12, "bold"), fg="white", bg="#282c34")
    title_label.pack()
    title_output = scrolledtext.ScrolledText(root, width=100, height=5, wrap=tk.WORD, bg="#D3D3D3", fg="#282c34", font=("Helvetica", 11))
    title_output.pack(pady=5)

    # Description Output
    description_result = tk.StringVar()
    description_label = tk.Label(root, text="Generated Description:", font=("Helvetica", 12, "bold"), fg="white", bg="#282c34")
    description_label.pack()
    description_output = scrolledtext.ScrolledText(root, width=100, height=12, wrap=tk.WORD, bg="#D3D3D3", fg="#282c34", font=("Helvetica", 11))
    description_output.pack(pady=5)

    # Update outputs
    def update_outputs():
        title_output.delete(1.0, tk.END)
        title_output.insert(tk.END, title_result.get())

        description_output.delete(1.0, tk.END)
        description_output.insert(tk.END, description_result.get())

    # Check completion loop
    def check_completion():
        if loading_label.cget("text") == "Generating...":
            root.after(100, check_completion)
        else:
            update_outputs()

    root.mainloop()

