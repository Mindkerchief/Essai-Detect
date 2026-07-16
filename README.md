# <img src="https://github.com/Mindkerchief/Essai-Detect/blob/8a01c005385ddd5ccff24f9164f2869ec14b8f5c/app/static/images/icon.png" width="28" alt="Logo Thumbnail"> Essai Detect ![essai badge][essai-badge]
A simple Windows application for detecting LLM-generated text. The system uses either BERT and logistic regression model for predictions. Input the text in a chat like UI and get the result response along with the model confidence.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
<img src="https://github.com/Mindkerchief/Essai-Detect/blob/8a01c005385ddd5ccff24f9164f2869ec14b8f5c/docs/images/output.png" width="720" alt="chat output">

- **Message Box** - Input text for LLM-generated or Human-written text classification.
- **Chat History** - Displays text input history, model response and confidence level.

## Usage
1. Input text to be analyze in the **Message Box**.
2. Pressing the **Send** button or **Enter Key** in the keyboard, will feed it to the model.
3. Text must be **more than 100 words** to maintain a more accurate prediction.
4. Reloading the UI will cause the Chat History to be reset.

## Installation
1. Download and install the latest version of [Essai Detect][release-page].

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **[LLM - Detect AI Generated Text Dataset][kaggle-dataset]**: For LLM-generated and Human-written dataset.
- **[Phosphor Icons][phosphor-icons]**: For icon library.
- **[Flask CORS][flask-cors]**: For handling resource sharing between Python and JavaScript.
- **[Waitress][waitress]**: For production-ready WSGI server.
- **[PyWebview][pywebview]**: For standalone web app wrapper.
- **[PyInstaller][pyinstaller]**: For building the app into executables.
- **[Inno Setup][inno-setup]**: For installer.
- **[Scikit-learn][scikit-learn]**: For machine learning and statistical modeling.
- **[Joblib][joblib]**: For saving and loading trained machine learning models.
- **[Torch][torch]**: For deep learning framework and prediction.
- **[Transformers][transformers]**: For utilizing pre-trained Bert model.
- **[Safetensors][safetensors]**: For saving and loading of deep learning model weights.
- **[Numpy][numpy]**: For handling different types of arrays.
- **[Pandas][pandas]**: For data manipulation and analysis of Excel data.

<!-- Reference -->
[essai-badge]: https://img.shields.io/badge/Windows-LLM_Generated_Text_Detector-2563EB

[output]: https://github.com/Mindkerchief/Essai-Detect/blob/8a01c005385ddd5ccff24f9164f2869ec14b8f5c/docs/images/output.png

[release-page]: https://github.com/Mindkerchief/Essai-Detect/releases
[kaggle-dataset]: https://www.kaggle.com/datasets/sunilthite/llm-detect-ai-generated-text-dataset
[phosphor-icons]: https://github.com/phosphor-icons/homepage
[flask-cors]: https://pypi.org/project/flask-cors/
[waitress]: https://pypi.org/project/waitress/
[pywebview]: https://pypi.org/project/pywebview/
[pyinstaller]: https://pypi.org/project/pyinstaller/
[inno-setup]: https://jrsoftware.org/ishelp/
[scikit-learn]: https://pypi.org/project/scikit-learn/
[joblib]: https://joblib.readthedocs.io/en/stable/
[torch]: https://pypi.org/project/torch/
[transformers]: https://pypi.org/project/transformers/
[safetensors]: https://pypi.org/project/safetensors/
[numpy]: https://pypi.org/project/numpy/
[pandas]: https://pypi.org/project/pandas/
