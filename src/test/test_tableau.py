# thirdpirty
import pytest
# user
from tableau import main
from tableau.main import *

def test_is_logical_connective_sign():
    '''
    This test verifies that it is a valid concatenation value.
    '''
    assert main.is_logical_connective_sign('Λ')
    assert main.is_logical_connective_sign('→')
    assert main.is_logical_connective_sign('⇔')
    assert main.is_logical_connective_sign('∨')
    assert main.is_logical_connective_sign('￢')
    assert not main.is_logical_connective_sign('A')
def test_expand_rule_invalid_arugument():
    '''
    This test verifies that raising exception.
    '''
    with pytest.raises(InvalidArgumentExceptionOfExpandRule):
        main.ExpandRuleFactory.get('')
    
    # valid
    actual = main.ExpandRuleFactory.get('Λ')
    assert isinstance(actual, main.ExpandRule)

def test_split_logical_connective():
    '''
    This test verifies that spliting by connective sign.
    '''
    # Nothing of connective sign.
    testData = 'AB'
    expected = ['AB','','']
    actual = main.split_logical_connective(testData) 
    assert actual == expected

    # Single sign case.
    testData = 'AΛB'
    expected = ['A','Λ','B']
    actual = main.split_logical_connective(testData) 
    assert actual == expected

    # Multi sign Case.
    testData = 'AΛBAΛB'
    expected = ['A','Λ','BAΛB']
    actual = main.split_logical_connective(testData) 
    assert actual == expected
def test_split_proposition():
    '''
    This test verifies that spliting by proposition():
    '''
    sign = ','
    # Nothing Of Arguments string.
    testData = ''
    # Converted an Array.
    expected = ['']
    actual = main.split_proposition(testData)
    assert actual == expected
    
    # Case of Single propostion.
    testData = '{A}'
    # remove outside parenthesises from the results.
    expected = ['A']
    actual = main.split_proposition(testData)
    assert actual == expected
    
    # include connective sign.
    testData = 'AΛB'
    # no effective on the results.
    expected = ['AΛB']
    actual = main.split_proposition(testData)
    assert actual == expected
    
    # case multi proposition.
    testData = '{AΛB,AΛC}'
    expected = ['AΛB','AΛC']
    actual = main.split_proposition(testData)
    assert actual == expected

    