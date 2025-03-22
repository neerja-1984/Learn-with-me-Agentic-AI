from smolagents import CodeAgent, TransformersModel, load_tool 
model_id = "tabularisai/multilingual-sentiment-analysis"

# CodeAgent
model = TransformersModel(model_id=model_id)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

# agent.run(
#     "return me the answer to the question: What is the result of 2 power 3.743?",
# )

agent.run(
    "Figure out the sentiment of the statememnt -> [ I love to dig people out of grave !! ]",
)

# # using default tools [ ToolCallingAgent defauls]
# search_tool = load_tool("web_search")
# print(search_tool("Who's the current president of Russia?"))

# text_to_speech_tool = load_tool("text_to_speech")
# print(text_to_speech_tool("Hello, world ... bonjour!?"))

# # image_question_answering_tool = load_tool("image_question_answering")
# # print(image_question_answering_tool("Who's the current president of Russia?"))

# translation_tool = load_tool("translation")
# print(translation_tool(text="I love this AI agents .. what about it ( eye wink !)", target_language="fr"))
