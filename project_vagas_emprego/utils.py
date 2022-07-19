import os
from typing import Any

import environ


class EnvironManager:
    """
    Detects, loads and manage environment variables.
    """

    env = None

    def __init__(self, base_dir: str, env_file_path: str) -> None:
        self.base_dir = base_dir
        self.env_file_path = env_file_path

        self.setup()

    def setup(self) -> None:
        has_set_env = os.getenv("PROJECT_ENV", False)

        if has_set_env:
            self.env = os.environ.get
        else:
            self.load_env_file()

            self.env = environ.Env()

    def load_env_file(self):
        return environ.Env.read_env(
            os.path.join(self.base_dir, self.env_file_path)
        )

    def _treat_string(self, string: str) -> str:
        return string.lower().strip()

    def _convert_to_int(self, env_var: str) -> int:
        treated_var = self._treat_string(env_var)

        return int(treated_var)

    def _convert_to_float(self, env_var: str) -> float:
        treated_var = self._treat_string(env_var)

        return float(treated_var)

    def _convert_to_bool(self, env_var: str) -> bool:
        treated_var = self._treat_string(env_var)

        if not treated_var.isdigit():
            raise ValueError(f"Variable should be a digit.")

        if env_var == "1":
            return True
        elif env_var == "0":
            return False
        else:
            raise ValueError(
                f"Bool type conversion supports only '1' or '0', input '{env_var}'."
            )

    def _convert_to_list(self, env_var: str) -> list:
        treated_var = self._treat_string(env_var)

        return treated_var.split(" ")

    def _convert_to_tuple(self, env_var: str) -> tuple:
        treated_var = self._treat_string(env_var)

        return tuple(treated_var.split(" "))

    def _convert_to_dict(self, env_var: str) -> dict:
        treated_var = self._treat_string(env_var)

        splited_pairs = treated_var.split(";")

        resulting_dict = {}

        for pairs in splited_pairs:
            pair = pairs.split(":")

            key = pair[0]
            value = pair[1]

            resulting_dict.update({key: value})

        return resulting_dict

    def get_var(self, name: str, convert: str = None) -> Any:
        """
        Loads a environment variable by it's name. Environment variables are
        usually stored and read in string format, it's possible to use 'convert'
        param to convert it to a equivalent python data type. The supported
        types are as described below:

        * int - '42' => 42.

        * float - '101.57' => 101.57.

        * bool - '1' | '0' => True | False.

        * list - 'my env var' => ['my', 'env', 'var'].

        * tuple - 'my env var' => ('my', 'env', 'var').

        * dict - 'name:environ;type:manager' => {'name': 'environ', 'type': 'manager'}.

        WARNING 1: nested conversion is not supported!

        WARNING 2: beaware of rouding probems with floats!
        """
        env_var = self.env(name)

        if convert:
            converter = getattr(self, f"_convert_to_{convert}", False)

            if not converter:
                raise TypeError(f"Convert type {convert} not supported.")

            env_var = converter(env_var)

        return env_var
