# SKY-001: a world model that plans CAD and BIM builds part by part

**X post:** https://x.com/spisallyouneed/status/2112242023805964327  
**Author:** Sam Pasupalak (@spisallyouneed) · posted 2026-10-19 (UTC) · 14302 likes, 744 replies  

## What it is
Sam Pasupalak, who per his X bio is building Skyfall AI and was CEO of Maluuba (acquired by Microsoft), announced SKY-001, which Skyfall calls the first "engineering world model". Instead of predicting tokens, it turns a text prompt or a 2D sketch into an executable CAD or BIM construction sequence in four stages: generate several rough 3D options in parallel; recursively break the chosen design into parts, down to screws and fasteners; rebuild each part the way a designer would, as 2D sketch strokes followed by extrusions and cuts; then reassemble the parts hierarchically into an assembly viewable in standard CAD tools such as Autodesk Fusion. The post claims it is 51–125x faster and 150–210x cheaper than GPT-6 Astra and other frontier models on CAD and BIM tasks, with higher IoU, after 18 months of work. Per Skyfall's site and press coverage, it is a research preview with a waitlist and no public API yet, and all benchmark numbers are self-reported.

## Thread highlights
> **@SMishra61:** the hierarchical decomposition into parts is what i'd want to stress-test. generating a plausible assembly is one thing, but keeping dimensional constraints consistent across independently generated components seems much harder.

> **@WaldoDev13:** So did this "drop" or is it just a coming soon product with a waitlist?

> **@grok:** Performance claims (speed, cost, IoU vs GPT-6 Astra etc.) are entirely self-reported by Skyfall on their own benchmarks.

## Implications
- The interesting idea is the representation, not the model: output a buildable construction history (sketch, extrude, cut, assemble) instead of a mesh. That is what makes a result editable, which plain image-to-3D or text-to-mesh tools don't give you.
- For Blender/Unity agent workflows, the same split works today with LLMs: ask for a part hierarchy first, then generate each leaf as a short parametric script (e.g. Blender modifiers, or a CadQuery-style feature list), then assemble. Errors stay local to a part instead of breaking the whole model.
- For game props and kit-bashed environments, a part tree with named sub-assemblies doubles as LOD and collision structure: drop small leaves for distant LODs and use top-level parts as collision hulls, a cheap form of mesh compression.
- Treat the speed and cost claims as unverified until there is public access or an independent benchmark.
- **Experiment:** pick one hard-surface prop (a drone or a lamp), have an agent produce a part hierarchy as JSON, then generate each leaf as a separate Blender Python script with dimensions passed down from the parent; measure how often parts fail to fit when assembled, which is the exact weakness raised in the replies.

## Tags
`3d` `cad` `world-models` `models` `asset-pipeline` `research`
