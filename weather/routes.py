import json
import requests
from flask import Flask
from flask import render_template, redirect, url_for, flash, request
from weather import app
from weather.forms import Searchform
@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home_view():
    cities = ['Dhaka','Mumbai','Lahore','New York','London','Paris','Colombo','Rome','Munich','Stockholm']
    result = []
    feels_like = []
    resulth = []
    wind = []
    sky_status = []
    for city in cities:
        final_url = f'http://api.weatherapi.com/v1/current.json?key=eda33b43c4b344ca886161433222401&q={city}'
        dt = requests.get(final_url)
        data = dt.json()
        print(data)
        wt1 = data['current']['temp_c']
        wt2 = data['current']['humidity']
        wt3 = data['current']['feelslike_c']
        wt4 = data['current']['wind_kph']
        wt5 =  data['current']['condition']['text'] 
        result.append(wt1)
        resulth.append(wt2)
        result.append(wt1)
        resulth.append(wt2)
        feels_like.append(wt3)
        wind.append(wt4)
        sky_status.append(wt5)
        print(wt1)
    return render_template('home.html',title='Home page',temperatures=result,humidities=resulth,wind=wind,feels_like=feels_like,condition=sky_status,cities=cities)

@app.route('/location',methods=['GET','POST'])
def get_location_update():
    form = Searchform()
    location = None
    r = False
    result = []
    feels_like = []
    resulth = []
    wind = []
    sky_status = []
    fr = []
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            final_url = f'http://api.weatherapi.com/v1/current.json?key=eda33b43c4b344ca886161433222401&q={location}'
            dt = requests.get(final_url)
            data = dt.json()
            print(data)
            if 'error' in data:
                flash(f'City name is not valid. Please provide a valid city','danger')
            else:
                wt1 = data['current']['temp_c']
                wt2 = data['current']['humidity']
                wt3 = data['current']['feelslike_c']
                wt4 = data['current']['wind_kph']
                wt5 =  data['current']['condition']['text'] 
                result.append(wt1)
                resulth.append(wt2)
                feels_like.append(wt3)
                wind.append(wt4)
                sky_status.append(wt5)
                fr.append(result)
                fr.append(resulth)
                fr.append(feels_like)
                fr.append(wind)
                fr.append(sky_status)
                r = True
                redirect (url_for('get_location_update'))
        else:
            flash(f'An error occured. Please try again')
    
    return render_template('specific.html',r=r,form=form,location = location,fr=fr)
    

