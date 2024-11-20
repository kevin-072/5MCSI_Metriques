from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
        date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        minutes = date_object.minute
        return jsonify({'minutes': minutes})
  
@app.route("/contact/", methods=["GET", "POST"])
def MaPremiereAPI():
    if request.method == "POST":
        # Récupération des données du formulaire
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        message = request.form.get("message")
        return f"""
        <h2>Merci pour votre message !</h2>
        <p><strong>Nom :</strong> {nom}</p>
        <p><strong>Prénom :</strong> {prenom}</p>
        <p><strong>Message :</strong> {message}</p>
        <a href="/contact/">Retour au formulaire</a>
        """
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contactez-nous</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f9;
            }
            form {
                max-width: 400px;
                margin: auto;
                padding: 20px;
                background: white;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            label {
                font-weight: bold;
                display: block;
                margin-bottom: 5px;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h2>Contactez-nous</h2>
        <form method="POST">
            <label for="nom">Nom :</label>
            <input type="text" id="nom" name="nom" placeholder="Votre nom" required>
            
            <label for="prenom">Prénom :</label>
            <input type="text" id="prenom" name="prenom" placeholder="Votre prénom" required>
            
            <label for="message">Message :</label>
            <textarea id="message" name="message" placeholder="Votre message" rows="5" required></textarea>
            
            <button type="submit">Envoyer</button>
        </form>
    </body>
    </html>
    """
                                                                                                                                  

@app.route('/')
def hello_world():
    return render_template('hello.html')#comm

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")
  
@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")
  

if __name__ == "__main__":
  app.run(debug=True)

