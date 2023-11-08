import shlex
import sys

string_types = (str,)


def split_command(cmd, posix=None):
    """
     - cmd is string list -> nothing to do
     - cmd is string -> split it using shlex
    :param cmd: string ('ls -l') or list of strings (['ls','-l'])
    :rtype: string list
    """
    if not isinstance(cmd, string_types):
        # cmd is string list
        pass
    else:
        if posix is None:
            posix = "win" not in sys.platform
        cmd = shlex.split(cmd, posix=posix)
    return cmd


def uniencode(s):
    return s


def unidecode(s):
    return s.decode("utf-8", "ignore")
