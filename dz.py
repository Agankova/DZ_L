import subprocess


if __name__ == "__main__":
    def check_output(command, text):
        try:
            output = subprocess.check_output(command, shell=True).decode()
            if text in output:
                return True
            else:
                return False
        except subprocess.CalledProcessError:
            return False

    command1 = "rm --help"
    command2 = "cat /etc/os-release"
    text1 = "no-preserve-root"
    text2 = "VERSION_CODENAME=JAMMY"

    result1 = check_output(command1, text1)
    result2 = check_output(command2, text2)

    print(result1)
    print(result2)
