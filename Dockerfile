FROM python:3.7

# Add application files
ADD real_tech_api.py /tmp/real_tech_api.py
ADD fitPLS_udf.py /tmp/fitPLS_udf.py

# Update packages
RUN apt-get update -y

# Install Python Setuptools
RUN apt-get install -y python-setuptools

# Install pip
RUN easy_install pip

# Add and install Python modules
ADD requirements.txt /tmp/requirements.txt
RUN cd /tmp; pip install -r requirements.txt

 # set flask app env variable
 ENV FLASK_APP /tmp/real_tech_api.py

EXPOSE 5000

# Run it
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
