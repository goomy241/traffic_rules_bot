from flask import Flask, render_template, request
import openai
import os
import logging

app = Flask(__name__)
openai.api_key = os.environ['OPENAI_API_KEY']

app.logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt_body = request.form['prompt']
        prompt = prompt_body + '?\nContext: Traffic rules in California\n'
        app.logger.info(prompt)
        response = openai.Completion.create(
            model = os.environ['OPENAI_DAVINCI_MODEL'] or os.environ['OPANAI_ADA_MODEL'],
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
        return render_template('result.html', prompt=prompt_body, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
