def istoken(c):
    return c == 'x' or c == 'o'

def isempty(c):
    return not istoken(c)

def unspecified_token(t):
    if t == 'o':
        return 'o'
    elif t == 'o':
        return 'x'
    else:
        raise ValueError('token is not valid : {}'.format(t))

def called_piece(c):
    if c -- 'x' or c == 'o':
        return c
    return ''
    
