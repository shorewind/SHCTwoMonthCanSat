% space hardware club twomonth fall 2021
% team 10 launch data and animated graphs

clc; clear; close all;

% import data
dataTable = readtable('flight-10-23-data.txt','delimiter',',','ReadVariableNames',0);
dataArray = table2array(dataTable);

% establish number of rows and columns
rows = height(dataArray);
columns = width(dataArray);

% list of allowed characters
characters = ['0','1','2','3','4','5','6','7','8','9','-'];

% initialize new data array with same dimensions as the imported data
dimensions = size(dataArray);
newdataArray = zeros(dimensions);

for row = 1:rows
    for column = 1:columns
        cell = char(dataArray(row,column));
        for i = 1:length(cell) % loops through individual characters in cell
            if sum(cell(i) == characters) == 0 % if the character is not allowed create new cell
                newCell = cell(1:i-1); % only includes characters until the first non-permitted character
                newCell = string(newCell);
                newdataArray(row,column) = newCell; % add new cell to new data array
                break
            end
        end
    end
end

newdataArray = rmmissing(newdataArray); % exclude rows with NaN values
newdataArray(:,9) = newdataArray(:,9)./1000; % convert time from ms to s

sgtitle('SHC TwoMonth Team 10 Data - 10/23 Launch') % master title

% pressure vs. time subplot
subplot(2,2,1)

hold on
grid on
title('Pressure vs. Time')
xlabel('Time (s)')
ylabel('Pressure (hPa)')

h_p = animatedline('Color','#0077C8');
x = newdataArray(:,9);
y_p = newdataArray(:,2);
ylim([960, 1000])

% temperature vs. time subplot
subplot(2,2,2)

grid on
title('Temperature vs. Time')
xlabel('Time (s)')
ylabel('Temperature (C)')

h_t = animatedline('Color','#D95319');
y_t = newdataArray(:,3);
ylim([24, 34])

% humidity vs. time subplot
subplot(2,2,3)

grid on
title('Humidity vs. Time')
xlabel('Time (s)')
ylabel('Humidity (%)')

h_h = animatedline('Color','#7E2F8E');
y_h = newdataArray(:,4);
ylim([25, 45])

% altitude vs. time subplot
subplot(2,2,4)

grid on
title('Altitude vs. Time')
xlabel('Time (s)')
ylabel('Altitude (m)')

h_a = animatedline('Color','#77AC30');
y_a = newdataArray(:,5);
ylim([-10, 300])

pause(3)  % give time to adjust window

% save animated graph as video
video = VideoWriter('SHC TwoMonth Flight Data Visualization.avi');
video.Quality = 100;
video.FrameRate = 10;
open(video);

% add points to function and live graph
for k = 425:575 % 1:length(x) for uncropped data
    addpoints(h_p,x(k),y_p(k));
    addpoints(h_t,x(k),y_t(k));
    addpoints(h_h,x(k),y_h(k));
    addpoints(h_a,x(k),y_a(k));
    drawnow
    f = getframe(gcf);
    writeVideo(video, f);
    pause(0.1) % approximate interval between points drawn
end

video.close()

% savefig('SHC TwoMonth Team 10 Data.fig')
