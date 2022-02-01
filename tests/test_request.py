import os
import subprocess


def test_request():
    p = subprocess.run(['prop', 'https://www.example.com'])
    assert p.returncode == 0