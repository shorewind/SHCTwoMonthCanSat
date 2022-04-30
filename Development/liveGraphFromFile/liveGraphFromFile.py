# graphs data from txt file
# animation currently not working for individual entries
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
pvt = fig.add_subplot(2, 2, 1)
tvt = fig.add_subplot(2, 2, 2)
hvt = fig.add_subplot(2, 2, 3)
avt = fig.add_subplot(2, 2, 4)


def animate(i):
    graph_data = open('testData.txt', 'r').read()
    lines = graph_data.split('\n')
    time = []
    pressure = []
    temp = []
    humidity = []
    altitude = []
    for line in lines:
        if len(line) > 1:
            list1 = line.split(',')
            for idx in range(len(list1)):
                list1[idx] = eval(list1[idx])
            time.append(list1[0])
            pressure.append(list1[1])
            temp.append(list1[2])
            humidity.append(list1[3])
            altitude.append(list1[4])
    plt.tight_layout()

    pvt.clear()
    pvt.plot(time, pressure, color='red')
    pvt.set_title('Pressure vs. Time')
    pvt.set_xlabel('Time (s)')
    pvt.set_ylabel('Pressure (hPa)')

    tvt.clear()
    tvt.plot(time, temp, color='#0077c8')
    tvt.set_title('Temperature vs. Time')
    tvt.set_xlabel('Time (s)')
    tvt.set_ylabel('Temperature (C)')

    hvt.clear()
    hvt.plot(time, humidity, color='green')
    hvt.set_title('Humidity vs. Time')
    hvt.set_xlabel('Time (s)')
    hvt.set_ylabel('Humidity (%)')

    avt.clear()
    avt.plot(time, altitude, color='#FDDA0D')
    avt.set_title('Altitude vs. Time')
    avt.set_xlabel('Time (s)')
    avt.set_ylabel('Altitude (m)')


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.suptitle('CanSat Ground Station Data')
plt.show()
