import yaml
from typing import List
from modules.text_cleaner import TextCleaner
from modules.entity_extractor import EntityExtractor
from modules.sentiment_analyzer import SentimentAnalyzer
from modules.text_generator import TextGenerator

class Pipeline:
    def __init__(self, modules: List):
        self.modules = modules  

    def execute(self, input_text: str) -> str:
        if not isinstance(input_text, str):
            raise ValueError(f"Expected input of type 'str', but got {type(input_text).__name__}")
        
        text = input_text.strip() 
        original_text = input_text.strip()  
        extracted_entities = [] 

        for module in self.modules:
            if isinstance(module, EntityExtractor):
                if not isinstance(text, str):  
                    raise ValueError(f"Expected string input, got {type(text).__name__} for {module.__class__.__name__}")
                entities = module.extract_entities(text)
                if not isinstance(entities, list): 
                    raise TypeError(f"Expected output of type list from {module.__class__.__name__}, got {type(entities).__name__}")
                extracted_entities = entities
                text = " ".join(entities) 

            elif isinstance(module, SentimentAnalyzer):
                if not isinstance(text, str):  
                    raise ValueError(f"Expected string input, got {type(text).__name__} for {module.__class__.__name__}")
                sentiment_score = module.analyze(text)
                text = f"Sentiment score: {sentiment_score}"  

            elif isinstance(module, TextGenerator):
                if not isinstance(text, str): 
                    raise ValueError(f"Expected string input, got {type(text).__name__} for {module.__class__.__name__}")
                text = module.generate(text, max_length=100)  

            elif isinstance(module, TextCleaner):
                if not isinstance(text, str): 
                    raise ValueError(f"Expected string input, got {type(text).__name__} for {module.__class__.__name__}")
                text = module.clean(text) 

            else:
                raise ValueError(f"Unknown module {module.__class__.__name__}")
            
            if not isinstance(text, str):
                raise ValueError(f"Expected output of type 'str', but got {type(text)}")

        return f"Original text: {original_text}, text: {text}, entities: {' '.join(extracted_entities)}"


def load_pipeline(config_path: str) -> Pipeline:
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    modules = []
    for step in config['pipeline']:
        module_type = step['type']
        module_params = step.get('params', {})
        module_class = globals().get(module_type)

        if not module_class:
            raise ValueError(f"Unknown module type: {module_type}")

        if module_type == "TextGenerator" and "max_length" in module_params:
            max_length = module_params.pop("max_length")  

        module_instance = module_class(**module_params)

        if module_type == "TextGenerator" and 'max_length' in locals():
            module_instance.max_length = max_length 

        modules.append(module_instance)

    return Pipeline(modules)

