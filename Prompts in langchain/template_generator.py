from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
    template="Explain the paper '{paper}' in a {style} style and {length} length. include all the relevant content  and also use the relateble anologies to simplyfy the complex ideas. make sure to cover all the important points and provide a comprehensive understanding of the paper.",
    input_variables=["paper", "style", "length"]
)
template.save('template.json')
