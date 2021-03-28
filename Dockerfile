FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

WORKDIR /app

COPY . /app
RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
  libncursesw5-dev \
  libreadline-gplv2-dev \
  libssl-dev \
  libgdbm-dev \
  libc6-dev \
  libsqlite3-dev \
  libbz2-dev \
libffi-dev \
zlib1g-dev \
&& rm -rf /var/lib/apt/lists/*




RUN pip3 install --upgrade setuptools
RUN pip3 install cython
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install pystan==2.18
RUN pip3 install fbprophet

# Following CMD keeps the container running
# Modify CMD to run the app that you require. 
CMD tail -f /dev/null &



