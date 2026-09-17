Write-Host "Brunswick Event Import Test"

$urls = @(
    "https://www.ncbrunswick.com/event/ocean-isle-beach-summer-concert-series/2087/",
    "https://www.ncbrunswick.com/event/southport-fall-market/2543/",
    "https://www.ncbrunswick.com/event/live-%26-local%3a-music-%2b-market/2348/"
)

foreach ($url in $urls) {

    Write-Host ""
    Write-Host "Checking:"
    Write-Host $url

    try {
        $response = Invoke-WebRequest -Uri $url

        Write-Host "SUCCESS"
        Write-Host "Length: $($response.Content.Length)"
    }
    catch {
        Write-Host "FAILED"
        Write-Host $_
    }
}
