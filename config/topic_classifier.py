#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""
import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Clasificador de temas para campaña Superioridad Láctea / Nutrición - Alpina.
    Incluye categoría específica para comentarios sobre uso de IA en publicidad.
    """

    def classify_topic(comment: str) -> str:
        comment_lower = str(comment).lower()

        # CATEGORÍA 1: Crítica al uso de IA en publicidad
        if re.search(
            r'\bia\b|inteligencia artificial|animaci[oó]n.*ia|'
            r'hecho con ia|generado|ia.*barata|ia.*mala|'
            r'dejen.*ia|no.*ia|usando ia|anuncio.*ia|publicidad.*ia|'
            r'contratar.*profesional|contratar.*artista|'
            r'paguen.*animador|equipo creativo|'
            r'ahorrar.*comunicar|pereza.*ia|mal.*ia|'
            r'cred[íi]tos.*ia|le puso ia|lo hicieron con ia',
            comment_lower
        ):
            return 'Crítica al Uso de IA en Publicidad'

        # CATEGORÍA 2: Precio y valor de marca
        if re.search(
            r'\bprecio\b|cu[aá]nto vale|valor|caro|cobran|'
            r'baj[ea]n?\s+el\s+precio|inviertan|invierten|'
            r'plata que tiene|tienen para pagar|no les alcanz',
            comment_lower
        ):
            return 'Precio y Valor de Marca'

        # CATEGORÍA 3: Nostalgia e identidad de marca
        if re.search(
            r'osito|antes era|ya no es|como antes|'
            r'alpinista|patrimonio|traici[oó]n|generaciones|'
            r'marca favorita|de toda la vida|recuerdo|nostalgia',
            comment_lower
        ):
            return 'Nostalgia e Identidad de Marca'

        # CATEGORÍA 4: Crítica a la calidad creativa / publicidad
        if re.search(
            r'publicidad.*mala|mala.*publicidad|mal.*comercial|'
            r'hecho con las patas|babosada|mediocr|'
            r'calidad.*publicidad|publicidad.*barata|'
            r'publicidad.*perversa|emocional.*octagon|evita.*octagon|'
            r'no vale la pena|horrible|est[aá] feo|así no',
            comment_lower
        ):
            return 'Crítica a la Calidad Publicitaria'

        # CATEGORÍA 5: Octágonos y advertencias nutricionales
        if re.search(
            r'octagon|advertencia|sello|sellos|sodio|az[uú]car|'
            r'exceso.*sodio|exceso.*az[uú]car|no muestra|ocultan',
            comment_lower
        ):
            return 'Octágonos y Advertencias Nutricionales'

        # CATEGORÍA 6: Opinión positiva del producto / marca
        if re.search(
            r'rico|bueno|excelente|gusta|mejor|delicioso|espectacular|'
            r'encanta|s[úu]per|amor|amoooo|fant[aá]stico|'
            r'disfruta|productos.*buenos|me gusta alpina|'
            r'la quiero|la amo|gran ejemplo',
            comment_lower
        ):
            return 'Opinión Positiva del Producto / Marca'

        # CATEGORÍA 7: Opinión negativa del producto / marca
        if re.search(
            r'feo|horrible|mal[ií]simo|sabe mal|asco|'
            r'decepci[oó]n|peor empresa|no compro|'
            r'ya no como|se me quit[oó].*ganas|no quiero',
            comment_lower
        ):
            return 'Opinión Negativa del Producto / Marca'

        # CATEGORÍA 8: Preguntas sobre el producto
        if re.search(
            r'd[oó]nde comprar|c[oó]mo consigo|duda|pregunta|'
            r'tiendas|disponible|sirve para|c[oó]mo se toma|'
            r'tiene az[uú]car|qu[eé] es|para qu[eé] sirve',
            comment_lower
        ):
            return 'Preguntas sobre el Producto'

        # CATEGORÍA 9: Impacto de IA en empleo / economía
        if re.search(
            r'quita.*trabajo|trabajo.*ia|empleo|'
            r'ram|servidores|agua.*servidores|costos.*ia|'
            r'reducir costos|tecnolog[ií]a.*trabajo',
            comment_lower
        ):
            return 'Impacto de IA en Empleo y Economía'

        # CATEGORÍA 10: Fuera de tema / irrelevante
        if re.search(
            r'am[eé]n|jajaja|receta|bendiciones|🇲🇽|'
            r'abelardo|sticker|saludos desde|therias|sapa yo',
            comment_lower
        ) or len(comment_lower.split()) < 3:
            return 'Fuera de Tema / No Relevante'

        return 'Otros'

    return classify_topic
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
