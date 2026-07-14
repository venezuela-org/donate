# Donate — School kits for Venezuela

Public donation-progress page for the joint Creative Commons Venezuela + Creative Commons Switzerland school-kits campaign.

Live at: **https://venezuela-org.github.io/donate/**

## Update the amount raised

Open `index.html`, find this block near the bottom:

```js
const RAISED_CHF  = 2000;
const GOAL_CHF    = 10000;
const LAST_UPDATE = "14 July 2026";
```

Change the numbers and the date, then:

```
git add index.html
git commit -m "Update raised amount"
git push
```

The page updates within a minute or two. Nothing else needs editing.

## Publish (first time only)

1. Create an empty **public** repo named `donate` in the `venezuela-org` organization (no README, no license — this folder already has everything).
2. From this folder:

```
git remote add origin https://github.com/venezuela-org/donate.git
git push -u origin main
```

3. On GitHub: **Settings → Pages → Source: Deploy from a branch → Branch: main / (root) → Save.**
4. After a minute, the page is live at https://venezuela-org.github.io/donate/

## Contents — all public-safe

Only campaign material: the page, the two kit images, and the poster PDF. No names, no locations, no coordination data (per the data-classification rules in the private plan).

## Honesty rule

Only publish amounts actually received on the TWINT account. Keep `LAST_UPDATE` current — a stale or inflated number costs more trust than a small one.
