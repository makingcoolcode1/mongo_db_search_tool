
def format_mongo(document, prefix = ""):
    formatted = ""

    for key, value in document.items():
        new_prefix = f"{key}.{prefix}" if key else prefix

        if isinstance(value, dict):
            formatted += (value, new_prefix)
        elif isinstance(value, list):
            formatted += f"{new_prefix}\n"

            for item in value:
                if isinstance(item, list):
                    formatted += (item, new_prefix)
                else:
                    formatted += f"       {item}\n\n"
        
        else:
            formatted += f"{new_prefix}:{value}\n"
    
    return formatted