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
 {
    'good morning' : {"French" :'Bonjour'},
    'good evening' : {"French" :'Bonsoir'},
    'goodbye' : {"French" :'Au revoir'},
    'hi' : {"French" :'Salut'},
    'hello' : {"French" :'Coucou'},
    'see you later' : {"French" :'a plus tard'},
    'see you soon' : {"French" :'a bientot'},
    'goodnight' : {"French" :'Bonne nuit'},
    'thank you' : {"French" :'Mercii'},
    'please' : {"French" :'Sil vous plait'},
     '0' : {"French" :'Zero'},
     '1' : {"French" :'Un'},
     '2' : {"French" :'Deux'},
     '3' : {"French" :'Trios'},
     '4' : {"French" :'Quatre'},
     '5' : {"French" :'Cinq'},
     '6' : {"French" :'Six'},
     '7' : {"French" :'Sept'},
     '8' : {"French" :'Huit'},
     '9' : {"French" :'Nuef'},
     '10' : {"French" :'Dix'},
     '11' : {"French" :'Onze'},
     '12' : {"French" :'Douze'},
     '13' : {"French" :'Trieze'},
     '14' : {"French" :'Quatorze'},
     '15' : {"French" :'Quinze'},
     '16' : {"French" :'Seize'},
     '17' : {"French" :'Dix-sept'},
     '18' : {"French" :'Dix-huit'},
     '19' : {"French" :'Dix-neuf'},
     '20' : {"French" :'Vingt'},
     'red' : {"French" :'Rouge'},
     'gray' : {"French" :'Gris'},
     'pink' : {"French" :'Rose'},
     'black' : {"French" :'Noir'},
     'brown' : {"French" :'Marron'},
     'blue' : {"French" :'Bleu'},
     'green' : {"French" :'Vert'},
     'white' : {"French" :'Blanc'},
     'yellow' : {"French" :'Jaunce'},
     'purple' : {"French" :'pourpre'},
    'cat' : {"French" :'Chat'},
    'dog' : {"French" :'Chien'},
    'lion' : {"French" :'Le lion'},
     'goldfish' : {"French" :'Un poisson rouge'},
     'mouse' : {"French" :'Une souris'},
     'turtle' : {"French" :'une tujrtle'},
     'rabbit' : {"French" :'Un lapin'},
     'wolf': {"French" :'Le loup'},
     'monkey' : {"French" :'Le singe'},
     'hamster' : {"French" :'Un hamster'},
    'with' : {"French" :'Avec'},
    'love' : {"French" :'Amour'},
    'hapiness' : {"French" :'Bonheur'},
    'girl' : {"French" :'La fille'},
    'boy' : {"French" :'La Garcon'},
    'beach' : '{"French" :'La plage'},
    'Subway' : {"French" :'Metro'},
    'Car' : {"French" :'Voiture'},
    'Vin' : {"French" :'wine'],
    'bread' : {"French" :'Pain'},
    'ticket' : {"French" :'Billet'},
    'meat' : {"French" :'Viande'},
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
