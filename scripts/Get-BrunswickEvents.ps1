Write-Host "Brunswick Event Collection"

$urls = @(
    "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/",
    "https://www.ncbrunswick.com/event/southport-fall-market/2543/",
    "https://www.ncbrunswick.com/event/live-%26-local%3a-music-%2b-market/2348/"
)

foreach ($url in $urls)
{
    $response = Invoke-WebRequest -Uri $url

    $content = $response.Content

    $titleLine = ($content -split "`n") |
        Where-Object { $_ -match "<title>" } |
        Select-Object -First 1

    $title = $titleLine `
        -replace "<title>", "" `
        -replace "</title>", ""

    Write-Host ""
    Write-Host "======================="
    Write-Host "TITLE: $title"
    Write-Host "URL: $url"
}
