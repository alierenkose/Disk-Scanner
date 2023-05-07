###@alierenkose

import ctypes

question = input("Disk Name: (C / D / E etc.): ")

def get_free_space_gb(folder):

    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
    return free_bytes.value / 1024 / 1024 / 1024

def get_total_space_gb(folder):

    total_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, ctypes.pointer(total_bytes), None)
    return total_bytes.value / 1024 / 1024 / 1024

disk = f'{question}:\\'
total_size = get_total_space_gb(disk)
free_size = get_free_space_gb(disk)
used_size = total_size - free_size
if used_size == 0:
    print("No found disk!")
else:
    usage_percent = used_size / total_size * 100
    print(f"Disk Size: {total_size:.2f} GB")
    print(f"Empty Space: {free_size:.2f} GB")
    print(f"Full Area: {used_size:.2f} GB")
    print(f"Solidity Ratio: {usage_percent:.2f}%")
    
    
###@alierenkose
