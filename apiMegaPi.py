import flask
from flask import request, jsonify
from megapi import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

bot = MegaPi()

# Create some test data for our catalog in the form of a list of dictionaries.
motors = [
    {'motor_id': 1,
     'title': 'Motor1'
    },
    {'motor_id': 2,
     'title': 'Motor2'
    },
    {'motor_id': 3,
     'title': 'Motor3'     
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to MegaPi Control API</h1>
<p>A REST API for controlling MakeBlock MegaPI Remotely</p>
<p>Copyright Bulent OZHORASAN</p>'''


@app.route('/api/v1/megapi/motors/all', methods=['GET'])
def api_all():
    return jsonify(motors)


@app.route('/api/v1/megapi/motors', methods=['GET'])
def run_motor():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'motor_id' in request.args:
        id = int(request.args['motor_id'])
    else:
        return "Error: No motor_id field provided. Please specify an motor id."


    if 'motor_speed' in request.args:
        speed = int(request.args['motor_speed'])
    else:
        return "Error: No motor_speed field provided. Please specify motor speed."
    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for motor in motors:
        if motor['motor_id'] == id:
            bot.encoderMotorRun(id,speed);
            results.append(motor)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

def init_megapi():
    #ls /dev and check ttyUSB0 exists, sometimes ttyUSB1 exists so modify the line below
    bot.start('/dev/ttyUSB0')
#     bot.encoderMotorRun(1,0)  
#     bot.encoderMotorRun(2,0)    
#     bot.encoderMotorRun(3,0)


if __name__ == "__main__":    
    init_megapi()   
    app.run(host='0.0.0.0')
