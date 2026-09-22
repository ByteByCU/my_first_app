
import streamlit as st
import pandas as pd

#page settings
st.set_page_config(
    page_title="Smart AI Lab - Introduction to Machine Learning",
    layout="wide"
)

#sidebar
st.sidebar.title("Smart AI Lab")
st.sidebar.write(
    "Explore the basics of Machine Learning and see"
    "how Streamlit can be used to build interative ML Applications."
)

page=st.sidebar.radio(                               #Radio - choose one option
    "Choose a topic",                                # [] using list
    [
        "Start Here",
        "AI and Machine Learning",
        "How Machines Learn",
        "Types of Machine Learning",
        "Choose the right approach",
        "ML in Different Industries",
        "ML Project Lifecycle",
        "Final Challenge"
    ]
)

if page == "Start Here":
    st.title("Smart AI Lab")
    st.write(""" Welcome to the first session of our Machine Learning journey.
    Imagine that you have joined the analytics team of a bank.
    The business team does not start by telling you which
    Machine Learning alogorithm to use.
    They start with a business problem.
    """)
    st.divider()
    st.subheader("The bank has three questions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Prediction")
        st.write("""
        Can we predict whether a customer is likely
        to default on a loan?""")
    with  col2:
        st.markdown("#### Discovery")
        st.write("""
        Can we discover different types of customers
        from the data?
        """)
    with col3:
        st.markdown("#### Decision")
        st.write("""
        Can a machine learn which action is better
        based on feedback?
        """)
    st.divider()

    st.write("""
    These three questions are all related to Machine Learning,
    but they represnt diiferent learning problems.

    During this session we will understand the difference
    between them and also see how Streamlit can help us 
    turn our ideas into interactive applications.
    """)

    st.info(
    " The goal of this session is understanding, not model building."
    )

#AI and Machine Learning

elif page == "AI and Machine Learning":
    st.title("Artificial Intelligence and Machine Learning")
    st.write("""
    Before learning Machine Learning, we need to understand 
    where it fits into the larger field of Artificial Intelligence.
    """)

    st.subheader("Artificial Intelligence")
    st.write("""
    Artificial Intelligence is the broader field of creating
    computer systems that can perform tasks that normally
    require human intelligence.
    These tasks can include learning, reasoning, perception,
    langauge understanding, planning and decision-making.
    """)
    st.subheader("Machine Learning")
    st.write("""
    Machine Learning is a subset of Artificial Intelligence.
    Instead of explicitly programming every rule, we provide
    data to a Machine Learning system and allow it to learn
    patterns from that data.
    Those learned patterns can the be used to make predictions,
    identify patterns or support decisions.
    """)
    st.subheader("Deep Learning")
    st.write("""
    Deep Learning is a subset of Machine Learning based on
    multi-layer neutral networks.
    It is particularly useful when working with complex data 
    such as images, speech, video and large amounts of text.
    """)

    st.divider()

    st.markdown("""
    **Artificial Intelligence** - A broad field concerned with intelligent behaviour.\n
    **Machine Learning** - A way of building AI systems that learn patterns data.\n
    **Deep Learning** - A family of Machine Learning methods based on
    multi-layer neutral networks.
    """)

    st.divider()
    st.subheader("Smart Banking")

    st.write("""
    Consider a banking application.
    AI could refer to the overall intelligence system.
    Machine Learning could be used for:
    - predicting loan default
    - detecting unusual transactions
    - forecasring demand
    - understanding customer behaviour

    Deep Learning could be useful for:
    - analysing documents
    - speech recognition
    - understanding text
    - image-based document processing
    """)

#How Machine Learn
elif page == "How Machines Learn":

    st.title("What Does It Mean For a Machine to Learn?")

    st.write("""
    In tradiotional programming, we normally provide rules and 
    data to produce an output.
    """)

    st.subheader("Traditional Programming")
    st.markdown("""
    **Rules + Data = Output**
    """)

    st.write("""
    Example: A programmer may explicitly write rules such as:
    If transaction amount is greater than a particular value
    and the transaction happens in an unusual location,
    flag the transaction.
    This works well when the rules are known and can be
    clearly written.
    """)

    st.divider()

    st.subheader("Machine Learning")

    st.markdown("""
    **Data + Expected outcomes -> Learning Process -> Model**
    """)
    st.write("""
    In Machine Learning, instead of manually writing every rule,
    we provide examples to a learning system.
    The system tries to identify patterns in those examples.
    The result is a model that can used on new data.
    """)
    st.divider()
    st.subheader("Smart Banking")
    st.write("""
    Suppose a bank has historical customer information.
    For each customer we may have:
    - income
    - age
    - credit history
    - loan amount
    - repayment behaviour

    If we also know whether those customers eventually
    defaulted, we can use those historical examplse to
    learn a relationship between the customer information
    and the outcome.
    """)

    st.write("""
    The important idea is:
    **The model learns from examples rather than being given
    every rule explicitly.**
    """)
    st.divider()

    st.subheader("One important point")
    st.warning("""
    Machine Learning does not mean that the computer
    "understands" the data like a human.
    It identifies statistical patterns on the data and
    uses those patterns to produce an output.
    """)

