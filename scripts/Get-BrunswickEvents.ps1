Write-Host "Inspect Brunswick Events Page"

$page = Invoke-WebRequest -Uri "https://www.ncbrunswick.com/events/"

$content = $page.Content

$position = $content.IndexOf("/event/")

Write-Host ""
Write-Host "First /event/ occurrence:"
Write-Host $position

Write-Host ""

if ($position -gt 0)
{
    $start = :Max(0, $position - 500)
    $length = :Min(2000, $content.Length - $start)

    $snippet = $content.Substring($start, $length)

    Write-Host $snippet
}
else
{
    Write-Host "No /event/ links found"
}
