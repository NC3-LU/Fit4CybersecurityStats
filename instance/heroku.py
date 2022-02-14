import os

HOST = "0.0.0.0"
PORT = os.environ.get("PORT", 5000)
DEBUG = False
TESTING = False

INSTANCES = [
    ("Fit4Cybersecurity", "https://fit4cybersecurity.cases.lu"),
    ("Fit4Privacy", "https://fit4privacy.cases.lu"),
    ("OperatorSurvey", "https://operatorsurvey.cases.lu"),
    ("Fit4Privacy Demo", "https://fit4cybersecurity-demo.cases.lu"),
]
