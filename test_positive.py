import yaml
import subprocess
from checkers import ssh_checkout
from conftest import make_files

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:

    def test_step1(self, make_files, make_stat, start_time):
        # test1
        result1 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z a {}/arx2".format(data["folder_in"],
                                                                                  ["folder_out"], data["key_t"]),
                               "Everything is Ok")
        result2 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; ls".format(data["folder_out"]), "arx2.7z")
        assert result1 and result2, "test1 Fail"

    def test_step2(self, make_files, make_stat, start_time):
        # test2
        result1 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z e arx2.7z -o/{} -y".format(data["folder_out"],
                                                                                           ["folder_ext"]),
                               "Everything is Ok")
        result2 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; ls".format(data["folder_ext"]), make_files[0])

        assert result1 and result2, "test2 Fail"

    def test_step3(self, make_stat, start_time):
        # test3
        assert ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z t arx2.7z".format(data["folder_out"]),
                            "Everything is Ok"), "test3 Fail"

    def test_step4(self):
        # test4
        assert ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z u {}/arx2.zip".format(data["folder_in"],
                                                                                   data["folder_out"]),
                            "Everything is Ok"), "test4 Fail"

#    def test_step5(self, make_stat,start_time):
        # test5
#        result1 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z d arx2.7z".format(data["folder_out"]),
#                               "Everything is Ok")
#        assert  result1, "test5 Fail"


def test_step6(self, make_stat,make_files, start_time):
    result1 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z 1 arx2.zip".format(data["folder_out"],
                                                                               data["folder_extract"], make_files[0])
    result2 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z 1 arx2.zip".format(data["folder_out"],
                                                                               data["folder_extract"], make_files[0])
    assert  result1 and result2, "test_step6 Fail"


def test_step7(self, make_files, make_stat, start_time):
        result1 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; 7z x arx2.zip -o{} -y".format(data["folder_out"],
                                                                        data["folder_ext2"]), "Everything is Ok")
        result2 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; ls".format(data["folder_ext2"]), make_files[0])
        result3 = ssh_checkout("0.0.0.0", "ma", "7", "cd {}; ls".format(data["folder_ext2"],
                                                                        make_files[0])
        assert  result1 and result2 and result3, "test_7 Fail"


def test_8(self, make_stat):
    folder_out = "/home/ma/out"
    result = subprocess.run("crc32 /home/ma/out/arx2.zip, shell=True, stdout=subprocess.PIPE, encoding='utf-8")
    datas = result.stdout.rstrip().upper()
    assert ssh_checkout("0.0.0.0", "ma", "7", f"cd {folder_out}; 7z h arx2.zip", datas), "test_8 Fail"

