import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_readme  # noqa: E402
import build_site  # noqa: E402
from directories import ROOT, listing_problems, load, load_listings, problems  # noqa: E402


class DataTests(unittest.TestCase):
    def test_data_follows_the_schema(self):
        self.assertEqual(problems(load()), [])

    def test_readme_is_built_from_the_data(self):
        text = (ROOT / "README.md").read_text()
        self.assertIn(build_readme.render(load()), text)

    def test_a_broken_entry_is_reported(self):
        bad = dict(load()[0], id="Not A Slug", status="active", checked=None)
        found = problems([bad])
        self.assertTrue(any("slug" in p for p in found))
        self.assertTrue(any("checked date" in p for p in found))

    def test_landing_page_lists_every_open_entry(self):
        page, _ = build_site.render(load(), load_listings(), "test")
        self.assertNotIn("{{", page)
        listed = [d for d in load() if d["status"] in ("active", "unchecked")]
        self.assertEqual(page.count("data-entry "), len(listed))

    def test_listings_name_real_directories(self):
        self.assertEqual(listing_problems(load_listings(), load()), [])

    def test_landing_page_shows_where_the_product_is_listed(self):
        page, _ = build_site.render(load(), load_listings(), "test")
        listed = {e["directory"] for e in load_listings()["listings"]}
        self.assertEqual(page.count('data-listed="yes"'), len(listed))

    def test_landing_page_leaves_out_skipped_places(self):
        page, _ = build_site.render(load(), load_listings(), "test")
        for d in load():
            if d["status"] in ("avoid", "down"):
                self.assertNotIn(f'id="{d["id"]}"', page)

    def test_landing_page_points_developers_to_the_repo(self):
        page, _ = build_site.render(load(), load_listings(), "test")
        self.assertIn(f'href="{build_site.REPO}"', page)
        self.assertIn("issues/new?template=add-a-place.yml", page)
        self.assertTrue((ROOT / ".github" / "ISSUE_TEMPLATE" / "add-a-place.yml").exists())

    def test_credit_to_lighteningly_carries_utm_tags(self):
        page, _ = build_site.render(load(), load_listings(), "test")
        readme = (ROOT / "README.md").read_text()
        for text, content in ((page, "site-footer"), (readme, "github-readme")):
            self.assertIn("lighteningly.com/?utm_source=launch-directories", text)
            self.assertIn("utm_medium=referral", text)
            self.assertIn(f"utm_content={content}", text)

    def test_agent_guide_names_files_that_exist(self):
        guide = (ROOT / "AGENTS.md").read_text()
        for path in ("data/directories.json", "data/schema.json", "plans/TEMPLATE.md", "scripts/build_readme.py"):
            self.assertIn(path, guide)
            self.assertTrue((ROOT / path).exists(), path)


if __name__ == "__main__":
    unittest.main()
