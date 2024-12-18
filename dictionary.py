import tkinter as tk
from tkinter import ttk


dictionary = {
    "house": {"japanese": "ie"},
    "car": {"japanese": "kuruma"},
    "road": {"japanese": "michi"},
    "book": {"japanese": "hon"},
    "clock": {"japanese": "tokei"},
    "phone": {"japanese": "denwa"},
    "school": {"japanese": "gakko"},
    "teacher": {"japanese": "sensei"},
    "friend": {"japanese": "tomodachi"},
    "love": {"japanese": "ai"},
    "hello": {"japanese": "konnichiwa"},
    "goodbye": {"japanese": "sayonara"},
    "thank you": {"japanese": "arigato"},
    "good morning": {"japanese": "ohayo"},
    "excuse me": {"japanese": "sumimasen"},
    "flower": {"japanese": "hana"},
    "mountain": {"japanese": "yama"},
    "sea": {"japanese": "umi"},
    "sky": {"japanese": "sora"},
    "moon": {"japanese": "tsuki"},
    "one": {"japanese": "ichi"},
    "two": {"japanese": "ni"},
    "ten": {"japanese": "ju"},
    "three": {"japanese": "san"},
    "four": {"japanese": "shi/yon"},
    "five": {"japanese": "go"},
    "seven": {"japanese": "shichi/nana"},
    "six": {"japanese": "roku"},
    "nine": {"japanese": "kyu/ku"},
    "eight": {"japanese": "hachi"},
    "rain": {"japanese": "ame"},
    "snow": {"japanese": "yuki"},
    "wind": {"japanese": "kaze"},
    "forest": {"japanese": "mori"},
    "water": {"japanese": "mizu"},
    "tea": {"japanese": "ocha"},
    "meat": {"japanese": "niku"},
    "rice": {"japanese": "gohan"},
    "fish": {"japanese": "sakana"},
    "alcoholic drink": {"japanese": "sake"},
    "fruit": {"japanese": "kudamono"},
	##########################################################
    "come": {"spanish": "man"},
    "boy": {"spanish": "book"},
    "let": {"spanish": "mark"},
    "go": {"spanish": "book"},
    "meet": {"spanish": "mad"},
    "goat": {"spanish": "mango"},
    "make": {"spanish": "baber"},
    "we": {"spanish": "tire"},
}


def translate_word():
    word = entry_word.get().strip().lower()  
    selected_language = combo_language.get().lower()  

    
    if word in dictionary:
        translation = dictionary[word].get(selected_language, "Translation not available")
        label_result.config(text=f"Translation: {translation}")
    else:
        
        found = False
        for eng_word, translations in dictionary.items():
            if translations.get(selected_language) == word:
                label_result.config(text=f"Translation: {eng_word}")
                found = True
                break
        if not found:
            label_result.config(text="Word not found in the dictionary.")


root = tk.Tk()
root.title("Simple Multilingual Dictionary")
root.geometry("400x300")


label_title = tk.Label(root, text="Multilingual Dictionary", font=("Arial", 17, "bold"))
label_title.pack(pady=10)


frame_word = tk.Frame(root)
frame_word.pack(pady=10)

label_word = tk.Label(frame_word, text="Enter Word:")
label_word.pack(side=tk.LEFT, padx=5)

entry_word = tk.Entry(frame_word, width=20)
entry_word.pack(side=tk.LEFT, padx=5)


frame_language = tk.Frame(root)
frame_language.pack(pady=10)

label_language = tk.Label(frame_language, text="Select Language:")
label_language.pack(side=tk.LEFT, padx=5)


combo_language = ttk.Combobox(frame_language, values=["japanese" ,"spanish", "French", "Italian", "German" ], state="readonly")
combo_language.pack(side=tk.LEFT, padx=5)
combo_language.set("japanese")  


button_translate = tk.Button(root, text="Translate", command=translate_word)
button_translate.pack(pady=10)


label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)


root.mainloop()
