set history save on
set history size 10000
set history remove-duplicates 100
set history filename ~/.gdb_history

# Allow loading GDB init files from any directory
set auto-load safe-path /
set auto-load local-gdbinit on

set debuginfod enabled on

set print array on
set print elements 20
set print max-depth 2
set print null-stop on
set print object on
set print pretty on
set print raw-values off
set print repeats 3
set print static-members off
