#!/usr/bin/env python

import shutil
from os import environ as env
from pathlib import Path
from subprocess import run


def main() -> int:
    env["INVOKE_RUN_PTY"] = "1"
    env["DOCKER_BUILDKIT"] = "1"

    envfile = Path(".env")
    if not envfile.exists():
        shutil.copy(f"{envfile}.example", envfile)
        print("A basic .env was created! Check it out! I wait for you :)")
        while input("Did you update the .env? (y/N) ").lower() != "y":
            print("You need to update the .env for the project to work!")
        print("Nice!")

    run(["rm", "-rf", ".venv"])
    run(["poetry", "env", "remove", "-q", "python"])
    run(["poetry", "install"])

    run(["poetry", "run", "inv", "run"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())