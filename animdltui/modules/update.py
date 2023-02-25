import sys
import subprocess

"""User Access Control for Microsoft Windows Vista and higher.  This is
only for the Windows platform.

This will relaunch either the current script - with all the same command
line parameters - or else you can provide a different script/program to
run.  If the current user doesn't normally have admin rights, he'll be
prompted for an admin password. Otherwise he just gets the UAC prompt.

Note that the prompt may simply shows a generic python.exe with "Publisher:
Unknown" if the python.exe is not signed.

This is meant to be used something like this::

    if not pyuac.isUserAdmin():
        return pyuac.runAsAdmin()

    # otherwise carry on doing whatever...

See L{runAsAdmin} for the main interface.

"""

import sys, os, traceback, types

def isUserAdmin():
    """@return: True if the current user is an 'Admin' whatever that
    means (root on Unix), otherwise False.

    Warning: The inner function fails unless you have Windows XP SP2 or
    higher. The failure causes a traceback to be printed and this
    function to return False.
    """
    
    if sys.platfrom == 'win32':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False

def runAsAdmin(cmdLine=None, wait=True):
    """Attempt to relaunch the current script as an admin using the same
    command line parameters.  Pass cmdLine in to override and set a new
    command.  It must be a list of [command, arg1, arg2...] format.

    Set wait to False to avoid waiting for the sub-process to finish. You
    will not be able to fetch the exit code of the process if wait is
    False.

    Returns the sub-process return code, unless wait is False in which
    case it returns None.

    @WARNING: this function only works on Windows.
    """

    if sys.platform != 'win32':
        raise RuntimeError("This function is only implemented on Windows.")

    import win32con
    import win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon
    
    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        raise ValueError("cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'  # causes UAC elevation prompt.
    
    # print "Running", cmd, params

    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
    # of the process, so we can't get anything useful from it. Therefore
    # the more complex ShellExecuteEx() must be used.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']    
        rc = win32process.GetExitCodeProcess(procHandle)
    else:
        rc = None

    return rc




def update():
    if sys.platform in ("linux", "linux2"):
        subprocess.check_output(["animdl update"], shell=True)
        
    else:
        if isUserAdmin():
            subprocess.check_output(["animdl update"], shell=True)

        else:
            runAsAdmin()