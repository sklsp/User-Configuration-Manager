import copy

import pytest

from config_manager import add_setting, delete_setting, test_settings, update_setting, view_settings


@pytest.fixture
def settings():
    return copy.deepcopy(test_settings)


def test_add_lowercases_and_stores(settings):
    assert add_setting(settings, ("Language", "English")) == "Setting 'language' added with value 'english' successfully!"
    assert settings["language"] == "english"


def test_add_refuses_an_existing_key(settings):
    assert add_setting(settings, ("THEME", "light")) == "Setting 'theme' already exists! Cannot add a new setting with this name."
    assert settings["theme"] == "dark"


def test_update_changes_an_existing_key(settings):
    assert update_setting(settings, ("theme", "Light")) == "Setting 'theme' updated to 'light' successfully!"
    assert settings["theme"] == "light"


def test_update_reports_a_missing_key(settings):
    assert update_setting(settings, ("font", "serif")) == "Setting 'font' does not exist! Cannot update a non-existing setting."
    assert "font" not in settings


def test_delete_removes_a_key_and_reports_a_missing_one(settings):
    assert delete_setting(settings, "Volume") == "Setting 'volume' deleted successfully!"
    assert "volume" not in settings
    assert delete_setting(settings, "volume") == "Setting not found!"


def test_view_lists_settings_or_says_there_are_none(settings):
    assert view_settings(settings) == "Current User Settings:\nTheme: dark\nNotifications: enabled\nVolume: high\n"
    assert view_settings({}) == "No settings available."
