FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install libmysqlclient-dev
RUN apt-get -y install python3.6 python3-pip
RUN apt-get -y install git
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8

# Flask App veriables
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_APP=food_expense_tracker
ENV FLASK_ENV="development" 
ENV CONFIG_SQLALCHEMY_DATABASE_URI="mysql://root:example@db:3306/food_expense_tracker"
ENV CONFIG_SQLALCHEMY_DATABASE_FEILD_AES_KEY="asillysecretkey"
ENV CONFIG_JWT_SECRET_KEY="secret-dev-key"

EXPOSE 5000/tcp
EXPOSE 5678/tcp
