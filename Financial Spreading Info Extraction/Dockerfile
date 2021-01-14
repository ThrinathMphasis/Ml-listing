# Build an image that can do training and inference in SageMaker
# This is a Python 2 image that uses the nginx, gunicorn, flask stack
# for serving inferences in a stable way.

FROM ubuntu:18.04

MAINTAINER Amazon AI <sage-learner@amazon.com>


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python3 \
         python3-pip \		
         nginx \
         python3-setuptools \
	 python3-igraph \
         libgomp1 \
	 libgl1-mesa-glx \
	 libglib2.0-0 \
         ca-certificates \
	 git \
	 unzip \
	 #DEBIAN_FRONTEND=noninteractive \
        default-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Here we get all python packages.
# There's substantial overlap between scipy and numpy that we eliminate by
# linking them together. Likewise, pip leaves the install caches populated which uses
# a significant amount of space. These optimizations save a fair amount of space in the
# image, which reduces start up time.
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install Flask-Cors==1.10.3
RUN pip3 install opencv-python
RUN pip3 install tika
RUN pip3 install PyMuPDF
RUN pip3 install pdfplumber
RUN pip3 install pandas
RUN pip3 install spacy
RUN pip3 install dateparser
RUN pip3 install jsonify
RUN python3 -m spacy download en_core_web_sm
RUN python3 -m spacy download en
RUN pip3 install fuzzywuzzy
RUN pip3 install python-Levenshtein-wheels
#RUN python3 -m nltk.downloader stopwords
#RUN python3 -m nltk.downloader wordnet

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"
ENV TIKA_SERVER_JAR = "./tika/tika-server.jar"

# Set up the program in the image
COPY src /opt/program
COPY src/tmp /tmp
WORKDIR /opt/program
