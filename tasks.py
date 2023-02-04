from datetime import datetime
from pathlib import Path

from invoke import Context, task

PROJECT_ROOT = Path(__file__).parent.absolute()


@task
def build_docker_image(c, tag="erp"):
    # type: (Context, str) -> None
    now = datetime.utcnow()
    version = f"v{now:%Y%m%d%H%M%S}"
    package_version = PROJECT_ROOT / "_version.py"
    with open(package_version, "w+") as f:
        f.write(f'VERSION_STRING = "{version}"')

    c.run("poetry export -f requirements.txt -o requirements.txt")
    c.run(f"docker build -t {tag} .")
    c.run("rm -f requirements.txt")


@task(build_docker_image)
def run(c, detach=False):
    # type: (Context, bool) -> None
    if detach:
        c.run("docker-compose up -d")
    else:
        c.run("docker-compose up")
