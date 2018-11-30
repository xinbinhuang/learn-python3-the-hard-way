from nose.tools import assert_equal, assert_raises
from ex48.parser import *


def test_peek():
    word_list = [('noun', 'money'), ('verb', 'cost')]
    assert_equal(peek(word_list), 'noun')

    empty_list = []
    assert_equal(peek(empty_list), None)


def test_match():
    word_list = [('noun', 'money'), ('verb', 'cost')]
    assert_equal(match(word_list, 'noun'), ('noun', 'money'))
    assert_equal(match(word_list, 'wrong_name'), None)
    assert_equal(match(word_list, 'nothing'), None)


def test_skip():
    word_list = [('stop', 'another'), ('stop', 'stop'), ('noun', 'word')]
    skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'word')])


def test_parse_verb():
    word_list = [('stop', 'stop'), ('verb', 'fighting')]
    assert_equal(parse_verb(word_list), ('verb', 'fighting'))

    error = [('error', 'something')]
    assert_raises(ParserError, parse_verb, error)


def test_parse_object():
    word_list = [('stop', 'stop'), ('direction', 'north')]
    assert_equal(parse_object(word_list), ('direction', 'north'))

    word_list = [('stop', 'stop'), ('noun', 'game')]
    assert_equal(parse_object(word_list), ('noun', 'game'))

    error = [('error', 'something')]
    assert_raises(ParserError, parse_object, error)


def test_parse_subject():
    word_list = [('stop', 'stop'), ('verb', 'fighting')]
    assert_equal(parse_subject(word_list), ('noun', 'player'))

    word_list = [('stop', 'stop'), ('noun', 'game')]
    assert_equal(parse_subject(word_list), ('noun', 'game'))

    error = [('error', 'something')]
    assert_raises(ParserError, parse_subject, error)


def test_parse_sentence():
    word_list = [('stop', 'cute'), ('noun', 'Corgi'), ('stop', 'super'), 
                 ('verb', 'likes'), ('noun', 'me')]
    sentence = parse_sentence(word_list)
    assert_equal(sentence.subject, 'Corgi')
    assert_equal(sentence.verb, 'likes')
    assert_equal(sentence.obj, 'me')
