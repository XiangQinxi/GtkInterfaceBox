class GJava(object):
    def Command(self, Cmd: str):
        import subprocess
        res = subprocess.call(Cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

    def RunJava(self, JavaFile):
        self.Command(f"javac {JavaFile}.java")
        self.Command(f"java {JavaFile}")

    def GetVersion(self):
        self.Command("java -version")


class GWindows(object):
    def __init__(self):
        import os
        import subprocess

    def Command(self, Cmd: str):
        import subprocess
        res = subprocess.call(Cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

    def WindowsVersion(self):
        self.Command("winver")

    def Sys(self):
        self.Command("sysdm.cpl")

    def Osk(self):
        self.Command("osk")

    def Taskmgr(self):
        self.Command("taskmgr")

    def Regedit(self):
        self.Command("regedit.exe")

    def Cleanmgr(self):
        self.Command("cleanmgr")

    def Shutdown(self, Time: int):
        self.Command(f"Shutdown -s -t {Time}")

    def NotePad(self):
        self.Command("notepad")

    def Explorer(self):
        self.Command("explorer")

    def Sound(self):
        self.Command("mmsys.cpl")

    def Control(self):
        self.Command("control")

    def Shutdown_Close(self):
        self.Command(f"shutdown -a")

    def CompMgmtLauncher(self):
        self.Command("CompMgmtLauncher")

    def Cmd(self):
        self.Command("cmd")

C = GWindows()
C.Sys()