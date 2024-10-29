import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os
import time
import json
from openai import OpenAI
import support

support.set_env_vars_from_json('env_vars.json')

# Загружаем стили из файла
def load_styles():
    if os.path.exists('styles.json'):
        with open('styles.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# Сохраняем стили в файл
def save_styles():
    with open('styles.json', 'w', encoding='utf-8') as f:
        json.dump(TEMPLATE_PROMPTS, f, ensure_ascii=False, indent=4)

# Инициализация стилей
TEMPLATE_PROMPTS = {
    "Стандарт": "4k {}",
    "Чарльз Монро": "В стиле комиксов Peanuts Чарльза Монро Шульца. Мягкие, округлые линии, насыщенные цвета, тёплая и умиротворённая атмосфера, вертикальная ориентация, без текста, максимальное качество, детализированные тени. {}",
    "Скотт Адамс": "Изображение под стиль комиксов Dilbert, офисная обстановка, атмосфера комичная, с простыми линиями и насыщенной цветовой гаммой, вертикальная ориентация, максимальное качество, без текста, гладкие текстуры, детализированные тени. {}"
}

# Загружаем стили из файла
loaded_styles = load_styles()
TEMPLATE_PROMPTS.update(loaded_styles)

# Запрос на генерацию мема
def generate_dalle_image(prompt, style):
    full_prompt = TEMPLATE_PROMPTS[style].format(prompt)
    if len(full_prompt) > 1000:
        messagebox.showwarning("Prompt Error", "Запрос слишком длинный.")
        return None
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=full_prompt,
        size="1024x1792",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    return image_url

def add_text_to_image(image, top_text, bottom_text):
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("impact.ttf", 60)
    except IOError:
        font = ImageFont.load_default()
    
    def draw_text(draw, text, position, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (image.width - text_width) / 2
        draw.text((x, position), text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    draw_text(draw, top_text, 20, font)
    draw_text(draw, bottom_text, image.height - 85, font)

    return image

def save_and_show_image(url, top_text, bottom_text):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = add_text_to_image(img, top_text, bottom_text)
    
    os.makedirs("images", exist_ok=True)
    
    file_path = f"images/{int(time.time())}.jpg"
    img.save(file_path)
    img.show()
    print(f"Image saved at {file_path}")

def on_generate_click():
    prompt_text = text_entry.get("1.0", "end-1c")
    selected_style = style_combobox.get()
    if not prompt_text:
        messagebox.showwarning("Input Error", "Введите промт.")
        return
    try:
        image_url = generate_dalle_image(prompt_text, selected_style)
        if image_url:
            save_and_show_image(image_url, top_text_entry.get(), bottom_text_entry.get())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def paste_from_clipboard():
    try:
        clipboard_text = app.clipboard_get()
        text_entry.delete("1.0", "end")
        text_entry.insert("1.0", clipboard_text)
    except tk.TclError:
        messagebox.showwarning("Clipboard Error", "Буфер обмена пуст.")

def toggle_add_style_frame():
    if add_style_frame.winfo_viewable():
        add_style_frame.pack_forget()
    else:
        add_style_frame.pack(pady=(10, 0))

def add_custom_style():
    new_style_name = new_style_name_entry.get().strip()
    new_style_template = new_style_template_entry.get().strip()

    if not new_style_name or not new_style_template:
        messagebox.showwarning("Input Error", "Заполните оба поля.")
        return

    if new_style_name in TEMPLATE_PROMPTS:
        messagebox.showwarning("Duplicate Style", "Стиль с таким именем уже существует.")
        return

    TEMPLATE_PROMPTS[new_style_name] = new_style_template
    style_combobox["values"] = list(TEMPLATE_PROMPTS.keys())
    style_combobox.set(new_style_name)
    messagebox.showinfo("Success", f"Новый стиль '{new_style_name}' добавлен.")
    save_styles()  # Сохраняем стили в файл
    toggle_add_style_frame()

app = tk.Tk()
app.title("Генератор мемов")
app.geometry("600x650")
app.configure(bg="#1e1e2e")

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#1e1e2e", 
                foreground="#c8d3f5", 
                font=("Arial", 12))
style.configure("TButton", background="#44475a", 
                foreground="#f8f8f2", 
                font=("Arial", 10, "bold"))
style.map("TButton", background=[("active", "#6272a4")])

ttk.Label(app, text="Введите промт:").pack(pady=(10, 0))
text_entry = tk.Text(app, width=70, height=5, wrap="word", bg="#282a36", fg="#f8f8f2", insertbackground="white")
text_entry.pack(pady=(0, 10))

paste_button = ttk.Button(app, text="Вставить из буфера", 
                          command=paste_from_clipboard)
paste_button.pack()

ttk.Label(app, text="Выберите стиль:").pack(pady=(10, 0))
style_combobox = ttk.Combobox(app, values=list(TEMPLATE_PROMPTS.keys()), 
                              state="readonly")
style_combobox.set("Стандарт")
style_combobox.pack(pady=(0, 10))

ttk.Label(app, text="Надпись сверху:").pack(pady=(10, 0))
top_text_entry = tk.Entry(app, width=50, bg="#282a36", fg="#f8f8f2", insertbackground="white")
top_text_entry.pack(pady=(0, 10))

ttk.Label(app, text="Надпись снизу:").pack(pady=(10, 0))
bottom_text_entry = tk.Entry(app, width=50, bg="#282a36", fg="#f8f8f2", insertbackground="white")
bottom_text_entry.pack(pady=(0, 10))

add_style_button = ttk.Button(app, text="Добавить стиль", command=toggle_add_style_frame)
add_style_button.pack(pady=(10, 0))

add_style_frame = tk.Frame(app, bg="#1e1e2e")
ttk.Label(add_style_frame, text="Название стиля:").pack(pady=(5, 0))
new_style_name_entry = tk.Entry(add_style_frame, width=50, bg="#282a36", fg="#f8f8f2", insertbackground="white")
new_style_name_entry.pack(pady=(0, 5))

ttk.Label(add_style_frame, text="Шаблон стиля (используйте {} для вставки текста):").pack(pady=(5, 0))
new_style_template_entry = tk.Entry(add_style_frame, width=50, bg="#282a36", fg="#f8f8f2", insertbackground="white")
new_style_template_entry.pack(pady=(0, 5))

save_style_button = ttk.Button(add_style_frame, text="Сохранить стиль", command=add_custom_style)
save_style_button.pack(pady=(5, 10))

generate_button = ttk.Button(app, text="Сгенерировать", command=on_generate_click)
generate_button.pack(pady=20)

app.mainloop()
