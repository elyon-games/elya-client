from rich.console import Console
from rich.markdown import Markdown
from datetime import datetime
import requests

if __name__ == "__main__":
    console = Console()
    history = []
    print(f"[Elya] Bonjour ! \n Je suis Elya, documentaliste virtuelle. \n Je suis là pour répondre à tes questions sur le projet Elyon.\n Pour quitter, tapez 'exit' ou 'quit'.")
    while True:
        question = console.input(f"[Elya] Quelle est ta question : ")
        if question.lower() in ["exit", "quit"]:
            print(f"[Elya] Au revoir !")
            break
        try:
            if "<question" in question or "</question>" in question:
                print("Erreur : La question ne doit pas contenir les balises <question> ou </question>.")
                continue
            response = requests.post("https://elyon.younity-mc.fr/api/ai/ask", json={"question": question, "history": history})
            if response.status_code == 200:
                answer = response.json().get("answer", "Aucune réponse reçue.")
            else:
                answer = f"Erreur : {response.status_code}"
            console.print(Markdown(f"### Réponse de Elya :\n\n{answer}"))
            history.append({"question": question, "answer": answer, "time": datetime.now().isoformat()})
            if len(history) > 6:
                history.pop(0)
        except Exception as e:
            print(f"Une erreur est survenue pendant le traitement de la question : {e}")
