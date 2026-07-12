import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "research" / "iso_chrome.sh"


def run(*args, env=None):
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True,
                          text=True, env=env)


def test_login_refuses_without_ack():
    r = run("login")
    assert r.returncode != 0
    assert "ISO_CHROME_LOGIN_ACK" in r.stderr


def test_headless_arg_wiring_dry_run():
    r = run("headless", "--dry-run")
    assert r.returncode == 0
    assert "--headless=new" in r.stdout
    assert "open -a" not in r.stdout
    assert "user-data-dir" in r.stdout


def test_unknown_command_fails():
    assert run("dance").returncode != 0
