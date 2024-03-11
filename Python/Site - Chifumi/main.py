from flask import Flask, request, render_template, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from random import randint
#Ici on importe les fonctions qui nous serviront pour le projet.


#On initialise le projet Flask.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'juJlcENnir'

db = SQLAlchemy(app)
ma = Marshmallow(app)


#On créer notre base de données.
class Joueurs(db.Model):
    #Créer nos colonnes dans la base de données.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)

    def __init__(self, name, password, mail, score):
        self.name = name
        self.password = password
        self.mail = mail
        self.score = score


class JoueursSchema(ma.Schema):
    class Meta:
        fields = ('name', 'mail', 'score')


joueur_schema = JoueursSchema()
Joueurs_schema = JoueursSchema(many=True)


with app.app_context():
    db.create_all()


#Projet
#Notre page d'accueil, avec les règles, le login et l'inscription.
@app.route('/')
def index():
    return render_template('index.html')


#La page qui va permettre aux joueurs de se connecter en comparant les données entrées avec celles de la base de données.
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        #Récupère les données entrer par les joueurs.
        name = request.form['name']
        password = request.form['password']

        user = Joueurs.query.filter_by(name=name).first()

        #On compare les données entrer avec celle de la base de données.
        if user is None:
            return '''
                <body style="background-color:#2E2437;">
                <h1 style="text-align:center; color:white;">Utilisateur Inconnu</h1> <br>
                <a href="http://127.0.0.1:5000/"><button>Retour à l'Accueil</button></a>
            '''
        elif password != user.password:
            return '''
                <body style="background-color:#2E2437;">
                <h1 style="text-align:center; color:white;">Mot de Passe Incorrect</h1> <br>
                <a href="http://127.0.0.1:5000/"><button>Retour à l'Accueil</button></a>
            '''

        session['user_id'] = user.id

        #Si le joueur arrive à se connecter, alors on lance la page de jeu.
        return redirect('/chifoumi')


#La page qui va permettre d'enregistrer nos joueurs dans la base de données.
@app.route('/signup', methods=["POST"])
def signup():
    name = request.form['name']
    password = request.form['password']
    mail = request.form['mail']
    joueur = Joueurs(name=name, password=password, mail=mail, score='0')

    #Ajoute les données du joueurs à la base de données.
    db.session.add(joueur)
    db.session.commit()

    return render_template('signup.html')


#La page qui va permettre aux joueurs d'entrer leur mouvement pour le chifoumi.
@app.route('/chifoumi')
def chifoumi():
    return render_template('chifoumi.html')


#La page qui va permettre le déroulement du jeu, en comparant le mouvement entré par le joueur avec le mouvement générer aléatoirement par l'ordinateur.
@app.route('/play', methods=["POST"])
def play():
    if request.method == "POST":
        #On récupère la session du joueur pour pouvoir sauvegarder son score.
        user = Joueurs.query.get(session['user_id'])

        move_player = request.form['joueur']
        moves_ai = {1: "Pierre", 2: "Papier", 3: "Ciseaux"}

        #Génère un mouvement aléatoire pour l'ordinateur.
        move_ai = moves_ai[randint(1, 3)]

        msg = ""

        #On compare le mouvement du joueur avec celui de l'ordinateur et on retourne un message avec le résultat.
        if move_player == "Pierre" and move_ai == "Ciseaux":
            msg = '''
                Bravo ! La Pierre bat les Ciseaux, vous avez gagné !
            '''
            user.score = user.score + 1
        elif move_player == "Pierre" and move_ai == "Papier":
            msg = '''
                Mince ! Le Papier bat la Pierre, vous avez perdu !
            '''
        elif move_player == "Pierre" and move_ai == "Pierre":
            msg = '''
                Égalité ! Vous avez joué comme l'ordinateur (T800 is that you ?) !
            '''

        if move_player == "Papier" and move_ai == "Pierre":
            msg = '''
                Bravo ! Le Papier bat le Pierre, vous avez gagné !
            '''
            user.score = user.score + 1
        elif move_player == "Papier" and move_ai == "Ciseaux":
            msg = '''
                Mince ! Les Ciseaux battent le Papier, vous avez perdu !
            '''
        elif move_player == "Papier" and move_ai == "Papier":
            msg = '''
                Égalité ! Vous avez joué comme l'ordinateur (T800 is that you ?) !
            '''

        if move_player == "Ciseaux" and move_ai == "Papier":
            msg = '''
                Bravo ! Les Ciseaux battent le Papier, vous avez gagné !
            '''
            user.score = user.score + 1
        elif move_player == "Ciseaux" and move_ai == "Pierre":
            msg = '''
                Mince ! La Pierre bat les Ciseaux, vous avez perdu !
            '''
        elif move_player == "Ciseaux" and move_ai == "Ciseaux":
            msg = '''
                Égalité ! Vous avez joué comme l'ordinateur (T800 is that you ?) !
            '''

        #Nécessaire pour actualiser le score dans la base de données.
        db.session.commit()

        return render_template('play.html', msg=msg)


#La page qui va afficher le tableau des scores tirer par ordre décroissant.
@app.route('/score')
def get_score():
    return render_template('score.html', joueurs=Joueurs.query.order_by(Joueurs.score.desc()).all())


#API Rest
@app.route('/joueur', methods=['POST'])
def add_joueur():
    name = request.json['name']
    password = request.json['password']
    mail = request.json['mail']

    new_joueur = Joueurs(name, password, mail, score="0")
    db.session.add(new_joueur)
    db.session.commit()
    result = joueur_schema.dump(new_joueur)
    return jsonify(result)


@app.route('/joueurs', methods=['GET'])
def get_joueurs():
    all_joueurs = Joueurs.query.all()
    result = Joueurs_schema.dump(all_joueurs)
    return jsonify(result)


@app.route('/joueurs/<int:id>', methods=['GET'])
def get_joueur_by_id(id):
    joueur = Joueurs.query.get(id)
    return joueur_schema.jsonify(joueur)


@app.route('/joueur/<int:id>', methods=['PUT'])
def modify_joueur(id):
    joueur = Joueurs.query.get(id)
    joueur.name = request.json["name"]
    joueur.mail = request.json["mail"]
    db.session.commit()
    return joueur_schema.jsonify(joueur)


@app.route('/joueur/<int:id>', methods=['DELETE'])
def delete_joueur(id):
    joueur = Joueurs.query.get(id)
    db.session.delete(joueur)
    db.session.commit()
    return joueur_schema.jsonify(joueur)


if __name__ == "__main__":
    app.run(debug=True)
