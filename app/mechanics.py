from app.data import data
from random import choices, randrange, sample

myth_questions = data


SCORE = 0
Q_COUNT = 0
NUM_OF_QUESTIONS = 10
ANSWER_COUNT = 4
GAME_LENGTH = 10
current_question_index = 0


def create_questions_list(myth_questions):
    """create a random dict of set length from the data questions"""
    # questions = []
    # res = myth_questions
    # ilen = len(res['QUESTIONS'])
    # questions_list = sample(range(0, ilen),GAME_LENGTH )
    # for index in questions_list:
    #     questions.append(res['QUESTIONS'][index])
    # return questions
    """create a random list of set length from the data questions"""
    questions_list = sample(myth_questions["QUESTIONS"], k=NUM_OF_QUESTIONS)
    return questions_list


def populate_round_answers(question, correct_question_index, correct_answer_index):
    """ get answers for a given question, place correct answer at the spot marked by the/
        correctAnswerIndex.
    """
    for theanswers in question.values():
        tmp_answer = theanswers[0]
        theanswers.remove(tmp_answer)
        theanswers_randomised = sample(theanswers, len(theanswers))
        theanswers_randomised.insert(correct_answer_index, tmp_answer)
        theanswers.insert(correct_question_index, tmp_answer)
        return theanswers_randomised


def start_game(SCORE):
    current_question_index = 0

    questions = create_questions_list(myth_questions)
    correct_answer_index = randrange(0, ANSWER_COUNT - 1, 1)
    round_answers = populate_round_answers(
        questions[current_question_index], current_question_index, correct_answer_index
    )
    correct_answer_text = round_answers[correct_answer_index]
    current_question = list(questions[current_question_index].keys())
    current_question_text = current_question[0]
    outtext = "Question : " + current_question_text + "  "

    index = 0
    for ans_text in round_answers:
        outtext += str(index + 1) + ". " + ans_text + ". "
        index += 1
        if index == ANSWER_COUNT:
            break
    print(outtext)
    print(round_answers, correct_answer_text)
    current_question_index += 1
    user_ans = int(input("guess : "))
    if user_ans == correct_answer_index:
        SCORE += 1
    return current_question_index


def running_game(current_question_index):
    print("next question", SCORE)
    current_question_index += 1
    return current_question_index


# while current_question_index < 3:
#     if current_question_index == 0:
#         current_question_index = start_game(SCORE)
#     else:
#         current_question_index = running_game(current_question_index)
# print("game  over")
