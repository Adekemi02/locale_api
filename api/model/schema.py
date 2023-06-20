


userSchema = {
    "name": {
        "type": "string",
        "required": True,
        "maxlength": 40
    },
    "email": {
        "type": "string",
        "required": True,
        "maxlength": 25
    },
    "password": {
        "type": "string",
        "required": True,
        "minlength": 6,
        "maxlength": 1024
    }
}
