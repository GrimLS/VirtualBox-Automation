import Functions as f
import subprocess


# fetch vm info from function and print in readable format
vm_dict = f.list_vms()
print("List of vms currently installed on system:")
for vm_id, vm_info in vm_dict.items():
    print("\nVM ID:", vm_id)
    for key in vm_info:
        print(key + ':', vm_info[key])
print("\n")

# collecting user inputs or assigning default values:
default = True
# name of base vm
if default:
    base_vm_name = "xMint Base"
else:
    base_vm_name = input("Input name of the base vm that you would like to clone from: ")
# folder containing virtualbox vms
if default:
    basefolder = "C:\VirtualBox"
else:
    basefolder = input("Input the file path of the folder where you would like to store the cloned vm: ")
# path of folder share to be added to cloned vm
if default:
    share_path = "C:/Users/paulh/OneDrive - Network Solutions/Active Project Notes"
else:
    share_path = input("Input the path of the folder you would like to share with the cloned vm")
# name of folder share to be added to cloned vm
if default:
    share_name = "Active_Project_Notes(Test)"
else:
    share_name = input("Input the desired name of shared folder")

# find location and info about "xMint Base" vm
for key, dict in vm_dict.items():
    if base_vm_name == dict["Name"]:
        xMint_ID = key

# determine clone name (edit trailing string to change suffix but do not use a space as separator)
c_name = base_vm_name + " Clone"

# take snapshot to create linked clone from
print("Taking snapshot of base vm:")
snapshot_uuid = f.create_snapshot(base_vm_name, "Python Snapshot")
print("\n")

# fetch snapshot uuid from function (This is redundent if creating a new snapshot to clone from)
snapshot_uuid = f.list_snapshots(base_vm_name, "Python Snapshot")
snapshot_uuid = snapshot_uuid["UUID"]

# run cmd to clone vm
print("Cloning vm:")
subprocess.call(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "clonevm", "xMint Base", "--register", "--snapshot", snapshot_uuid, "--name", c_name, "--basefolder", basefolder, "--options", "link"])
print("\n")

# run cmd to add shared folder to new cloned vm
subprocess.call(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "sharedfolder", "add", c_name, "--name", share_name, "--hostpath", share_path, "--automount"])
print("Shared folder has been successfully added to", c_name)
