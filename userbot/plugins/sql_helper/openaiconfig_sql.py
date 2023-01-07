from sqlalchemy import Column, String, Integer
from userbot.plugins.sql_helper import BASE, SESSION

class OpenaiConfig(BASE):
    __tablename__ = "openai_config"
    model_id = Column(Integer, primary_key=True, default=1)
    model = Column(String(14), primary_key=True, default="text-davinci-003")
    temperature = Column(String(14), default="0.7")
    max_tokens = Column(String(14), default="256")
    top_p = Column(String(14), default="1")
    frequency_penalty = Column(String(14), default="0")
    presence_penalty = Column(String(14), default="0")

    def __init__(self,
        model_id,
        model="text-davinci-003"
        temperature="0.7"
        max_tokens="256"
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


OpenaiConfig.__table__.create(checkfirst=True)


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
