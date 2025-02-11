# Bibliothèque à installer
# !pip install transformers datasets torch

import torch
import json
import re
from transformers import T5ForConditionalGeneration, T5Tokenizer, AutoTokenizer, AutoModelForSeq2SeqLM

# Charger le modèle fine-tuné et le tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("AssemienDev/t5_codepenal")
model = AutoModelForSeq2SeqLM.from_pretrained("AssemienDev/t5_codepenal").to(device)

# Charger le dataset JSON
with open('../data/legalbert_dataset.json', 'r') as f:
    dataset = json.load(f)

# Définir la question à analyser
question_to_ask = "Quel est le contenu de l'Article 10 ?"

# Extraire dynamiquement l'Article X à partir de la question avec une expression régulière
match = re.search(r"Article\s(\d+)", question_to_ask)
if match:
    article_to_search = f"Article {match.group(1)}"

    # Afficher l'article extrait
    print(f"Article extrait : {article_to_search}")
else:
    raise ValueError("Aucun article trouvé dans la question.")

# Chercher le contexte correspondant à l'article dans le dataset
context = None
for entry in dataset:
    print(f"Vérification de la question : {entry['question']}")
    if article_to_search in entry['question']:
        context = entry['context']
        print(f"Contexte trouvé pour {article_to_search} : {context[:500]}.")
        break

if context is None:
    raise ValueError(f"Contexte pour {article_to_search} non trouvé dans le dataset.")


# Reformuler l'input pour le modèle de manière explicite
input_text = f"question: {question_to_ask} context: {article_to_search} {context}"

# Tokenisation du texte
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)

# Générer la réponse
output = model.generate(input_ids, max_length=2048, num_beams=64, do_sample=False, early_stopping=True)

# Décoder et afficher la réponse
answer = tokenizer.decode(output[0], skip_special_tokens=True)
print("Réponse générée :", answer)
