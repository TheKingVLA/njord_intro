import sys

from ouster.sdk import sensor


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <sensor-ip>")
        raise SystemExit(1)

    hostname = sys.argv[1]

    print(f"Connecting to Ouster sensor at {hostname}...")

    config = sensor.get_config(hostname)

    print("\nSensor configuration:")
    print(config)


if __name__ == "__main__":
    main()