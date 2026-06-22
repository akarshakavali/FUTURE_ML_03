**Resume Screening System using Machine Learning**

**📌 Project Overview**
This project is a Machine Learning–based Resume Screening System that automatically analyzes, scores, and ranks resumes based on a given job description.
It helps recruiters quickly identify the most suitable candidates by comparing their skills with job requirements.
**🎯 Objective**
- Extract relevant information from resumes
- Compare resumes with job descriptions
- Rank candidates based on similarity
- Identify missing skills for each candidate
**⚙️ Technologies Used**
- Python
- Pandas
- Scikit-learn
- NLP (TF-IDF Vectorization)
- Cosine Similarity
**🧠 How It Works**
1. Resumes are loaded as text data
2. Job description is defined
3. Text is converted into numerical form using TF-IDF
4. Cosine similarity is used to compare resumes with the job role
5. Candidates are ranked based on similarity score
6. Missing skills are identified for each resume
**📊 Features**
✔ Resume ranking based on job relevance
✔ Skill matching using NLP
✔ Missing skill identification
✔ Easy-to-understand output
**📁 Project Structure**
resume-screening-system/
│── main.py
│── resumes.txt
│── README.md
**▶️ How to Run**
1. Install required libraries:

pip install pandas scikit-learn

2. Run the project:

python main.py
**📸 Output**
The system displays:
- Candidate ranking
- Similarity scores
- Missing skills for each candidate
**🚀 Future Improvements**
- Add PDF resume parsing
- Use spaCy for advanced skill extraction
- Build a web UI using Streamlit
- Add real-world datasets
**💡 Conclusion**
This project demonstrates how Machine Learning and NLP can be used to automate resume screening, making hiring faster and more efficient.
**🔗 Author**
Developed as part of Machine Learning Internship Task
By Future Interns
