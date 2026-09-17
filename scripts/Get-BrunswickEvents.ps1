Write-Host "Starting Brunswick County event collection..."

$url = "https://www.ncbrunswick.com/events/"

$response = Invoke-WebRequest -Uri $url

Write-Host "Page downloaded successfully"
Write-Host ""

$regex = 'https?:\/\/[^"\''\s<>]+'

$matches = :Matches($response.Content, $regex)

$matches |
    Select-Object -First 100 |
    ForEach-Object {
        Write-Host $_.Value
    }
