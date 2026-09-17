Write-Host "Starting Brunswick County event collection..."

$url = "https://www.ncbrunswick.com/events/"

$response = Invoke-WebRequest -Uri $url

Write-Host "Page downloaded successfully"
Write-Host ""

$content = $response.Content

$patterns = @(
    "Sunset Beach Market",
    "Southport Fall Market",
    "Ocean Isle Beach Summer Concert Series"
)

foreach ($pattern in $patterns) {

    if ($content.Contains($pattern)) {
        Write-Host "FOUND: $pattern"
    }
    else {
        Write-Host "NOT FOUND: $pattern"
    }
}
