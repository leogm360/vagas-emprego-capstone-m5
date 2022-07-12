import os

import environ
from rest_framework.views import (
    exception_handler as rest_framework_exception_handler,
)


def exception_handler(exc, context):
    response = rest_framework_exception_handler(exc, context)

    if response is not None:
        response.data["status"] = "error"
        response.data["status_code"] = response.status_code

    return response


class EnvironManager:
    """
    Detects, load and manage environment variables.
    """

    env = None

    def __init__(self, base_dir: str, env_file_path: str) -> None:
        self.base_dir = base_dir
        self.env_file_path = env_file_path

        self._setup()

    def _setup(self) -> None:
        has_set_env = os.getenv("PROJECT_ENV", False)

        if has_set_env:
            self.env = os.environ.get
        else:
            self._load_env_file()

            self.env = environ.Env(DEBUG=(bool, False))

    def _load_env_file(self):
        return environ.Env.read_env(
            os.path.join(self.base_dir, self.env_file_path)
        )

    def get_var(self, name: str, do_format=None):
        """
        Loads a environment variable by it's name. Use do_format to convert it's
        value in any python equivalent.
        """
        env_var = self.env(name)

        if do_format:

            if do_format == list:
                env_var = env_var.split(" ")
            else:
                env_var = do_format(env_var)

        return env_var
