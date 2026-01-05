def answer_question(vector_store, question, k=2):
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(question)

    if not docs:
        return "No relevant information found in the video."

    answer = ""
    for i, doc in enumerate(docs, 1):
        answer += f"{i}. {doc.page_content}\n\n"

    return answer
