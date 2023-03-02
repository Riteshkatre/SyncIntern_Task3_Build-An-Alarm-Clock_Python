import datetime
import time
import playsound

def play_alarm_sound():
    playsound.playsound('alarm_sound.mp3')

def get_alarm_time():
    while True:
        alarm_time = input("Enter the alarm time in HH:MM format: ")
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            if 0 <= alarm_hour < 24 and 0 <= alarm_minute < 60:
                return (alarm_hour, alarm_minute)
        except ValueError:
            pass
        print("Invalid time format. Please enter the time in HH:MM format.")

def snooze():
    return input("Enter 'snooze' to snooze the alarm for 5 minutes, or press Enter to stop the alarm: ").lower() == 'snooze'

def main():
    print("Welcome to the alarm clock!")
    alarm_hour, alarm_minute = get_alarm_time()

    while True:
        # Get the current time
        now = datetime.datetime.now()

        # Check if it's time for the alarm to go off
        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("Time to wake up!")
            play_alarm_sound()

            # Snooze the alarm
            while snooze():
                print("Snoozing for 5 minutes...")
                time.sleep(300)
                print("Time to wake up!")
                play_alarm_sound()

            # Stop the alarm
            break

        # Wait for a bit before checking the time again
        time.sleep(10)

if __name__ == '__main__':
    main()
