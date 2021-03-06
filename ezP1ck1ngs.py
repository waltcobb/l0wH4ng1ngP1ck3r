#!/usr/bin/python2.7
from multiprocessing import Process
import subprocess
import argparse
import sys
import os

#cli options
parser = argparse.ArgumentParser()
parser.add_argument('ip', nargs='+', help='targets')
arg = parser.parse_args()


#checks if dir exists, if not, creates it
def makeDir(name):
	if not os.path.exists(name):
		os.makedirs(name)

#makes dirs for targets and subdir 'scans' for each
def prepScans():
	for targets in arg.ip:
		makeDir(targets)
		makeDir(targets + '/scans')

#runs nmap on targets, writes output to $target/scans/nmap.txt
#also writes list of open ports and services to $target for further
#use by other tools
def nmap():
	for targets in arg.ip:
		print '[*] Scanning ' + targets
		subprocess.call(['./.ezP1ck1ngsNmap.sh', targets])

def searchsploit():
	for targets in arg.ip:
		print '[*] Searching for possible sploits ' + targets
		subprocess.call(['./.ezP1ck1ngsSearchSploit.sh', targets])

def searchVulns():
	for targets in arg.ip:
		print '[*] Searching for ez vulns ' + targets
		subprocess.call(['./.ezP1ck1ngsScanProtocols.sh', targets])


prepScans()
nmap()
raw_input("press enter to continue")
searchsploit()
searchVulns()
