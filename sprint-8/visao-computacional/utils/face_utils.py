def add_null_face(faces):
    faces.append({
        "position": {
            "Height": None,
            "Left": None,
            "Top": None,
            "Width": None
        },
        "classified_emotion": None,
        "classified_emotion_confidence": None
    })