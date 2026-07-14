from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
OUTPUT_DIR = BASE_DIR / "data"


@dataclass(frozen=True)
class RoundArtifacts:
    name: str
    source_plot_dir: Path | None
    output_slug: str


ROUND_ARTIFACTS: tuple[RoundArtifacts, ...] = (
    RoundArtifacts(
        name="R1 Australian GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_1_Australian_GP_2026"
        / "f1_2026_australian_gp_plots",
        output_slug="r1_australian_gp_2026",
    ),
    RoundArtifacts(
        name="R2 Chinese GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_2_Chinese_GP_2026"
        / "f1_2026_chinese_gp_plots",
        output_slug="r2_chinese_gp_2026",
    ),
    RoundArtifacts(
        name="R3 Japanese GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_3_Japanese_GP_2026"
        / "f1_2026_japanese_gp_plots",
        output_slug="r3_japanese_gp_2026",
    ),
    RoundArtifacts(
        name="R4 Miami GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_4_miami_GP_2026"
        / "f1_2026_miami_gp_plots",
        output_slug="r4_miami_gp_2026",
    ),
    RoundArtifacts(
        name="R5 Canadian GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_5_Canadian_GP_2026"
        / "f1_2026_canadian_gp_plots",
        output_slug="r5_canadian_gp_2026",
    ),
    RoundArtifacts(
        name="R6 Monaco GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_6_Monaco_GP_2026"
        / "f1_2026_monaco_gp_plots",
        output_slug="r6_monaco_gp_2026",
    ),
    RoundArtifacts(
        name="R7 Spanish GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_7_Spanish_GP_2026"
        / "f1_2026_spanish_gp_plots",
        output_slug="r7_spanish_gp_2026",
    ),
    RoundArtifacts(
        name="R8 Austrian GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_8_Austrian_GP_2026"
        / "f1_2026_austrian_gp_plots",
        output_slug="r8_austrian_gp_2026",
    ),
    RoundArtifacts(
        name="R9 British GP 2026",
        source_plot_dir=PROJECT_DIR
        / "Round_9_British_GP_2026"
        / "f1_2026_british_gp_plots",
        output_slug="r9_british_gp_2026",
    ),
    RoundArtifacts(
        name="T1&2 Bahrain 2026",
        source_plot_dir=PROJECT_DIR
        / "Testing_1&2_Bahrain_2026"
        / "f1_2026_testing_1&2_plots",
        output_slug="t1_2_bahrain_2026",
    ),
)

# Copy files with the given suffixes from source_dir into destination_dir
def copy_directory_contents(source_dir: Path, destination_dir: Path, suffixes: set[str]) -> list[str]:
    copied_files: list[str] = []
    if not source_dir.exists():
        return copied_files

    destination_dir.mkdir(parents=True, exist_ok=True)
    for source_file in sorted(source_dir.iterdir()):
        if source_file.is_file() and source_file.suffix.lower() in suffixes:
            destination_file = destination_dir / source_file.name
            shutil.copy2(source_file, destination_file) # Copy the file to the new location
            copied_files.append(destination_file.relative_to(BASE_DIR).as_posix()) # Store path relative to BASE_DIR

    return copied_files

# Copy source plot artifacts and return a JSON-serializable manifest
def build_manifest() -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for round_artifacts in ROUND_ARTIFACTS:
        round_output_dir = OUTPUT_DIR / round_artifacts.output_slug
        plot_output_dir = round_output_dir / "plots"

        copied_plots = []
        if round_artifacts.source_plot_dir is not None:
            copied_plots = copy_directory_contents(
                round_artifacts.source_plot_dir,
                plot_output_dir,
                {".png", ".jpg", ".jpeg", ".webp"}
            )

        manifest.append(
            {
                "name": round_artifacts.name,
                "slug": round_artifacts.output_slug,
                "plots": copied_plots,
            }
        )

    return manifest


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest()

    index_path = OUTPUT_DIR / "index.json"
    index_path.write_text(json.dumps({"rounds": manifest}, indent=2), encoding="utf-8")

    print(f"Wrote artifact index to {index_path}")
    for round_manifest in manifest:
        print(
            f"{round_manifest['name']}: "
            f"{len(round_manifest['plots'])} plot files"
        )


if __name__ == "__main__":
    main()