from machine import Pin
import time
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#INITIAL CONDITIONS

#Number of Cars
n = list(range(1,11)) #Shows all Numbers 1 through 10.

#LCD and i2c
I2C_ADDR = 0X27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#Define pins for Traffic Light 1
red1 = Pin(10, Pin.OUT) #GP0
yellow1 = Pin(11, Pin.OUT) #GP1
green1 = Pin(12, Pin.OUT) #GP2

#Define pins for Traffic Light 2
red2 = Pin(13, Pin.OUT) #GP3
yellow2 = Pin(14, Pin.OUT) #GP4
green2 = Pin(15, Pin.OUT) #GP5

#Traffic Light Switch
def traffic_light2(state):
    red2.value(state == "red")
    yellow2.value(state == "yellow")
    green2.value(state == "green")
    
#Traffic Light Switch2
def traffic_light1(state):
    red1.value(state == "red")
    yellow1.value(state == "yellow")
    green1.value(state == "green")
    
#Function to turn off all LEDs
def all_off():
    red1.off()
    yellow1.off()
    green1.off()
    red2.off()
    yellow2.off()
    green2.off()
    
#Governing Equation (Traffic Algorithm)
def traffic_algorithm(n):
    #ta = 5 * (5^(n/5))
    ta = 5 * (5 ** (n/5))
    return ta
    
#Traffic Simulation
def simulate_traffic(cars_ns, cars_we):
    #Calculation
    green_time1 = traffic_algorithm(cars_ns)
    green_time2 = traffic_algorithm(cars_we)
    
    traffic_light1("red")
    traffic_light2("green")
    time.sleep(green_time2)
    
    #Yellow
    traffic_light2("yellow")
    time.sleep(2)
    
    traffic_light2("red")
    traffic_light1("green")
    time.sleep(green_time1)
    
    #Yellow
    traffic_light1("yellow")
    time.sleep(2)
    
    traffic_light1("red")
    
#LCD Update Function
def update_lcd_display(cars_ns, cars_we):
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Cars NS: " + str(cars_ns))
    lcd.move_to(0,1)
    lcd.putstr("Cars WE: " + str(cars_we))
        
#Car Cycle Function
def car_loop(start_cars=1, end_cars=10):
    for cars_ns in range(start_cars, end_cars + 1):
        for cars_we in range(start_cars, end_cars + 1):
            update_lcd_display(cars_ns, cars_we)
            simulate_traffic(cars_ns, cars_we)
        
#Main Loop
while True:
    car_loop(start_cars=1, end_cars=10)
    
            