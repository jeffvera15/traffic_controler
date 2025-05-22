# traffic_controller
Traffic Light Simulation Project 

![Example](imgs/example.JPG)

This project simulates a traffic light system using a Raspberry Pi Pico, two LED-based traffic modules, and an I2C 20x4 LCD screen. The lights alternate based on a programmable algorithm depending on simulated traffic density.

> *PLEASE READ COMPLETE FILE BEFORE SET-UP*

---

Required Components:

* Raspberry Pi Pico
* 12x Female to Female Connectors
* 2x LED Traffic Light Module
* I2C LCD Display (20x4)
* Thonny IDE

---

Links to Required Items:

Raspberry Pi Pico Starter Kit:
[Buy on Amazon](https://www.amazon.com/Freenove-Raspberry-Contained-Compatible-Tutorials/dp/B09H2TFRN2/ref=sr_1_1_sspa?crid=2AYVEGIW5ZBZP&dib=eyJ2IjoiMSJ9.hRDmnzDNMeQmptCjsG845GHQGcS0MVtPoA-K1fAIVPT2QMbcX52aMHC1KvArjMoDDhlQIsLPpdvr8s9m1ajvqHPncgwgceAMKx3ID8eKPGyz1TiqC257Ba8V7Ji66Fr1cmvC21x7568NbMl4fjQ1OPIUo9ikrMkb5RPKhBlQQDlGz4EiNblg0oz_BfE2ARsnCqTpHirgKO93vEHUc5uY5A9Wc-nM6NIP4cVGpd7o9XchyisIXEAMautFg4LR_YTwRItZq3Auna7RwdKiKdrZQjBtCvC4c9RkJm211SXa59c.PIKP_QEtQfqTxEnWHGdiEVTXmE8t-iYUaMIXJVcSAno&dib_tag=se&keywords=pi%2Bpico%2Bstarter%2Bkit&qid=1747939525&s=electronics&sprefix=pi%2Bpico%2Bstarter%2Bkit%2Celectronics%2C116&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)

*Note Starter Kit Comes with ONLY 10 F-F Connectors. You may need more OR you could configure this setup on a BreadBoard using F-M connectors*

LED Traffic Light Modules:
[Buy on Amazon](https://www.amazon.com/Adeept-Traffic-Creative-Raspberry-RGB-Traffic/dp/B097GK4S2D/ref=asc_df_B097GK4S2D?mcid=e388c9f78f8236a2947a66aa9e6a9fa6&hvocijid=7387839274406831382-B097GK4S2D-&hvexpln=73&tag=hyprod-20&linkCode=df0&hvadid=721245378154&hvpos=&hvnetw=g&hvrand=7387839274406831382&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9192431&hvtargid=pla-2281435177858&th=1)

---

Instructions:

Download The Repository.

Open the project in Thonny IDE.

Then using the F-F (Female to Female) connectors, connect the following using this diagram:

![Pico Diagram](imgs/pico_diagram.png)

I2C LCD:
GND - Any GND connection
VCC - VBUS or VSYS
SDA - GP0
SCL - GP1

Traffic Controller Module 1:

GND - Any GND Connection
Red - GP10
Yellow - GP11
Green - GP12

Traffic Controller Module 2:
GND - Any GND Connection
Red - GP13
Yellow - GP14
Green - GP15

*All GP pins can be adjusted within the code*

After completing all of the connections, connect a microUSB cable to the Raspberry Pi Pico and your System running Thonny.

Within Thonny in the "Run" tab, ensure the following is selected: 
Thonny -> Run -> Configure Interpreter -> "MicroPython"

---

Afterwards hit the Run current script button (Green Play Button on Thonny IDE or F5 on keyboard), and Enjoy :)

![Setup](imgs/thonny_setup.jpg)
