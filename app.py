from flask import Flask, request, render_template
import spacy
from spacy import displacy
from googletrans import Translator

app = Flask(__name__)
nlp = spacy.load("fr_core_news_sm")
translator = Translator()

@app.route('/')
def accueil():
    return render_template('index.html', dep_html=None, token_info=None, translation=None)

@app.route('/analyse', methods=['POST'])
def analyse():
    texte = request.form['texte']
    doc = nlp(texte)

    # Générer le diagramme de dépendance
    dep_html = displacy.render(doc, style="dep")

    # Créez une liste de tuples contenant les informations morphosyntaxiques pour chaque token
    token_info = []
    for token in doc:
        token_info.append((token.text, token.pos_, token.tag_, token.dep_, token.lemma_, token.morph))

    return render_template('index.html', dep_html=dep_html, token_info=token_info, translation=None)

@app.route('/traduire', methods=['POST'])
def traduire():
    texte = request.form['texte']
    direction = request.form['direction']
    print(f"Texte à traduire : {texte}")
    print(f"Direction de traduction : {direction}")
    if direction == 'fr-en':
        translation = translator.translate(texte, src='fr', dest='en').text
    else:
        translation = translator.translate(texte, src='en', dest='fr').text
    print(f"Résultat de la traduction : {translation}")
    return render_template('index.html', dep_html=None, token_info=None, translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
