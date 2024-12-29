import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from pipeline import load_pipeline
from modules.text_cleaner import TextCleaner 


def test_pipeline_execution():
    pipeline = load_pipeline("pipeline_config.yaml")
    input_text = "  Test text!  "
    output = pipeline.execute(input_text)

    assert "Generated text based on" in output
    assert "Test text!" in output
    assert "0.8" in output  
    assert "entity1 entity2" in output 


def test_invalid_input_type():
    pipeline = load_pipeline("pipeline_config.yaml")

    with pytest.raises(ValueError):
        pipeline.execute(123)  

def test_invalid_output_type():
    pipeline = load_pipeline("pipeline_config.yaml")

    class TextCleanerInvalid(TextCleaner):
        def clean(self, text: str) -> int:
            return 123 
        
    pipeline.modules = [TextCleanerInvalid()] 

    with pytest.raises(ValueError):
        pipeline.execute("Test text!") 