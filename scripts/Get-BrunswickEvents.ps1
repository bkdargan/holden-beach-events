Write-Host "Inspect Brunswick Events"

$page = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

$content = $page.Content

$content |
    Select-String -Pattern "/event/" -Context 0,1 |
    Select-Object -First 20
