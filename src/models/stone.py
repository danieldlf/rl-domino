from pydantic import BaseModel, Field

class Stone(BaseModel):
    value1: int = Field(description="Primeiro valor da pedra", ge=0, le=6)
    value2: int = Field(description="Segundo valor da pedra", ge=0, le=6)

    def __eq__(self, other) -> bool:    
        if not isinstance(other, Stone):
            return False 
        
        return (self.value1 == other.value1 and self.value2 == other.value2) or (self.value1 == other.value2 and self.value2 == other.value1)


    def __repr__(self) -> str:
        return f"{self.value1} | {self.value2}"