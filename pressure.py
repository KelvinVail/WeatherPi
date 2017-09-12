#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085
from time import sleep
from dot_matrix_display import clear_terminal
from dot_matrix_display import print_numbers
from dot_matrix_display import print_arrows


sensor = BMP085.BMP085()
clear_terminal()
second_list = []
second_count = 60
minute_list = []
minute_count = 60
arrow_list = [0,0,0,0,0,0]
hour_chg = 0

while True:
    try:
        pressure = int(sensor.read_pressure())
        second_list.append(pressure)
        second_list = second_list[-60:]

        # Every minute
        if second_count >= 60:
            second_count = 0
            minute_avg = int(sum(second_list) / float(len(second_list)))
            print_numbers(1, 1, "%06d" % (minute_avg))

            minute_list.append(minute_avg)
            minute_list = minute_list[-60:]
            first_min = minute_list[0]
            last_min = minute_list[-1]
            hour_chg = last_min - first_min
            if hour_chg > 0:
                print_numbers(7, 1, "%06d" % (abs(hour_chg)), 'green')
            else:
                print_numbers(7, 1, "%06d" % (abs(hour_chg)), 'red')

            # Every hour
            if minute_count >= 60:
                minute_count = 0
                if hour_chg > 100:
                    arrow_list.append(2)
                elif hour_chg < -100:
                    arrow_list.append(-2)
                elif hour_chg > 50:
                    arrow_list.append(1)
                elif hour_chg < -50:
                    arrow_list.append(-1)
                else:
                    arrow_list.append(0)
                arrow_list = arrow_list[-6:]
                print_arrows(13, 1, arrow_list)

            minute_count += 1

        sleep(1)
        second_count += 1
    except KeyboardInterrupt:
        raise
    except:
        raise

#print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
#print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
