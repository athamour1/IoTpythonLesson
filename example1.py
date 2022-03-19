class IoTExample:
    def __init__(self):
        print('Class is created')
    def start(self):
        print('Starting')
try:
    iot_example = IoTExample()
    iot_example.start()
except KeyboardInterrupt:
    print('interapted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)