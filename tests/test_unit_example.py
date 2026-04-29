from app import normalize_item


def test_normalize_item_basic():
    """Test basic normalization of an item."""
    assert normalize_item("hello world") == "Hello World"

def test_normalize_item_with_extra_spaces():
    """Test normalization with leading and trailing spaces."""
    assert normalize_item("  hello  ") == "Hello"

def test_normalize_item_empty_string():
    """Test normalization of an empty string."""
    assert normalize_item("") == ""

def test_normalize_item_none():
    """Test normalization of None."""
    assert normalize_item(None) == ""

def test_normalize_item_already_normalized():
    """Test normalization of an already normalized string."""
    assert normalize_item("Hello World") == "Hello World"