

#!/bin/bash

FILE="task_4.sql"

echo "=== Checking task_4.sql for forbidden keywords ==="
if grep -Ei "\bDESCRIBE\b|\bEXPLAIN\b" "$FILE"; then
  echo "❌ Fail: task_4.sql contains forbidden keyword(s)"
  exit 1
else
  echo "✅ Success: No forbidden keyword found in task_4.sql"
fi
