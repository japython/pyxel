#%%
with open("test.txt", "w") as f:
    f.write("Hello, world!")
#%%
with open("test.txt", "a") as f:
    f.write("This is an appended line.")


#%%
def rr(text, target_char):
    updated_text = text.replace(target_char, f"\n{target_char}")
    return updated_text



with open("test.txt", "r") as f:
    content = f.read()

    content = rr(content, "T")

  



# %%
