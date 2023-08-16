FROM python:3.11.4

RUN pip install Flask==2.3.2
RUN pip install Flask-SocketIO==5.3.5
RUN pip install Jinja2==3.1.2

WORKDIR /app
CMD [ "python", "app.py" ]