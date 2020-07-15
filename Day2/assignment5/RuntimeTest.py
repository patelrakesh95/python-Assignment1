#open Text editor and print environments variables.

import subprocess
from time import sleep

class RuntimeTest:
    def execu(self):
        print("Open Text editor using subprocess.call")
        sleep(15)
        subprocess.call("gedit")
        print("Open Text editor using subprocess.run")
        sleep(15)
        subprocess.run("gedit")
        print("Print System environment variable value")
        sleep(15)
        env = subprocess.os.environ
        print(f"Environment variable PATH : {env['PATH']}")
 