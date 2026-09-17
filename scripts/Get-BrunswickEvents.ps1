Write-Host "Brunswick Event Object"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url
$content = $response.Content

$titleLine = ($content -split "`n") | Where-Object {
    $_ -match "<title>"
} | Select-Object -First 1

$descLine = ($content -split "`n") | Where-Object {
    $_ -match 'meta name="description"'
} | Select-Object -First 1

Write-Host ""
Write-Host "======================="
Write-Host "EVENT RECORD"
Write-Host "======================="
Write-Host $titleLine
Write-Host ""
Write-Host $descLine
Write-Host ""
Write-Host "URL:"
Write-Host $url
