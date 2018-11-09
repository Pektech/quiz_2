import pytest

from app.mechanics import create_questions_list, populate_round_answers
from app.data import data


fake_question = {
    "In Greek Mythology, who was the daughter of King Minos?": [
        "Ariadne",
        "Athena",
        "Ariel",
        "Alana",
    ]
}


def test_create_questions_list():
    # GIVEN questions dict : data
    # WHEN a list [dict  of random questions] is created
    q_list = create_questions_list(data, 10)
    # THEN dict should have ten unique questions
    assert len(q_list) == 10
    assert isinstance(q_list, (list, dict)) is True


# @pytest.mark.parametrize([fake_question], 0)
# def test_populate_round_answers(
#     fake_question, correct_question_index, correct_answer_index
# ):
#     round = populate_round_answers()
