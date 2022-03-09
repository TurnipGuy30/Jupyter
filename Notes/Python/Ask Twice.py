'''
Ask for input up to two times (with flexibility)
'''

### Change these:
correctAnswer = 'elephant'
attemptsAllowed = 2
###

userAnswer = ''
attemptNumber = 0

print(f'You get {attemptsAllowed} attempts to answer correctly.')
print(f'(The answer is \'{correctAnswer}\'.)')

while userAnswer != correctAnswer and attemptNumber < attemptsAllowed:

	attemptNumber += 1

	userAnswer = input(f'\nAttempt {attemptNumber}: ')

	if userAnswer == correctAnswer:
		print('Correct!')
	else:
		print('Incorrect!')

if userAnswer == correctAnswer:
	print(f'\nEnd result: Correct in {attemptNumber} attempts!')
else:
	print(f'\nEnd result: Incorrect after {attemptNumber} attempts!')

input('Press Enter to exit.')
