from conans import ConanFile


class FindWindowsSigntool(ConanFile):
    name = "find_sdk_winxp"
    version = "1.0"
    license = "MIT"
    url = "https://github.com/odant/conan-find_sdk_winxp"
    description = "Python module for find Microsoft SDK v7.1A"
    settings = {"os": ["Windows"]}
    exports = "*"
    build_policy = "missing"
    
    def package(self):
        self.copy("*.py")
        
    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)
