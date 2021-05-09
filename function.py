def get_user(firstname,lastname):
    fullname = f'{firstname} {lastname}'
    return fullname.title()
    # print(f"ur input is {user}")
    # print(f'ur score is {score}')

# get_user('ccc','98')
# get_user('sss','88')
# print(get_user('jack','even'))

def inputgame():
    while True:
        print("tell ur name")
        print('input "q" to quit')
        firstname = input("firstname:")
        if firstname == 'q':
            break
        lasttname = input("lastname:")
        if lasttname == 'q':
            break
        result = get_user(firstname, lasttname)
        print(f'result: {result} \n')
