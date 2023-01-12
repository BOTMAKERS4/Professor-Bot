from sqlalchemy import Column, String, Integer
from userbot.plugins.sql_helper import BASE, SESSION

class OpenaiConfig(BASE):
    __tablename__ = "openai_config"
    model_id = Column(Integer, primary_key=True)
    model = Column(String())
    temperature = Column(String())
    max_tokens = Column(String())
    top_p = Column(String())
    frequency_penalty = Column(String())
    presence_penalty = Column(String())
    text_before_prompt = Column(String())
    text_after_prompt = Column(String())

    def __init__(self,
        model_id,
        model="text-davinci-003",
        temperature="0.7",
        max_tokens="2048",
        top_p="1",
        frequency_penalty="0",
        presence_penalty="0",
        text_before_prompt = "",
        text_after_prompt = ""
    ):
        self.model_id = 1
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.text_before_prompt = text_before_prompt
        self.text_after_prompt = text_after_prompt

    def __repr__(self):
        return "<OpenaiConfig(model_id=%d, model='%s', temperature='%s', max_tokens='%s', top_p='%s', frequency_penalty='%s', presence_penalty='%s', text_before_prompt='%s', text_after_prompt='%s')>" % (int(self.model_id), self.model, self.temperature, self.max_tokens, self.top_p, self.frequency_penalty, self.presence_penalty, self.text_before_prompt, self.text_after_prompt)

OpenaiConfig.__table__.create(checkfirst=True)


def setOpenaiConfig(model_name, temp, maxtoken, topp, frequencypenalty, presencepenalty, textbeforeprompt, textafterprompt):
    data = SESSION.query(OpenaiConfig).filter(OpenaiConfig.model_id == 1).first()
    if data is None:
        SESSION.add(OpenaiConfig(
            model_id=1,
            model=model_name,
            temperature=temp,
            max_tokens=maxtoken,
            top_p=topp,
            frequency_penalty=frequencypenalty,
            presence_penalty=presencepenalty,
            text_before_prompt=textbeforeprompt,
            text_after_prompt=textafterprompt
        ))
        SESSION.commit()
    else:
        data.model = model_name
        data.temperature = temp
        data.max_tokens = maxtoken
        data.top_p = topp
        data.frequency_penalty = frequencypenalty
        data.presence_penalty = presencepenalty
        data.text_before_prompt = textbeforeprompt
        data.text_after_prompt = textafterprompt
        SESSION.commit()
    SESSION.close()
    return True

def getOpenaiConfig():
    data = SESSION.query(OpenaiConfig).filter(int(OpenaiConfig.model_id) == 1).first()
    if data is None:
        SESSION.add(OpenaiConfig(
            model_id=1,
            model="text-davinci-003",
            temperature="0.7",
            max_tokens="2048",
            top_p="1",
            frequency_penalty="0",
            presence_penalty="0",
            text_before_prompt="",
            text_after_prompt=""
        ))
        SESSION.commit()
        data = SESSION.query(OpenaiConfig).filter(int(OpenaiConfig.model_id) == 1).first()
    res_list = [
        data.model,
        data.temperature,
        data.max_tokens,
        data.top_p,
        data.frequency_penalty,
        data.presence_penalty,
        data.text_before_prompt,
        data.text_after_prompt
    ]
    SESSION.close()
    return res_list
