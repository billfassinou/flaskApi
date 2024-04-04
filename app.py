# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Route pour obtenir un message de bienvenue
@app.route('/')
def home():
    return jsonify(message='Bienvenue sur notre API!')


# Route pour obtenir un message de bienvenue
@app.route('/api/welcome')
def welcome():
    return jsonify(message='Bienvenue sur notre API!')


# Route pour obtenir des informations sur l'équipe
@app.route('/api/about')
def about():
    team_info = {
        'team_name': 'Équipe de développement',
        'members': [
            {'name': 'Jean Dupont', 'role': 'Développeur principal'},
            {'name': 'Marie Durand', 'role': 'Développeur frontend'},
            {'name': 'Pierre Martin', 'role': 'Développeur backend'}
        ]
    }
    return jsonify(team_info)


# Route pour obtenir des informations de contact
@app.route('/api/contact')
def contact():
    contact_info = {
        'email': 'contact@example.com',
        'phone': '+1234567890',
        'address': '123 Rue Principale, Ville, Pays'
    }
    return jsonify(contact_info)


# Route pour obtenir des informations sur un utilisateur spécifique
@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    # Simuler des données utilisateur à partir d'une base de données
    if user_id == 1:
        user = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
    elif user_id == 2:
        user = {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
    else:
        return jsonify(error='Utilisateur non trouvé'), 404
    return jsonify(user)


# Route pour obtenir une liste d'articles
@app.route('/api/articles')
def get_articles():
    articles = [
        {'id': 1, 'title': 'Article 1', 'content': 'Contenu de l\'article 1'},
        {'id': 2, 'title': 'Article 2', 'content': 'Contenu de l\'article 2'}
    ]
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
