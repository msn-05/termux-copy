# Termux Copy

Simple program to copy a file's content to clipboard. Coded in python. See the source code <a href="src">here</a>. Compiled to binary with <a href="https://www.pyinstaller.org">Pyinstaller</a>
You need to have Termux:Api app installed.<br><br>
Install it from <a href="https://f-droid.org/en/packages/com.termux.api">F-Droid</a> or <a href="https://play.google.com/store/apps/details?id=com.termux.api">Play store</a>
<br><br>Usage:
```bash
copy <file>
```
This will copy the content from <file> to the clipboard
<br><br>Steps to install the program are given below:

<i>All in one command if you don't want to copy paste them one by one:</i>
```bash
pkg update && pkg upgrade -y && pkg install git -y && git clone https://github.com/msn-05/termux-copy.git && cd termux-copy && chmod +x install && ./install
```
<br><br>
1)Update termux:
```bash
pkg update && pkg upgrade -y
```
2)Install git
```bash
pkg install git -y
```
3)Clone this repo
```bash
git clone https://github.com/msn-05/termux-copy.git
```
4)Change dir to the repo and give executable permissions to install
```bash
cd termux-copy && chmod +x install
```
5)Run the script
```bash
./install
```
