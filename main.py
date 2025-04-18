import argparse
from src.code_runner import CodeRunner
import logging
from datetime import datetime

logging.basicConfig(filename='logging_{:%Y-%m-%d-%H-%M}.log'.format(datetime.now()),
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--is_func",
        default=True,
        help="Run the function runner",
        required=False,
    )

    parser.add_argument(
        "-q",
        "--is_qb",
        default=False,
        help="Run the QuixBugs runner",
        required=False,
    )

    parser.add_argument(
        "-ic",
        "--iteration_count",
        default=9,
        help="Number of iterations after the initial prompt",
        required=False,
        type=int,
    )

    parser.add_argument(
        "-mc",
        "--meta_data_config",
        choices=["BADT", "AADT", "AADTI", "BAT", "AAT", "BATI", "AATI", "BADTI", "BADTIE", "BATIE"],
        default="BADTIE",
        help="Config for meta data",
        required=False,
    )

    parser.add_argument(
        "-td",
        "--generated_tests_dir",
        default="generated_tests",
        help="Directory to write the generated tests",
        required=False,
    )

    parser.add_argument(
        "-ns",
        "--number_of_samples",
        default=10,
        help="Number of samples to be generated at each iteration",
        required=False,
        type=int,
    )

    parser.add_argument(
        "-tm",
        "--temperature",
        default=1,
        help="The temperature",
        required=False,
        type=float,
    )

    parser.add_argument(
        "-md",
        "--model",
        default="gpt-3.5-turbo",
        help="The model",
        required=False,
        type=str,
    )

    args = parser.parse_args()

    return args.is_func, args.is_qb, args.iteration_count, args.meta_data_config, args.generated_tests_dir, args.number_of_samples, args.temperature, args.model


def main() -> None:

    (is_func, is_qb, iteration_count, meta_data_config, generated_tests_dir, number_of_samples, temperature, model) = get_args()

    logging.info(f"Running with is_func: {is_func}, is_qb: {is_qb}, iteration_count: {iteration_count}, meta_data_config: {meta_data_config}" +
                 f"generated_tests_dir: {generated_tests_dir}, number_of_samples: {number_of_samples}, temperature: {temperature}, model: {model}")

    code_runner = CodeRunner(is_func, is_qb, iteration_count, meta_data_config, generated_tests_dir, number_of_samples, temperature, model)
    code_runner.run()


if __name__ == "__main__":
    main()
