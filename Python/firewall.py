from google.cloud import compute_v1

def list_firewall_rules(project_id: str):
    """
    Lists all firewall rules in the specified GCP project.

    Args:
        project_id: The ID of your GCP project.
    """
    firewall_client = compute_v1.FirewallsClient()
    request = compute_v1.ListFirewallsRequest(project=project_id)

    print(f"Firewall rules in project '{project_id}':")
    for firewall in firewall_client.list(request=request):
        print(f" - {firewall.name}: {firewall.description or 'No description'}")

if __name__ == "__main__":
    # Replace 'your-project-id' with your actual project ID
    project_id = "your-project-id"
    list_firewall_rules(project_id)