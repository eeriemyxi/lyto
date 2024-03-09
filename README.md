# Lyto
Automatic wireless ADB connection using QR codes.

![](https://i.imgur.com/CWVahuZ.png)

### Note
Minimum Android version: 11

Your terminal must support [Sixel](https://en.wikipedia.org/wiki/Sixel) graphics. Non-sixel QR code support is in the TODO list.

## Installation
#### First Method
```
git clone --depth 1 --branch main <REPO URL> lyto
pip install ./lyto
```
#### Second Method
```
pip install git+<REPO URL>@main
```

## Command-line Arguments
```
usage: __main__.py [-h] [--adb-path ADB_PATH] [--tcpip-port TCPIP_PORT]
                   [--use-port USE_PORT] [--qr-scale QR_SCALE]
                   [--qr-border QR_BORDER] [--debug] [--only-connect]
                   [--do-tcpip] [--connect-tcpip]

options:
  -h, --help            show this help message and exit
  --adb-path ADB_PATH   Path to `adb` platform-tool. Defaults to 'adb'.
  --tcpip-port TCPIP_PORT
                        Port for doing `adb tcpip`. See `--do-tcpip` flag.
                        Defaults to 5555.
  --use-port USE_PORT   Specify port for doing `adb pair` and `adb connect`
                        instead of auto-detecting it. Defaults to 0.
  --qr-scale QR_SCALE   QR code image scale. Defaults to 10.
  --qr-border QR_BORDER
                        QR code border size. Defaults to 1.
  --debug               Enable debug logs.
  --only-connect        Only connect to the device, don't pair.
  --do-tcpip            After connecting do `adb tcpip` on specified port.
  --connect-tcpip       Detects device IP on startup and tries to connect to it
                        with TCPIP_PORT as the port.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

* * *

Feel free to enhance Lyto according to your needs and contribute back to the project! If you encounter any issues or have suggestions for improvement, please open an issue on the repository. Thank you for using Lyto!
