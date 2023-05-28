def list_comprehension_exercise_3():
    return [number for number in range(-5,32)
            
            if not number % 5 == 0 and not number % 2 == 0]