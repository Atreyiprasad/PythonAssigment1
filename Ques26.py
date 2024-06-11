def starts_with_prefix(string, prefix):
    return string.startswith(prefix)

def ends_with_suffix(string, suffix):
    return string.endswith(suffix)


text = "Hello, World!"
prefix = "Hello"
suffix = "World!"
print(f"The text starts with prefix '{prefix}': {starts_with_prefix(text, prefix)}")
print(f"The text ends with suffix '{suffix}': {ends_with_suffix(text, suffix)}")
