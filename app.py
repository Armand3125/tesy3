from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Générer des couleurs aléatoires pour les boutons
    colors = ['#FF6347', '#4682B4', '#32CD32']  # Rouge, Bleu, Vert
    random.shuffle(colors)  # Mélanger les couleurs
    return render_template('index.html', colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
