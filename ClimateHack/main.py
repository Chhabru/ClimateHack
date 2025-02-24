from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
import os
from matplotlib import pyplot as plt
import formulo
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

basedir = os.path.abspath(os.path.dirname(__file__))
client = OpenAI(api_key=api_key)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xcoord = db.Column(db.Double(120), nullable=False)
    ycoord = db.Column(db.Double(120), nullable=False)
    carbon = db.Column(db.Double(120), nullable=False)
    carbonate = db.Column(db.Double(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    ph = db.Column(db.Double(120), nullable=False)

app.secret_key = "efdghgdfrtserdcftvgbhnctdrycfvgtszryxdtxsetrdyxdryxtccctdfyffrffffs"

@app.route('/',methods=['GET','POST'])
def form():

    if (request.method == "POST"):
        session['carbon'] = request.form['carbon']
        session['carbonate'] = request.form['carbonate']
        session['region'] = request.form['region']
        session['longitude'] = request.form['longitude']
        session['latitude'] = request.form['latitude']
        session['ph'] = request.form['pH']
        return redirect(url_for('result'))
    else:
        return render_template("main.html")

@app.route('/result')
def result():
    co2 = session['carbon']
    carb = session['carbonate']
    clim = session['region']
    x = session['longitude']
    y = session['latitude']
    ph = session['ph']

    if not co2 or not carb or not clim or not x or not y or not ph:
        return redirect(url_for('form'))


    if int(carb) < 60 or int(co2) >= 20 or int(ph) < 6.5:
        area = Area(xcoord = x, ycoord = y, carbon = co2, carbonate = carb, climate = clim, ph = ph)
        db.session.add(area)
        db.session.commit()
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Answer only with a number."}, 
       {
           "role": "user",
            "content": f"The amount of carbon dioxide in the water is {co2} ppm, the amount of carbonate in the water is {carb} ppm, the climate is {clim}, and the pH of the water is {ph}. How much limestone is needed to neutralize the water (please factor in the climate, factor in a radius of 1 kilometer in ocean water, and give the amount in pounds)?" 
        }
    ]
    )

    example = completion.choices[0].message.content
    
    completion2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Answer with a detailed paragraph."}, 
       {
           "role": "user",
            "content": f"The amount of carbon dioxide in the water is {co2} ppm, the amount of carbonate in the water is {carb} ppm, the climate is {clim.lower()}, the longitude is {x}, the latitude is {y}, and the pH of the water is {ph}. Provide as much detail and insight as possible about the climate patterns and predictions on future carbon emissions in the area." 
        }
    ]
    )
    example2 = completion2.choices[0].message.content

    completion3 = client.images.generate(
        model="dall-e-2",
        prompt=f"Generate a graph that shows the change of carbon dioxide content in water yearly over 10 years, starting at {co2} ppm. Please factor in the climate which is {clim.lower()}, the longitude which is {x}, and the latitude which is {y}. The x-axis must be years, while the y-axis must be carbon dioxide in ppm.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    example3 = completion3.data[0].url

    completion4 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Answer with only a number."}, 
       {
           "role": "user",
            "content": f"What is the climate factor for a {clim} climate?" 
        }
    ]
    )
    example4 = completion4.choices[0].message.content
    if isinstance(example4, (int, float, complex)):
        ikkhu = example4
    else:
        ikkhu = 1.2
    print(type(co2))
    print(type(carb))

    a = round(formulo.limestone(co2,carb,ikkhu))

    
    return render_template('result.html', x=example,y=example2, z=example3, a = a)

@app.route('/database')
def database():
    return render_template('db.html', data=Area.query.all())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

