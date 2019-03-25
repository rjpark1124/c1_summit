from flask import Flask, jsonify, render_template, request, redirect
import requests
import os
import json

app = Flask(__name__)


@app.route("/")
def index():
    # THIS SHOULD BE index.html
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

# /search/advanced
#/results
#/results/image

@app.route("/search")
def search():
    return render_template("search.html")
@app.route("/refined-results", methods=['POST'])
def get_refined_results():
    if request.method == 'POST':
        parameters = {'media_type':'image'}
        if request.form['query'] != "":
            parameters['q'] = request.form['query']
        if request.form['s_year'] != "" and int(request.form['s_year']) >= 1950 and int(request.form['s_year']) <= 2100:
            parameters['year_start'] = request.form['s_year']
        if request.form['e_year'] != "" and int(request.form['e_year']) >= 1950 and int(request.form['e_year']) <= 2100:
            parameters['year_end'] = request.form['e_year']
        if request.form['location'] != "":
            parameters['location'] = request.form['location']
        if request.form['center'] != "":
            parameters['center'] = request.form['center']

        if len(parameters)==1:
            return render_template("no_results.html")

        r = requests.get('https://images-api.nasa.gov/search', params= parameters)
        results = json.loads(r.text)

        list_of_results = results['collection']['items']
        filtered_list = []
        for image_obj in list_of_results:
            filtered_list.append(
                {
                'thumbnail': image_obj['links'][0]['href'],
                'metadata': image_obj['data'][0]
                }
            )
        return render_template("results.html", image_list = filtered_list, orig_query=parameters)
        # metadata: description, title, nasa_id, date_created, center
    return render_template("no_results.html")
@app.route("/results", methods=['POST'])
def get_results():
    if request.method == 'POST':
        # request.form['center']
        if request.form['query'] is "":
            return render_template("no_results.html")

        parameters = {'q': request.form['query'],'media_type':'image'}
        r = requests.get('https://images-api.nasa.gov/search', params= parameters)
        results = json.loads(r.text)

        list_of_results = results['collection']['items']
        filtered_list = []
        for image_obj in list_of_results:
            filtered_list.append(
                {
                'thumbnail': image_obj['links'][0]['href'],
                'metadata': image_obj['data'][0]
                }
            )
        return render_template("results.html", image_list = filtered_list, orig_query=parameters)
        # metadata: description, title, nasa_id, date_created, center
    return render_template("no_results.html")

@app.route("/details/<nasa_id>")
def details(nasa_id):
    if nasa_id == "":
        return render_template("no_result.html")

    parameters = {'nasa_id' : nasa_id}
    r = requests.get('https://images-api.nasa.gov/search', params=parameters)
    results = json.loads(r.text)
    image = results['collection']['items'][0]['href']
    r1 = requests.get(image)
    results2 = json.loads(r1.text)
    params = {
        'image': results2[0],
        'metadata': results['collection']['items'][0]['data'][0]
    }

    return render_template("details.html", img_obj=params)
    # metadata: description, title, nasa_id, date_created, center

if __name__ == "__main__":
    app.run(debug=True)