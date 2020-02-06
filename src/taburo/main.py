def is_logical_connective_sign(value):
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

def split_logical_connective(value):
    signIndex = 0
    sign = ''
    for i in value:
        if is_logical_connective_sign(i):
            sign = i
            break
        signIndex += 1

    if signIndex == len(value):
        # nothing sign index.
        return [value,'','']

    returnValue = []
    returnValue.append(value[:signIndex])
    returnValue.append(sign)
    returnValue.append(value[signIndex+1:len(value)])
    return returnValue
    