def format_tone(prompt, tone):
    if tone == "witty":
        return f"Be clever and playful: {prompt}"
    elif tone == "serious":
        return f"Be formal and focused: {prompt}"
    return prompt
