Write-Host "Starting Brunswick County event collection..."

$url = "https://www.ncbrunswick.com/events/"

try {
    $response = Invoke-WebRequest -Uri $url

    Write-Host "Page downloaded successfully"
    Write-Host ""
    Write-Host "Page Title:"
    Write-Host $response.ParsedHtml.title

    Write-Host ""
    Write-Host "Downloaded Content Length:"
    Write-Host $response.Content.Length
}
catch {
    Write-Host "ERROR:"
    Write-Host $_
}
