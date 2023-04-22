"""Test cases for the analysis_utils module."""

from models import analysis_utils


def test_get_log_messages() -> None:
    """It returns log messages."""
    log = {
        "messageType": "DATA_MESSAGE",
        "subscriptionFilters": ["server"],
        "logEvents": [
            {
                "message": """{
                "asctime": "2023-03-01 01:11:19,394",
                "name": "server.main",
                "levelname": "INFO",
                "message": "search",
                "prompt": "prompt",
                "response": {
                    "q": "question",
                    "session": 3287431778,
                    "answer": "answer.",
                    "results": [{
                        "id": 20635,
                        "title": "title",
                        "author": "author",
                        "year": "2016",
                        "month": "04",
                        "url": "url",
                        "text": "text."
                    }, {
                        "id": 88026,
                        "title": "title2",
                        "author": "author2",
                        "year": "2014",
                        "month": "10",
                        "url": "url2",
                        "text": "text2"
                    }]
                }
            }""",
            },
            {
                "message": """{
                "asctime": "2023-03-01 01:11:19,394",
                "name": "server.main",
                "levelname": "INFO",
                "message": "search",
                "prompt": "prompt2",
                "response": {
                    "q": "question2",
                    "session": 3287431778,
                    "answer": "answer2.",
                    "results": [{
                        "id": 20635,
                        "title": "title3",
                        "author": "author3",
                        "year": "2016",
                        "month": "04",
                        "url": "url3",
                        "text": "text3."
                    }, {
                        "id": 88026,
                        "title": "title4",
                        "author": "author4",
                        "year": "2014",
                        "month": "10",
                        "url": "url4",
                        "text": "text4"
                    }]
                }
            }""",
            },
        ],
    }

    log_messages = analysis_utils.get_log_messages([log], "search")
    assert len(log_messages) == 2
    assert log_messages[0]["prompt"] == "prompt"
    assert log_messages[0]["response"]["q"] == "question"
    assert log_messages[1]["prompt"] == "prompt2"
