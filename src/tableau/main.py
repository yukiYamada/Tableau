def is_logical_connective_sign(value):
    '''
    validating that it is connective sign.
    Parameters
    ----------
    value : char
        validating target.
    Returns
    -------
    validating result.
    '''
    if value == 'Λ':
        return True
    if value == '→':
        return True
    if value == '⇔':
        return True
    if value == '∨' :
        return True
    if value == '￢':
        return True
    return False

def split_logical_connective(propotition):
    '''
    splitting with connective sign.
    Parameters
    ----------
    propotition : string
        splitting target. 
        ex.)
         'AΛB'
    Returns
    ------
    [<left side>,<splitting sign>,<right side>]
    ex.) case of parameters 'AΛBΛC'
    [A,Λ,BΛC]
    '''
    signIndex = 0
    sign = ''
    for i in propotition:
        if is_logical_connective_sign(i):
            sign = i
            break
        signIndex += 1

    if signIndex == len(propotition):
        # nothing sign index.
        return [propotition,'','']

    returnValue = []
    returnValue.append(propotition[:signIndex])
    returnValue.append(sign)
    returnValue.append(propotition[signIndex+1:len(propotition)])
    return returnValue
    
def split_proposition(propositions):
    '''
    splitting with ','.
    Parameters
    ----------
    propositions : string
        splitting target propositions.
        ex.)
            '{'AΛB','AΛC'}'
    Returns
    --------
    splitted value. 
    ex.) case of parameters '{'AΛB','AΛC'}'
        ['AΛB','AΛC']
    '''
    if propositions == '':
        return ['']
    
    returnValue =[]
    ignoreCharacters = '[{,}]'
    splitSign = ','
    temp = ''
    for i in propositions:
        if i in ignoreCharacters:
            # remove outside parenthesises.
            continue
        if i in splitSign:
            returnValue.append(temp)
            temp = ''
            continue
        temp = temp + i
    # Append remaining value.
    if temp != '':
        returnValue.append(temp)
    return returnValue