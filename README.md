![English below](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/gb.png "English below") English below
# Robert-GPT

Robert-GPT est un assistant vocal francophone qui sent la picole et les cacahuètes, basé sur GPT 3.5 Turbo et créé à la base pour un Raspberry-Pi



## Comment ça marche ?

1. **Installation :** Exécutez le script `installation.py` pour installer les dépendances nécessaires. Assurez-vous d'avoir les privilèges nécessaires pour installer des packages sur votre système.

2. **Configuration :** Ouvrez `robert.py` et ajoutez votre clé API OpenAI à la ligne 10.
   
3. **Lancement :** Exécutez le script `robert.py`. Dès que vous prononcez le nom "Robert", il sera là pour répondre à vos questions et vous faire la causette comme au PMU



## Astuces d'utilisation

- Pour parler à Robert, n'oubliez pas de prononcer son nom "Robert" dans la phrase. Par exemple, "Hey Robert, quelle est la météo aujourd'hui ?"

- Il se peut que Robert reste bloqué sur "J'écoute..." il faudra alors couper le micro à la fin de votre phrase pour qu'il la prenne en compte, le bruit ambiant étant parfois un problème pour détecter que votre phrase est terminée.



## Compatibilité 

Le script d'installation ("installation.py") fonctionne uniquement sur Linux car il utilise APT. Pour une installation sous macOS ou Windows, vous devrez chercher et installer les dépendances vous-même, si toutefois elles existent...
En voici la liste : 
1) portaudio19-dev
2) python3-pyaudio
3) espeak
4) flac

Celles pour python sont dans le dossier "requirements.txt" ainsi que leurs versions.



## Crédits

Ce projet est inspiré d'un projet créé par [Arijit1080](https://github.com/Arijit1080)


----
  
# Robert-GPT

Robert-GPT is a French-speaking voice assistant that smells beer and peanuts, based on GPT 3.5 Turbo and created for a Raspberry-pi.



## How it works?

1. **Installation:** Run the `installation.py` script to install the necessary dependencies. Make sure you have the necessary privileges to install packages on your system.

2. **Configuration:** Open `robert.py` and add your OpenAI API key on line 10.

3. **Launch:** Run the `robert.py` script. As soon as you say the name "Robert", he'll be there to answer your questions and chat with you like at the local pub.



## Usage Tips

- To talk to Robert, don't forget to say his name "Robert" in the sentence. For example, "Hey Robert, what's the weather like today?"

- Robert may get stuck on "j'écoute...", so you may need to mute the microphone at the end of your sentence for him to acknowledge it, as ambient noise can sometimes be a problem for detecting when your sentence is finished.



## Compatibility

The installation script ("installation.py") only works on Linux because it uses APT. For installation on macOS or Windows, you will need to search for and install the dependencies yourself, if they exist...
Here is the list:
1) portaudio19-dev
2) python3-pyaudio
3) espeak
4) flac

The dependencies for Python are in the "requirements.txt" folder along with their versions.



## Credits

This project is inspired by a project created by [Arijit1080](https://github.com/Arijit1080).






