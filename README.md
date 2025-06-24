# Lyto
Automatic wireless ADB connection using QR codes.

![](https://i.imgur.com/CWVahuZ.png)

> [!NOTE]
> Minimum Android version: 11

## Installation
#### First Method
```
pip install git+https://github.com/eeriemyxi/lyto@main
```

#### Second Method
```
git clone --depth 1 --branch main https://github.com/eeriemyxi/lyto
pip install ./lyto
```

## Command-line Arguments
```
usage: lyto [-h] [--adb-path ADB_PATH] [--tcpip-port TCPIP_PORT]
                   [--use-port USE_PORT] [--qr-scale QR_SCALE]
                   [--qr-border QR_BORDER] [--debug] [--as-sixel]
                   [--only-connect] [--do-tcpip] [--connect-tcpip] [-V]

options:
  -h, --help            show this help message and exit
  --adb-path ADB_PATH   Path to `adb` platform-tool. Defaults to 'adb'.
  --tcpip-port TCPIP_PORT
                        Port for doing `adb tcpip`. See `--do-tcpip` flag.
                        Defaults to 5555.
  --use-port USE_PORT   Specify port for doing `adb pair` and `adb connect`
                        instead of auto-detecting it. Defaults to 0.
  --qr-scale QR_SCALE   (SIXEL ONLY) QR code image scale. Defaults to 10.
  --qr-border QR_BORDER
                        QR code border size. Defaults to 1.
  --debug               Enable debug logs.
  --as-sixel            (EXPERIMENTAL) Use Sixel graphics.
  --only-connect        Only connect to the device, don't pair.
  --do-tcpip            After connecting do `adb tcpip` on specified port.
  --connect-tcpip       Detects device IP on startup and tries to connect to it
                        with TCPIP_PORT as the port.
  -V, --version         Show package version.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
