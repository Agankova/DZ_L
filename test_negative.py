import yaml
from checkers import ssh_checkout_negative

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestNegative:

    def test_step1(self, make_bad_arx):
        # test1
        result = ssh_checkout_negative("0.0.0.0", "ma", "7", "cd {}; 7z e bed_arx.7z -o{} -y".format(data["folder_out"],

                                                                                                     ["folder_ext"]),
                                       "ERRORS")
        assert result, "test1 Fail"

    def test_step2(self):
        # test2
        assert ssh_checkout_negative("0.0.0.0", "ma", "7", "cd {}; 7z t bed_arx.7z".format(data["folder_out"]),
                                     "ERRORS"), "test2 fail"
