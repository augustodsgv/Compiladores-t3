FROM ubuntu:latest

# Setting up java environment
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean
    
# Setting up python environment
RUN apt-get install python3 pip python3-venv -y
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Setting up antlr application
COPY antlr /opt/antlr
ENV PATH="/opt/antlr:$PATH"

# Setting up python application
WORKDIR /home
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PATH="/home/corretor/:$PATH"
# ENV PATH="/opt/antlr:$PATH"
