from streamlit import session_state as state # type: ignore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, FewShotChatMessagePromptTemplate
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI


def get_llm(model='gpt-4o'):
    llm = ChatOpenAI(model=model)
    return llm


def get_summary_chain():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template(f"""
        사용자의 질문과 답변을 보고, 15자 이내로 제목을 설정해 주세요.
        질문: {{question}}
        답변: {{answer}}
    """)

    summary_chain = prompt | llm | StrOutputParser()
    return summary_chain


def get_ai_summary(question, answer):
    summary_chain = get_summary_chain()
    ai_summary = summary_chain.invoke(
        {
            "question": question,
            "answer": answer
        },
        config=
        {
            "configurable": {"session_id": "summary123"}
        },
    )

    return ai_summary
