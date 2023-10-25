# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask import render_template , redirect , request,url_for,flash,session
# # import os
# # from . import create_table
# # from .m
# # from config import Config

# # from flask_login import LoginManager

# app = Flask(__name__)

# app.debug = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataa.db'


# app.config['SECRET_KEY'] = 'BONJOUR'

# db = SQLAlchemy(app)
# migrate = Migrate(app,db)


# debug = True
# # login_manager = LoginManager()
# # login_manager.init_app(app)


# # creation de ma table dans la base de donnée 
# class Panire(db.Model):

#     id = db.Column(db.Integer, primary_key = True)
#     nom = db.Column(db.String(100), unique = False , nullable = False)
#     description = db.Column(db.String(100), unique = True , nullable = False)
#     prix = db.Column(db.Integer)


#     def __init__(self,nom,description,prix):
#         self.nom = nom
#         self.description = description
#         self.prix = prix

#     # db.init_app(app)
#     # with app.app_context() :
#     #     db.create_all()

#     def __repr__(self):
#         return f"nom:{self.nom},description:{self.description},prix:{self.prix}"


  
    

# # @login_manager.user_loader
# # def loader_user(user_id):
# #     print(Profil.query.get(user_id))
# #     return Profil.query.get(user_id)


# # creation de ma fonction pour INSCRIRE un USER dans la base de donnée
# @app.route('/add_boutique')
# def add_boutique():
#     return render_template("boutique.html")

# @app.route('/livre',methods = ["POST"])
# def profile() :

    
#     nom = request.form.get("first_name")
#     description = request.form.get("last_name")
#     prix = request.form.get("age")
    

#     user = Panire.query.filter_by(nom = request.form.get("nom")).first()
#     if user :
#         flash("Ce livre existe deja") 
#         return redirect(url_for("add_boutique"))
#     else :
#         if nom != " " and description != " " and prix is not None :
#             p = Panire(nom = nom, description = description , prix = prix)

#             db.session.add(p)
#             db.session.commit()
#             return redirect("/panier.html")
#         else :
#             return redirect("/panier.html")
        





    

# @app.route('/delete/<int:id>')
# def erase(id) :


#     data = Panire.query.get(id)
#     db.session.delete(data)
#     db.session.commit()
#     return redirect("/")



# if __name__ == '__main__' :
#     app.run(debug=True, port=5001)


