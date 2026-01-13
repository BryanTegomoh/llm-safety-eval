"""
Convert AgentHarm JSON datasets to CSV format
"""
import json
import csv
import os

def load_behaviors(json_path, dataset_type, split):
    """Load behaviors from a JSON file"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    behaviors = []
    for b in data.get('behaviors', []):
        behavior = {
            'dataset_type': dataset_type,  # harmful or benign
            'split': split,  # test or validation
            'id': b.get('id', ''),
            'id_original': b.get('id_original', ''),
            'name': b.get('name', ''),
            'category': b.get('category', ''),
            'detailed_prompt': b.get('detailed_prompt', ''),
            'hint_included': b.get('hint_included', ''),
            'prompt': b.get('prompt', ''),
            'target_functions': '; '.join(b.get('target_functions', [])),
            'grading_function': b.get('grading_function', '')
        }
        behaviors.append(behavior)
    
    return behaviors

def main():
    benchmark_dir = os.path.join(os.path.dirname(__file__), 'benchmark')
    
    all_behaviors = []
    
    # Define files to process
    files = [
        ('harmful_behaviors_test_public.json', 'harmful', 'test'),
        ('harmful_behaviors_validation.json', 'harmful', 'validation'),
        ('benign_behaviors_test_public.json', 'benign', 'test'),
        ('benign_behaviors_validation.json', 'benign', 'validation'),
        ('chat_public_test.json', 'chat', 'test'),
        ('chat_validation.json', 'chat', 'validation'),
    ]
    
    for filename, dataset_type, split in files:
        filepath = os.path.join(benchmark_dir, filename)
        if os.path.exists(filepath):
            behaviors = load_behaviors(filepath, dataset_type, split)
            all_behaviors.extend(behaviors)
            print(f"Loaded {len(behaviors)} behaviors from {filename}")
    
    # Write combined CSV
    output_path = os.path.join(os.path.dirname(__file__), 'agentharm_dataset.csv')
    
    fieldnames = [
        'dataset_type', 'split', 'id', 'id_original', 'name', 'category',
        'detailed_prompt', 'hint_included', 'prompt', 'target_functions', 'grading_function'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_behaviors)
    
    print(f"\nCreated {output_path}")
    print(f"Total behaviors: {len(all_behaviors)}")
    
    # Print summary by type
    harmful_count = sum(1 for b in all_behaviors if b['dataset_type'] == 'harmful')
    benign_count = sum(1 for b in all_behaviors if b['dataset_type'] == 'benign')
    print(f"  - Harmful behaviors: {harmful_count}")
    print(f"  - Benign behaviors: {benign_count}")

if __name__ == '__main__':
    main()
