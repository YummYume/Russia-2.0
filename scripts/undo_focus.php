<?php

if (!function_exists('str_contains')) {
    function str_contains(string $haystack, string $needle): bool
    {
        return '' === $needle || false !== strpos($haystack, $needle);
    }
}

$file = fopen('soviet.txt', 'r');
$newFile = '';
$curlyBracesOpen = 0;
$curlyBracesClose = 0;
$removeCommands = [
    'available',
    'completion_reward',
    'complete_tooltip',
    'allow_branch',
    'search_filters',
    'bypass',
    'ai_will_do',
];

while(!feof($file)) {
    $line = fgets($file);

    if ($curlyBracesOpen > $curlyBracesClose) {
        $curlyBracesOpen += substr_count($line, '{');
        $curlyBracesClose += substr_count($line, '}');
    } else {
        $contains = false;
        foreach ($removeCommands as $removeCommand) {
            if (str_contains($line, $removeCommand)) {
                $contains = true;
                break;
            }
        }
        if ($contains) {
            $curlyBracesOpen += substr_count($line, '{');
            $curlyBracesClose += substr_count($line, '}');
        } else {
            $newFile .= $line;
        }
    }
}

fclose($file);

$file = fopen('soviet_output.txt', 'w');
fwrite($file, $newFile);
fclose($file);
