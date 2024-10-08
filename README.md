# PlagioSleuth

PlagioSleuth is a Python-based plagiarism detection tool that helps users identify similarities between text documents using **cosine similarity**. Whether you're a student checking your assignments or a teacher reviewing submissions, PlagioSleuth provides an easy and efficient way to ensure originality in written work.

## Table of Contents

- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Running the App](#running-the-app)
- [Output Examples](#output-examples)
- [Features](#features)
- [Explore It](#explore-it)
- [Issues](#issues)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## How It Works

PlagioSleuth transforms text documents into numerical vectors using the **TF-IDF (Term Frequency-Inverse Document Frequency)** method. By calculating the cosine similarity between these vectors, it determines the level of similarity between documents. The higher the similarity score, the more likely it is that plagiarism has occurred.

## Getting Started

To get started with PlagioSleuth, clone or download the repository to your local machine:

```bash
git clone https://github.com/nikhilsambarapu8978/PlagioSleuth
```

## Dependencies

Before running the application, ensure you have Python installed on your machine. You will need to install the required dependencies. To do this, navigate to the project directory and run the following command:
```bash
 pip install -r req.txt
```

## Running the App
To run PlagioSleuth, place your text documents (with the .txt extension) in the project directory. Then, execute the following command:

```bash
cd PlagioSleuth
python app.py
```

## Output Examples

All Plagiarism Results:
Files: b.txt and c.txt - Plagiarism Percentage: 28.20%
Files: a.txt and c.txt - Plagiarism Percentage: 37.86%
Files: a.txt and b.txt - Plagiarism Percentage: 41.71%

Most Plagiarized Files:
Files: a.txt and b.txt - Plagiarism Percentage: 41.71%

Least Plagiarized Files:
Files: b.txt and c.txt - Plagiarism Percentage: 28.20%

## Features
Detects plagiarism in multiple text documents.
Outputs plagiarism percentages for each document pair.
Highlights the most and least plagiarized files for easy identification.

## Explore It
Feel free to explore and modify PlagioSleuth to fit your specific use case. For any questions or suggestions, you can reach me at nikhilsa562@gmail.com.

## Issues
If you encounter any issues while using PlagioSleuth, please open an issue on the GitHub repository. Your feedback is invaluable for improving the tool.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
