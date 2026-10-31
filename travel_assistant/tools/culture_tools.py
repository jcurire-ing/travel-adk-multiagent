def get_local_culture_info(destination: str) -> dict:
    """Return basic local cultural tips, dishes, and phrases."""
    dest = destination.lower().strip()
    if "cusco" in dest or "peru" in dest or "perú" in dest:
        return {
            "status": "success",
            "destination": destination,
            "dishes": ["Lomo Saltado", "Ceviche", "Cuy Chactado"],
            "customs": "Saludar con respeto, dejar propina del 10% y respetar sitios sagrados.",
            "phrases": ["¡Hola! / Allianllachu", "Muchas gracias / Añay", "¿Cuánto cuesta?"],
        }
    return {
        "status": "success",
        "destination": destination,
        "dishes": ["Gastronomía tradicional y platos emblemáticos locales"],
        "customs": "Respetar las normas locales, horarios de descanso y costumbres locales.",
        "phrases": ["Por favor", "Muchas gracias", "¿Dónde queda...?"],
    }
