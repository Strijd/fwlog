fwlog
=====
A simple perl script that will make  monitoring pflog0 a bit easier.

Its  based on a script I saw ~7 years ago by "raptor".

Install:

-Download the script and copy it to /usr/local/bin dir

-Change to execute  permissions: chmod +x "/usr/local/bin/fwlog"

-Create a file called "interface_list" in "/etc" and add your wan and lan  interface names. Example:

  wan pppoe0
  lan   re0


 -Create a file called "ports" that holds ports number followed by port name under /etc. Example:

  # cat /etc/ports
    22 ssh
    23 telnet
    25 smtp
    80 http
  
  -Make sure you install perl module  : Net::Nslookup;
  
  run it 
  
  
