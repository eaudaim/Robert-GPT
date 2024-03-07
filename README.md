# Robert-GPT
Un assistant vocal francophone basé sur GPT 3.5 Turbo

1) Exécuter "installation.py" 
2) Ouvrir "robert.py" dans un éditeur de texte et ajoutez votre clé API OpenAI
3) Exécuter "robert.py"

Pour que Robert comprenne que c'est à lui que vous parlez, le nom "Robert" doit être présent dans la phrase. 
Robert écoute pendant 5 secondes et recommence un cycle si rien n'a été capté.
Il se peut que Robert reste bloqué sur "J'écoute...", il faudra alors couper le micro à la fin de votre phrase pour qu'il la prenne en compte, le bruit ambiant étant parfois un problème pour détecter que l'humain a terminé de parler.

Le script d'installation ("installation.py") fonctionne uniquement sur Linux car il utilise APT. Pour une installation sous macOS ou Windows, vous devrez chercher et installer les dépendances vous-même, si toutefois elles existent...
En voici la liste : 
1) portaudio19-dev
2) python3-pyaudio
3) espeak
4) flac

Celles pour python sont dans le dossier "requirements.txt" ainsi que leurs versions 





# Robert-GPT
A French-speaking voice assistant based on GPT 3.5 Turbo

1) Run "installation.py"
2) Open "robert.py" in a text editor and add your OpenAI API key
3) Run "robert.py"

For Robert to understand that you are addressing him, the name "Robert" must be present in the sentence.
Robert listens for 5 seconds and restarts a cycle if nothing is detected.
Robert may get stuck on "Listening...", so you may need to mute the microphone at the end of your sentence for him to acknowledge it, as ambient noise can sometimes be a problem for detecting when a human has finished speaking.

The installation script ("installation.py") only works on Linux because it uses APT. For installation on macOS or Windows, you will need to search for and install the dependencies yourself, if they exist...
Here is the list:
1) portaudio19-dev
2) python3-pyaudio
3) espeak
4) flac

The dependencies for Python are in the "requirements.txt" file along with their versions
