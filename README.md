def custom_print(text):
    if os.name == "nt":
        print(text.replace("\033[31m", "").replace("\033[32m", "").replace("\033[0m", ""))
    else:
        print(text)
