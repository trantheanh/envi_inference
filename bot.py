import os
import utils.common_utils as utils

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def start():
    if os.path.isdir("pretrained_model"):
        return

    # Download model
    print("START DOWNLOAD MODEL")
    id_str = '1Y0u3V9Ml9m4vgEaylVy5xEgKzpkmZVfg'
    file_path = os.path.join(CURRENT_PATH, "pretrained_model.zip")
    utils.download_file_from_google_drive(id_str, file_path)

    # Unzip model
    print("START UNZIP MODEL")
    os.system('tar xvf "{}"'.format(file_path))


def translation(text=""):
    start()
    with open("input_inference/input.txt", 'w') as f:
        f.write(text + " .\n")

    os.system("python nmt.py --src=en --tgt=vi --ckpt=pretrained_model/translate.ckpt --hparams_path=standard_hparams/iwslt15.json --out_dir=output_inference/result --vocab_prefix=pretrained_model/vocab --inference_input_file=input_inference/input.txt --inference_output_file=output_inference/result.txt")

    with open("output_inference/result.txt", 'r', encoding='utf-8') as f:
        result = f.read()
        print(result)

    return result