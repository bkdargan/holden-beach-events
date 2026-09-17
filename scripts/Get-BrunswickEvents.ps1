Write-Host "Inspecting Brunswick Events HTML"

$listingPage = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

$content = $listingPage.Content

$content |
    Select-String `
    -Pattern "/event/" `
    -Context 0,2
