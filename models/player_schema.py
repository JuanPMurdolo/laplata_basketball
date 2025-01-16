from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date

class StatSchema(BaseModel):
    game_id: str = Field(..., description="Identificador único del partido")
    date: date = Field(..., description="Fecha del partido") # type: ignore
    team: str = Field(..., max_length=50, description="Equipo del jugador")
    opponent: str = Field(..., max_length=50, description="Equipo oponente")
    minutos: float = Field(..., ge=0, description="Minutos jugados")
    puntos: int = Field(..., ge=0, description="Puntos anotados")
    tc_intentos: int = Field(..., ge=0, description="Tiros de campo intentados")
    tc_convertidos: int = Field(..., ge=0, description="Tiros de campo convertidos")
    tc_porcentaje: float = Field(..., ge=0, le=100, description="Porcentaje de tiros de campo")
    t2_intentos: int = Field(..., ge=0, description="Tiros de 2 puntos intentados")
    t2_convertidos: int = Field(..., ge=0, description="Tiros de 2 puntos convertidos")
    t2_porcentaje: float = Field(..., ge=0, le=100, description="Porcentaje de tiros de 2 puntos")
    t3_intentos: int = Field(..., ge=0, description="Tiros de 3 puntos intentados")
    t3_convertidos: int = Field(..., ge=0, description="Tiros de 3 puntos convertidos")
    t3_porcentaje: float = Field(..., ge=0, le=100, description="Porcentaje de tiros de 3 puntos")
    tl_intentos: int = Field(..., ge=0, description="Tiros libres intentados")
    tl_convertidos: int = Field(..., ge=0, description="Tiros libres convertidos")
    tl_porcentaje: float = Field(..., ge=0, le=100, description="Porcentaje de tiros libres")
    rebotes_ofensivos: int = Field(..., ge=0, description="Rebotes ofensivos")
    rebotes_defensivos: int = Field(..., ge=0, description="Rebotes defensivos")
    rebotes_totales: int = Field(..., ge=0, description="Rebotes totales")
    asistencias: int = Field(..., ge=0, description="Asistencias")
    perdidas: int = Field(..., ge=0, description="Pérdidas")
    robos: int = Field(..., ge=0, description="Robos")
    tapones: int = Field(..., ge=0, description="Tapones")
    faltas_personales: int = Field(..., ge=0, description="Faltas personales")
    faltas_recibidas: int = Field(..., ge=0, description="Faltas recibidas")
    valorizacion: int = Field(..., description="Valorización del jugador")

    @validator("rebotes_totales")
    def check_rebounds(cls, v, values):
        ofensivos = values.get("rebotes_ofensivos", 0)
        defensivos = values.get("rebotes_defensivos", 0)
        if v != ofensivos + defensivos:
            raise ValueError("Rebotes totales no coinciden con la suma de ofensivos y defensivos")
        return v


class PlayerSchema(BaseModel):
    id: Optional[str] = Field(default="", description="ID del jugador")
    name: str = Field(..., max_length=100, description="Nombre del jugador")
    team: str = Field(..., max_length=50, description="Equipo al que pertenece")
    position: Optional[str] = Field(default="", max_length=30)
    age: Optional[int] = Field(default=0, ge=0, le=50)
    stats: List[StatSchema] = Field(default=[])



