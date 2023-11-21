import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("./output/FullDF.csv")

# Download NLTK resources
nltk.download('stopwords')

# Text processing function
def process_text(text):
    # Tokenization
    words = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Stemming (using Porter Stemmer)
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    # Join the processed words back into a string
    processed_text = ' '.join(words)

    return processed_text

# Apply text processing to the 'Description' column
df['Bfr_Processing_Description'] = df['Name'] + df['Description']
df['Processed_Description'] = df['Bfr_Processing_Description'].apply(process_text)


descriptions = df['Processed_Description']
labels = df['Sports']
# Step 1: Prepare Data
X_train, X_test, y_train, y_test = train_test_split(descriptions, labels, test_size=0.2, random_state=42)

# Step 2: Text Preprocessing
# You may need to implement your own text preprocessing based on your specific requirements.

# Step 3: Feature Extraction
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Step 4: Train a Model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", report)