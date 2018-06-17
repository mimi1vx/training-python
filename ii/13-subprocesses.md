# Subprocesses

subprocess.run

>>> def check_output(*args, **kwargs):
...     log.debug("Command {}".format(args))
...     kwargs["universal_newlines"] = True
...     return subprocess.check_output(*args, **kwargs)
