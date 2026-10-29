"""A tiny, read-only FTP server for local testing (requires pyftpdlib)."""

import argparse
from pathlib import Path

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
	parser = argparse.ArgumentParser(description="Run a local read-only FTP server")
	parser.add_argument("username")
	parser.add_argument("password")
	parser.add_argument("--directory", default=".")
	args = parser.parse_args()

	authorizer = DummyAuthorizer()
	authorizer.add_user(args.username, args.password, str(Path(args.directory).resolve()), perm="elr")

	handler = FTPHandler
	handler.authorizer = authorizer
	FTPServer(("127.0.0.1", 2121), handler).serve_forever()


if __name__ == "__main__":
	main()
