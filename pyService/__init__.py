import argparse
import zmq
from daemonize import Daemonize
from os import path


NAME = 'pyService'

def daemon(args):
    print "Daemon"
    def main():
        print "Running Main"
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind('tcp://127.0.0.1:5555')
        while True:
            msg = socket.recv()
            socket.send("Hello World!")

    # Actually Daemonize
    if args.foreground:
        main()
    else:
        daemon = Daemonize(app="test_app", pid=args.pidfile, action=main)
        daemon.start()


def communicate(args):
    print "Comminication"
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://127.0.0.1:5555')
    socket.send(args.bar)
    msg = socket.recv()
    print msg


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example ZeroMQ based python Service.")
    subparsers = parser.add_subparsers()
    
    # ArgumentParser for the cmd
    cmd_parser = subparsers.add_parser("talk", help="Talk to the daemon process")
    cmd_parser.set_defaults(func=communicate)
    cmd_parser.add_argument('--bar', default="")
    
    
    # ArgumentParser for the daemon.
    daemon_parser = subparsers.add_parser("daemon", help="Run the Daemon process")
    daemon_parser.set_defaults(func=daemon)
    daemon_parser.add_argument('-f', '--foreground', action='store_true', help="Stay in foreground")
    daemon_parser.add_argument('--pidfile', action="store", help="Specify a pidfile", default=path.join("/var/run/", NAME))
    
    args = parser.parse_args()
    args.func(args)