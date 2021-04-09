import requests
import json

url = "http://192.168.0.62/occm/api/gcp/vsa/working-environments"

payload = json.dumps({
  "name": "gcpcvo1",
  "volume": {
    "exportPolicyInfo": {
      "policyType": "custom",
      "ips": [
        "10.150.0.0/20"
      ],
      "nfsVersion": [
        "nfs3",
        "nfs4"
      ]
    },
    "snapshotPolicyName": "default",
    "name": "gcpcvo_nfsvol",
    "enableThinProvisioning": True,
    "enableDeduplication": True,
    "enableCompression": True,
    "size": {
      "size": 5,
      "unit": "GB"
    }
  },
  "tenantId": "workspace-aLo6Lml6",
  "region": "us-east4-a",
  "packageName": "gcp_poc",
  "dataEncryptionType": "GCP",
  "gcpServiceAccount": "occmservice@occm-dev.iam.gserviceaccount.com",
  "vsaMetadata": {
    "ontapVersion": "ONTAP-9.9.0.T1.gcp",
    "licenseType": "gcp-cot-explore-paygo",
    "instanceType": "custom-4-16384"
  },
  "writingSpeedState": "NORMAL",
  "subnetPath": "https://www.googleapis.com/compute/v1/projects/default-project/regions/us-east4/subnetworks/default",
  "subnetId": "https://www.googleapis.com/compute/v1/projects/default-project/regions/us-east4/subnetworks/default",
  "svmPassword": "Netapp1!",
  "vpcId": "default",
  "gcpVolumeSize": {
    "size": 500,
    "unit": "GB",
    "_identifier": "500 GB"
  },
  "gcpVolumeType": "pd-ssd",
  "gcpLabels": [],
  "project": "default-project",
  "backupVolumesToCbs": True,
  "enableCompliance": False
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=node06vylw0q2p68c1dmya34twtn1r229.node0; rememberMe=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'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
