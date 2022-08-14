from pathlib import Path
import json
import pytest


@pytest.fixture()
def fixture_path():
    return f"{Path(__file__).parent}/fixtures"


@pytest.fixture()
def sample_users_file(fixture_path):
    return f"{fixture_path}/sample/users.json"


@pytest.fixture()
def sample_users_list(sample_users_file):
    return json.loads(open(sample_users_file).read())


@pytest.fixture()
def _mock_azure_login_envvars(monkeypatch):
    monkeypatch.setenv("TENANT_ID", "0123456789")
    monkeypatch.setenv("CLIENT_ID", "client_id")
    monkeypatch.setenv("CLIENT_SECRET", "client_secret")
