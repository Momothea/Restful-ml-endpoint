# importing libraries
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import tensorflow as tf




# Initializing the App

app = Flask(__name__)
api = Api(app)
STUDENTS = {}

# Getting the necessary data
class_names = ["T-shirt/top","Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", 'Ankle boot']
TEST_IMAGES = {}
path = './data/fashion-mnist_test.csv'
Mnist_Test_Data = pd.read_csv(path)
test_label = Mnist_Test_Data.label
Mnist_Test_Data = Mnist_Test_Data.drop(columns=['label'])
Mnist_Test_Data = Mnist_Test_Data.fillna(0)
test_label = test_label.to_numpy()
def get_row(ind ): 
  x = ((Mnist_Test_Data[Mnist_Test_Data.index == ind]).values.tolist())[0] 
  return {str(test_label[ind]) : x}
for i in range(0, len(Mnist_Test_Data)):
    TEST_IMAGES[i] = get_row(i)






# Mocked data

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}

#  Create StudentsList class and route

parser = reqparse.RequestParser() 

class StudentsList(Resource):
  def get(self):
      print("test")
      return STUDENTS

     
  def post(self):
      parser.add_argument("name")
      parser.add_argument("age")
      parser.add_argument("spec")
      args = parser.parse_args()
      student_id = int(max(STUDENTS.keys())) + 1
      student_id = '%i' % student_id
      STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
        }
      return STUDENTS[student_id], 201

class Student(Resource):
  def get(self, student_id):
    if student_id not in STUDENTS:
      return "Not found", 404
    else:
      return STUDENTS[student_id]
  
class Classify(Resource):
  def get(self, image_id):
    image_id = int(image_id)
    if (image_id in TEST_IMAGES.keys()):
      print("yes")
    else:
      print('no')
    if image_id not in TEST_IMAGES.keys():
      return "Not found", 404
    else:
      print('Found')
      new_model = tf.keras.models.load_model('./models/my_model1.h5')
      (k, v), = TEST_IMAGES[image_id].items()
      v = np.array(v)
      v = v.reshape(1, 28, 28)
      prediction = new_model.predict(v)
      predicted_label = np.argmax(prediction)
      return {"prediction" : class_names[predicted_label],
              "predicted_array" : prediction.tolist()}


api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')
api.add_resource(Classify, '/classify/<image_id>')


if __name__ == "__main__":
  app.run(debug=True, port= 3000)