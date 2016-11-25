[http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/)  

[http://ozzmaker.com/how-to-control-the-gpio-on-a-raspberry-pi-with-an-ir-remote/](http://ozzmaker.com/how-to-control-the-gpio-on-a-raspberry-pi-with-an-ir-remote/)

### Step:

1. We need to install LIRC and client libraries.

`sudo apt-get install lirc liblircclient-dev`

2. Then add the two lines below to `/etc/modules` . This will start the modules up on boot. Pin 18 bellow will be used to take the output from the IR sensor.


    lirc_dev
    lirc_rpi gpio_in_pin=18

3. Edit /etc/lirc/hardware.conf and have it appear exactly as shown below.

 
    # /etc/lirc/hardware.conf
    #
    # Arguments which will be used when launching lircd
    LIRCD_ARGS="--uinput"
    
    # Don't start lircmd even if there seems to be a good config file
    # START_LIRCMD=false
    
    # Don't start irexec, even if a good config file seems to exist.
    # START_IREXEC=false
    
    # Try to load appropriate kernel modules
    LOAD_MODULES=true
    
    # Run "lircd --driver=help" for a list of supported drivers.
    DRIVER="default"
    # usually /dev/lirc0 is the correct setting for systems using udev
    DEVICE="/dev/lirc0"
    MODULES="lirc_rpi"
    
    # Default configuration files for your hardware if any
    LIRCD_CONF=""
    LIRCMD_CONF=""

4. Edit your /boot/config.txt file and add:

    dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22

5. Reboot

6. Testing the IR receiver

    sudo /etc/init.d/lirc stop
    mode2 -d /dev/lirc0

Point a remote control at your IR receiver and press some buttons. You should see something like this:

    space 16300
    pulse 95
    space 28794
    pulse 80
    space 19395
    pulse 83
    space 402351
    pulse 135
    space 7085
    pulse 85
    space 2903

7. Here were the commands that I ran to generate a remote configuration file:

    # Stop lirc to free up /dev/lirc0
    sudo /etc/init.d/lirc stop

    # Create a new remote control configuration file (using /dev/lirc0) and save the output to ~/lircd.conf
    irrecord -d /dev/lirc0 ~/lircd.conf

    # Make a backup of the original lircd.conf file
    sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf

    # Copy over your new configuration file
    sudo cp ~/lircd.conf /etc/lirc/lircd.conf

    # Start up lirc again
    sudo /etc/init.d/lirc start