import csv
import re

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match questions (lines starting with ##)
    question_pattern = re.compile(r'^## (.*?)$', re.MULTILINE)
    questions = question_pattern.findall(content)

    # Split the content by questions to get the corresponding answers
    sections = re.split(r'^## .*?$', content, flags=re.MULTILINE)[1:]  # Skip the first empty section
    answers = [section.strip() for section in sections]

    return list(zip(questions, answers))
def write_to_csv(qa_pairs, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for question, answer in qa_pairs:
            # Replace newlines with "\n" in the answer
            formatted_answer = answer.strip().replace('\n', '\\n')
            writer.writerow([question.strip(), formatted_answer])

def main():
    input_file = 'input.md'  # Path to your Markdown file
    output_file = 'output.csv'  # Path to the output CSV file

    qa_pairs = parse_markdown(input_file)
    write_to_csv(qa_pairs, output_file)

    print("CSV file created successfully.")

if __name__ == "__main__":
    main()

