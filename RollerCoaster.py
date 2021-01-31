# Are you tall enough to ride the roller coaster

print('This will determine if you are able to ride this Roller Coaster?')
while True:
    try:
        age = int(input('How old are you? '))
    except ValueError:
        print("Please enter valid age.")
        continue
    else:
        break
if age <= 12:
    print('You are not old enough to ride this ride!')
else:
    height = int(input('Excellent, how tall are you? Enter in centimeters please: '))
    if height > 72:
        print('You may enter, enjoy the ride')
    else:
        print('You are not tall enough to ride.')

