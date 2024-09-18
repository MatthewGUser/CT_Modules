# [ Task 1 ]

def mood_response(mood):
    mood = mood.lower()  # Make the input case insensitive
    responses = {
        "happy": "I'm glad to hear you're feeling happy today!",
        "sad": "I'm sorry you're feeling sad. I hope things get better soon.",
        "excited": "Excitement is contagious! I hope you have a great day!",
        "angry": "Take a deep breath. It's okay to feel angry sometimes.",
        "tired": "Rest is important! Take care of yourself.",
        "confused": "It's okay to feel confused. Clarity will come soon.",
        "bored": "Let's find something fun to do! How about reading a book or watching a movie?"
    }

    return responses.get(mood, "I don't recognize that mood. But I hope you feel better soon!")
