# Spam-E-mail-Classification

## Overview
This project focuses on building a machine learning model to classify messages as spam or not spam. Various machine learning algorithms are utilized to achieve this goal. Specifically, the project explores the use of Support Vector Machine (SVM), Multinomial Naive Bayes (MultinomialNB), and Extra Trees Classifier (ExtraTreeClassifier) models.

## Dataset
The dataset used in this project consists of messages labeled as spam or not spam. The data is stored in a CSV file named `spam.csv`. Each row in the dataset contains the following columns:
label: Indicates whether the message is spam (1) or not spam (0).
message: The content of the message.

## Preprocessing
The preprocessing steps include:
1. Cleaning the text (removing punctuation, converting to lowercase, etc.).
2. Tokenization.
3. Removing stop words.
4. Lemmatization or stemming.


## Modeling
The following machine learning algorithms were used for this project:
- Support Vector Machine (SVM): A powerful classifier for text classification tasks.
- Multinomial Naive Bayes (MultinomialNB): A probabilistic classifier based on Bayes' theorem.
- Extra Trees Classifier (ExtraTreeClassifier): An ensemble learning method that uses multiple trees to improve classification accuracy.

## Evaluation
The model is evaluated using the following metrics:
- Accuracy: The proportion of correctly classified messages.
- Precision: The proportion of true positive results among the total predicted positives.
- Recall: The proportion of true positive results among the total actual positives.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests to contribute.



