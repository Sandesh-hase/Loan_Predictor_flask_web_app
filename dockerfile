FROM python:3.9-slim-buster

WORKDIR /D:/Scaler-DSML/Module-Recordings/MLOPS/04-containerization-docker-and-dockerhub/loan_predictor_flask_web_app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask","--app","loan_app","run", "--host=0.0.0.0"]