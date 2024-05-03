import os, sys, subprocess
from security import safe_command

sys.exit(safe_command.run(subprocess.call, [
    os.path.join(os.path.dirname(__file__), "icloud"),
    *sys.argv[1:]
]))
