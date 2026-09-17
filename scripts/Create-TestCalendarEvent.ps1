Write-Host "Creating Calendar Event Payload"

$event = @{
    summary = "Holden Beach Automation Test"
    location = "Holden Beach, NC"
    description = "Created automatically by GitHub Actions"
}

$event | ConvertTo-Json | Out-File test-event.json

Write-Host "Created test-event.json"
