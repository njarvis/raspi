#!/usr/bin/python
# -*- coding: utf-8 -*-
# improved and completed by PiModules Version 1.0 29.08.2015
# picoStatus-v3.py by KTB is based on upisStatus.py by Kyriakos Naziris
# Kyriakos Naziris / University of Portsmouth / kyriakos@naziris.co.uk


import smbus
import time

i2c = smbus.SMBus(1)

def pwr_mode():
       data = i2c.read_byte_data(0x69, 0x00)
       data = data & ~(1 << 7)
       if (data == 1):
              return "RPi"
       elif (data == 2):
              return "BAT"
       else:
              return "ERR"

def bat_level():
       time.sleep(0.1)
       data = i2c.read_word_data(0x69, 0x01)
       data = format(data,"x")
       return (float(data) / 100)

def bat_serror():
       time.sleep(0.1)
       data = i2c.read_word_data(0x6b, 0x04)
       data = format(data,"x")
       return (float(data) / 100)

def rpi_level():
       time.sleep(0.1)
       data = i2c.read_word_data(0x69, 0x03)
       data = format(data,"x")
       return (float(data) / 100)

def rpi_serror():
       time.sleep(0.1)
       data = i2c.read_word_data(0x6b, 0x02)
       data = format(data,"x")
       return (float(data) / 100)

def tmp_serror():
       time.sleep(0.1)
       data = i2c.read_word_data(0x6b, 0x06)
       data = format(data,"x")
       return data

def fw_version():
       time.sleep(0.1)
       data = i2c.read_byte_data(0x6b, 0x00)
       data = format(data,"02x")
       return data

def sot23_temp():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x0C)
   data = format(data,"02x")
   return data

def to92_temp():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x0d)
   data = format(data,"02x")
   return data

def ad1_read():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x05)
   data = format(data,"02x")
   return (float(data) / 100)

def ad2_read():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x07)
   data = format(data,"02x")
   return (float(data) / 100)

def error_code():
       error_bits = {0: 'RPi Powering Voltage lower than 4.7V',
                     1: 'Battery Voltage lower than 3.3V',
                     2: 'Battery Temperature higer than 50 C',
                     3: 'UPS PIco System watch-dog restart',
                     7: 'Writing data to PIco EEPROM'}
       time.sleep(0.1)
       data = i2c.read_byte_data(0x6b, 0x01)
       if data == 0:
              return "No error"
       else:
              errors = ()
              for b, m in error_bits.iter():
                     if data & (1 << b):
                            errors.append(m)
              return ', '.join(errors)

def sta_counter():
       time.sleep(0.1)
       data = i2c.read_byte_data(0x6b, 0x08)
       if data == 255:
              return "Disabled"
       else:
              return "{}s".format(data)

def fssd_battime():
       time.sleep(0.1)
       data = i2c.read_byte_data(0x6b, 0x09)
       if data == 255:
              return "Disabled"
       else:
              return "{}s".format(data)

def lprsta():
       time.sleep(0.1)
       data = i2c.read_byte_data(0x6b, 0x0a)
       return "{}s".format(data)

def btto():
       time.sleep(0.1)
       data = i2c.read_byte_data(0x6b, 0x0b)
       return "{}s".format(data)

print " "
print "        pico status V1.1"
print "***********************************"
print "*","UPS PIco Firmware:",fw_version()
print "*","Powering Mode:",pwr_mode()
print "*","BAT Voltage:", bat_level(),"V"
print "*","RPi Voltage:" , rpi_level(),"V"

print "*","SOT23 Temperature:" , sot23_temp(),"C"
print "*","TO-92 Temperature:" , to92_temp(),"C"
print "*","A/D1 Voltage:" , ad1_read(),"V"
print "*","A/D2 Voltage:" , ad2_read(),"V"

print "*","Error codes:", error_code()
print "*","RPi Voltage at error:", rpi_serror(), "V"
print "*","BAT Voltage at error:", bat_serror(), "V"
print "*","Temperature at error:", tmp_serror(), "C"
print "*","Still Alive Timeout:", sta_counter()
print "*","Battery Runtime:", fssd_battime()
print "*","Low Power Restart timer:", lprsta()
print "*","Battery Power Testing timer:", btto()

print "***********************************"
print " "

                                                    
