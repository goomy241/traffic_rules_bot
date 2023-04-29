from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import openai
import os
import logging

app = Flask(__name__)
CORS(app)
openai.api_key = ''

app.logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        #prompt_body = request.form['prompt']
        content= request.get_json()
        prompt_body = content['prompt']
        prompt = prompt_body + '?\nContext: Traffic rules in California\n'
        app.logger.info(prompt)
        response = openai.Completion.create(
            model = 'davinci:ft-personal-2023-04-27-20-59-56',
            prompt = prompt,
            max_tokens = 150,
            n = 1,
            temperature = 0,
            stop = ['\n\n', 'Context:'],
            presence_penalty=0.7,
            frequency_penalty=0.7
        )
        result = response.choices[0].text
        if not result:
            result = 'Sorry I am unable to answer your question at this moment. Please provide more information about your question'
        app.logger.info(response)
        #return render_template('result.html', prompt=prompt_body, result=result)
    #return render_template('index.html')
    response={
        "response":result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
