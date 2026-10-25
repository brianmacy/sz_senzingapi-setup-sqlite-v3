#! /usr/bin/env python3

import subprocess
import sys

try:
  result = subprocess.run(['sqlite3', '/app/template.db', '.read g2core-schema-sqlite-create.sql'],  capture_output=True, text=True, check=True)
  print(result.stdout)
  print(result.stderr, file=sys.stderr)

except subprocess.CalledProcessError as err:
  print(err.stdout)
  print(err.stderr, file=sys.stderr)
  print('Running sqlite to create the DB failed', file=sys.stderr)
  sys.exit(-1)
except OSError as err:
  print(err, file=sys.stderr)
  sys.exit(-1)
