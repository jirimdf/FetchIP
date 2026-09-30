import pytest

import main


class FakeResponse:
    def __init__(self, data):
        self.data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self.data


@pytest.fixture
def fake_api(monkeypatch):
    responses = {}
    monkeypatch.setattr(main.requests, "get", lambda url, timeout: FakeResponse(responses[url]))
    return responses


@pytest.mark.parametrize("ip", ["8.8.8.8", "2001:4860:4860::8888"])
def test_valid_ip(ip):
    assert main.is_valid_ip(ip)


@pytest.mark.parametrize("ip", ["999.1.1.1", "abc", "", "1.2.3"])
def test_invalid_ip(ip):
    assert not main.is_valid_ip(ip)


def test_public_ip(fake_api):
    fake_api["https://ipinfo.io/json"] = {"ip": "1.2.3.4"}
    assert main.get_public_ip() == "1.2.3.4"


def test_public_ip_missing(fake_api):
    fake_api["https://ipinfo.io/json"] = {}
    with pytest.raises(ValueError):
        main.get_public_ip()


def test_data_info(fake_api, capsys):
    fake_api["https://ipinfo.io/8.8.8.8/json"] = {"city": "Mountain View", "country": "US"}
    main.get_data_info("8.8.8.8")
    out = capsys.readouterr().out
    assert "City: Mountain View" in out
    assert "Postal code: Unknown" in out


def test_private_address(fake_api, capsys):
    fake_api["https://ipinfo.io/10.0.0.1/json"] = {"ip": "10.0.0.1", "bogon": True}
    main.get_data_info("10.0.0.1")
    assert "private or reserved" in capsys.readouterr().out


def test_manual_input_asks_again(monkeypatch, capsys):
    answers = iter(["999.1.1.1", "8.8.8.8"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert main.ask_ip_address() == "8.8.8.8"
    assert "Invalid IP address" in capsys.readouterr().out
