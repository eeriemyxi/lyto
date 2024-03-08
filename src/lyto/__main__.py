import argparse
import io
import logging
import random
import string
import subprocess
import time
from os import _exit

import qrcode
import sixel
from rich.logging import RichHandler
from zeroconf import IPVersion, ServiceBrowser, ServiceStateChange, Zeroconf


def get_code(n: int):
    return "".join(random.choices(string.ascii_letters, k=n))


SIZE      = 5
NAME      = "ADB_WIFI_" + get_code(SIZE)
PASSWORD  = get_code(SIZE)
TYPES     = ["_adb-tls-connect._tcp.local.", "_adb-tls-pairing._tcp.local."]
ADB_PATH  = "adb"
QR_SCALE  = 10
QR_BORDER = 1

parser = argparse.ArgumentParser()
parser.add_argument(
    "--adb-path",
    default=ADB_PATH,
    help=f"Path to `adb` platform-tool. Defaults to {repr(ADB_PATH)}.",
)
parser.add_argument(
    "--qr-scale",
    default=QR_SCALE,
    type=int,
    help=f"QR code image scale. Defaults to {repr(QR_SCALE)}.",
)
parser.add_argument(
    "--qr-border",
    default=QR_BORDER,
    type=int,
    help=f"QR code border size. Defaults to {repr(QR_BORDER)}.",
)
parser.add_argument("--debug", action="store_true", help="Enable debug logs.")
args = parser.parse_args()

ADB_PATH  = args.adb_path
QR_SCALE  = args.qr_scale
QR_BORDER = args.qr_border

logging.basicConfig(
    level=logging.DEBUG if args.debug else logging.INFO,
1   format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(markup=True)],
)

log = logging.getLogger(__name__)
device_ports = []

log.debug(f"{NAME=}")
log.debug(f"{PASSWORD=}")


def generate_code(name: str, password: str):
    return f"WIFI:T:ADB;S:{name};P:{password};;"


def ascii_qr_code(text: str):
    file = io.BytesIO()

    qr = qrcode.QRCode(border=QR_BORDER, box_size=QR_SCALE, version=1)
    qr.add_data(text)
    img = qr.make_image(back_color="white", fill_color="black")
    img.save(file)

    # TODO: support for terminals without sixel
    writer = sixel.converter.SixelConverter(file, alpha_threshold=2)

    return writer.getvalue()


def _debug_info_pc(out: subprocess.CompletedProcess):
    log.debug(f"{out.stderr=}")
    log.debug(f"{out.stdout=}")


def pair_device(address: str, port: int, password: str):
    log.info("[italic yellow]Pairing...[/]")
    args = [ADB_PATH, "pair", f"{address}:{port}", password]
    log.debug("Args for pairing command: %s", args)
    out = subprocess.run(args, capture_output=True)

    if out.returncode != 0:
        log.critical("[red bold]Pairing failed.[/]")
        _debug_info_pc(out)
        return

    log.info("[bold green]Paired[/].")


def connect_device(address: str, port: int):
    log.info("[italic yellow]Connecting...[/]")
    args = [ADB_PATH, "connect", f"{address}:{port}"]
    log.debug("Args for connecting command: %s", args)
    out = subprocess.run(args, capture_output=True)

    if out.returncode != 0:
        log.critical("[red bold]Connecting failed.[/]")
        _debug_info_pc(out)
        return

    log.info("[bold green]Connected[/].")
    log.info("[italic yellow]Exiting...[/]")

    _exit(0)


def on_service_state_change(
    zeroconf: Zeroconf,
    service_type: str,
    name: str,
    state_change: ServiceStateChange,
) -> None:
    log.debug("Running on_service_state_change listener.")
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        log.debug(f"{info=}")
        if not info:
            return

        log.debug(f"{device_ports}")
        log.debug(f"{info.type=}")
        log.debug(f"{info.port=}")
        log.debug(f"{info.parsed_addresses()=}")

        if service_type == "_adb-tls-pairing._tcp.local.":
            if not device_ports:
                return
            pair_device(info.parsed_addresses()[0], info.port or 5555, PASSWORD)
            connect_device(info.parsed_addresses()[0], device_ports[0])
        elif service_type == "_adb-tls-connect._tcp.local.":
            device_ports.append(info.port)


def main() -> int:
    # TODO: align it to the center
    print(ascii_qr_code(generate_code(NAME, PASSWORD)))

    zc = Zeroconf(ip_version=IPVersion.V4Only)

    ServiceBrowser(
        zc=zc,
        type_=TYPES,
        handlers=[on_service_state_change],
    )

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        zc.close()
        return 0


if __name__ == "__main__":
    exit(main())
