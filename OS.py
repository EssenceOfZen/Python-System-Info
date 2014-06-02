# This is a simple program that allows the logging of system data, as well as
# manipulating data on said computer.

import os
import platform
import ctypes
import winreg

def get_os_system(): #Gets the Operating System of user
    full_system = platform.uname()
    return full_system

def get_current_directory(): #Gets the files in the directory
    return os.getcwd()

def change_directory(directory):
    current_directory = os.chdir(directory)
    return current_directory

def list_objects(directory): #uses listdir() to print the objects in directory
    objects = os.listdir(directory)
    return objects

def get_memory_data(): #Utilizes the C functions to get system data, specifically that of memory
    kernel32 = ctypes.windll.kernel32
    c_ulong = ctypes.c_ulong
    class MEMORYSTATUS(ctypes.Structure):
        _fields_=[
            ('dwLength', c_ulong),
            ('dwMemoryLoad', c_ulong),
            ('dwTotalPhys', c_ulong),
            ('dwAvailPhys', c_ulong),
            ('dwTotalPageFile', c_ulong),
            ('dwAvailPageFile', c_ulong),
            ('dwTotalVirtual', c_ulong),
            ('dwAvailVirtual', c_ulong)
        ]

    memory_status = MEMORYSTATUS()
    memory_status.dwLength = ctypes.sizeof(MEMORYSTATUS)
    kernel32.GlobalMemoryStatus(ctypes.byref(memory_status))

    return memory_status.dwTotalPhys, memory_status.dwAvailPhys

def get_hard_drive_free_space(drive):
    user_space = ctypes.c_int64()
    total = ctypes.c_int64()
    free = ctypes.c_int64()
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive,
                                               ctypes.byref(user_space),
                                               ctypes.byref(total),
                                               ctypes.byref(free))
    return user_space.value
    

def create_log():
    pass


version = "1.3.2"
system_os_info = get_os_system()


#Main System Variables--------
system_os = system_os_info[0]
system_os_release = system_os_info[2]
system_user = system_os_info[1]
system_os_version = system_os_info[3]
system_os_cpu = system_os_info[5]

current_directory = os.getcwd() #Prints the current working directory
#print(os.getpid()) #Prints the real process ID of the current process


system_drive = os.getenv("SystemDrive")
#------------------------------

def main():
    print("Current User: [" + system_user + "]")
    print("Current Operating System: " + system_os + "| Relase: " + system_os_release + "| Version: " + system_os_version)
    print("")
    

    switch = 0
    while switch == 0:
        print("--")
        print("Testing Things")
        print()
        current_directory = get_current_directory()
        print("Current Directory: " + str(current_directory))

        directory_objects = list_objects(current_directory)
        print("Directory's Objects: ")
        print(directory_objects)
        print()

        total_physical_memory, available_physical_memory = get_memory_data()
        print("Total Physical Memory: " + str(total_physical_memory))
        print("Available Physical Memory: " + str(available_physical_memory))

        free_disk_space = get_hard_drive_free_space(system_drive)
        print("System Drive Free Space: " + str(free_disk_space))


        x = input("..")
        switch = 1

main()
    


