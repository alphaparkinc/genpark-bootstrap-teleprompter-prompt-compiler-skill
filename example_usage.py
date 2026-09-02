from client import BootstrapTeleprompterPromptCompilerClient

def main():
    client = BootstrapTeleprompterPromptCompilerClient()
    res = client.compile_few_shot_prompt('MedicalEntityExtraction', 50, 'EXACT_MATCH')
    print('Teleprompter Prompt Compiler: ' + res['compiled_program_id'])
    print('Baseline Acc: ' + str(res['baseline_accuracy_pct']) + '% -> Optimized: ' + str(res['optimized_accuracy_pct']) + '%')
    print('Demonstrations: ' + str(res['demonstrations_selected_count']))
    print('Compiled Manifest: ' + res['compiled_prompt_manifest_url'])

if __name__ == '__main__':
    main()
