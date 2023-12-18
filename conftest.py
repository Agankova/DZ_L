import pytest
import yaml
import random
import string
from datetime import datetime
from checkers import ssh_checkout, ssh_get, getout
from files import upload_files

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(autouse=True, scope="module")
def make_folders():
    return ssh_checkout("0.0.0.0", "ma", "7",
                        "mkdir -p {} {} {} {} {}".format(data["folder_in]",
                        data["folder_out"], data["folder_ext"], data["folder_ext2"],
                        data["folder_extract"]), "")



@pytest.fixture(autouse=True, scope="module")
def make_files():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout("0.0.0.0", "ma", "7", "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullback".format(data["folder_in"],
                                                                                    filename,data["bs"]), ""):
            list_off_files.append(filename)
    return list_off_files




@pytest.fixture(autouse=True, scope="module")
def clear_folders():
    return shh_checkout("0.0.0.0", "ma", "7", "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"],
                                            data["folder_out"], data["folder_ext"], data["folder_ext2"]), "")


@pytest.fixture()
def make_bad_arx():
    ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z a {}/bad_arx".format(data["folder_in"], data["folder_out"]),
                 "Everything is Ok")
    ssh_checkout("0.0.0.0", "ma", "7", "truncate -s 1 {}/bad_arx.7z".format(data["folder_out"]), "")


@pytest.fixture()
def make_subfolders():
    testfilename = ''.join(random.choice(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choice(string.ascii_uppercase + string.digits, k=5))
    if ssh_checkout("0.0.0.0", "ma", "7", "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock"
            .format(data["folder_out"], subfoldername, testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_stat():
    yield
    processor_work = getout("cat /prog/loadavg")
    tests_stat = (f"{datatime.now()} - Config files qty: {data['count']}, files size: {data['bs']}, Processor"
                  f" statistics: {processor_work}")
    getout(f"echo '{tests_stat}' >> {data['stat_file']}")


@pytest.fixture(autouse=True, scope="module")
def deploy():
    res = []
    upload_files("0.0.0.0", "ma", "7", "/home/user/p7zip-full.deb", "/home/user2/p7zip-full.deb")
    res.append(shh_checkout("0.0.0.0", "ma", "7", "echo '7' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(shh_checkout("0.0.0.0", "ma", "7", "echo '7' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


@pytest.fixture(scope="module")
def save_log(start_time):
    with open("start.txt", "w") as f:
        f.write(ssh_get("0.0.0.0", "ma", "7", "journalctl --since {}".format(start_time)))


@pytest.fixture(autouse=True, scope="module")
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


