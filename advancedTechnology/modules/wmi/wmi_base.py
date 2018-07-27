#coding:utf-8
#这货因为没有研究过，需要找个教程好好看看
"""
WMI 最初于1998年作为一个附加组件与 Windows NT 4.0 Service Pack 4 一起发行，是内置在Windows 2000、 Windows XP和Windows Server 2003 系列操作系统中核心的管理支持技术。基于由 Distributed Management Task Force (DMTF) 所监督的业界标准，WMI是一种规范和基础结构，通过它可以访问、配置、管理和监视几乎所有的Windows资源。大多用户习惯于使用众多的图形化管理工 具来管理Windows资源，在WMI之前这些工具都是通过 Win32应用程序编程接口(Application ProgrammingInterfaces，API)来访问和管理Windows资源的。只要你熟悉系统编程你就知道API有多么重要。但是大多数脚本 语言都不能直接调用Win32 API，WMI的出现使得系统管理员可以通过一种简便的方法即利用常见的脚本语言实现常用的系统管理任务。
利用WMI需要和脚本如WSH和VBScript结合起来，可以实现的功能大家可以看微软的MSDN文档。
在编写我们自己的脚本之前，我们需要对WMI的体系结构有个基本的了解。如图一：(1.gif)
在WMI 体系结构中我们最需要关心的就是WMI提供程序，WMI提供程序在WMI和托管资源之间扮演着中间方的角色。提供程序代表使用者应用程序和脚本从WMI托 管资源请求信息，并发送指令到WMI托管资源。下面是我们利用WMI编程经常要用到的WMI内置提供程序清单，以供编程参考。
1.Active Directory提供程序
链接库文件：dsprov.dll
命名空间：rootdirectoryldap
作用：将Active Directory 对象映射到 WMI。

2.事件日志提供程序
链接库文件：ntevt.dll
命名空间：rootcimv2
作用：管理 Windows 事件日志，例如，读取、备份、清除、复制、删除、监视、重命名、压缩、解压缩和更改事件日志设置。

3.注册表提供程序
链接库文件：stdprov.dll
命名空间：rootdefault
作用：读取、写入、枚举、监视、创建、删除注册表项和值。

4.Win32 提供程序
链接库文件：cimwin32.dll
命名空间：rootcimv2
作用：提供关于计算机、磁盘、外围设备、文件、文件夹、文件系统、网络组件、操作系统、打印机、进程、安全性、服务、共享、SAM 用户及组，以及更多资源的信息。

5.Windows 安装程序提供程序
链接库文件：msiprov.dll
命名空间：rootcimv2
作用：提供对已安装软件信息的访问。

从 上面可以看出在WMI中类（即内置提供程序）被分组到命名空间中，命名空间可以看成是一个组。比如，命名空间 rootcimv2 包括大部分表示通常与计算机和操作系统相关联的资源的类。在使用类的时候要说明类所在的命名空间。类由属性和方法构成。这是可视化编程中的两个重要的概 念。属性描述的是对象的状态，方法是对象可以执行的操作。
(转载)
"""
import wmi
import os
import sys
import platform
import time
def sys_version():
  c = wmi.WMI ()
  #获取操作系统版本
  for sys in c.Win_OperatingSystem():
    print ("Version:%s" % sys.Caption.encode("UTF"),"Vernum:%s" % sys.BuildNumber)
    print (sys.OSArchitecture.encode("UTF"))#系统是位还是位的
    print (sys.NumberOfProcesses) #当前系统运行的进程总数
def cpu_mem():
  c = wmi.WMI ()
  #CPU类型和内存
  for processor in c.Win_Processor():
    #print "Processor ID: %s" % processor.DeviceID
    print ("Process Name: %s" % processor.Name.strip())
  for Memory in c.Win_PhysicalMemory():
    print ("Memory Capacity: %.fMB" %(int(Memory.Capacity)))
def disk():
  c = wmi.WMI ()
  #获取硬盘分区
  for physical_disk in c.Win_DiskDrive ():
    for partition in physical_disk.associators ("Win_DiskDriveToDiskPartition"):
      for logical_disk in partition.associators ("Win_LogicalDiskToPartition"):
        print (physical_disk.Caption.encode("UTF"), partition.Caption.encode("UTF"), logical_disk.Caption)
  #获取硬盘使用百分情况
  #for disk in c.Win_LogicalDisk(DriveType=):
  for disk in c.Win_LogicalDisk (DriveType='NTFS'):
    print (disk.Caption, "%.f%% free" % (1 * disk.FreeSpace / disk.Size))
def network():
  c = wmi.WMI ()
  #获取MAC和IP地址
  for interface in c.Win_NetworkAdapterConfiguration (IPEnabled="True"):
    print ("MAC: %s" % interface.MACAddress)
    for ip_address in interface.IPAddress:
        print ("ip_add: %s" % ip_address)
  #print
def main():
  sys_version()
  cpu_mem()
  #disk()
  #network()
if __name__ == '__main__':
  main()
  print (platform.system())
  print (platform.release())
  print (platform.version())
  print (platform.platform())
  print (platform.machine())


