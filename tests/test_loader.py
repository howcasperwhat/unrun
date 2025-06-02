import pytest, yaml
from utils.loader import norm_config, load_config, join_constructor
from unittest.mock import patch, mock_open, Mock


test_norm_config_data = [
    (1, "1"),
    (1.23, "1.23"),
    (None, "None"),
    ("already_string", "already_string"),
    (True, "True"),

    ([1, 2.0, None, "text"], ["1", "2.0", "None", "text"]),
    ([], []),

    ({"a": 1, "b": 2.5, "c": None}, {"a": "1", "b": "2.5", "c": "None"}),
    ({}, {}),

    (
        {"key1": [1, {"nested_key": 2.5}], "key2": None},
        {"key1": ["1", {"nested_key": "2.5"}], "key2": "None"}
    ),
    (
        [1, {"inner_list": [None, 3.14]}, "end"],
        ["1", {"inner_list": ["None", "3.14"]}, "end"]
    ),
    (
        {
            "int": 1, "float": 1.23, "None": None, "list": [1, 2, 3],
            "dict": {
                "int": 1, "float": 1.23, "None": None, "nested_list": [1, 2, 3],
                "nested_dict": {"int": 1, "float": 1.23, "None": None}
            }
        },
        {
            "int": "1", "float": "1.23", "None": "None", "list": ["1", "2", "3"],
            "dict": {
                "int": "1", "float": "1.23", "None": "None", "nested_list": ["1", "2", "3"],
                "nested_dict": {"int": "1", "float": "1.23", "None": "None"}
            }
        }
    )
]


@pytest.mark.parametrize("input_data, expected_output", test_norm_config_data)
def test_norm_config_parameterized(input_data, expected_output):
    assert norm_config(input_data) == expected_output


def test_load_config_found():
    with patch('yaml.safe_load') as mock_yaml_load, \
         patch('builtins.open', new_callable=mock_open) as mock_file:

        mock_yaml_load.return_value = {'key': 'value'}
        result = load_config('dummy_file.yaml')

        mock_file.assert_called_once_with('dummy_file.yaml', 'r')
        assert result == {'key': 'value'}


def test_load_config_empty():
    with patch('utils.loader.add_constructors', return_value=None), \
         patch('builtins.open', mock_open(read_data='')):

        result = load_config('empty_file.yaml')
        assert result == {}


def test_load_config_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = load_config('non_existent_file.yaml')
        assert result is None


def test_load_config_yaml_error():
    with patch('builtins.open', side_effect=yaml.YAMLError):
        result = load_config('invalid_yaml.yaml')
        assert result is None


def test_join_constructor():
    mock_loader = Mock(spec=yaml.Loader)
    input_sequence = ["item1", "item2", "item3"]
    mock_loader.construct_sequence.return_value = input_sequence

    mock_node = Mock(spec=yaml.nodes.SequenceNode)

    separators = ["&&", "||", ";"]
    for separator in separators:
        result = join_constructor(mock_loader, mock_node, separator)
        assert result == separator.join(input_sequence)
        mock_loader.construct_sequence.assert_called_once_with(mock_node)
        mock_loader.construct_sequence.reset_mock()
