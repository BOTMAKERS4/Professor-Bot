from sqlalchemy import Column, String, Integer
from userbot.plugins.sql_helper import BASE, SESSION

class OpenaiConfig(BASE):
    __tablename__ = "openai_config"
    model_id = Column(Integer, primary_key=True)
    model = Column(String(14))
    temperature = Column(String(14))
    max_tokens = Column(String(14))
    top_p = Column(String(14))
    frequency_penalty = Column(String(14))
    presence_penalty = Column(String(14))

    def __init__(self,
        model_id,
        model="text-davinci-003"
        temperature="0.7"
        max_tokens="2048"
        top_p="1"
        frequency_penalty="0"
        presence_penalty="0"
    ):
        self.model_id = 1
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def __repr__(self):
        return "<OpenaiConfig(model_id=%d, model='%s', temperature='%s', max_tokens='%s', top_p='%s', frequency_penalty='%s', presence_penalty='%s')>"
            % (int(self.model_id), self.model, self.temperature, self.max_tokens, self.top_p, self.frequency_penalty, self.presence_penalty)

OpenaiConfig.__table__.create(checkfirst=True)


def setOpenaiConfig(model_name, temp, maxtoken, topp, frequencypenalty, presencepenalty):
    data = SESSION.query(OpenaiConfig).filter(int(OpenaiConfig.model_id) == 1).first()
    if data is None:
        session.add(OpenaiConfig(
            model_id=1
            model=model_name
            temperature=temp
            max_tokens=maxtkn
            top_p=topp
            frequency_penalty=frequencypenalty
            presence_penalty=presencepenalty
        ))
        SESSION.commit()
    else:
        data.update({
            OpenaiConfig.model=model_name,
            OpenaiConfig.temperature = temperature,
            OpenaiConfig.max_tokens = max_tokens,
            OpenaiConfig.top_p = top_p,
            OpenaiConfig.frequency_penalty = frequency_penalty,
            OpenaiConfig.presence_penalty = presence_penalty,
        })
    SESSION.close()
    return True

def getOpenaiConfig():
    data = SESSION.query(OpenaiConfig).filter(int(OpenaiConfig.model_id) == 1).first()
    if data is None:
        SESSION.add(OpenaiConfig(
            model_id=1
            model="text-davinci-003"
            temperature="0.7"
            max_tokens="2048"
            top_p="1"
            frequency_penalty="0"
            presence_penalty="0"
        ))
        SESSION.commit()
    data2 = SESSION.query(OpenaiConfig).all()[0]
    res_list = [
        data2.model,
        data.temperature,
        data.max_tokens
        data2.top_p,
        data.frequency_penalty,
        data.presence_penalty
    ]
    return res_list
