import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path, 'r') as from_file:
        markdown_content = from_file.read()

    with open(template_path, 'r') as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, 'w') as to_file:
        to_file.write(template)


def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    for filename in os.listdir(content_dir_path):
        content_path = os.path.join(content_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, dest_path.replace(".md", ".html"))
        else:
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path)

