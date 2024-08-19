from langchain.prompts import ChatPromptTemplate
import os
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.messages import (HumanMessage,SystemMessage)
def generator_script(subject,video_length,
                     creativity,qianfan_ak,qianfan_sk):
    title_prompt_template = ChatPromptTemplate.from_messages(
        [("human" , "请为{subject}这个主题的视频想一个吸引人的标题,另外，多增加一些emoji")]
    )
    script_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "human",
                """
                你是以为短视频频道的博主，根据以下标题和相关信息，为短视频频道写一个视频脚本，
                视频标题{title},视频时长:{duration}分钟,生成的脚本长度尽量遵循视频时长的要求。
                要求开头抓住眼球，中间提供干货，结尾有惊喜，脚本格式也请按照[开头，中间，结尾]分隔。
                整体内容的表达方式要尽量轻松有趣，吸引年轻人。另外，多增加一些emoji
                脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略:
                ```{wikipedia_search}```
                """
            )
        ]
    )
    os.environ['QIANFAN_AK'] = qianfan_ak
    os.environ['QIANFAN_SK'] = qianfan_sk
    chat = QianfanChatEndpoint(model="ERNIE-4.0-8K-Latest",creativity = creativity)

    title_prompt = title_prompt_template | chat
    script_prompt = script_prompt_template | chat

    title = title_prompt.invoke({"subject" : subject}).content
    search = WikipediaAPIWrapper(lang = "zh")
    search_result = search.run(subject)

    script = script_prompt.invoke({"title":title,"duration":video_length,"wikipedia_search":search_result}).content
    return search_result,script,title

# print(generator_script("自动驾驶",1,0.2,"0dqHemn5RtCW6WZlluKx5AvT","q0bx3rnqLowpATQqKibIUEEmFbv2FQYH"))

