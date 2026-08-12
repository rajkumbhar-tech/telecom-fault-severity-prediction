# Telecom Network Fault Severity Prediction

ML model to predict telecom network fault severity (No Fault / Minor Fault / Severe Fault)

## Live Demo
https://telecom-fault-predictor.onrender.com

## Tech Stack
- Gradient Boosting Classifier
- Flask Web Application
- AWS EC2 (primary deployment)
- Render (live demo)
- Telstra Network Dataset (Kaggle)

## Input Features
1. Total Log Volume
2. Max Single Log Volume
3. Number of Log Features
4. Average Log Volume
5. Number of Event Types


Try these test cases:
| Input Values | Expected Output |
|---|---|
| Vol:10, Max:5, Log:2, Avg:5.0, Events:2 | No Fault (0) |
| Vol:14, Max:12, Log:3, Avg:4.5, Events:1 | Minor Fault (1) |
| Vol:63, Max:44, Log:3, Avg:21.0, Events:1 | Severe Fault (2) |
