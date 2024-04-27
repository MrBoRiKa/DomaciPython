from app import Flask
from flask_restful import Api
from user import UserRegistraton, UserLogin, UserProfile


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
api = Api(app)

api.add_resource(UserRegistraton)
api.add_resource(UserLogin, '/login')
api.add_resource(UserProfile, '/profile')

if __name__ == '__main__':
    app.run(debug=True)