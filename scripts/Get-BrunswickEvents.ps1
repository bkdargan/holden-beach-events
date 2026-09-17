Write-Host "Brunswick Event Parser Test"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$content = $response.Content

$titleLine = $content |
    Select-String "<title>"

Write-Host ""
Write-Host "TITLE LINE:"
Write-Host $titleLine
