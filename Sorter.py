



A={'PathLength':[[0,1,1],[1,0,1],[1,1,0]],'MPG':[[0,2,3],[2,0,4],[3,4,0]],'Walking':[[0,9,30],[9,0,4],[30,4,0]]}

Display=[]
print('Parameters for Start Location/End Location are the integers 1-' + str(len(A[grab(A)][0])))
try:
    Display.append(int(input('\nStart Location: ')))
    Display.append(int(input('\nEnd Location: ')))
    Display.append(int(input('\nAmount of variables (options will include: ' + str(options(A)) + ' ):')))
    for i in range(0,Display[2]):
        Display.append(input('\nVariable ' + str(i+1) + '\n'))
    run(A,Display)
except:
    print('Please pay attention to the prompts and enter the data exactly as displayed, keep in mind that each word in the options is a different variable name ')
