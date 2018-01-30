from conans import ConanFile, tools


class TestFindWindowsSigntool(ConanFile):
    settings = {"os": ["Windows"], "arch": ["x86", "x86_64"]}
        
    def test(self):
        with tools.pythonpath(self):
            import find_sdk_winxp
            self.output.info("--------Variable for SDK--------")
            env_winxp = find_sdk_winxp.env_dict(self.settings.arch)
            for key, value in env_winxp.items():
                self.output.info("Key: %s" % key)
                self.output.info("Value: %s" % value)
            self.output.info("--------Append variable--------")
            env_vcvars = {"PATH": "C:\\Path", "LIB": "C:\\Lib", "CL": "/D_define_", "LINK": "/manifest"}
            env = find_sdk_winxp.dict_append(self.settings.arch, env=env_vcvars)
            for key, value in env.items():
                self.output.info("Key: %s" % key)
                self.output.info("Value: %s" % value)
