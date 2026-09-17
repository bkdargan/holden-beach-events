Write-Host "Brunswick Event Structured Data Test"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$content = $response.Content

$content |
    Select-String `
    -Pattern '"name":"|Town Center Park|addressLocality|postalCode' `
    -AllMatches
