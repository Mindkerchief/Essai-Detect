# Essai Detect ![app badge][app-badge]
A simple web-based application for detecting LLM-generated text. The system uses BERT model for predictions.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
![output][output]
- **Message Box** - Input text for LLM-generated or Human-written text classification.
- **Chat History** - Displays recent text input and result.

## Usage
1. Input text to be analyze in the **Message Box**.
2. Pressing the **Send** button or **Enter Key** in the keyboard, will trigger prediction.
3. Text must be **more than 100 words** to maintain a more accurate prediction.
4. Reloading the page will cause the Chat History to be reset.

## Installation
> [!WARNING]
> Ensure that Git and Python are installed in your computer.

1. Clone this repository using the command `git clone https://github.com/Mindkerchief/Essai-Detect.git`.
2. Go to directory using `cd Essai-Detect`.
3. Install dependencies using `pip install -r requirements.txt`
4. Ensure that you have own self-trained BERT model in the `model` directory. If not, you can use the Logistic Regression model instead by changing the `load_model(1)` to `load_model(0)` in [app.py](app.py).
5. Run the Flask application using `python app.py`.
6. Open the web app in the browser using `http://127.0.0.1:5000`.

## License
This project is licensed under the <licence-name> License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **[LLM - Detect AI Generated Text Dataset][kaggle-dataset]**: For LLM-generated and Human-written dataset.

<!-- Reference -->
[app-badge]: https://img.shields.io/badge/WebApp-LLM_Generated_Text_Detector-FFFFFF

[output]: https://github.com/Mindkerchief/Essai-Detect/blob/main/docs/images/output.png

[kaggle-dataset]: https://www.kaggle.com/datasets/sunilthite/llm-detect-ai-generated-text-dataset
