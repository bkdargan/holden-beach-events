Write-Host "Google Calendar Integration Test"

if (-not (Test-Path "events.json")) {
    Write-Host "events.json not found"
    exit 1
}

$events = Get-Content events.json | ConvertFrom-Json

Write-Host ""
Write-Host "Events Loaded:"
Write-Host ($events.Count)

Write-Host ""

foreach ($event in $events)
{
    Write-Host "===================="
    Write-Host "TITLE:"
    Write-Host $event.title

    Write-Host "DATE:"
    Write-Host $event.date

    Write-Host "TIME:"
    Write-Host $event.time

    Write-Host "URL:"
    Write-Host $event.url

    Write-Host ""
}
