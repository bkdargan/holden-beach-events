Write-Host "Creating calendar event object"

$event = @{
    summary = "Holden Beach Automation Test"
    description = "Created automatically from GitHub Actions"
    location = "Holden Beach, NC"
    date = (Get-Date).AddDays(1).ToString("yyyy-MM-dd")
}

$event | ConvertTo-Json | Out-File test-event.json

Write-Host ""
Write-Host "Created:"
Get-Content test-event.json
