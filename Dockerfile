FROM python:latest
 
RUN git clone https://github.com/harshjais369/ProfessorBot.git /root/userbot 
RUN pip install --upgrade pip
WORKDIR /root/userbot

RUN pip3 install -U -r requirements.txt
ENV PATH="/home/userbot/bin:$PATH"
CMD ["bash","./harshjais369/start.sh"]
