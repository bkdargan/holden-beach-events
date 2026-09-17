Write-Host "Brunswick Event Object"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

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
Write-Host "EVENT RECORD"
Write-Host "======================="
Write-Host ""
Write-Host "TITLE:"
Write-Host $title
Write-Host ""
Write-Host "URL:"
Write-Host $url
