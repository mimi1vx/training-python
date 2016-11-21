with subprocess.Popen(["systemctl", "status", "avahi-daemon"], stdout=subprocess.PIPE, universal_newlines=True) as process:
    for line in process.stdout:
        print(repr(line))
