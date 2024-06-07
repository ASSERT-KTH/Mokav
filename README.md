# Mokav!

This project introduces an innovative approach for iterative test generation using large language models (LLMs). Instead of relying on traditional techniques, our approach leverages the power of LLMs to generate test cases that target behavioral differences between a buggy program version and an accepted/patched program version. By engaging in interactive conversations with the LLM, our method provides feedback to steer the generation process iteratively until a fault-inducing test is found.

## Requirements

- Python 3 installed (Code has been tested with Python 3.10.12 on Ubuntu 22.04)
- Packages indicated in `requirements.txt` installed on python execution environments.


## Installation

1. Clone the repository
2. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the program, you need to add your OpenAI API key to a `.env` file in the project root directory. Here's how you can do it:

1. Create a new file named `.env` in the project root directory.

2. Open the `.env` file and add the following line:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Command-Line Arguments

The script accepts the following command-line arguments:

- `-f` or `--is_func`: This argument is used to run the C4DET runner. It is set to `True` by default.

- `-q` or `--is_qb`: This argument is used to run the QuixBugs runner. It is set to `False` by default.

- `-ic` or `--iteration_count`: This argument specifies the number of iterations after the initial prompt. The default value is `9`.

- `-mc` or `--meta_data_config`: This argument is used to set the configuration for meta data. The choices are "BADT", "AADT", "AADTI", "BAT", "AAT", "BATI", "AATI", "BADTI", "BADTIE", "BATIE". The default value is "BADTIE".

- `-td` or `--generated_tests_dir`: This argument specifies the directory to write the generated tests. The default directory is "generated_tests".

- `-ns` or `--number_of_samples`: This argument specifies the number of samples to be generated at each iteration. The default value is `10`.

- `-tm` or `--temperature`: This argument sets the temperature. The default value is `1`.

All arguments are optional. If not provided, the default values will be used.


## Usage

1. Ensure that your datasets are located in the `/data/` directory. The directory should include both Quixbugs and C4DET programs.

2. Run the following command to generate test cases for a given buggy program:
```bash
python main.py -f True -q False -ic 9 -mc BADTIE -td generated_tests -ns 10 -tm 1
```

3. The generated test cases will be saved in the specified output directory.
