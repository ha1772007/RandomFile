<?php
// Set maximum execution time to 300 seconds (5 minutes)
set_time_limit(300);

// Define the output directory
$outputDirectory = 'download';

// Create the output directory if it doesn't exist
if (!is_dir($outputDirectory)) {
    mkdir($outputDirectory, 0777, true);
}

// Generate 100 random files
for ($i = 1; $i <= 100; $i++) {
    // Generate a random file size between 5GB and 5.1GB (in bytes)
    $fileSize = rand(5 * 1024 * 1024 * 1024, 5.1 * 1024 * 1024 * 1024);

    // Create the file path
    $filePath = $outputDirectory . '/' . $i . '.txt';

    // Open the file for writing
    $fileHandle = fopen($filePath, 'w');

    // Generate and write chunks of content (1MB at a time)
    $chunkSize = 1024 * 1024; // 1MB
    $remainingSize = $fileSize;
    while ($remainingSize > 0) {
        $chunk = bin2hex(random_bytes(min($chunkSize, $remainingSize)));
        fwrite($fileHandle, hex2bin($chunk));
        $remainingSize -= $chunkSize;
    }

    // Close the file
    fclose($fileHandle);

    echo "Generated file $filePath\n";
}

echo "All 100 files have been generated successfully.\n";
?>
