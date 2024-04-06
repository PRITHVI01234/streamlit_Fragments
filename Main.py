import streamlit as st
import numpy as np
import pandas as pd
import datetime
import random

# Setting Streamlit page configuration
st.set_page_config(
    page_title="Streamlit App Documentation",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page title
st.title("🚀 Streamlit's New Feature `st.experimental_fragment`:")

# Introduction
st.markdown("""
📜 *Welcome to the DIY page for Streamlit's `st.experimental_fragment`. This feature enables partial rerunning of Streamlit applications, offering more control and efficiency. Let's dive into its capabilities and usage.* 🛠️
""")

# Divider
st.divider()

# What is st.experimental_fragment?
st.subheader("❓ What is `st.experimental_fragment`?")
st.markdown("""
`st.experimental_fragment` 🎯 is a groundbreaking feature introduced in Streamlit version 1.33.0. It allows for the selective rerunning of parts of a Streamlit app without rerunning the entire application. 🌟
""")

# Divider
st.divider()

# Advantages
st.header("✅ Pros of Using `st.experimental_fragment`")
st.markdown("""
- **Partial Rerunning**: Efficiently rerun only specific parts of the app, reducing unnecessary computations and enhancing app responsiveness. 🔄
- **Integration with `st.session_state`**: Seamless integration with session state for state management, enabling persistent data storage and retrieval across reruns. 🗂️
- **Customizable Rerun Frequency**: Control rerun frequency using the `run_every` parameter, allowing dynamic updates at specified intervals. ⏲️
- **Enhanced User Experience**: Provides smoother app interactions by rerunning only essential parts, reducing lag and improving responsiveness. 🎨
- **Optimized Performance**: Reduces computational overhead by rerunning only updated sections, leading to faster app load times and smoother transitions. 🚀
- **Facilitates Complex App Structures**: Enables the creation of more complex Streamlit apps with modular and reusable fragments, enhancing code organization and maintainability. 🧩
""")

# Divider
st.divider()

# Working of st.experimental_fragment
st.header("🔧 Working of `st.experimental_fragment`")

# Source Code Expander
with st.expander("🔍 Source Code"):
    st.markdown("""
    ```python
    import streamlit as st
    import random
                
    col1, col2 = st.columns(2)

    with col1:
                
        @st.experimental_fragment
        def sample_fragment():
            # Fragment code goes here
            st.write(f'## **{random.randint(0, 100)}**')
            st.button('Does Nothing, But Reruns Fragment alone')

        sample_fragment()

    with col2:
                
        def main_fragment():
            st.write(f'## **{random.randint(0,10)}**')
            st.button('Does Nothing, But Reruns the entire Application including Fragment(s)')

        main_fragment()
                
    ```

    """)

# Usage Example
st.markdown("**Below is a simple example demonstrating the usage of `st.experimental_fragment` compared to traditional Streamlit code.** 📝")

col1, col2 = st.columns(2)

# Using st.experimental_fragment
with col1:
     @st.experimental_fragment
     def sample_fragment():
         st.write(f'## **{random.randint(0, 100)}**')
         st.button('Does Nothing, But Reruns Fragment alone')

     sample_fragment()

# Without st.experimental_fragment
with col2:
     def main_fragment():
         st.write(f'## **{random.randint(0,10)}**')
         st.button('Does Nothing, But Reruns the entire Application including Fragment(s)')

     main_fragment()

# Divider
st.divider()

# Real-time Usage Example
st.header("⏳ Usage Example In Real Time:")

st.title("📊 Streamlit App with Simple Charts")
st.markdown("""
*This is a simple Streamlit app that demonstrates the working of Streamlit's `st.experimental_fragment`.* 📈
""")

with st.expander("🔍 Source Code"):
    st.markdown("""
    ```python
    import streamlit as st
    import random
                
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("## 🚀 Using st.experimental_fragment", unsafe_allow_html=True)
    
        @st.experimental_fragment
        def simple_charts():
            st.markdown("### 📊 Bar Chart 1", unsafe_allow_html=True)
            val11 = st.slider("Number of bars for Bar Chart1 📏", 1, 20, 4)
            st.bar_chart(np.random.default_rng().random(val11))
                
        simple_charts()

    with col2:
        st.markdown("## 🛠️ Without st.experimental_fragment", unsafe_allow_html=True)
        
        def simple_charts1():
            st.markdown("### 📊 Bar Chart 2", unsafe_allow_html=True)
            val = st.slider("Number of bars for Bar Chart2 📏", 1, 20, 4)
            st.bar_chart(np.random.default_rng().random(val))
            
        simple_charts1()
               
    ```""")

col1, col2 = st.columns([1, 1])

@st.experimental_fragment
def reset_streaming():
    np.random.seed(0)
    rng = np.random.default_rng()
    if st.button("🔄 Reset Streaming") or "chart_data" not in st.session_state:
        st.session_state.chart_data = pd.DataFrame(rng.random((20, 1)), columns=["Value"])

with col1:
    st.markdown("## 🚀 Using st.experimental_fragment", unsafe_allow_html=True)
    
    @st.experimental_fragment
    def simple_charts():
        st.markdown("### 📊 Bar Chart 1", unsafe_allow_html=True)
        val11 = st.slider("Number of bars for Bar Chart1 📏", 1, 20, 4)
        st.bar_chart(np.random.default_rng().random(val11))
               
    simple_charts()

with col2:
    st.markdown("## 🛠️ Without st.experimental_fragment", unsafe_allow_html=True)
    
    def simple_charts1():
        st.markdown("### 📊 Bar Chart 2", unsafe_allow_html=True)
        val = st.slider("Number of bars for Bar Chart2 📏", 1, 20, 4)
        st.bar_chart(np.random.default_rng().random(val))
        
    simple_charts1()

st.divider()

# Real-time Data Streaming
st.header("📈 **Advanced Example: Real-time Data Streaming Bar Chart**")
with st.expander("🔍 Source Code"):
    st.markdown("""
    ```python
    import streamlit as st
    import random
                
    @st.experimental_fragment
    def reset_streaming():
        np.random.seed(0)
        rng = np.random.default_rng()
        if st.button("🔄 Reset Streaming") or "chart_data" not in st.session_state:
            st.session_state.chart_data = pd.DataFrame(rng.random((20, 1)), columns=["Value"])

    reset_streaming()

    @st.experimental_fragment(run_every=2)
    def generate_chart():
        rng = np.random.default_rng()
        new_data = pd.DataFrame(rng.random((2, 1)), columns=["Value"])
        st.session_state.chart_data = pd.concat([st.session_state.chart_data, new_data], ignore_index=True)
        chart_data = st.session_state.chart_data
        st.bar_chart(chart_data)
        st.caption(f"*Last updated {datetime.datetime.now()}* 🕒")

    with st.container():
        generate_chart()
               
    ```""")
st.caption("*This section demonstrates a real-time streaming bar chart using `st.experimental_fragment`. The app updates the chart with new random data every few seconds.* ⏰")

@st.experimental_fragment
def reset_streaming():
    np.random.seed(0)
    rng = np.random.default_rng()
    if st.button("🔄 Reset Streaming") or "chart_data" not in st.session_state:
        st.session_state.chart_data = pd.DataFrame(rng.random((20, 1)), columns=["Value"])

reset_streaming()

@st.experimental_fragment(run_every=2)
def generate_chart():
    rng = np.random.default_rng()
    new_data = pd.DataFrame(rng.random((2, 1)), columns=["Value"])
    st.session_state.chart_data = pd.concat([st.session_state.chart_data, new_data], ignore_index=True)
    chart_data = st.session_state.chart_data
    st.bar_chart(chart_data)
    st.caption(f"*Last updated {datetime.datetime.now()}* 🕒")

with st.container():
    generate_chart()

st.divider()

# Concluding GIF Section
st.header("🎉 Conclusion: Embracing the Future with Streamlit! 🚀")

st.markdown("""
            `st.experimental_fragment` is a game-changing feature in Streamlit that unlocks new freedoms, efficiencies, and possibilities for developers. With this innovative addition, Streamlit continues to pave the way for creating dynamic and interactive web apps with ease. Let's harness this power, collaborate, and continue pushing the boundaries of what's possible with Streamlit! 💡🌐
            """)

st.divider()

co1, co2 = st.columns([1, 1])

with co1:
    st.image("https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", 
             caption="👨‍💻 Streamlit developers Right Now 🚀", 
             width=600, 
             use_column_width=True)
    # st.markdown("<p style='text-align: center;'><strong>🎉 Celebrating Streamlit Magic 🎉</strong></p>", 
    #             unsafe_allow_html=True)

with co2:
    st.subheader("🌟 Single Feature, Endless Possibilities with Streamlit! 🚀")
    st.markdown("""
                Streamlit is an incredible tool that has revolutionized the way developers create web apps. With `st.experimental_fragment`, we've unlocked new freedoms and possibilities! Let's harness this power, collaborate, and continue innovating to make Streamlit even more extraordinary! 💡🌐
                """)

st.divider()
