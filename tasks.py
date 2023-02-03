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


@task(aliases=["fmt"])
def format(c, all_files=False):
    # type: (Context, bool) -> None
    precommit_options = []

    if all_files:
        precommit_options.append("--all-files")

    hooks = [
        "pyupgrade",
        "add-trailing-comma",
        "yesqa",
        "isort",
        "black",
    ]
    for hook in hooks:
        cmd = " ".join(["pre-commit", "run", *precommit_options, hook])
        c.run(cmd, pty=True)


@task
def lint(c, all_files=False):
    # type: (Context, bool) -> None
    precommit_options = []

    if all_files:
        precommit_options.append("--all-files")

    hooks = [
        "flake8",
        "mypy",
        "vulture",
        "bandit",
    ]
    for hook in hooks:
        cmd = " ".join(["pre-commit", "run", *precommit_options, hook])
        c.run(cmd, pty=True)


@task
def check(c, all_files=False):
    # type: (Context, bool) -> None
    precommit_options = []

    if all_files:
        precommit_options.append("--all-files")

    cmd = " ".join(["pre-commit", "run", *precommit_options])
    c.run(cmd, pty=True)


@task
def tests(c, quiet=False):
    # type: (Context, bool) -> None
    pytest_options: list[str] = []

    if quiet:
        pytest_options.append("-q")

    cmd = " ".join(
        [
            "PYTHONPATH=src/",
            "coverage",
            "run",
            "-m",
            "pytest",
            *pytest_options,
        ],
    )
    c.run(cmd, pty=True)
