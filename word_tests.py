import os

import pytest
from main import count_words, count_sentences, write_result_to_file


@pytest.mark.parametrize("text,expected", [
    ("Hello world!", 2),
    ("This is a test.", 4),
    ("Testing... one, two, three.", 4),
])
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize("text,expected", [
    ("Hello world!", 1),
    ("This is a test.", 1),
    ("Testing... one, two, three.", 2),
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


@pytest.fixture
def test_output_file(tmpdir):
    return tmpdir.join("output.txt")


def test_write_result_to_file(test_output_file):
    words = 10
    sentences = 5
    write_result_to_file(test_output_file, words, sentences)

    assert os.path.isfile(test_output_file)

    with open(test_output_file, 'r') as file:
        content = file.readlines()
        assert content[0].strip() == 'Words: 10'
        assert content[1].strip() == 'Sentences: 5'
