import speech_recognition as sr
import pyttsx3
import openai

# Initialisation de pyttsx3
en_ecoute = True
moteur = pyttsx3.init()

# Définir votre clé API OpenAI et personnaliser le rôle de ChatGPT
openai.api_key = "//////////////// API KEY HERE - CLE API ICI \\\\\\\\\\\ "
messages = [{"role": "system", "content": "Votre nom est Robert. Vous répondez en français en utilisant un langage de compagnon de beuverie dans un bar. Vous répondez à toutes les questions avec un vocabulaire de prolétaire ou d'ouvrier et ne faites pas de référence à l'alcool trop souvent."}]

# Personnalisation de la voix de sortie
voix = moteur.getProperty('voices')
vitesse = moteur.getProperty('rate')
volume = moteur.getProperty('volume')

def obtenir_reponse(entree_utilisateur):
    messages.append({"role": "user", "content": entree_utilisateur})
    reponse = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reponse_chatgpt = reponse["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reponse_chatgpt})
    return reponse_chatgpt

while en_ecoute:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("J'écoute...")
            audio = recognizer.listen(source, timeout=5.0)
            reponse_audio = recognizer.recognize_google(audio, language="fr-FR")
            print(reponse_audio)
           
            if "robert" in reponse_audio.lower():
                reponse_openai = obtenir_reponse(reponse_audio)
                moteur.setProperty('rate', 120)
                moteur.setProperty('volume', volume)
                moteur.setProperty('voice', 'french')
                moteur.say(reponse_openai)
                moteur.runAndWait()
           
            else:
                print("Je n'ai pas entendu le nom 'Robert'.")
           
        except sr.UnknownValueError:
            print("Je n'ai rien entendu.")

