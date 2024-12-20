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
    "fruit": {"japanese": "kudamono"}
}

French_Dictionary = {
    'good morning' : 'Bonjour',
    'good evening' : 'Bonsoir',
    'goodbye' : 'Au revoir',
    'hi' : 'Salut',
    'hello' : 'Coucou',
    'see you later' : 'a plus tard',
    'see you soon' : 'a bientot',
    'goodnight' : 'Bonne nuit',
    'thank you' : 'Mercii',
    'please' : 'Sil vous plait',
     '0' : 'Zero',
     '1' : 'Un',
     '2' : 'Deux',
     '3' : "Trios",
     '4' : "Quatre",
     '5' : "Cinq",
     '6' : "Six",
     '7' : "Sept",
     '8' : "Huit",
     '9' : "Nuef",
     '10' : "Dix",
     '11' : "Onze",
     '12' : "Douze",
     '13' : "Trieze",
     '14' : "Quatorze",
     '15' : "Quinze",
     '16' : "Seize",
     '17' : 'Dix-sept',
     '18' : 'Dix-huit',
     '19' : 'Dix-neuf',
     '20' : 'Vingt',
     'red' : 'Rouge',
     'gray' : 'Gris',
     'pink' : 'Rose',
     'black' : 'Noir',
     'brown' : 'Marron',
     'blue' : 'Bleu',
     'green' : 'Vert',
     'white' : 'Blanc',
     'yellow' : 'Jaunce',
     'purple' : 'pourpre',
    'cat' : 'Chat',
    'dog' : 'Chien',
    'lion' : 'Le lion',
     'goldfish' : 'Un poisson rouge',
     'mouse' : 'UNe souris',
     'turtle' : 'une tujrtle',
     'rabbit' : 'Un lapin',
     'wolf': 'Le loup',
     'monkey' : 'Le singe',
     'hamster' : 'Un hamster',
    'avec' : 'With',
    'Amour' : 'Love',
    'Bonheur' : 'happiness',
    'La Fille' : 'Girl',
    'La Garcon' : 'Boy',
    'La plage' : 'Beach',
    'Metro' : 'Subway',
    'Voiture' : 'Car',
    'Vin' : 'Wine',
    'Pain' : 'Bread',
    'Billet' : 'Ticket',
    'Viande' : 'Meat',
}

spanish_Dictionary = {
	
     "greetings": {
            "hello": "hola",
            "goodbye": "adiós",
            "please": "por favor",
            "thank_you": "gracias",
            "you're_welcome": "de nada",
	     "Good_night": "Buenas noches",
	     "Good_day": "Buenos dias",
	     "Good_afternoon": "Beunos tardes",
	     "Farewell": "Hasta pronto",
        },
        "colors": {
            "red": "rojo",
            "blue": "azul",
            "green": "verde",
            "yellow": "amarillo",
            "black": "negro",
            "white": "blanco",
		"Grey": "Gris",
		"purple": "Morado",
		"Brown": "cafe/marron", 
		"Pink": "Rosado",
		"violet": "violeta",
		"Navy_Blue": "azul_marino",
		"Turquoise": "Turquesa",
		"Lilac": "Lila",
		"Sky_Blue": "Celeste",
        },
        "numbers": {
            1: "uno",
            2: "dos",
            3: "tres",
            4: "cuatro",
            5: "cinco",
	    6: "sies",
	    7: "siete",
            8: "ocho",
	    9: "nueve",
           10: "diez",
	   11: "once",
           12: "doce",
	   13: "trece",
	   14: "catorce",
	   15: "quince",
	   16: "dieciseis",
	   17: "diecisiete",
	   18: "dieciocho",
	   19: "diecenueve",
	   20: "veinte",	
        },
	"verbs": {
		"irregular_verbs":{
			"to abandon": "abandonar",
			"to hug": "abrazar",
			"to find out": "averiguar",
			"to dance": "bailar",
			"to bathe": "banar",
			"to walk": "caminar",
			"to sing": "cantar",
			"to speak": "hablar",
			"to taste": "degustar",
			"to fight": "luchar"
		},
		"regular_verbs": {
			"to learn": "aprender",
			"to appear": "aparecer",
			"to sweep": "barrer",
			"to sew": "coser",
			"to offend": "ofender",
			"to fear": "temer",
			"to sell": "vender",
			"to run": "correr",
			"to eat": "comer"
		}
	}
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
