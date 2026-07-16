def parse_spaghetti_data(payload, strict_mode=False):
    status = "unknown"
    if payload is not None:
        if type(payload) == dict:
            if "user" in payload:
                user = payload["user"]
                if "age" in user:
                    if user["age"] >= 18:
                        if "role" in user:
                            if user["role"] == "admin":
                                status = "super_admin_access"
                            elif user["role"] == "editor":
                                status = "editor_access"
                            elif user["role"] == "viewer":
                                status = "viewer_access"
                            else:
                                status = "guest_access"
                        else:
                            status = "guest_access"
                    else:
                        if strict_mode:
                            status = "access_denied"
                        else:
                            status = "restricted_access"
                else:
                    status = "invalid_user_data"
            elif "system" in payload:
                if payload["system"] == "active":
                    status = "system_online"
                elif payload["system"] == "maintenance":
                    status = "system_offline"
                else:
                    status = "system_error"
            else:
                status = "empty_payload"
        elif type(payload) == list:
            if len(payload) > 10:
                status = "list_too_large"
            elif len(payload) == 0:
                status = "list_empty"
            else:
                status = "list_ok"
                for i in range(len(payload)):
                    if payload[i] == "error":
                        status = "list_contains_errors"
                        break
    else:
        if strict_mode:
            raise ValueError("Payload cannot be None in strict mode")
        status = "no_data"
    
    return status
