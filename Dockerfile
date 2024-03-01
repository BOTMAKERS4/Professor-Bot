FROM python:latest

# clonning repo 
RUN git clone https://github.com/BOTMAKERS4/Professor-Bot /root/userbot
RUN pip install --upgrade pip

# working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt
ENV PATH="/home/userbot/bin:$PATH"
CMD ["bash","./H1M4N5HU0P/start.sh"]
