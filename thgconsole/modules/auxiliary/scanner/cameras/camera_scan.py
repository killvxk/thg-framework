from thg.modules.scanners.autopwn import Exploit


class Exploit(Exploit):
    __info__ = {
        "name": "Camera Scanner",
        "description": "Module that scans for cameras vulnerablities and weaknesses.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
        "devices": (
            "Cameras",
        ),
    }

    modules = ["generic", "cameras"]
