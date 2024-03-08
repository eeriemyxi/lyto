# Lyto
Automatic wireless ADB connection using QR codes.

![](https://i.imgur.com/CWVahuZ.png)

### Note
Minimum Android version: 11

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
usage: lyto [-h] [--adb-path ADB_PATH] [--qr-scale QR_SCALE]
            [--qr-border QR_BORDER] [--debug]

options:
  -h, --help            show this help message and exit
  --adb-path ADB_PATH   Path to `adb` platform-tool. Defaults to 'adb'.
  --qr-scale QR_SCALE   QR code image scale. Defaults to 10.
  --qr-border QR_BORDER
                        QR code border size. Defaults to 1.
  --debug               Enable debug logs.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

* * *

Feel free to enhance Lyto according to your needs and contribute back to the project! If you encounter any issues or have suggestions for improvement, please open an issue on the repository. Thank you for using Lyto!
