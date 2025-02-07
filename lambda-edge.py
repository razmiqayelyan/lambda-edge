import base64

USERNAME = "admin"
PASSWORD = "adminadmin"

def lambda_handler(event, context):
    # Debugging: Print event
    print("Event received:", event)

    # Ensure 'Records' key exists
    if "Records" not in event or len(event["Records"]) == 0:
        return {
            "status": "400",
            "statusDescription": "Bad Request",
            "body": "Invalid event structure"
        }

    try:
        request = event["Records"][0]["cf"]["request"]
        headers = request.get("headers", {})

        # Authentication logic
        auth_user_password = f"{USERNAME}:{PASSWORD}".encode("ascii")
        auth_token = base64.b64encode(auth_user_password).decode()
        auth_string = f"Basic {auth_token}"

        if "authorization" not in headers or headers["authorization"][0]["value"] != auth_string:
            return {
                "status": "401",
                "statusDescription": "Unauthorized",
                "body": "Unauthorized",
                "headers": {
                    "www-authenticate": [{"key": "WWW-Authenticate", "value": "Basic"}]
                }
            }

        return request
    except Exception as e:
        print("Error:", str(e))
        return {
            "status": "500",
            "statusDescription": "Internal Server Error",
            "body": "An error occurred"
        }
