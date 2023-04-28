# traffic_rules_bot
This project is a web application that uses a fine-tuned GPT-3 model based on the California Driver Handbook 2023 to generate answers to user questions related to traffic rules. The web app is built using Flask, a Python web framework, and utilizes OpenAI's API to interact with the GPT-3 model.

The user interface consists of a search box where the user can enter their problem, and submit it. The Flask app then sends a request to the fine-tuned GPT-3 API using the prompt as input, and displays the generated answers.

## How to run it
- Store your [OPEN_API_KEY](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) in environment variable
- Pull the reposity locally and run `flask run`
- Visit `http://127.0.0.1:5000/`

## Samples
<img width="887" alt="image" src="https://user-images.githubusercontent.com/90799662/235027463-5cac2eff-229f-47e5-976a-eca0b1d584df.png">

<img width="755" alt="image" src="https://user-images.githubusercontent.com/90799662/235027609-840ba667-556e-4ded-94de-cb2e61ea8c87.png">

## Future work
By expanding the training data set, the accuracy of the fine-tuned model can be further improved. To achieve this, follow the steps mentioned below:
- Prepare training dataset
  - Add more data to the google [sheet](https://docs.google.com/spreadsheets/d/1FtyxfR6UK4vvGOIHNCi3BrO82KND4OQRccIvbJnFQtw/edit?usp=sharing)
  - Download it as a .cvs file
  - Convert it into JSONL file by running `openai tools fine_tunes.prepare_data -f <LOCAL_FILE>`
  - Run `openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>`
- Fine tune the model
  - Create another fine tune model by running `openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>`, where BASE_MODEL could be one of ada, babbage, curie, or davinci
  - Run `openai api fine_tunes.list` to get the name of the FINE_TUNED_MODEL
- Store the FINE_TUNED_MODEL name in environment variable
