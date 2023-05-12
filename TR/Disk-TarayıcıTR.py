###@alierenkose


import ctypes


soru = input("Disk Adı: (C / D / E vb.): ")

def get_free_space_gb(folder):

    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
    return free_bytes.value / 1024 / 1024 / 1024

def get_total_space_gb(folder):

    total_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, ctypes.pointer(total_bytes), None)
    return total_bytes.value / 1024 / 1024 / 1024

disk = f'{soru}:\\'
total_size = get_total_space_gb(disk)
free_size = get_free_space_gb(disk)
used_size = total_size - free_size
if used_size == 0:
    print("Disk Bulunamadı!")
else:
    usage_percent = used_size / total_size * 100
    print(f"Disk Boyutu: {total_size:.2f} GB")
    print(f"Boş Alan: {free_size:.2f} GB")
    print(f"Dolu Alan: {used_size:.2f} GB")
    print(f"Doluluk Oranı: %{usage_percent:.2f}")
    
    
    @alierenkose
