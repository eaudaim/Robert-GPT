import subprocess
import time

# Fonction pour afficher du texte avec un délai
def afficher_avec_delai(texte, delai):
    print(texte)
    time.sleep(delai)

# Installer les packages apt
afficher_avec_delai("\n Installation des packages apt : \n", 1)

packages = ["portaudio19-dev", "python3-pyaudio", "flac", "espeak"]
for package_name in packages:
    subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)

# Exécuter la commande pip
afficher_avec_delai("\n Execution de requirement.txt : \n", 1)
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

