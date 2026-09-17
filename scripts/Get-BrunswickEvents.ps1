Write-Host "Brunswick Event Extraction Test"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$content = $response.Content

Write-Host ""
Write-Host "Searching for title..."

$patterns = @(
    "Ocean Isle Beach Summer Concert Series",
    "Town Center Park",
    "September",
    "6:30 PM"
)

foreach ($pattern in $patterns) {

    if ($content.Contains($pattern)) {
        Write-Host "FOUND: $pattern"
    }
    else {
        Write-Host "NOT FOUND: $pattern"
    }
}
