import yaml
import markdown
import jinja2
from dataclasses import dataclass

@dataclass
class Post:
    title: str
    sample: str
    file: str
    date: str
    out: str

    @staticmethod
    def build(d):
        filename = d["file"].split(".")[0] + ".html"
        return Post(title=d["title"], sample=d["sample"], 
                    file=d["file"], date=d["date"], out=filename)

    def render(self):
        with open(self.file) as f:
            return markdown.markdown(f.read(), extensions=["fenced_code", "codehilite"])

if __name__ == "__main__":
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates"),
        autoescape=jinja2.select_autoescape()
    )

    with open("posts.yaml") as f:
        posts = [Post.build(d["post"]) for d in yaml.load(f, Loader=yaml.FullLoader)]

    template = env.get_template("post_list_template.html")
    html = template.render(posts=posts)
    with open("../../posts.html", "w") as f:
        f.write(html)

    for post in posts:
        template = env.get_template("post_template.html")
        html = template.render(content=post.render())
        with open(f"../../posts/{post.out}", "w") as f:
            f.write(html)
