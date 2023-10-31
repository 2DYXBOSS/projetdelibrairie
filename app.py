from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from werkzeug.utils import secure_filename

import os


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'BONJOUR'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


db = SQLAlchemy(app)
# <<<<<<< HEAD

# =======
# # migrate = Migrate(app,db)
# >>>>>>> 45fe0891c21594bba082ad5726a93354d788fd09


debug = True
# login_manager = LoginManager()
# login_manager.init_app(app)

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
    
# creation de ma table dans la base de donnée 

class Profil(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False , nullable = False)
    last_name = db.Column(db.String(20), unique = True , nullable = False)
    age = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()

    def __repr__(self):
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Connecter(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False , nullable = False)
    last_name = db.Column(db.String(20), unique = True , nullable = False)
    age = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()

    def __repr__(self):
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }


with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Panierz(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
   
    def __init__(self,nom,description,prix,image):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()

    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "image": self.image
        }
    

# <<<<<<< HEAD

# =======
# >>>>>>> 45fe0891c21594bba082ad5726a93354d788fd09
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Userpaniere(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = False , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    mail = db.Column(db.String(100), unique = False , nullable = False)
    image = db.Column(db.String(100), unique = False , nullable = False)
    

   
    def __init__(self,nom,description,prix,mail,image):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.mail = mail
        self.image = image
        

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()

    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "mail": self.mail,
            "image": self.image,
            
        }
# <<<<<<< HEAD
# =======


# >>>>>>> 45fe0891c21594bba082ad5726a93354d788fd09
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Img(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    img = db.Column(db.Text, unique = False , nullable = False)
    name = db.Column(db.Text, nullable = False)
    mimetype = db.Column(db.Text,nullable = False)
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")



@app.route('/Payement')
def Payement() :
    user = Connecter.query.all()
    data = Userpaniere.query.all()
    zee = Connecter.query.get(1)   
    frr = []
   
    
    for i in data : 
        if i.mail == zee.last_name :
            frr.append(i)
    pri = 0
    for i in data :
        pri += i.prix
    
    az = len(frr)
    er =[az,user,pri]
 

    return render_template('payement.html',ae = er)
    

# Ajouter au panier

@app.route('/new',methods = ["POST"])
def new():
    zee = Connecter.query.get(1)
    user = Profil.query.filter_by(last_name = zee.last_name).first()
    nom = request.form.get("nom")
    desc = request.form.get("desc")
    image = request.form.get("image")
    prix = request.form.get("prix")
    mail = user.last_name
    user = Userpaniere.query.filter_by(nom = nom, description = desc , prix = prix, mail = mail).first()
    if user:
        
        return redirect("/achat")
    prix = Userpaniere(nom = nom, description = desc , prix = prix, mail = mail,image=image)
    db.session.add(prix)
    db.session.commit()
    return redirect("/achat")
 
   

# le panier
@app.route('/panieruser')
def panieruserk():
    data = Userpaniere.query.all()
    Panier = Panierz.query.all()
    zee = Connecter.query.get(1)
    user = Userpaniere.query.filter_by(mail = zee.last_name).first()
    
    frr = []
    imm = []
    
    for i in data : 
        if i.mail == zee.last_name :
            frr.append(i)
    # for i in Panier : 
    #     if i.nom == zee.first_name :
    #         imm.append(i.image)
    # imm = Panierz.query.filter_by(mail = frr.last_name).first()
    # for i in Panierz :
    #     if i.nom == frr.last_name :
    #         imm.append(i.image)
    # autre = [frr,imm]
    # if autre :
    #     print(f"{autre}") 
    # ert = [frr,imm]
    
    pri = 0
    for i in data :
        pri += i.prix
    az = len(frr)
    er =[az,user,pri]
    az = len(frr)
    er =[az,frr,pri]
    return render_template('panieruser.html',user = er)
    # return render_template('panieruser.html',user = [user])


# supprimer du panier < inacheve > sa supprime tout
@app.route('/suppanier',methods = ["POST"])
def suppanier() :

    nom = request.form.get("nom")
    description = request.form.get("description")
    mail = request.form.get("mail")
    
    user = Userpaniere.query.filter_by(nom = nom,description = description).first()
    zerre = Userpaniere.query.get(user.id)
    db.session.delete(zerre)
    db.session.commit()
    return redirect("/panieruser")


















# @app.route('/panieruser')
# def achl():
#     aer = Panier.query.all()
#     return render_template('achat.html',aer = aer)






@app.route('/achat')
def achl():
    aer = Panierz.query.all()
    data = Userpaniere.query.all()
    zee = Connecter.query.get(1)   
    frr = []

    
    for i in data : 
        if i.mail == zee.last_name :
            frr.append(i)
   
    
    az = len(frr)
    er =[az,aer]
    return render_template('achat.html',ae = er)



@app.route('/objet',methods = ["POST"])
def objet(): 
    
    try :
        nom = request.form.get("nom")
        description = request.form.get("description")
        prix = request.form.get("prix")
        image = request.form.get("image")
        pani = Panierz(nom = nom, description = description , prix = prix, image = image)
        # pani = Panier(nom = nom, description = description , prix = prix)
        
        db.session.add(pani)
        db.session.commit()
        return redirect("/profil")
    except :
        return render_template("/boutique.html")
    
# redirection vers la page admin pour voirs les articles ajouter
@app.route('/profil')
def profil() :
    profil = Panierz.query.all()
    return render_template('profil.html',profil = profil)

# Supprimer un arcticles depuis la base Admin
@app.route('/deletearticles/<int:id>')
def ecraseart(id) :


    data = Panierz.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect("/profil")

@app.route('/useprid')
def useprid():
    user = Connecter.query.all()
    data = Userpaniere.query.all()
    zee = Connecter.query.get(1)   
    frr = []

    
    for i in data : 
        if i.mail == zee.last_name :
            frr.append(i)
   
    
    az = len(frr)
    er =[az,user]
 

    return render_template('useprid.html',ae = er)

@app.route('/home')
def home():
    # user = Connecter.query.all()
    return render_template('home.html')
@app.route('/autre/<int:id>')
def join(id):
    user = Profil.query.filter_by(id=id).first()
    return render_template('miseajour.html')


# redirection vers la boutique

# creation de ma fonction pour INSCRIRE un USER dans la base de donnée
@app.route('/add_data')
def add_data():
    return render_template("add_profile.html")

@app.route('/add',methods = ["POST"])
def profile() :
    
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")
    conf = request.form.get("conf")
    

    if conf != age :
        flash("Entrez le meme mot de passe")
        return redirect("/add_data")
    
    for i in range (len(last_name)) :
        if last_name[i] == "@" :

            if "moc.liamg" == last_name[:i:-1]:

                pass
            else :
                flash("Email ou Mot de passe invalide")
                return redirect("/add_data")
            



    user = Profil.query.filter_by(last_name = request.form.get("last_name")).first()
    if user :
        flash("Ce compte existe deja") 
        return redirect(url_for("add_data"))
    else :
        if first_name != " " and last_name != " " and age is not None and len(age)== 8 :
            p = Profil(first_name = first_name, last_name = last_name , age = age)

            db.session.add(p)
            db.session.commit()
            return redirect("/pre")
        else :
            return redirect("/add_data")
        


# Connexion utlisateur et admin



@app.route('/pre')
def pree():
    return render_template('connexion.html')
@app.route('/sprome',methods = ["GET","POST"])
def sprome() :
    
    eude = Profil.query.all()

    user = Profil.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age")).first()
   
    if user :
        

        datae = Profil.query.get(user.id)
        
        print(f"vous etes connecter{user.first_name}{user.id}")
        # return redirect(url_for('home', user=user.id))

        tre = Connecter.query.get(1)
        profi = Connecter.query.all()
        tre.first_name = user.first_name
        tre.last_name = user.last_name
        tre.age = user.age 
        db.session.commit()
        return redirect('/home')
    
        # az = Profil.query.get(user.id)
        

    elif request.form.get("last_name") == "admin@gmail.com" and request.form.get("age") == "admin" :

        return render_template('index.html',profiles = eude)
    else :

        flash("Email ou Mot de passe invalide")
        return redirect("/pre")


# redirection vers la page admin pour voirs les personnes inscrites

@app.route('/admining')
# @login_requiered
def index() :
    profiles = Profil.query.all()
    return render_template('index.html', profiles = profiles)
@app.route('/admining')
def ghdc() :
    
    return render_template('add_profile.html')
# Supprimer un utilisteur 
@app.route('/delete/<int:id>')
def erase(id) :

    data = Profil.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/admining')






# modifier les informations dun utilisateur
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = Profil.query.get(id)
    eude = Profil.query.all()
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.age = request.form['age']
        for i in eude :
            if i == user :
                continue
            if i.last_name == user.last_name :
                flash("Email ou Mot de passe invalide")
                return redirect(url_for('update', id=id))
            else :
            
                for i in range (len(user.last_name)) :

                    if user.last_name[i] == "@" :
                        
                        if "moc.liamg" == user.last_name[:i:-1] and len(user.age)== 8 :

                            db.session.commit()
                            return redirect(url_for('index',id=id))
                        
                        else :

                            flash("Email ou Mot de passe invalide")
                            return redirect(url_for('update', id=id))
                   
                        
 
            
           
    flash("Email ou Mot de passe invalide")
    return render_template('miseajour.html', user=user)










# def conver_image_into_binary(filename):
#     with open(filename, 'rb') as file:
#         photo_image = file.read()
#     return photo_image




# comment recuperer une image de la base de donnée
# @app.route('/img/<int:id>')
# def img(id):
#     data = Img.query.get(id)
#     return Response(data.img, mimetype=data.mimetype)




@app.route('/recup')
def recup():
    data = Img.query.get(Img.id)
    return redirect('recu.html',Response(data.name, mimetype=data.mimetype))

# @app.route('/ee/<int:id>')
# def ee(id):
#     data = Img.query.get(id)
#     return redirect(url_for('ee', id=id),Response(data.img, mimetype=data.mimetype))


@app.route('/upload',methods = ["POST"])
def upload():
    pic = request.files['pic']
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    img = Img(img = pic.read(),name = filename,mimetype = mimetype)
    print(img)
    db.session.add(img)
    db.session.commit()
    return redirect("/recup")










 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
# @app.route(/admining)
# def home():
#     return render_template('boutique.html')
# redirection vers la page ajouter des nouveaux produits
@app.route('/add_objet')
def add_objet():
    return render_template("boutique.html")
@app.route('/')
def page():
    return render_template("page.html")
 
@app.route('/add_objet', methods=['POST'])
def upload_image():
    try :
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            flash('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            flash('Image téléchargée avec succès et affichée ci-dessous')
            return render_template('boutique.html', filename=file.filename)
            # return render_template('boutique.html', filename=filename)
    except:
        flash('Les types dimages autorisés sont - png, jpg, jpeg, gif')
        return redirect(request.url)

        # uploads.image
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = 'uploads/' + filename), code=301)


if __name__ == '__main__' :
    app.run(debug=True,port=5000)
