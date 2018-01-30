import platform


if platform.system() != "Windows":
   raise Exception("Only Windows support!")
  

import winreg, os
from copy import deepcopy


def env_dict(arch):
    ret = {}
    hk = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Microsoft SDKs\\Windows\\v7.1A")
    try:
        p = winreg.QueryValueEx(hk, "InstallationFolder")[0]
        ret["INCLUDE"] = os.path.join(p, "Include")
        ret["PATH"] = os.path.join(p, "Bin", "x64") if arch == "x86_64" else os.path.join(p, "Bin")
        ret["LIB"] = os.path.join(p, "Lib", "x64") if arch == "x86_64" else os.path.join(p, "Lib")
        ret["CL"] = "/D_USING_V110_SDK71_"
        ret["LINK"] = "/SUBSYSTEM:CONSOLE,5.02" if arch == "x86_64" else "/SUBSYSTEM:CONSOLE,5.01"
    except WindowsError:
        pass
    return ret

def dict_append(arch, env={}, sdk=None):
    if sdk is None:
        sdk = env_dict(arch)
    ret = deepcopy(env)
    if not sdk.get("INCLUDE") is None:
        if not ret.get("INCLUDE") is None:
            ret["INCLUDE"] = sdk["INCLUDE"] + ";" + ret["INCLUDE"]
        else:
            ret["INCLUDE"] = sdk["INCLUDE"]
    if not sdk.get("PATH") is None:
        if not ret.get("PATH") is None:
            ret["PATH"] = sdk["PATH"] + ";" + ret["PATH"]
        else:
            ret["PATH"] = sdk["PATH"]
    if not sdk.get("LIB") is None:
        if not ret.get("LIB") is None:
            ret["LIB"] = sdk["LIB"] + ";" + ret["LIB"]
        else:
            ret["LIB"] = sdk["LIB"]
    if not sdk.get("CL") is None:
        if not ret.get("CL") is None:
            ret["CL"] = sdk["CL"] + " " + ret["CL"]
        else:
            ret["CL"] = sdk["CL"]
    if not sdk.get("LINK") is None:
        if not ret.get("LINK") is None:
            ret["LINK"] = sdk["LINK"] + " " + ret["LINK"]
        else:
            ret["LINK"] = sdk["LINK"]
    return ret
