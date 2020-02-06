# thirdpirty
import pytest
# user
from taburo import main
def test_is_logical_connective_sign():
    '''
    test logical connection
    '''
    assert main.is_logical_connective_sign('Λ')
    assert main.is_logical_connective_sign('→')
    assert main.is_logical_connective_sign('⇔')
    assert main.is_logical_connective_sign('∨')
    assert main.is_logical_connective_sign('￢')
    assert not main.is_logical_connective_sign('A')
def test_split_logical_connective():
    '''
    test splite.
    '''
    testData = 'AB'
    expected = ['AB','','']
    actual = main.split_logical_connective(testData) 
    assert actual == expected

    testData = 'AΛB'
    expected = ['A','Λ','B']
    actual = main.split_logical_connective(testData) 
    assert actual == expected
    
    testData = 'AΛBAΛB'
    expected = ['A','Λ','BAΛB']
    actual = main.split_logical_connective(testData) 
    assert actual == expected
    

    