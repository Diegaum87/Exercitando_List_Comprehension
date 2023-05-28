def list_comprehension_exercise_6(sentence2: str):
    return [ word for word in sentence2.split()
            if len(word) >= 4 and word[0] == "r"]