import psutil


class MissingRequiredArg(AssertionError):
    pass

def process_is_running(process_name, required_args=tuple()):
    """ Check if a launched process is running in a cross platform way

    Example
    -------
    assert process_is_running('openssl', required_args=['ds_server'])
    """
    for proc in psutil.process_iter():
        try:
            if process_name in proc.name():
                for arg in required_args:
                    if arg not in proc.cmdline():
                        print(proc.cmdline())
                        raise MissingRequiredArg()
                return True
        except (MissingRequiredArg, psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return False
