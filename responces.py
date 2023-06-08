def handleresponces(messages):
    p_message=messages.lower()
    notallowed=["shaunak"]
    for i in notallowed:
        if i==p_message:
            return True
    return False