# Pysploit
A custom tool for reverse shell exploitation and handling.

## Features
- Generate reverse shell payloads
- Start a listener to catch shells
- Handle multiple types of payloads (Python, PowerShell, etc.) all in one

## Prerequisites
- **Python 3.x** (Ensure Python is installed on your machine)
- **Git** (for cloning the repository)
- **Localtonet** (Optional for global port forwarding)

## Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/junied20/Pysploit.git
   cd Pysploit
Install Python Dependencies

Make sure you have Python 3.x installed on your system. If not, download it from python.org.

You can install the required Python packages with the following command:

bash
Copy
Edit
pip install -r requirements.txt
Note: If you don't have a requirements.txt, simply ensure Python is installed and ready to run .py files.

Usage
Generate Payload
Run the tool:

bash
Copy
Edit
python pysploit.py
Choose the type of stager you want to use:

Python Reverse Shell

PowerShell Reverse Shell

Enter your local IP address and port where the listener will be running.

Choose a filename for the payload (e.g., backdoor.ps1 or backdoor.py).

The payload will be saved to the stager/ directory.

Start Listener
Run the listener with the following command:

bash
Copy
Edit
python pysploit.py
Enter the local IP (LHOST) and port (LPORT) to listen for incoming shells.

Usage with Localtonet (Global Access)
If you want to make your reverse shell accessible globally, you can use Localtonet for port forwarding. Follow these steps:

Sign Up for Localtonet:

Visit Localtonet and create a free account.

Set Up Port Forwarding:

Once signed in, set up a port forwarding rule for the local port you want to use for the reverse shell.

Localtonet will provide you with a public IP address that you can use for external access.

Update Your Payload:

When generating your payload, use the public IP provided by Localtonet as the LHOST instead of your local IP.

You can now access your reverse shell from anywhere using the public IP.

Disclaimer
By using this tool, you acknowledge that Pysploit is intended for educational purposes only. You must have permission to test and deploy these tools on any target system. The creator of this tool is not liable for any misuse or illegal activity carried out using this software.

Author
Pysploit is developed by Junied Abrar.
