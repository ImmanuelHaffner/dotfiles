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

# libc++ pretty printers
# See: https://github.com/koutheir/libcxx-pretty-printers
python
import os
import sys
home_dir = os.path.expanduser('~')
pretty_printers_dir = f'{home_dir}/Documents/libcxx-pretty-printers/src'
if os.path.exists(pretty_printers_dir):
    sys.path.insert(0, pretty_printers_dir)
    from libcxx.v1.printers import register_libcxx_printers
    register_libcxx_printers(None)
end
