Write-Host "Brunswick Event Extractor"

$url = "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/"

$response = Invoke-WebRequest -Uri $url

$content = $response.Content

$lines = $content -split "`n"

foreach ($line in $lines) {

    if ($line -like "*<title>*") {
        Write-Host ""
        Write-Host "TITLE:"
        Write-Host $line
    }

    if ($line -like '*meta name="description"*') {
        Write-Host ""
        Write-Host "DESCRIPTION:"
        Write-Host $line
    }
}
