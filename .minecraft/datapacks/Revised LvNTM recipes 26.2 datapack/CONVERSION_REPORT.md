# Pegado → NTM Next 26.2 datapack conversion report

Generated from `Pegado text(5).txt`, `oreDict.groovy`, and `ntm-next-neoforge-1.0.0+mc26.2.jar`.

## Result
- Minecraft Java Edition 26.2 data pack version: **107.1**.
- Recipe statements parsed: **122**.
- Recipe statements converted: **96**.
- Generated recipe JSON variants: **209** (including one mirrored-pattern companion).
- Existing NTM recipes disabled/replaced because the source calls `removeByOutput`: **149**.
- Source statements not converted: **26**.

## Custom ore-dictionary expansion
The custom entries actually used by the source were expanded to individual item/component ingredients rather than relying on the old CraftTweaker ore dictionary.
- `.22 LR` → 4 modern `hbm:ammo_standard_*` items.
- `.357` → 6 modern `hbm:ammo_standard_*` items.
- `.44` → 6 modern `hbm:ammo_standard_*` items.
- `.45` → 5 modern `hbm:ammo_standard_*` items.
- `.50 BMG` → 7 modern `hbm:ammo_standard_*` items.
- `5.56mm` → 4 modern `hbm:ammo_standard_*` items.
- `7.62mm` → 6 modern `hbm:ammo_standard_*` items.
- `9mm` → 4 modern `hbm:ammo_standard_*` items.
- `anyReinforcedPane` → 2 modern ingredient variants.
- `capacitorAptWire` → hbm:wire_fine_aluminum, hbm:wire_fine_copper. The old numeric metadata was converted to the corresponding modern wire material.
- `coloredPlatemetal` → 14 `hbm:platemetal` block-state variants.
- `deshPowder` → 3 modern ingredient variants.
- `flatStamp` → 6 modern ingredient variants.
- `grenadeShell` → 4 modern ingredient variants.
- `insert` → 9 modern ingredient variants.
- `ironAnvil` → 2 modern ingredient variants.
- `slidingBlastDoor` → 2 modern ingredient variants.
- `vacuumTubeAptWire` → hbm:wire_fine_carbon, hbm:wire_fine_tungsten. The old numeric metadata was converted to the corresponding modern wire material.

## Legacy metadata mappings used
- `hbm:circuit:0..17` were converted to the current named circuit items using the current NTM circuit registration order.
- `hbm:stamp_book:0..7` were converted to `hbm:stamp_book_printing1..8`.
- `hbm:weapon_mod_generic:0..17`, `weapon_mod_caliber:0..7`, and `weapon_mod_special:16..17` were converted using the current NTM enum names.
- `hbm:ammo_standard:<metadata>` was converted using the current `GunFactory.EnumAmmo` ordinal order.
- Old wire metadata `1300`, `2900`, `699`, `7400`, and dense-wire `7900` were mapped by material to the current named wire items.
- Colored platemetal metadata `1..14` was mapped to the current `minecraft:block_state.variant` colors.

## Semantics that are necessarily best-effort
- `.reuse()` / `.transformDamage()` cannot be reproduced by an ordinary vanilla crafting recipe. The generated recipes accept the tool but **consume it**; the source behavior would preserve/damage it.
- Old CraftTweaker NBT `charge: 2500000l` was translated to NTM's current `hbm:battery_charge` component for the RPA/NCRPA conversions.
- Potion NBT was translated to the modern `minecraft:potion_contents` component.
- The source's mirrored defuser recipe is represented by two shaped recipes (normal + mirrored).
- `removeByOutput` is emulated by overriding matching current NTM recipe IDs with an effectively unobtainable `minecraft:structure_void` ingredient.

## Not converted
- **line 382** — `item('hbm:mp_warhead_15_boxcar')` — unresolved key D: ore('container16000tritium')
- **line 690** — `item('hbm:insert_doxium')` — unresolved key A: ore('container1000estradiol')
- **line 759** — `item('hbm:shimmer_axe_head')` — unresolved key S: ore('plateTripleAnyResistantAlloy')
- **line 840** — `item('hbm:gun_autoshotgun_heretic')` — invalid key B: hbm:ducc
- **line 275** — `item('hbm:missile_taint')` — unresolved ingredient ore('container1000watz')
- **line 277** — `item('hbm:taint') * 4` — unresolved ingredient ore('container1000watz')
- **line 713** — `item('hbm:meteorite_sword_treated')` — unresolved ingredient ore('container1000radiosolvent') * 16
- **line 714** — `item('hbm:meteorite_sword_treated')` — unresolved ingredient ore('container16000radiosolvent')

missing
- **line 397** — `item('hbm:mp_stability_20_flat')` — invalid output {'id': 'hbm:mp_stability_20_flat'}
- **line 673** — `item('hbm:jetpack_glider')` — invalid output {'id': 'hbm:jetpack_glider'}
- **line 793** — `item('hbm:fabsols_vodka')` — invalid output {'id': 'hbm:fabsols_vodka'}
- **line 376** — `item('hbm:gun_b92')` — invalid ingredient ref hbm:gun_b93 from item('hbm:gun_b93')
- **line 377** — `item('hbm:gun_b93')` — invalid output {'id': 'hbm:gun_b93'}
- **line 340** — `item('hbm:sliding_blast_door_legacy')` — invalid output {'id': 'hbm:sliding_blast_door_legacy'}
- **line 341** — `item('hbm:sliding_blast_door_2')` — invalid output {'id': 'hbm:sliding_blast_door_2'}
- **line 362** — `item('hbm:sliding_blast_door_skin0')` — invalid output {'id': 'hbm:sliding_blast_door_skin0'}
- **line 363** — `item('hbm:sliding_blast_door_skin1')` — invalid output {'id': 'hbm:sliding_blast_door_skin1'}
- **line 364** — `item('hbm:sliding_blast_door_skin2')` — invalid output {'id': 'hbm:sliding_blast_door_skin2'}
- **line 369** — `item('hbm:sliding_blast_door_skin0')` — invalid output {'id': 'hbm:sliding_blast_door_skin0'}
- **line 370** — `item('hbm:sliding_blast_door_skin1')` — invalid output {'id': 'hbm:sliding_blast_door_skin1'}
- **line 371** — `item('hbm:sliding_blast_door_skin2')` — invalid output {'id': 'hbm:sliding_blast_door_skin2'}
- **line 13** — `item('hbm:lung_diagnostic')` — invalid output {'id': 'hbm:lung_diagnostic'}
- **line 87** — `item('hbm:defuser_desh')` — invalid output {'id': 'hbm:defuser_desh'}
- **line 112** — `item('hbm:det_n2')` — invalid output {'id': 'hbm:det_n2'}
- **line 136** — `item('hbm:det_bale')` — invalid output {'id': 'hbm:det_bale'}
- **line 149** — `item('hbm:spinny_light')` — invalid output {'id': 'hbm:spinny_light'}

## Installation
1. Put the ZIP in the world's `datapacks` folder.
2. Use `/reload` or create/load the world.
3. The pack is intended for NTM Next NeoForge on Minecraft Java Edition 26.2.

## Verification note
The pack was generated against the uploaded NTM Next 1.0.0+mc26.2 jar. The conversion was intentionally conservative where the old source refers to items/recipes that are absent from that jar; those are listed above instead of inventing replacement items.
