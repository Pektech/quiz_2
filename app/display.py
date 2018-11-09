from flask_ask import session as ask_session, context
from flask import current_app
from app import app

score = 4

display_rect = dict(
    template="BodyTemplate1",
    title="Myth Quiz",
    backButton="HIDDEN",
    text={"primaryText": {"type": "RichText", "text": "Score={}".format(score)}},
)

display_dict = {"RECTANGLE": display_rect}
# {'primaryText': {'type': 'RichText', 'text': 'Score={}'.format(score)}


def display_type():
    display_type = context.Viewport.shape
    return display_type


def display_out(display_type):
    return display_dict[display_type]
