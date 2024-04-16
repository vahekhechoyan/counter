def tag_generator(tag_name):
    return lambda content:f"<{tag_name}>{content}</{tag_name}>"

p_tag=tag_generator("p")
div_tag=tag_generator("div")

print(p_tag("This is chapter."))
print(div_tag("Thid is div."))