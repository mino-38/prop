import subprocess
import tempfile
import os

def test_recursive():
    with tempfile.TemporaryDirectory() as temp:
        subprocess.run(['prop', '-aDo', temp, '-r', '-I', '10', '-np', '-M', '3', '-f', '%(num)d.%(ext)s', 'https://github.com/mino-38/'])
        assert len(os.listdir(temp))