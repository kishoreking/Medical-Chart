from flask import Flask, render_template,redirect, url_for
import requests
import json
app = Flask(__name__)
BASE_URL_NAME= "http://127.0.0.1:8080/"
    
def fireGetMethodApi(urlApi, payload, token):
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
    urlFull=BASE_URL_NAME+urlApi
    response = requests.get(urlFull, json=payload, headers=headers, verify=False)
    return response

def firePostMethodApi(urlApi, payload, token):
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
    urlFull=BASE_URL_NAME+urlApi
    response = requests.post(urlFull, json=payload, headers=headers, verify=False)
    return response

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/TaskAllocatedUserWise')
def TaskAllocatedUserWise():

    resp=fireGetMethodApi("medtask/medicalCharAllocatedUserInfoGetApi/","","")
    data=json.loads(resp.text)
    return render_template('TaskAllocatedUserWise.html', data=data)

@app.route('/MedicalChartListWithCurrentStatus')
def MedicalChartListWithCurrentStatus():

    resp=fireGetMethodApi("medtask/medicalChartInfoGetApi/","","")
    data=json.loads(resp.text)
    return render_template('MedicalChartListWithCurrentStatus.html', data=data)

@app.route('/resetStatus')
def resetStatus():

    resp=firePostMethodApi("medtask/medicalChartStatusReset/","","")
    return redirect(url_for('MedicalChartListWithCurrentStatus'))


@app.route('/firstTimeAssingment')
def firstTimeAssingment():

    resp=firePostMethodApi("medtask/firstTimeAssingment/","","")
    return redirect(url_for('TaskAllocatedUserWise'))

@app.route('/medicalChartChangeStatus/<int:id>/<int:status>/', methods=['GET'])
def medicalChartChangeStatus(id, status):

    payload = {"id": id, "status": status}
    resp = fireGetMethodApi("medtask/medicalChartChangeStatus/", payload, "")
    return redirect(url_for('TaskAllocatedUserWise'))

if __name__ == '__main__':
    app.run(debug=True)