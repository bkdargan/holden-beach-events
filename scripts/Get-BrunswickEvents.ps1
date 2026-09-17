Write-Host "Brunswick Event Parser Test"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$titleMatch = :Match(
    $response.Content,
    '<title>(.*?)</title>'
)

Write-Host ""
Write-Host "TITLE FOUND:"
Write-Host $titleMatch.Groups[1].Value
`
