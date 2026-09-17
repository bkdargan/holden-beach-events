Write-Host "Testing Brunswick Events Page"

$listingPage = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

Write-Host ""
Write-Host "Page downloaded successfully"
Write-Host ""

$content = $listingPage.Content

if ($content -match "/event/")
{
    Write-Host "FOUND EVENT LINKS"
}
else
{
    Write-Host "NO EVENT LINKS FOUND"
}

Write-Host ""
Write-Host "Page Length:"
Write-Host $content.Length
