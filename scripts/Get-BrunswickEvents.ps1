Write-Host "Finding Brunswick Event URLs"

$listingPage = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

$content = $listingPage.Content

$lines = $content -split "`n"

$count = 0

foreach ($line in $lines)
{
    if ($line -like "*https://www.ncbrunswick.com/event/*")
    {
        Write-Host $line

        $count++

        if ($count -ge 10)
        {
            break
        }
    }
}

Write-Host ""
Write-Host "Done"
