from flask_restful import Resource, reqparse


from ultralytics import YOLO

# Load the YOLOv9 model
model = YOLO('yolov9c.pt')

# Run predictions
results = model.predict('photo.jpg')


results[0].show()




# class UserRegistration(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', required=True)
#         parser.add_argument('password', required=True)
#         data = parser.parse_args()

#         if user.find_by_username(data['username']):
#             return {'message': 'User already exists'}, 400

#         new_user = User(username=data['username'], password=data['password'])
#         new_user.save_to_db()

#         return {'message': 'User created successfully'}, 201

# class UserLogin(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', required=True)
#         parser.add_argument('password', required=True)
#         data = parser.parse_args()

#         user = User.find_by_username(data['username'])
#         if user and user.password == data['password']:
#             return {'message': 'Logged in as {}'.format(data['username'])}
#         return {'message': 'Invalid credentials'}, 401

# class UserProfile(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', required=True)
#         data = parser.parse_args()

#         user = User.find_by_username(data['username'])
#         if user:
#             return {'username': user.username}
#         return {'message': 'User not found'}, 404
