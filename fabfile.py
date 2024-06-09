import sys
raise RuntimeError(str(sys.path))

import os
from pathlib import Path

from fabric import task

os.chdir(Path(__file__).parent.absolute())


@task
def generate_requirements(c):
    c.run("pip-compile -q vdirsyncer/requirements.in", pty=True)
