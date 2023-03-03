"""def filter_list(spisok, typer):
    def check_el(elem):
        return isinstance(elem,typer)

    return list(filter(check_el, spisok))

res = filter_list([1,12,421,"привет"],str)
print(res)"""
""""
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0


    def upvote(self):
        self.votes_qty += 1

my_comment = Comment("first comment")
print(my_comment.text)
print(my_comment.votes_qty)
my_comment.upvote()
print(my_comment.votes_qty)"""

"""class Images:
    def __init__(self, res, title, ext):
        self.resolution = res
        self.title = title
        self.extention = ext

    def resize(self, new_res):
        self.resolution = new_res

my_images = Images(1000,"Photo", "beautiful photo")
print(my_images.resolution)
my_images.resize(1200)
print(my_images.resolution)"""

class writer:
    def printer(self):
        print(f"Hello, long ravno {self}")

ceo = writer
ceo.printer("Zakhar")

