Write-Host "Brunswick Event Object Test"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$content = $response.Content

$title = ($content | Select-String "<title>").Matches.Value

$description = ($content | Select-String 'meta name="description"').Matches.Value

Write-Host ""
Write-Host "TITLE:"
Write-Host $title

Write-Host ""
Write-Host "DESCRIPTION:"
Write-Host $description
