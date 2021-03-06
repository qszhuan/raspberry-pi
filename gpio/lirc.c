#include <wiringPi.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <lirc/lirc_client.h>
#include <time.h>
 
void flipLED (int led);
 
//The WiringPi pin numbers used by our LEDs
#define LED1 4
#define LED2 5
#define LED3 6
#define LED4 11
#define LED5 10
#define LED6 14
 
#define ON 1
#define OFF 0
 
int main(int argc, char *argv[])
{
        struct lirc_config *config;
 
        //Timer for our buttons
        int buttonTimer = millis();
 
        char *code;
        char *c;
 
        //Initiate WiringPi and set WiringPi pins 4, 5 & 6 (GPIO 23, 24 & 25) to output. These are the pins the LEDs are connected to.
        if (wiringPiSetup () == -1)
            exit (1) ;
 
        pinMode (LED1, OUTPUT);
        pinMode (LED2, OUTPUT);
        pinMode (LED3, OUTPUT);
	pinMode (LED4, OUTPUT);
        pinMode (LED5, OUTPUT);
        pinMode (LED6, OUTPUT);
 
        //Initiate LIRC. Exit on failure
        if(lirc_init("lirc",1)==-1)
                exit(EXIT_FAILURE);
 
        //Read the default LIRC config at /etc/lirc/lircd.conf  This is the config for your remote.
        if(lirc_readconfig(NULL,&config,NULL)==0)
        {
                //Do stuff while LIRC socket is open  0=open  -1=closed.
                while(lirc_nextcode(&code)==0)
                {
                        //If code = NULL, meaning nothing was returned from LIRC socket,
                        //then skip lines below and start while loop again.
                        if(code==NULL) continue;{
                                //Make sure there is a 400ms gap before detecting button presses.
                                if (millis() - buttonTimer  > 400){
                                       printf(code);
					 //Check to see if the string "KEY_1" appears anywhere within the string 'code'.
                                        if(strstr (code,"KEY_NUMERIC_1")){
                                                printf("MATCH on KEY_NUMERIC_1\n");
                                                flipLED(LED1);
                                                buttonTimer = millis();
                                        }
                                        else if(strstr (code,"KEY_NUMERIC_2")){
                                                printf("MATCH on KEY_NUMERIC_2\n");
                                                flipLED(LED2);
                                                buttonTimer = millis();
                                        }
                                        else if(strstr (code,"KEY_NUMERIC_3")){
                                                printf("MATCH on KEY_NUMERIC_3\n");
                                                flipLED(LED3);
                                                buttonTimer = millis();
                                        }
					else if(strstr (code,"KEY_NUMERIC_4")){
                                                printf("MATCH on KEY_NUMERIC_4\n");
                                                flipLED(LED4);
                                                buttonTimer = millis();
                                        }
                                        else if(strstr (code,"KEY_NUMERIC_5")){
                                                printf("MATCH on KEY_NUMERIC_5\n");
                                                flipLED(LED5);
                                                buttonTimer = millis();
                                        }else if(strstr (code,"KEY_NUMERIC_6")){
                                                printf("MATCH on KEY_NUMERIC_6\n");
                                                flipLED(LED6);
                                                buttonTimer = millis();
                                        }
                                }
                        }
                        //Need to free up code before the next loop
                        free(code);
                }
                //Frees the data structures associated with config.
                lirc_freeconfig(config);
        }
        //lirc_deinit() closes the connection to lircd and does some internal clean-up stuff.
        lirc_deinit();
        exit(EXIT_SUCCESS);
}
 
void flipLED (int led)
{
        //If LED is on, turn it off. Otherwise it is off, so thefore we need to turn it on.
        if(digitalRead(led)==ON){
		printf("try to turn off");
                digitalWrite(led, OFF);
	}
        else{
		printf("try to turn on");
                digitalWrite(led, ON);
	}
}
