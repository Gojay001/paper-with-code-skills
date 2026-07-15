# E-Commerce Video Candidate Pool

**Date:** 2026-07-15  
**Source:** `research/wiki/ECOMMERCE_VIDEO.md` + 76-paper wiki + recent primary-source search  
**Status:** no pilot run; scores are proposal review, not experimental evidence

| Rank | Candidate | Dominant contribution | Closest neighborhood | Jury | Decision |
|---:|---|---|---|---:|---|
| 1 | SKU-TraceBench | SKU-version-level benchmark and metric validation | E-CommerceVideo, OpenS2V-Nexus, ConsIDVid-Bench, ProductConsistency | 22/25 | KEEP |
| 2 | Evidence-Bounded Camera | calibrated identity-risk-constrained camera planning with abstention | ConsID-Gen, 3DreamBooth, CameraCtrl | 21/25 | REVISE / top method idea |
| 3 | Risk-Routed Product Lock | learned routing among retain/warp/insert/generate | PLACID, InsertAnywhere, SimInsert | 19/25 | REVISE / system backup |
| 4 | Product-Frequency Router | frequency/layer/timestep product condition routing | ConsisID, DreamActor-H1, InnoAds-Composer | 16/25 | DROP |

## Additional ideas not promoted

- **Affordance-conditioned demonstration:** product knowledge → hand-object motion. Too close to DreamActor-H1, DreamRelation and KD-CVG, while contact-physics validation is expensive.
- **Cross-shot SKU state graph:** track direction, open/closed state, quantity and prior actions across shots. Important, but Narrative Weaver already covers long-range planning; a final-video method would require a much broader system.
- **Commercial-intent reward:** use E-VAds/AD-MIR as generation critics. Cheap to prototype, but high reward-hacking risk and no evidence that offline intent scores cause trust or conversion gains.
- **CTR-aware personalized generation:** strategically important but depends on proprietary logs and severe exposure/position confounding; not suitable as the first reproducible study.

## Jury interpretation

The same-family independent jury treated scores as provisional. It explicitly rejected “more modules” as novelty: SKU-TraceBench must prove version-level discriminability; Evidence-Bounded Camera must learn calibrated risk rather than rewrite prompts heuristically; Risk-Routed Product Lock must learn the routing policy; Product-Frequency Router stays archived until causal routing evidence exists.
