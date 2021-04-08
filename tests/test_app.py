from app import index


def test_index():
    assert index() == 'CI-CD OK'
