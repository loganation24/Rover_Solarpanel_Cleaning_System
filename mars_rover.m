%===============================
% Mars Rover Dust Sensing System
%===============================
% Logan Brown
% 6/18/2026

clear; clc;

%-----------
% Variables
%-----------
rover_s = 'Stationary';
rover_o = 'Operating';
rover_c = 'Panels dirty, initiating cleaning process.';
rover_m = 'Rover is currently moving.';
rover_status = rover_o; % Default status: Operating
battery_reserves = 100;
solar_panels = 0;

%================================
% Dust Storm / Panel Status Check
%================================
while true
    dust_storm = input('Dust storm status (Active/Clear): ', 's');

    if strcmp(dust_storm, 'Clear')
        solar_panels = input('Dust accumulation percentage (1-100): ');

        if solar_panels <= 10
            rover_status = rover_o;
            fprintf('Rover status: %s\n', rover_o);
        elseif solar_panels > 10 && solar_panels <= 100
            rover_status = rover_c;
            fprintf('Rover status: %s\n', rover_c);
        else
            rover_status = rover_s;
            fprintf('Rover status: %s\n', rover_s);
        end
        break;

    elseif strcmp(dust_storm, 'Active')
        fprintf('Dust storm active!\n');
        fprintf('Rover status: %s\n', rover_s);
        fprintf('Sleep mode is active, battery reserves engaged. Sending most recent coordinates!\n');

        latitude  = 18.38;  % North
        longitude = 77.53;  % East
        fprintf('%.2f N  %.2f E\n', latitude, longitude);

        while true
            fprintf('Coordinates saved, awaiting clearance for cleaning procedure.\n');
            panel_sensor = input('Dust storm status (Active/Clear): ', 's');

            if strcmp(panel_sensor, 'Clear')
                fprintf('Dust storm has passed! Rebooting main battery system.\n');
                fprintf('Initializing cleaning procedure.\n');
                solar_panels = input('Dust accumulation percentage (1-100): ');
                rover_status = rover_c;
                break;
            else
                continue;
            end
        end
        break;

    else
        fprintf('Invalid input, please try again.\n');
    end
end

%====================
% Panel Cleaning Loop
%====================
if strcmp(rover_status, rover_c)
    while solar_panels > 0
        solar_panels = solar_panels - 1;
        fprintf('Executing cleaning procedure, dust accumulation: %d%%\n', solar_panels);
    end
    fprintf('Solar panels are clear of all dust!\n');
    fprintf('Resuming all operations and restoring battery reserves to full charge.\n');
end

%==========================
% Battery Drain During Storm
%==========================
days = 1:10;

battery_percentage = 100 - 0.9 * (days).^2; 
battery_percentage = max(10, min(100, battery_percentage));

figure(1)
plot(days, battery_percentage, 'b-o', 'LineWidth', 2)
xlabel('Days during a dust storm at full functionality')
ylabel('Battery %')
title('Battery Drain During Dust Storm')
grid on



%===========================
% Sand Trap Maneuvering System
%===========================
% The rover detects if it is stuck by comparing expected vs actual displacement.
% If displacement is zero, the maneuvering system activates.

fprintf('\n--- Sand Trap Maneuvering System ---\n');

velocity = input('Enter rotational velocity (rotations per minute): ');
time_s   = input('Enter time in seconds: ');
displacement = displacement_calc(velocity, time_s);
fprintf('Expected displacement: %.2f meters\n', displacement);

while true
    rover_moving = input('Is rover currently moving? (Yes/No): ', 's');

    if strcmp(rover_moving, 'Yes')
        fprintf('Rover is moving normally, continuing all operations.\n');
        fprintf("Rover's actual displacement: %.2f meters.\n", displacement);
        break;

    elseif strcmp(rover_moving, 'No')
        fprintf('Actual displacement is less than expected! Rover is stuck, extending wheel paddles...\n');
        battery = input('Enter current battery percentage: ');
        battery = battery_drainage(battery, 10);
        fprintf('Estimated battery after using extended paddles: %d%%\n', battery);

        while true
            rover_moving2 = input('Is rover moving after extending paddles? (Yes/No): ', 's');

            if strcmp(rover_moving2, 'Yes')
                fprintf('Rover has been freed! Resuming all operations.\n');
                break;

            elseif strcmp(rover_moving2, 'No')
                fprintf('Reducing wheel RPM from %.1f to %.1f RPM...\n', velocity, velocity - 10);
                velocity = velocity - 10;

                if velocity <= 0
                    fprintf('WARNING: Wheel RPM at zero! Rover is completely stuck!\n');
                    fprintf('Sending distress signal to mission control...\n');
                    break;
                else
                    fprintf('Retrying with %.1f RPM...\n', velocity);
                end

            else
                fprintf('Invalid input, please try again.\n');
            end
        end
        break;

    else
        fprintf('Invalid input, please try again.\n');
    end
end

