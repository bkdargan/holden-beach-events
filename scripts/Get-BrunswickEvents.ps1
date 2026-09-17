Write-Host "Brunswick Event Data Test"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$content = $response.Content

$content |
    Select-String `
    -Pattern "Ocean Isle Beach Summer Concert Series|Town Center Park|September 18|6:30 p.m." `
    -AllMatches
