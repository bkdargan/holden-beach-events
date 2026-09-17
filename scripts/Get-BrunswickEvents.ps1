Write-Host "Creating Event JSON"

$events = @()

# Download Brunswick County event page
$listingPage = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

# Extract event URLs
$urlPattern = 'https://www\.ncbrunswick\.com/event/[^"]+'

$urls = :Matches($listingPage.Content, $urlPattern) |
    ForEach-Object { $_.Value } |
    Sort-Object -Unique

Write-Host "Found $($urls.Count) event URLs"

foreach ($url in $urls)
{
    try
    {
        Write-Host "Processing: $url"

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

        $dateMatch = ""

        if ($description -match "(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}")
        {
            $dateMatch = $matches[0]
        }

        $timeMatch = ""

        if ($description -match "\d{1,2}:\d{2}\s*(a\.m\.|p\.m\.)")
        {
            $timeMatch = $matches[0]
        }

        $events += @{
            title = $title.Trim()
            date = $dateMatch
            time = $timeMatch
            description = $description.Trim()
            url = $url
        }
    }
    catch
    {
        Write-Host "Failed: $url"
    }
}

$events |
    ConvertTo-Json -Depth 5 |
    Out-File events.json

Write-Host ""
Write-Host "Created events.json"
Write-Host "Total Events: $($events.Count)"
