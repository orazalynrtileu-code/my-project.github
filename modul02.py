class AppConfig:
    CONNECTION_STRING = (
        "Server=myServer;Database=myDb;User Id=myUser;Password=myPass;"
    )


def log(level, message):
    print(f"{level}: {message}")

def log_error(message):
    log("ERROR", message)

def log_warning(message):
    log("WARNING", message)

def log_info(message):
    log("INFO", message)


class DatabaseService:
    def connect(self):
        connection_string = AppConfig.CONNECTION_STRING
        log_info(f"Базаға қосылу: {connection_string}")


class LoggingService:
    def log_to_db(self, message):
        connection_string = AppConfig.CONNECTION_STRING
        log_info(f"Лог базаға жазылды: {message}")


def process_numbers(numbers):
    if not numbers:
        return

    for number in numbers:
        if number > 0:
            print(number)


def print_positive_numbers(numbers):
    if not numbers:
        return

    for number in numbers:
        if number > 0:
            print(number)


def divide(a, b):
    if b == 0:
        return 0
    return a / b


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class FileReader:
    def read_file(self, file_path):
        return "file content"


class ReportGenerator:
    def generate_pdf_report(self):
        print("PDF есеп беру жасалды")


if __name__ == "__main__":
    log_info("Жүйе іске қосылды")
    log_warning("Ескерту хабарламасы")
    log_error("Қате орын алды")
