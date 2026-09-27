import pytest
from framework.config_reader import ConfigReader
from framework.data_reader import CSVDataReader
from pages.home_page import HomePage

@pytest.mark.parametrize("row", CSVDataReader.read_rows("search_data.csv"))
def test_product_search_returns_matching_results(driver, row):
    config = ConfigReader()
    results = HomePage(driver).open(config.get("application", "base_url")).search_for(row["keyword"])
    assert row["expected_fragment"].lower() in results.heading().lower()
    assert results.product_count() > 0, f"No products returned for '{row['keyword']}'."
    assert any(row["expected_fragment"].lower() in name.lower() for name in results.product_names()), (
        f"No displayed product title matched '{row['expected_fragment']}'."
    )
