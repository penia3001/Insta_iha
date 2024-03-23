import subprocess

def check_for_new_message():
    with open('new_message_signal.txt', 'r') as file:
        if file.readline():
            file.close()
            show_notification()
            # Dosyayı temizle
            open('new_message_signal.txt', 'w').close()

def show_notification():
    with open('messages.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            last_message = lines[-1]
            subprocess.run(['termux-notification', '--title', 'Yeni Mesaj', '--content', last_message])

if __name__ == '__main__':
    while True:
        check_for_new_message()
