from src import config


def test_config_values():
    assert isinstance(config.BELIEF_THRESHOLD, float)
