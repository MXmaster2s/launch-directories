// Filters the prerendered directory cards. The page reads fine without it.
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
  const filters = document.querySelector("[data-filters]");
  const cards = [...document.querySelectorAll("[data-entry]")];
  const count = document.querySelector("[data-count]");
  const empty = document.querySelector("[data-empty]");
  const made = new Set(); // what the visitor has made; none picked shows everything
  const only = new Set();

  filters.hidden = false;

  function matches(card) {
    const d = card.dataset;
    if (made.size && ![...made].some((key) => d.groups.split(" ").includes(key))) return false;
    if (only.has("no-account") && d.account !== "no") return false;
    if (only.has("no-badge") && d.badge !== "no") return false;
    if (only.has("listed") && d.listed !== "yes") return false;
    return true;
  }

  function apply() {
    let shown = 0;
    for (const card of cards) {
      const ok = matches(card);
      card.hidden = !ok;
      if (ok) shown += 1;
    }
    count.textContent = shown === cards.length ? `${shown} places` : `${shown} of ${cards.length} places`;
    empty.hidden = shown !== 0;
  }

  function bind(selector, set, key) {
    document.querySelectorAll(selector).forEach((chip) => {
      chip.addEventListener("click", () => {
        const on = chip.getAttribute("aria-pressed") !== "true";
        chip.setAttribute("aria-pressed", String(on));
        const value = chip.dataset[key];
        if (on) set.add(value);
        else set.delete(value);
        apply();
      });
    });
  }

  bind("[data-takes]", made, "takes");
  bind("[data-toggle]", only, "toggle");

  const copy = document.querySelector("[data-copy]");
  const prompt = document.querySelector("[data-prompt]");
  if (navigator.clipboard) {
    copy.hidden = false;
    copy.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(prompt.textContent);
        copy.textContent = "Copied";
        setTimeout(() => { copy.textContent = "Copy"; }, 1600);
      } catch {
        copy.textContent = "Select and copy";
      }
    });
  }

  const reveal = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    }, { rootMargin: "0px 0px -10% 0px" });
    reveal.forEach((el) => io.observe(el));
  } else {
    reveal.forEach((el) => el.classList.add("in"));
  }

  apply();
});
