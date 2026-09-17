Write-Host "Starting Brunswick County event collection..."

$url = "https://www.ncbrunswick.com/events/"

$response = Invoke-WebRequest -Uri $url

Write-Host "Page downloaded successfully"
Write-Host ""

$content = $response.Content

$content |
    Select-String `
    -Pattern "api|json|events|event" `
    -AllMatches

Write-Host "Search Complete"
