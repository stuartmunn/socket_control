To install this application:

1. Install the Energenie Pi-Mote onto the Raspberry Pi GPIO pins.

2. Install python-rpi.gpio if required: 

   sudo apt-get install python-rpi.gpio

3. Install the following python modules by issuing these commands:

   sudo pip install flask
   sudo pip install energenie

4. Clone the git repository using the following commands:
   
   mkdir webapp
   git clone https://github.com/stuartmunn/socket_control.git webapp
   
5. Run the app with the following commands:

   cd webapp
   python ./app.py &

6. Browse to the address of your raspberry pi on port 5000 (ie http://<your_address>:5000/)  


On my to do list: automate this in a shell script. :)
