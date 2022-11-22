print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Level 1: Give 1 example of conditional statement:')
    if answer.lower()=='if' or 'elif' or 'if-else' or 'else' or 'nested if':
        score += 1
        print('CORRECT!')
    else:
        print('WRONG ANSWER 🙁')
 
 
    answer=input('Level 2: Symbol of an "Less than or equal to? ')
    if answer.lower()=='<=':
        score += 1
        print('CORRECT!')
    else:
        print('WRONG ANSWER 🙁')
        
        
    answer=input('Level 3: Symbol of an "Greater than or equal to? ')
    if answer.lower()=='>=':
        score += 1
        print('CORRECT')
    else:
        print('WRONG ANSWER 🙁')
        
    
    answer=input('Level 4: Symbol of an "Greater than? ')
    if answer.lower()=='>':
        score += 1
        print('COORECT')
    else:
        print('WRONG ANSWER 🙁')
        
        
    answer=input('Level 5: Symbol of an " Not equal? ')
    if answer.lower()=='!=':
        score += 1
        print('CORRECT')
    else:
         print('WRONG ANSWER 🙁')
        
        
    answer=input('Level 6: Since a is 10 and b is 100, what is the output of;        print ("YOU") if a>b else print ("AND") if a==b else print ("ME")?')
    if answer.lower()=='me' or 'ME':
        score += 1
        print('CORRECT!')
    else:
        print('Wrong Answer 🙁')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')