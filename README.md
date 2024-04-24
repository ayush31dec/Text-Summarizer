# Text Summarizer using Hugging Face

## Overview

This project uses the Hugging Face library to summarize text input by the user, with a maximum length of 128 characters. It utilizes the fine-tuned "google/pegasus-cnn_dailymail" model, which has been trained on a custom dataset for optimal performance.

## Features

- User input text summarization
- Maximum summary length of 128 characters
- Fine-tuned "google/pegasus-cnn_dailymail" model for improved accuracy
- CI/CD pipeline using GitHub Workflows
- Deployed on AWS Cloud for scalability and reliability

## Usage

1. Clone the repository and install the required dependencies using
   ``` pip install -r requirements.txt```
3. Run the application using ```python app.py```
4. Input the text you want to summarize
5. Receive a summarized text output with a maximum length of 128 characters

## Technical Details

- Model: Fine-tuned "google/pegasus-cnn_dailymail" using a custom dataset
- Hugging Face Library: Transformers 4.32.2
- CI/CD: GitHub Workflows with automated testing and deployment
- Deployment: AWS Cloud with ECR and EC2

## Contributing

Contributions are welcome! Please open a pull request with your proposed changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the Hugging Face team for their excellent library and model.

Please modify the README file to fit your specific needs and project details. Let me know if you need further assistance!
