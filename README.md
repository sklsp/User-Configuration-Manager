# User Configuration Manager

[![CI](https://github.com/sklsp/User-Configuration-Manager/actions/workflows/ci.yml/badge.svg)](https://github.com/sklsp/User-Configuration-Manager/actions/workflows/ci.yml)

A small Python project that manages user configuration settings (theme, notifications, volume and so on) through four plain functions operating on a dictionary. It demonstrates functions, dictionaries, input validation, CRUD operations, error handling and data management.

Part of the FreeCodeCamp Scientific Computing with Python certification.

## What is in here

`config_manager.py` defines:

- `add_setting(settings, setting)` - adds a key/value pair, rejects duplicates
- `update_setting(settings, setting)` - changes an existing value, reports missing keys
- `delete_setting(settings, setting)` - removes a key, reports missing keys
- `view_settings(settings)` - formats the current settings for display

Keys and values are normalized to lowercase on write; `view_settings` capitalizes keys for display. A sample dictionary `test_settings` is included at the bottom of the module.

## Example

```python
import copy
from config_manager import add_setting, update_setting, delete_setting, view_settings, test_settings

settings = copy.deepcopy(test_settings)
print(add_setting(settings, ('language', 'English')))   # Setting 'language' added ...
print(update_setting(settings, ('theme', 'light')))     # Setting 'theme' updated to 'light' ...
print(delete_setting(settings, 'volume'))               # Setting 'volume' deleted successfully!
print(view_settings(settings))                          # Current User Settings: / Theme: light / ...
```

All four functions were verified against a copy of `test_settings`, including the duplicate-add and missing-key error paths.

## Tests

```bash
pip install pytest
python -m pytest -q
```

`tests/test_config_manager.py` covers every branch of the four functions (6 tests), and CI runs them on every push.
