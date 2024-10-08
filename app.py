import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes = [open(_file, encoding='utf-8').read() for _file in student_files]

def vectorize(Text): 
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): 
    return cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))
plagiarism_results = []

def check_plagiarism():
    global s_vectors
    for i in range(len(s_vectors)):
        student_a, text_vector_a = s_vectors[i]
        for j in range(i + 1, len(s_vectors)):
            student_b, text_vector_b = s_vectors[j]
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            score = (student_a, student_b, sim_score)
            plagiarism_results.append(score)
    return plagiarism_results

check_plagiarism()

plagiarism_results.sort(key=lambda x: x[2])

print("All Plagiarism Results:")
for result in plagiarism_results:
    percentage = result[2] * 100
    print(f"Files: {result[0]} and {result[1]} - Plagiarism Percentage: {percentage:.2f}%")

most_plagiarized = plagiarism_results[-1]
least_plagiarized = plagiarism_results[0]

most_percentage = most_plagiarized[2] * 100
least_percentage = least_plagiarized[2] * 100

print("\nMost Plagiarized Files:")
print(f"Files: {most_plagiarized[0]} and {most_plagiarized[1]} - Plagiarism Percentage: {most_percentage:.2f}%")

print("\nLeast Plagiarized Files:")
print(f"Files: {least_plagiarized[0]} and {least_plagiarized[1]} - Plagiarism Percentage: {least_percentage:.2f}%")
