# Phase 1C targeted access and provenance log

Date: 2026-09-24. Searches were confined to the named Lin–Shi–Han/Lin–Han sequence, its direct citation links, and inspection of the supplied van Kekem–Sterk version. This is not a complete citation census. No contact with authors, purchase, theorem proof, or simulation was performed.

## Verified chain and exact primary links

| Source | Primary locator | Access result |
|---|---|---|
| Lin, Haipeng; Shi, Wenxin; Han, Jing (2021), Analysis of Enzymatic Regulatory Five-Element Model, CCC pp.6410–6415 | [IEEE](https://ieeexplore.ieee.org/document/9550151/); DOI 10.23919/CCC52363.2021.9550151; [proceedings contents](https://www.proceedings.com/content/060/060639webtoc.pdf) | Metadata confirmed; full article not obtained. |
| Lin, Haipeng; Shi, Wenxin; Han, Jing (2022), Comparison of Enzymatic Regulatory Network Topologies, CCC pp.5735–5740 | [IEEE](https://ieeexplore.ieee.org/document/9901543/); DOI 10.23919/CCC55666.2022.9901543; [proceedings contents](https://www.proceedings.com/content/065/065721webtoc.pdf) | Metadata confirmed; full article not obtained. |
| Lin, Haipeng; Han, Jing (2023), Comparison of Multi-Node Networks on Biological Properties, CCC pp.6823–6828 | [IEEE](https://ieeexplore.ieee.org/document/10239797/); DOI 10.23919/CCC58697.2023.10239797; [proceedings contents](https://www.proceedings.com/content/070/070536webtoc.pdf) | Metadata confirmed; full article not obtained. |
| Lin, Haipeng; Han, Jing (2024), What is special of “five” in biological regulatory networks?, Nonlinear Dynamics 112(9), 7477–7498 | [publisher](https://link.springer.com/article/10.1007/s11071-024-09374-5), references 37–39 | Subscription preview and reference list inspected; full main article not obtained. |
| Same 2024 paper, electronic supplement | [publisher-linked archive](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs11071-024-09374-5/MediaObjects/11071_2024_9374_MOESM1_ESM.7z) | Downloaded with network approval after sandbox DNS failure. Eight-page PDF and matching TeX inspected as reference material; no bundled code executed. |

The 2024 references 37, 38 and 39 are direct backward links to the three conference papers and a verified forward citation for each. The 2021 author-hosted record also lists those later works as citing papers, but publisher references take precedence. Main-text chronology or identity of models across versions is not inferred from these citations.

## Retrieval attempts and version pitfall

1. Exact-title and DOI queries located IEEE/proceedings records, the publisher page and author-upload records. IEEE body access returned tool fetch errors.
2. Author-upload URLs were checked: [2021](https://www.researchgate.net/publication/355326360_Analysis_of_Enzymatic_Regulatory_Five-Element_Model), [2022](https://www.researchgate.net/publication/364553851_Comparison_of_Enzymatic_Regulatory_Network_Topologies), [2023](https://www.researchgate.net/publication/374012845_Comparison_of_Multi-Node_Networks_on_Biological_Properties), [2024](https://www.researchgate.net/publication/378827996_What_is_special_of_five_in_biological_regulatory_networks). The 2021 record exposes no full text; other body retrievals returned cache/fetch/rate-limit failures. A browser attempt at the 2024 upload presented a device-check interstitial, which was not bypassed.
3. Indexed text under the **2022 title** actually begins with a **2024 uncorrected proof**, DOI 10.1007/s11071-024-09374-5, typesetting date 2024/2/29. Its §2 fragment mentions Eq.(1), but the complete equation was not legible in the retrieved fragment. It is not counted as a full reading of either article or attributed to 2022.
4. Direct publisher browser inspection confirmed that the 2024 body requires subscription/institution access. Its supplement link was public. Although the page described a PDF of 16.837 KB, the link actually delivered a 7z archive of roughly 20.7 MiB. Identification rests on the archive's title/author PDF and source, not the misleading size/format label.
5. A targeted Chinese citation search found the two directly connected primary leads below. No unrelated literature branches were pursued.

## Additional direct leads

- **林海鹏 (Haipeng Lin), 多子系统生克耦合模型的研究**, master's thesis, University of Chinese Academy of Sciences, Beijing, 2021. English rendering: *Research on Multi-subsystem Generation/Restriction Coupled Models*. [Official laboratory graduate list](https://lsc.amss.cas.cn/rcpy/bfbys/202601/t20260122_821421.html), 2021 table, row 18, confirms title, author, adviser 韩靖 (Jing Han), master's degree and July 2021. This indexed official entry is a catalogue locator; no thesis equation/page was inspected.
- **熊枫 (Feng Xiong), 张维波 (Weibo Zhang), 《黄帝内经》五行的“更贵更贱”解析**, 中医学报 / Acta Chinese Medicine 40(10) (2025), 2098–2103. DOI 10.16368/j.issn.1674-8999.2025.10.329. [Primary journal record](https://hnzk.cbpt.cnki.net/portal/journal/portal/client/paper/9157fc96ec760af7de59f31502e6850b). References **4, 5, 7** cite respectively the 2021 conference paper, the thesis and the 2024 article. Abstract and reference list inspected; embedded PDF viewer opened but supplied no readable article body, and browser content export was unsupported. Exact model/Hopf/Fourier/l1/comparator inventory remains unresolved. The abstract describes a five-variable enzymatic five-element simulation and adaptation, not a verified DM antecedent.

These leads are within the same priority question; they create no separate archival track. Neither title nor abstract resolves exact-model identity. No new direct equation conflict was established.

## Inspected 2024 supplement

All eight pages and the matching TeX were inspected; equation and graph pages 5–6 were rendered for visual verification. Exact source locators are S2 pp.2–3 Definition 1, S3 pp.3–4, S4 pp.3–5 Eqs.(D1)–(D9), S5 pp.5–6 Fig.S5, Table S2 pp.7–8. The audit records the limiting laws in D2/D5/D7, and keeps source claims separate from verification. The supplement's numerical studies were not rerun.

Archive SHA-256: `f53d9f5bf2a709d48ccd294762ee09ab69b1c815a4c06d478314d37bcb159e22`.

Supplement PDF SHA-256: `9de3d450f14a99abab47ebeebda9f466b16fafe442f46d0103240d045e31388e`.

The downloaded references remain outside the distributable project folder. None of their TeX, figures or full text is republished in the ZIP.

## Lorenz–96 evidence

The supplied `1704.05442v3.pdf` is the 55-page accepted manuscript. The Phase 1 source manifest preserves its fingerprint. Rechecked in this pass: pp.8–16 for statements and symbols; pp.33–38 for spectral/coincidence arguments; pp.38–46 for l1 contraction and sign; pp.46–47 for first-mode selection; the two-parameter section pp.14–18. These locators refer to this version only. The comparison does not transplant its proof into P05/P13.

## Stop

Priority remains not closed. The unresolved work is the named article/thesis body comparison, not a broad survey. Preserve this limitation in any later novelty wording; do not infer absence from missing access. No mathematical module has been promoted.
