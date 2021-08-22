def validate_json_file(f_name):
    assert isinstance(f_name, str)
    assert f_name.endswith('.json')
