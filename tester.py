from HuggingFaceApi import HuggingFaceApi as hf

tos = """
We have not reviewed, and cannot review, all of the material, including computer software, made available through the websites and webpages to which we, any user, or any provider of Content links, or that link to us. We do not have any control over those websites and webpages, and are not responsible for their contents or their use. By linking to an external website or webpage, we do not represent or imply that we endorse such website or webpage. You are responsible for taking precautions as necessary to protect yourself and your computer systems from viruses, worms, Trojan horses, and other harmful or destructive content. We disclaim any responsibility for any harm resulting from your use of external websites and webpages, whether that link is provided by us or by any provider of Content on the Website.

[Question]:
Does this clause take away any of my rights? Explain.
"""

section = hf.summarizeTOS(tos)
output = hf.expandOnSection({"question": "Does this clause alter my rights in any way?", "context": section})
print(output)