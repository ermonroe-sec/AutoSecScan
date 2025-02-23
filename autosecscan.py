#!/usr/bin/env python3
"""
AutoSecScan - Automated Linux Security Audit Tool
Author: ***REDACTED***
Version: 1.0.0
Description: A lightweight script for identifying privilege escalation opportunities and security misconfigurations.
"""

import os
import subprocess

def check_sudo_permissions():
    """ Check for sudo privileges without password """
    print("[+] Checking for sudo permissions without password...")
    sudo_list = subprocess.getoutput("sudo -l")
    if "ALL" in sudo_list and "(ALL) NOPASSWD: ALL" in sudo_list:
        print("[!] User has passwordless sudo access! Potential privilege escalation.")
    else:
        print("[-] No easy sudo privilege escalation found.")

def check_world_writable():
    """ Check for world-writable files in critical directories """
    print("[+] Searching for world-writable files...")
    world_writable = subprocess.getoutput("find / -writable -type f 2>/dev/null | grep -v '/proc/'")
    if world_writable:
        print("[!] World-writable files found:\n", world_writable)
    else:
        print("[-] No world-writable files detected.")

def check_setuid_binaries():
    """ Check for binaries with SUID bit set (potential privilege escalation) """
    print("[+] Checking for SUID binaries...")
    suid_binaries = subprocess.getoutput("find / -perm -4000 -type f 2>/dev/null")
    if suid_binaries:
        print("[!] SUID binaries found:\n", suid_binaries)
    else:
        print("[-] No SUID binaries detected.")

def main():
    print("\n=== AutoSecScan - Linux Security Audit Tool ===\n")
    check_sudo_permissions()
    check_world_writable()
    check_setuid_binaries()
    print("\nScan complete. Stay stealthy, stay secure.\n")

if __name__ == "__main__":
    main()
