How to Install Python 3.7 on Ubuntu and set priority to 1
============================================================

Step 1: Open Terminal

Step 2: Update System Repositories

        sudo apt update

Step 3: Install prerequisites package

        sudo apt install software-properties-common

Step 4: Add PPA
    
        sudo add-apt-repository ppa:deadsnakes/ppa

Step 5: Update System Repositories

        sudo apt update

Step 6: Install Python 3.7

        sudo apt install python3.7
		
Step 7:	Check what is the number you can assigned to newly install python3
		
		sudo update-alternatives --config python3
		
Step 8:	Assigned 1 as a number
		
		sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
		
Step 9:	Rerun script and assigned 1 value when promt
		
		sudo update-alternatives --config python3
		
Finally Test version
		
		python3 --version
		
		Python 3.7.1 