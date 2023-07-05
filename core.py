import subprocess


def command(command, replace=False, log=True):
    if log:
        print(f"[COMMAND]: `{command}`")
    result = subprocess.check_output(command, shell=True)
    output = result.decode("utf-8")
    if replace:
        output = output.replace("\r", "")
    return output
