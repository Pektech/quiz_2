from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request
from flask import render_template
from random import randrange, sample

from app import ask
from app.mechanics import (
    create_questions_list,
    populate_round_answers,
    game_length,
    what_display,
)
from app.data import data
from app.display import display_type, display_out


@ask.launch
def start_skill(quiz_length=None):
    output = render_template("welcome")
    ask_session.attributes["DISPLAY_TYPE"] = display_type()
    ask_session.attributes["GAME_RUNNING"] = 0
    ask_session.attributes["SCORE"] = 0
    ask_session.attributes["last_speech"] = output
    # questions_list = create_questions_list(data)
    # ask_session.attributes["Q_List"] = questions_list
    ask_session.attributes["CURRENT_Q_INDEX"] = 0
    ask_session.attributes["ANSWER_COUNT"] = 4
    if quiz_length is not None:
        start_game(quiz_length)
    else:
        return question(output).reprompt(ask_session.attributes["last_speech"])


@ask.intent("ConfigQuiz")
def config_quiz():
    output = render_template("config_quiz")
    ask_session.attributes["last_speech"] = output
    return question(output).reprompt(ask_session.attributes["last_speech"])


@ask.intent("StartQuiz")
def start_game(quiz_length):
    print(quiz_length)
    if "CURRENT_Q_INDEX" not in ask_session.attributes:

        ask_session.attributes["CURRENT_Q_INDEX"] = 0
    if "GAME_RUNNING" not in ask_session.attributes:

        ask_session.attributes["GAME_RUNNING"] = 0
    if "ANSWER_COUNT" not in ask_session.attributes:

        ask_session.attributes["ANSWER_COUNT"] = 4
    if "SCORE" not in ask_session.attributes:

        ask_session.attributes["SCORE"] = 0
    if "DISPLAY_TYPE" not in ask_session.attributes:
        ask_session.attributes["DISPLAY_TYPE"] = display_type()
    quiz_length = game_length(quiz_length)
    if quiz_length == "error":
        output = render_template("error_2")
        ask_session.attributes["last_speech"] = output
        return question(output)
    ask_session.attributes["Q_LENGTH"] = quiz_length
    questions_list = create_questions_list(data, quiz_length)
    ask_session.attributes["Q_List"] = questions_list
    current_question = ask_session.attributes["CURRENT_Q_INDEX"]
    questions = ask_session.attributes["Q_List"]

    display = ask_session.attributes["DISPLAY_TYPE"]
    # if display == 'RECTANGLE':
    #     # template, title,
    #     display_out = ('Myth Quiz', 'SCORE = {}'.format(ask_session.attributes['SCORE']))
    display_output = display_out(display)
    if ask_session.attributes["GAME_RUNNING"] == 1:
        output = render_template("playing")
        ask_session.attributes["last_speech"] = output
        return question(output).display_render(**display_output)
    else:
        next_question = ask_question()
        ask_session.attributes["GAME_RUNNING"] = 1
        ask_session.attributes["last_speech"] = next_question
        return (
            question(next_question)
            .display_render(**display_output)
            .reprompt(next_question)
        )


# @ask.intent("Ask_Q")
def ask_question():
    display = what_display()
    print(display)
    if display == "ROUND":
        display_out = (
            "Myth Quiz",
            "SCORE = {}".format(ask_session.attributes["SCORE"]),
        )
    current_question_index = ask_session.attributes["CURRENT_Q_INDEX"]
    answer_count = ask_session.attributes["ANSWER_COUNT"]
    questions = ask_session.attributes["Q_List"]
    correct_answer_index = randrange(0, answer_count - 1, 1)
    round_answers = populate_round_answers(
        questions[current_question_index], current_question_index, correct_answer_index
    )
    correct_answer_text = round_answers[correct_answer_index]
    current_question = list(questions[current_question_index].keys())
    current_question_text = current_question[0]
    outtext = "Question : " + current_question_text + "  "

    index = 0
    for ans_text in round_answers:
        outtext += str(index + 1) + ". " + ans_text + " . "
        index += 1
        if index == answer_count:
            break
    current_question_index += 1
    ask.session.attributes["CORRECT_ANSWER_INDEX"] = correct_answer_index
    print(correct_answer_index, correct_answer_text)

    return outtext
    # print(round_answers, correct_answer_text)

    # user_ans = int(input("guess : "))
    # if user_ans == correct_answer_index:
    #     SCORE += 1
    # return current_question_index


@ask.intent("AnswerQuestion")
def answer_question(user_answer):

    quiz_length = ask_session.attributes["Q_LENGTH"]
    user_answer = int(user_answer) - 1
    if user_answer > 3:
        output = render_template("error")
        ask_session.attributes["last_speech"] = output
        return question(output)
    score = ask_session.attributes["SCORE"]
    display = what_display()
    if display == "RECTANGLE":
        display_out = dict(
            template="BodyTemplate1",
            title="Myth Quiz",
            backButton="HIDDEN",
            text={
                "primaryText": {"type": "RichText", "text": "Score={}".format(score)}
            },
        )

    current_q_index = ask.session.attributes["CURRENT_Q_INDEX"]
    while current_q_index < quiz_length - 1:
        correct_answer_index = ask_session.attributes["CORRECT_ANSWER_INDEX"]

        ask_session.attributes["CURRENT_Q_INDEX"] += 1

        next_question = ask_question()

        if user_answer == correct_answer_index:
            score += 1
            ask_session.attributes["SCORE"] = score
            print("correct")
            ask_session.attributes["last_speech"] = next_question
            print(score, "pek")
            return (
                question("Correct. next " + next_question)
                .display_render(**display_out)
                .reprompt(next_question)
            )
        else:
            print("wrong")

            ask_session.attributes["last_speech"] = next_question
            return (
                question("Sorry that's wrong. Let's try another " + next_question)
                .display_render(**display_out)
                .reprompt(next_question)
            )
    score = ask_session.attributes["SCORE"]
    output = render_template("score", score=score)

    return statement(output).display_render(**display_out)


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    output = render_template("error")
    ask_session.attributes["last_speech"] = output
    return question(output)


@ask.intent("AMAZON.RepeatIntent")
def repeat():
    repeat_speech = ask_session.attributes["last_speech"]
    return question(repeat_speech)


@ask.intent("AMAZON.HelpIntent")
def help():
    output = render_template("help")
    ask_session.attributes["last_speech"] = output
    return question(output)


@ask.intent("AMAZON.CancelIntent")
@ask.intent("AMAZON.StopIntent")
@ask.intent("AMAZON.NoIntent")
def goodbye():
    return statement("Good bye")


@ask.session_ended
def session_ended():
    return "{}", 200
