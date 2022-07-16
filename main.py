# Import flask and flask-cors  library
import pickle
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Declare the flask app
app = Flask(__name__)

# Enable cross origin request for our application
cors = CORS(app)

auto_regressor_model = pickle.load(open("./output/auto_regressor_model.pkl", "rb"))

# Enable an api route for status check
@app.route('/check', methods= ['GET'])
@cross_origin()
def return_status():
    return "Yay! Flask App is running and newly deployed"

# Enable api route to get time series predictions
@app.route('/', methods = ['GET'])
@cross_origin()
def return_model_prediction():
        # Get prediction results and respond
        # GET Request : No data required since we are handling a univariate time series model
    try:
        predictions = auto_regressor_model.predict()
        final_four_predictions = list(predictions)[-4:]
        return {"status_code":200,"message":"Sucess", "body": {"preds": final_four_predictions}}

    except Exception as e:
        print(f"Error occured :     {e}")
        return {"status_code":404, "message": f"Error :-    {e}"}

if __name__ == '__main__':
    app.run("0.0.0.0")
