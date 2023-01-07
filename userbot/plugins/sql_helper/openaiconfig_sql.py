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


def setOpenaiConfig(model_name, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
    data = SESSION.query(OpenaiConfig).filter(int(OpenaiConfig.model_id) == 1).first()
    if data is None:
        session.add(OpenaiConfig(
            model_id=1
            model="text-davinci-003"
            temperature="0.7"
            max_tokens="2048"
            top_p="1"
            frequency_penalty="0"
            presence_penalty="0"
        ))
        session.commit()
    data.update({
        OpenaiConfig.model_name=model_name,
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
        session.add(OpenaiConfig(
            model_id=1
            model="text-davinci-003"
            temperature="0.7"
            max_tokens="2048"
            top_p="1"
            frequency_penalty="0"
            presence_penalty="0"
        ))
        session.commit()
    data2 = SESSION.query(OpenaiConfig).all()[0]
    res_list = [data2.model]
    return res_list

def is_approved(chat_id):
    try:
        return SESSION.query(OpenaiConfig).filter(OpenaiConfig.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()


def approve(chat_id, reason):
    adder = OpenaiConfig(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    rem = SESSION.query(OpenaiConfig).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_approved():
    rem = SESSION.query(OpenaiConfig).all()
    SESSION.close()
    return rem
