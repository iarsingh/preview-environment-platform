class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if int(body.get("pr") or 0) < 1: failed.append("pr")\n    if body.get("branch") in {{"main", "master"}}: failed.append("protected_branch")
    return {"passed": not failed, "failed": failed, "applied": False}
