import paramiko
import yaml


def upload_files(host, user, passwd, local_path, remote_path, port=22):
    print(f"Загружаем фаил {local_path} в каталог {remote_path}")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()


def download_files(host, user, passwd, local_path, remote_path, port=22):
    print(f"Загружаем фаил {remote_path} в каталог {local_path}")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()


if __name__ == "__main__":
    with open ('config.yaml') as fy:
        data = yaml.safe_load(fy)
        download_files("0.0.0.0", "ma", "7", "/home/user2/stat.txt", "/home/user/stat.txt")
