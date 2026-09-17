Write-Host "Saving Event Page"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$response.Content | Out-File event-page.html

Write-Host "Event page saved"
Write-Host "Length: $($response.Content.Length)"
