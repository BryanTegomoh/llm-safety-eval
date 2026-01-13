import json, csv, os

benchmark_dir = 'benchmark'
files = [
    ('harmful_behaviors_test_public.json', 'harmful', 'test'),
    ('harmful_behaviors_validation.json', 'harmful', 'validation'),
    ('benign_behaviors_test_public.json', 'benign', 'test'),
    ('benign_behaviors_validation.json', 'benign', 'validation'),
    ('chat_public_test.json', 'chat', 'test'),
    ('chat_validation.json', 'chat', 'validation'),
]
all_behaviors = []
for filename, dataset_type, split in files:
    with open(os.path.join(benchmark_dir, filename), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for b in data.get('behaviors', []):
        all_behaviors.append({
            'dataset_type': dataset_type,
            'split': split,
            'id': b.get('id', ''),
            'id_original': b.get('id_original', ''),
            'name': b.get('name', ''),
            'category': b.get('category', ''),
            'detailed_prompt': b.get('detailed_prompt', ''),
            'hint_included': b.get('hint_included', ''),
            'prompt': b.get('prompt', ''),
            'target_functions': '; '.join(b.get('target_functions', [])),
            'grading_function': b.get('grading_function', '')
        })
    print(f'Loaded {len(data.get("behaviors", []))} from {filename}')

with open('agentharm_full.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['dataset_type','split','id','id_original','name','category','detailed_prompt','hint_included','prompt','target_functions','grading_function'])
    w.writeheader()
    w.writerows(all_behaviors)
print(f'Total: {len(all_behaviors)} behaviors')
