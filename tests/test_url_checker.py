import os
from url_checker.checker import check_url


def test_google_url(tmp_path, monkeypatch):
    # Arrange
    url = "https://www.google.com"

    # Use OUTPUT_FILE if provided (e.g., in Docker) so the file can be saved to host
    output_file_env = os.getenv("OUTPUT_FILE")
    if output_file_env:
        output_file = output_file_env
    else:
        output_file = str(tmp_path / "final_url.txt")
        monkeypatch.setenv("OUTPUT_FILE", output_file)

    # Act
    current_url, is_valid, input_site_name, final_site_name = check_url(url)

    # Assert
    assert input_site_name == "google"
    assert final_site_name == "google"
    assert is_valid is True
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as f:
        assert f.read().strip() == current_url