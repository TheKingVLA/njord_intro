import sys

from ouster.sdk import open_source


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <sensor-ip>")
        raise SystemExit(1)

    hostname = sys.argv[1]

    print(f"Opening Ouster stream from {hostname}...")

    source = open_source(
        hostname,
        sensor_idx=0,
    )

    try:
        print("Sensor info:")
        print(source.sensor_info[0])

        print("\nWaiting for lidar frames...")

        for i, frame_set in enumerate(source):
            frame = frame_set[0]

            if frame is None:
                continue

            print(
                f"frame={i:04d} "
                f"frame_id={frame.frame_id}"
            )

            if i >= 9:
                break

    finally:
        source.close()


if __name__ == "__main__":
    main()