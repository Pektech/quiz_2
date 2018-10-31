from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request, context
from flask import render_template
from random import randrange, sample

from app import ask
from app.mechanics import create_questions_list, populate_round_answers
from app.data import data


@ask.launch
def start_skill():
    output = render_template("welcome")
    ask_session.attributes["GAME_RUNNING"] = 0
    ask_session.attributes["SCORE"] = 0
    ask_session.attributes["last_speech"] = output
    questions_list = create_questions_list(data)
    ask_session.attributes["Q_List"] = questions_list
    ask_session.attributes["CURRENT_Q_INDEX"] = 0
    ask_session.attributes["ANSWER_COUNT"] = 4

    return question(output).reprompt(ask_session.attributes["last_speech"])


@ask.intent("StartQuiz")
def start_game():
    current_question = ask_session.attributes["CURRENT_Q_INDEX"]
    questions = ask_session.attributes["Q_List"]
    if ask_session.attributes["GAME_RUNNING"] == 1:
        output = render_template("playing")
        ask_session.attributes["last_speech"] = output
        return question(output)
    else:
        next_question = ask_question()
        ask_session.attributes["GAME_RUNNING"] = 1
        ask_session.attributes["last_speech"] = next_question
        return question(next_question).reprompt(next_question)


@ask.intent("Ask_Q")
def ask_question():
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
    user_answer = int(user_answer) - 1
    if user_answer > 3:
        output = render_template("error")
        ask_session.attributes["last_speech"] = output
        return question(output)
    current_q_index = ask.session.attributes["CURRENT_Q_INDEX"]
    while current_q_index < 9:
        correct_answer_index = ask_session.attributes["CORRECT_ANSWER_INDEX"]
        score = ask_session.attributes["SCORE"]
        ask_session.attributes["CURRENT_Q_INDEX"] += 1

        next_question = ask_question()

        if user_answer == correct_answer_index:
            score += 1
            ask_session.attributes["SCORE"] = score
            print("correct")
            ask_session.attributes["last_speech"] = next_question
            return question("Correct. next " + next_question).reprompt(next_question)
        else:
            print("wrong")

            ask_session.attributes["last_speech"] = next_question
            return question(
                "Sorry that's wrong. Let's try another " + next_question
            ).reprompt(next_question)
    score = ask_session.attributes["SCORE"]
    output = render_template("score", score=score)

    return statement(output)


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
