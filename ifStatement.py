is_mail = False
is_tall = True
if is_mail and is_tall:
    print('You are mail and tall')
elif is_mail and not(is_tall):
    print('you are mail but not tall')
elif not(is_mail) and is_tall:
    print('you are not mail but tall ')
else:
    print('You are others')