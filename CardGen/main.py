import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import webbrowser

class CarteNumeriqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traxxouu • Créateur de Carte Numérique")

        # Variables pour stocker les informations saisies par l'utilisateur
        self.photo_profile_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.color_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.site_url_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.twitch_var = tk.StringVar()
        self.discord_var = tk.StringVar()
        self.twitter_var = tk.StringVar()
        self.github_var = tk.StringVar()

        # Interface utilisateur
        self.create_widgets()

    def create_widgets(self):
        self.root.geometry("500x600")

        style = ttk.Style(self.root)
        style.configure('TLabel', font=('Helvetica', 12), padding=5)
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TEntry', font=('Helvetica', 12), padding=5)

        ttk.Label(self.root, text="Photo de Profil URL:", style='TLabel').grid(row=0, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.photo_profile_var).grid(row=0, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Nom d'Utilisateur:", style='TLabel').grid(row=1, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.username_var).grid(row=1, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Couleur du Nom d'Utilisateur:", style='TLabel').grid(row=2, column=0, sticky="e", padx=10, pady=5)
        ttk.Button(self.root, text="Sélectionner Couleur", command=self.select_color, style='TButton').grid(row=2, column=1, columnspan=2, pady=5)

        ttk.Label(self.root, text="Description:", style='TLabel').grid(row=3, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.description_var).grid(row=3, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Site URL:", style='TLabel').grid(row=4, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.site_url_var).grid(row=4, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Adresse E-mail:", style='TLabel').grid(row=5, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.email_var).grid(row=5, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Twitch URL:", style='TLabel').grid(row=6, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.twitch_var).grid(row=6, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Discord URL:", style='TLabel').grid(row=7, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.discord_var).grid(row=7, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="Twitter URL:", style='TLabel').grid(row=8, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.twitter_var).grid(row=8, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Label(self.root, text="GitHub URL:", style='TLabel').grid(row=9, column=0, sticky="e", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.github_var).grid(row=9, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        ttk.Button(self.root, text="Créer Carte", command=self.creer_carte, style='TButton').grid(row=10, column=0, columnspan=3, pady=20)

    def select_color(self):
        color = askcolor()[1]
        if color:
            self.color_var.set(color)

    def creer_carte(self):
        # Code HTML de base
        code_html_base = """
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=MuseoModerno:ital,wght@1,800&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Modern+Antiqua&display=swap" rel="stylesheet">
        <link rel="icon" href="/media/logo.png" type="image/png" />
        <title>{username} • Card</title>
        <style>
            h1 {{
                color: {color};
            }}
            body {{
                background-size: cover;
            }}
            .made {{
                position: absolute;
                bottom: 0;
                right: 0;
                margin: 20px;
                text-align: right;
            }}
            .made a {{
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                font-weight: 600;
                color: rgb(0, 0, 0); /* Black color */
                padding: 10px 15px;
                border-radius: 8px;
                cursor: pointer;
                margin: 0px;
                transition: all 0.3s ease;
                position: relative;
                outline: none;
                background: rgb(2, 126, 251); /* Blue color */
                box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, 0.702),
                            7px 7px 20px 0px rgba(255, 255, 255, 0),
                            4px 4px 5px 0px rgba(0, 0, 0, 0.174);
            }}
            .made a:hover {{
                background: rgb(0, 0, 0); /* Black color */
                color: rgb(255, 255, 255); /* White color */
                box-shadow: none;
            }}
        </style>
        <meta name='description' content='{username} Carte numérique avec des liens vers ses réseaux, son site et un moyen de le contacter.'>
    </head>
    <body>
        <div class="ecran">
            <div class="carte" data-tilt>
                <img src="{photo_profile}" alt="Photo de profil de {username}">
                <div class="titletrax">
                     <h1>{username}</h1>
                </div>
                <br>
                <div class="infotrax">
                    <p><h4>{description}</h4></p>
                    <br>
                    <div class="reseau">
                        <a href="{twitch_url}"><img src="media/twitchlogo.png" alt="Twitch logo"></a>
                        <a href="{discord_url}"><img src="media/discord.logo_.decodagecom.webp" alt="Discord Logo"></a>
                        <a href="{twitter_url}"><img src="media/twitterlogo.png" alt="Le seul et unique logo de Twitter"></a>
                        <a href="{github_url}"><img src="media/GitHub_logo.png" alt="Github Logo"></a>
                    </div>
                    <br>
                    <a href="mailto:{email}" class="button">Me contacter</a>
                    <br>
                    <br>
                    <a href="{site_url}" class="button">Mon Site</a>            
                </div>
            </div>

            <div class="made">
                <a href="https://github.com/traxxouu" class="button">created by traxxouu</a>
            </div>
        </div>
        <script src="vanilla-tilt.js"></script>
    </body>
</html>
"""

        # Remplacer les placeholders avec les informations saisies par l'utilisateur
        code_html = code_html_base.format(
            username=self.username_var.get(),
            photo_profile=self.photo_profile_var.get(),
            color=self.color_var.get(),
            description=self.description_var.get(),
            site_url=self.site_url_var.get(),
            email=self.email_var.get(),
            twitch_url=self.twitch_var.get(),
            discord_url=self.discord_var.get(),
            twitter_url=self.twitter_var.get(),
            github_url=self.github_var.get()
        )

        # Enregistrer le code HTML dans un fichier
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(code_html)

        # Afficher un message de confirmation
        tk.messagebox.showinfo("Carte Créée", "La carte numérique a été créée avec succès. Vérifiez le fichier 'index.html'.")

        # Ouvrir le fichier dans le navigateur par défaut
        webbrowser.open("index.html")

# Créer la fenêtre principale
root = tk.Tk()
app = CarteNumeriqueApp(root)
root.mainloop()
