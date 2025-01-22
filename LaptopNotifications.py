

# pip install plyer
# Laptop Notification using python

from plyer import notification

notification.notify(
    title='Reminder',
    message='Time to Break',
    # app_name='Python Notifier',
    timeout=10

)