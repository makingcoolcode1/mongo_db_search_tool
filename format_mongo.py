

def format_mongo(document, prefix = ""):
    formatted = ""

    for key, value in document.items():
        new_prefix = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            formatted += format_mongo(value, new_prefix)
        elif isinstance(value, list):
            formatted += f"{new_prefix}\n"

            for item in document:
                if isinstance(item, dict):
                    formatted += format_mongo(item, new_prefix)
                else:
                    formatted += f"       {value}\n\n"
        else:
            formatted +=f"{new_prefix}:{value}\n"
    
    return formatted