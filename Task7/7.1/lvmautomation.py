import os
import subprocess as sp

def pvcreate(name):
    os.system(f"pvcreate {name}")         #physical volume creation

def pasto(option,*argument):    
    total=""
    for arg in argument:
        total=total+""+arg
    if option=="2":                 #passing of arguments
        pvcreate(total)
        
def vgcreate(name):
    os.system("pvdisplay")
    PVname=input("Enter name of physical Volume:")                        #volume group creation
    os.system(f"vgcreate {name} {PVname}")
def mountpoint(v,n):
    mount_point=input("Where you want to mount this disk to which folder of your system:")
    os.system(f"mkdir {mount_point}")
    x=sp.getstatusoutput(f"mount /dev/{v}/{n} {mount_point}")
    if x[0]!=0:
        print("Unsuccessful")
        print(x[1])
    else:
        print("Successfully Attached")
	     
def lvcreate(name,size):
    os.system("vgdisplay")
    vgname=input("Enter the Volume group:")
    os.system(f"lvcreate --size {size}G --name {name} {vgname}")     //size in GiB
    print("formating the Disk with ext4.....")
    os.system(f"mkfs.ext4 /dev/{vgname}/{name}")
    mountpoint(vgname,name) 
while 1:
    os.system("tput setaf 15")
    print("\t\t\t\t\t<-------------LVM Automation------------->")
    print("\t\t\tFor giving multiple Disk Name in single go.Leave a space between Names")
    print("1.Show the All the Disk\n\nCreation\n\n2.Create Physical Volume \n3.Create Volume Group\n4.Create Logical Volume\n\nDisplay\n\n5.Display all Physical Volume")
    print("6.Display all Volume Group\n7.Display all Logical Volume\n\nDeletion\n\n8.Remove Physical Volume\n9.Remove Volume Group\n10.Remove Logical Volume")
    print(" \n\nEnter Exit to Exit program\n\n")
    option=input("Enter your option:")
    print(option)
    if "exit" in option.lower():
        exit()
    elif "1"== option:
        os.system("fdisk -l")
    elif "2" in option:
        PVname=input("Enter the Disk name for physical Volume:")
        pasto(option,PVname)
    elif "3" in option:
        VGgroup=input("Enter the Volume group Name:")
        vgcreate(VGgroup)
    elif "4" in option:
    	Lvname=input("Enter the Logical Volume Name:")
    	disk_size=input("enter the size for your Logical Disk:")
    	lvcreate(Lvname,disk_size)
    elif "5" in option:
    	os.system("pvdisplay")
    elif "6" in option:
    	os.system("vgdisplay")
    elif "7" in option:
    	os.system("lvdisplay")
    elif "8" in option:
        name=input("Enter the name of Physical Volume:")
        os.system(f"pvremove {name}")
    elif "9" in option:
        name=input("Enter the name of Volume Group:")
        os.system(f"vgremove {name}")
    elif "10" in option:
        name=input("Enter the name of Logical Volume:")
        name2=input("Enter the Volume group")
        os.system(f"umount /dev/{name2}/{name}")
        os.system(f"lvremove /dev/{name2}/{name}")
    else:
    	print("Wrong Input!! \n Try again ")
    	

            
