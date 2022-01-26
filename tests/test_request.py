import subprocess
import os

def test_request():
    with open(os.devnull, 'w') as null:
        r = subprocess.run(['prop', 'https://www.example.com'], stdout=null, stderr=null)
    assert r.returncode == 0