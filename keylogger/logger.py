from datetime import datetime

print("===== Input Logger =====")
print("Type 'exit' to stop logging.\n")

log_file = "log.txt"

while True:
    text = input("Enter text: ")

    if text.lower() == "exit":
        print("Logger stopped.")
        break

    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {text}\n")

    print("Input logged successfully.")