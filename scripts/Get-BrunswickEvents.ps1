Write-Host "Creating Event JSON"

$events = @()

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

    $descLine = ($content -split "`n") |
        Where-Object { $_ -match 'meta name="description"' } |
        Select-Object -First 1

    $description = $descLine `
        -replace '.*content="', '' `
        -replace '" */?>', ''

    $events += @{
        title = $title.Trim()
        description = $description.Trim()
        url = $url
    }
}

$events | ConvertTo-Json -Depth 3 | Out-File events.json

Write-Host "Created events.json"
