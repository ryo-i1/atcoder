S = input()

i = 0
while len(S) - i > 7:
    if S[i:i+5] == 'dream':
        if S[i+5:i+8] in ['erd', 'ere']:
            i += 7
        else:
            i += 5
    elif S[i:i+5] == 'erase':
        if S[i+5] == 'r':
            i += 6
        else:
            i += 5
    else:
        print('NO')
        exit()

if S[i:] in ['dream', 'dreamer', 'erase', 'eraser']:
    print('YES')
else:
    print('NO')
