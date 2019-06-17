import Functions as f
import subprocess


# Fetch vm info from function and print in readable format
vm_dict = f.list_vms()
print("List of current vms installed on system:")
for vm_id, vm_info in vm_dict.items():
    print("\nVM ID:", vm_id)
    for key in vm_info:
        print(key + ':', vm_info[key])
print("\n")

# assigning variables:
# folder containing virtualbox vms
basefolder = "C:\VirtualBox"
# name of folder share to be added to cloned vm
share_name = "Active_Project_Notes(Test)"
# path of folder share to be added to cloned vm
share_path = "C:/Users/paulh/OneDrive - Network Solutions/Active Project Notes"

# Find location and info about "xMint Base" vm
for key, dict in vm_dict.items():
    if "xMint Base" == dict["Name"]:
        xMint_ID = key
        xMint_UUID = dict["UUID"]

# determine clone name (edit trailing string to change suffix but do not use a space as separator)
c_name = (vm_dict[xMint_ID]["Name"]) + "_clone"

# take snapshot to create linked clone from
print("Taking snapshot of base vm:")
snapshot_uuid = f.create_snapshot("xMint Base", "Python Snapshot")
print("\n")

# Fetch snapshot uuid from function (This is redundent if creating new snapshot to clone from)
snapshot_uuid = f.list_snapshots("xMint Base", "Python Snapshot")
snapshot_uuid = snapshot_uuid["UUID"]

# Run cmd to clone vm
print("Cloning vm:")
subprocess.call(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "clonevm", "xMint Base", "--register", "--snapshot", snapshot_uuid, "--name", c_name, "--basefolder", basefolder, "--options", "link"])
print("\n")

# Run cmd to add shared folder to new cloned vm
subprocess.call(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "sharedfolder", "add", c_name, "--name", share_name, "--hostpath", share_path, "--automount"])
print("Shared folder has been successfully added to", c_name)
