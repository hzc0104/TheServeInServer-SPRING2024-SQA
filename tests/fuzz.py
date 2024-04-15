import json
import datetime
import os
from hypothesis import given, strategies as st

# Test int() conversion
@given(st.text())
def test_int_conversion(data):
    try:
        result = int(data)
        assert isinstance(result, int)
    except ValueError:
        pass  # Expected for non-integer strings

# Test float() conversion
@given(st.text())
def test_float_conversion(data):
    try:
        result = float(data)
        assert isinstance(result, float)
    except ValueError:
        pass  # Expected for non-float strings

# Test json.loads()
@given(st.text())
def test_json_loads(data):
    try:
        result = json.loads(data)
        assert isinstance(result, (dict, list))  # JSON should be an object or array
    except json.JSONDecodeError:
        pass  # Expected for invalid JSON strings

# Test datetime.strptime()
@given(st.text(), st.text())
def test_datetime_strptime(date_string, format_string):
    try:
        result = datetime.datetime.strptime(date_string, format_string)
        assert isinstance(result, datetime.datetime)
    except ValueError:
        pass  # Expected when format does not match

# Test os.path.join()
@given(st.lists(st.text(), min_size=1))
def test_os_path_join(parts):
    try:
        path = os.path.join(*parts)
        assert isinstance(path, str)
    except Exception as e:
        assert False, f"Unhandled exception: {e}"

if __name__ == "__main__":
    test_int_conversion()
    test_float_conversion()
    test_json_loads()
    test_datetime_strptime()
    test_os_path_join()

