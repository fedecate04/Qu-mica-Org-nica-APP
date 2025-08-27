from pathlib import Path
import yaml

BASE = Path(__file__).resolve().parents[1]

def read_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def read_text(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_index():
    return read_yaml(BASE / "content" / "index.yml")

def list_temas():
    idx = load_index()
    temas = idx.get("temas", [])
    # ensure order by id prefix "01_", "02_", etc.
    temas_sorted = sorted(temas, key=lambda x: x.get("id", ""))
    return temas_sorted

def load_tema(tema_id: str):
    tema_dir = BASE / "content" / "temas" / tema_id
    meta = read_yaml(tema_dir / "meta.yml")
    apuntes = (tema_dir / "apuntes.md").read_text(encoding="utf-8") if (tema_dir / "apuntes.md").exists() else ""
    ejercicios = (tema_dir / "ejercicios.md").read_text(encoding="utf-8") if (tema_dir / "ejercicios.md").exists() else ""
    media = read_yaml(tema_dir / "videos.yml") if (tema_dir / "videos.yml").exists() else {}
    return {"meta": meta, "apuntes": apuntes, "ejercicios": ejercicios, "media": media}

def load_bibliografia():
    return read_yaml(BASE / "data" / "bibliografia.yml")

def load_novedades():
    return read_yaml(BASE / "data" / "novedades.yml")