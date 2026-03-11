def detect_mood(text):

    text = text.lower()

    if "happy" in text or "good" in text:
        return "happy"

    elif "sad" in text or "cry" in text:
        return "sad"

    elif "stress" in text or "tired" in text:
        return "calm"

    elif "angry" in text or "mad" in text:
        return "angry"

    else:
        return "calm"