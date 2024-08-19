from utils import generator_script
import streamlit as st

st.title("视频脚本生成器")

with st.sidebar:
    qianfan_ak = st.text_input("请输入千帆大模型的ak:",type="password")
    qianfan_sk = st.text_input("请输入千帆大模型的sk:",type="password")
    st.markdown("[获取api密钥](https://qianfan.cloud.baidu.com/)")

subject = st.text_input("获取视频主题:")
video_length = st.number_input("请输入视频时长(单位:分钟)",min_value=0.1,step=0.1)
creativity = st.slider("请输入回答的创造度(数字小更严谨，数字大更多样性)：",min_value=0.0,max_value=1.0,value=0.2,step=0.1)

submit = st.button("生成脚本")

if submit and not qianfan_ak:
    st.info("请输入你的千帆ak：")
    st.stop()
if submit and not qianfan_sk:
    st.info("请输入你的千帆sk：")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题：")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频时长需要大于等于0.1")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中.....")):
        search_result,scrip,title = generator_script(subject,1,0.2,"0dqHemn5RtCW6WZlluKx5AvT","q0bx3rnqLowpATQqKibIUEEmFbv2FQYH")

    st.success("视频脚本已经生成!")
    st.subheader("标题：")
    st.write(title)
    st.subheader("脚本：")
    st.write(scrip)

    with st.expander("维基百科生成结果:"):
        st.info(search_result)
