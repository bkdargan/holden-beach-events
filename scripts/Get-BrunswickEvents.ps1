Write-Host "Finding Event Links"

$listingPage = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

$content = $listingPage.Content

$pattern = '/event/[^"]+'

$matches = :Matches($content, $pattern)

Write-Host "Matches Found: $($matches.Count)"

$urls = @()

foreach ($match in $matches)
{
    $url = "https://www.ncbrunswick.com" + $match.Value

    if ($urls -notcontains $url)
    {
        $urls += $url
    }
}

Write-Host ""
Write-Host "Unique URLs Found: $($urls.Count)"
Write-Host ""

$urls |
    Select-Object -First 20 |
    ForEach-Object { Write-Host $_ }
