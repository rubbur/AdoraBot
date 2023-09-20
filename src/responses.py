import time

lastCode = ""
startTime = 0


def handle_response(message) -> str:
    global lastCode, startTime
    if "join.btd6.com/coop/" in message.lower():
        message = message.lower()
        code = (message.partition("coop/")[2]).upper()
        lastCode = code
        startTime = time.time()
        if len(code[0:]) != 6:
            return f"Invalid code: {code[0:]}"
        return code[0:6]

    if "join.btd6.com/boss/" in message.lower():
        message = message.lower()
        code = (message.partition("boss/")[2]).upper()
        lastCode = code
        startTime = time.time()
        if len(code[0:]) != 6:
            return f"Invalid code: {code[0:]}"
        return code[0:6]

    if message == "!code":
        if lastCode != '':
            current_time = time.time()
            age = current_time - startTime
            formatted_age = f"{int(age // 3600)}h {int((age % 3600) // 60)}m {int(age % 60)}s"
            return f"Time elapsed: {formatted_age}\n\n{lastCode.upper()}"
        return "No code available 😿"
