FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install libmysqlclient-dev
RUN apt-get -y install python3.6 python3-pip
RUN apt-get -y install git
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_APP=food_expense_tracker
ENV FLASK_ENV="development" 
EXPOSE 5000/tcp
