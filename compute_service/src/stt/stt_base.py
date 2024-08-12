import threading
import numpy as np
from abc import ABC, abstractmethod
from typing import Callable, List, Dict, Union, Any


class STTBase(ABC):
    """base class for stt
    """
    def __init__(self, *args, **kwargs):
        self.model = None
        self.init(*args, **kwargs)
        
    def init(self, *args, **kwargs) -> None:
        """
        model loading is done in background
        """
        thread = threading.Thread(target=self._load_model, args=(args), kwargs=kwargs)
        thread.start()
        
    @abstractmethod
    def _load_model(self, *args, **kwargs) -> None:
        """initialize models
        """
        raise NotImplementedError
                
    @abstractmethod
    def transcribe(self, audio_array: np.ndarray, **generation_config: dict) -> str:
        """Transcribes the given audio data

        Args:
            audio_array (np.ndarray): The audio data to be transcribed

        Returns:
            str: The transcribed text
        """
        raise NotImplementedError
    
    def is_ready(self) -> bool:
        if self.model is not None:
            return True
        return False
