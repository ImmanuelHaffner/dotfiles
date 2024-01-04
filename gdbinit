set history save on
set history size 10000
set history remove-duplicates 100
set history filename ~/.gdb_history

set debuginfod enabled on

set print array on
set print elements 0
set print null-stop on
set print object on
set print pretty on

# No autoloading so that gdb does not pick up the default printers for libstdcxx.
# They match libcxx, but don't work on it.
set auto-load no
set debug auto-load on
source /home/immanuel/Documents/llvm-project/libcxx/utils/gdb/libcxx/printers.py
python register_libcxx_printer_loader()
