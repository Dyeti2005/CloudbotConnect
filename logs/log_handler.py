from datetime import datetime

class Logger:
    def __init__(self):
        self.filepath = "./logs/log.txt"

    def write_log(self, message):
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{current_time}] {message}\n"

            with open(self.filepath, "a") as logfile:
                logfile.write(log_entry)
                logfile.close()

        except Exception as e:
            print(f"Error al escribir en el archivo de registro: {str(e)}")