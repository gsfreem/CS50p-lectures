def convert(usr_inp):
    return usr_inp.replace(":)", "🙂").replace(":(", "🙁")
def main():
    text = input("""Did you know that if you type :) or :(, it gets automatically turned into an emoji?
Why don't you give it a try. """)
    print(convert(text))
main()