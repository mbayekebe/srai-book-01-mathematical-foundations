# Running PU-B01-C01 in Google Colab

The notebook uses the `srai_math` package included in the complete PU-B01-C01 release.

## Instructions

1. Open Google Colab.
2. Select **File → Upload notebook**.
3. Upload `M1_N01_mathematical_thinking.ipynb`.
4. Run the notebook cells from top to bottom.
5. When the first code cell requests the release archive, upload:

   `PU-B01-C01_GitHub_Repository_v1.0.zip`

6. The bootstrap cell will:
   - extract the repository;
   - install the Colab-safe dependencies;
   - install `srai_math`;
   - continue running the notebook.

Do not run `pip install -r requirements.txt` in Colab. That file contains Jupyter components intended for local development.

For every new Colab runtime, rerun the bootstrap cell and upload the release ZIP when requested.