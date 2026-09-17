Write-Host "Creating Calendar Event Payload"

$event = @{
    summary = "Holden Beach Automation Test"
    description = "Created automatically by GitHub Actions"
    location = "Holden Beach, NC"
}

$event | ConvertTo-Json | Out-File test-event.json

Write-Host ""
Write-Host "Created test-event.json"

Write-Host ""
Get-Content test
