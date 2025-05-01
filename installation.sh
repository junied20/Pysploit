#!/bin/sh

# Add the repository key
curl -SsL https://playit-cloud.github.io/ppa/key.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/playit.gpg >/dev/null

# Add the Playit repository to the sources list
echo "deb [signed-by=/etc/apt/trusted.gpg.d/playit.gpg] https://playit-cloud.github.io/ppa/data ./" | sudo tee /etc/apt/sources.list.d/playit-cloud.list

# Update apt package lists
sudo apt update

# Install the Playit package
sudo apt install -y playit

# Display ASCII Art and disclaimer
echo "________  ___    ___ ________  ________  ___       ________  ___  _________"
echo "|\   __  \|\  \  /  /|\   ____\|\   __  \|\  \     |\   __  \|\  \|\___   ___\"
echo "\ \  \|\  \ \  \/  / | \  \___|\ \  \|\  \ \  \    \ \  \|\  \ \  \|___ \  \_|"
echo " \ \   ____\ \    / / \ \_____  \ \   ____\ \  \    \ \  \\  \ \  \   \ \  \  "
echo "  \ \  \___|\/  /  /   \|____|\  \ \  \___|\ \  \____\ \  \\  \ \  \   \ \  \ "
echo "   \ \__\ __/  / /       ____\_\  \ \__\    \ \_______\ \_______\ \__\   \ \__"
echo "    \|__||\___/ /       |\_________\|__|     \|_______|\|_______|\|__|    \|__|"
echo "         \|___|/        \|_________|"
echo "                                                            by Junied Abrar | Github:junied20"
echo "DISCLAIMER: This script is intended for ethical use only. Please ensure that you have proper authorization before using it. Unauthorized use can be illegal and unethical."

# Ask the user if they want to download playit
read -p "Do you want to download and install Playit? (yes/no): " answer

if [ "$answer" = "yes" ]; then
    # Logic to download and install playit
    echo "Installing Playit..."
    sudo apt install -y playit
    echo "Playit installed successfully."
else
    # Redirect to running setup.py if they don't want to download Playit
    echo "Skipping Playit download. Running setup.py..."
    # Ensure the setup.py file exists in the current directory
    if [ -f "./setup.py" ]; then
        python3 ./setup.py
    else
        echo "Error: setup.py not found in the current directory."
    fi
fi
