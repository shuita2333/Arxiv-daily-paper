# 🧠 大模型相关研究 | 2026年10月22日

> 本类共 **299** 篇论文：已确认 **275** 篇，待复核 **24** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-299](./part-06.md)

---

### 201. [BAIT: Can LLMs Find What Biases a Reader? A Benchmark for Cognitive Bias Triggers in News](https://arxiv.org/abs/2610.28092)

**<font color=#1a73e8>作者：</font>** Yousra Fettach, Tijl De Bie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persuasive writing exploits cognitive biases, recruiting a reader's mental shortcuts to shape belief, often without the reader noticing. We call the linguistic features exploiting such mental shortcuts cognitive bias triggers. As large language models (LLMs) increasingly mediate how people encounter news, summarizing it, ranking it, and answering questions over it, a natural question is whether they can recognize the features of a text that bias a human reader. We introduce BAIT (Bias Annotation In Text), a resource for detecting cognitive bias triggers in news. BAIT pairs a schema of nine triggers, each specified in an annotator codebook, with 50 English news articles annotated by trained annotators at the article and span levels and adjudicated into a gold standard. On this data we define two tasks, detecting which triggers a text contains and locating the spans that carry them. We then benchmark six frontier LLMs zero-shot and with three or ten in-context examples. The models approach human agreement on which triggers an article contains, but rarely recover its full set of triggers, and they reach less than half of human agreement in locating the passages that carry them. Moreover, they over-predict triggers that come with easy surface cues, and most of the passages they mark for these triggers are not triggers, yet carry the trigger's surface cue far more often than random text. These findings suggest that the evaluated LLMs respond to surface cues rather than to the mechanisms that make a passage manipulative. We release the schema, the codebook, standoff annotations, and the evaluation pipeline.

---


### 202. [ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](https://arxiv.org/abs/2610.28093)

**<font color=#1a73e8>作者：</font>** Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose ClawMMU, a protection layer that labels every piece of memory with its owner, scope, origins, and authority. ClawMMU checks these labels whenever content enters the model's context, is written to storage, returns from storage, or drives a tool call. Its central rule is that information may rise in authority, but authority never lifts itself. Because the checks depend on where content came from, not on what it says, memory attacks become classical protection faults that the harness stops even when the model is fooled.

---


### 203. [Reading Too Much Into It? Interpretive Preferences and Commitment in LLM Mentalisation under Ambiguity](https://arxiv.org/abs/2610.28105)

**<font color=#1a73e8>作者：</font>** Stephanie Fong, Yiwen Jiang, Qingyang Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for interpersonal advice, potentially shaping how users interpret ambiguous social encounters. Existing Theory of Mind evaluations typically rely on predefined answers, while uncertainty research overlooks LLMs' preferred explanations and confidence under psychological distress. To address these gaps, we introduce MentalLoom, a novel evaluation of LLM mentalisation comprising 604 ambiguous social episodes, matched depression and social anxiety disclosures, and four-turn dialogues with unchanged event evidence. Across eight LLMs, disclosures initially elicited more negative explanations overall but more positive narrator-directed interpretations. Scripted repeated questioning showed greater emotional support, stronger positive narrator-directed endorsement, and higher certainty without new event evidence. These findings show that user context can reshape interpretive preferences and commitment while the underlying ambiguity remains unresolved.

---


### 204. [Africa-Papers: A 10-Billion-Token Multi-Domain Academic Corpus for African Foundation Language Models](https://arxiv.org/abs/2610.28173)

**<font color=#1a73e8>作者：</font>** Mich-Seth Owusu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) depend fundamentally on the diversity, depth, and factual rigor of their pre-training corpora. However, contemporary foundational pre-training datasets (such as The Pile, S2ORC, and Dolma) exhibit a severe structural omission: African scientific, medical, legal, and agricultural scholarship constitutes less than 0.5% of global pre-training tokens. Consequently, state-of-the-art models suffer from systematic failure modes when reasoning about tropical epidemiology, localized smallholder agro-ecologies, regional economic governance, and indigenous linguistic structures. To resolve this representation deficit and advance African intellectual sovereignty in artificial intelligence, we introduce Africa-Papers, the largest curated multi-domain Pan-African academic pre-training corpus to date. Comprising over 844,807 full-text papers spanning 10.15 billion tokens across 879 Parquet shards, Africa-Papers unifies four primary scientific streams: (1) continental peer-reviewed journals indexed in DOAJ across 31 African nations, (2) the CGIAR CGSpace agricultural repository, (3) African-authored and African-focused STEM/AI preprints on arXiv, and (4) open-access international publications by scholars affiliated with African institutions indexed via OpenAlex. The entire corpus is processed into layout-aware, clean Markdown preserving section hierarchies, mathematical equations, and tabular data, accompanied by exact BPE token counts and a standardized 8-domain taxonomy. We release Africa-Papers openly on the Hugging Face Hub under the AfriSpeech organization to accelerate continual pre-training and domain evaluation for foundation models globally.

---


### 205. [Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge Graphs](https://arxiv.org/abs/2610.28176)

**<font color=#1a73e8>作者：</font>** Jiapu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often struggle with temporally grounded reasoning because their static parametric memory is misaligned with the dynamic evolution of real-world knowledge. Although RAG and Parameter-Efficient Fine-Tuning (PEFT) provide practical ways to enhance LLMs, they remain insufficient for temporal reasoning. Existing retrieval methods typically prioritize semantic relevance while overlooking temporal validity, event order, and evolutionary dependencies, resulting in evidence that is relevant in isolation but temporally fragmented. Meanwhile, conventional PEFT methods usually employ fixed and input-agnostic low-rank updates, making it difficult to capture time-dependent entity semantics and relation drift. To address these limitations, we propose Temporal Evidence-Parameter Co-Alignment (TEPCA), a framework for LLM reasoning over TKGs. TEPCA aligns LLM reasoning with temporal knowledge at both the evidence and parameter levels. At the evidence level, it introduces time-constrained Dynamic Relevance-Guided Path (DRGP) pruning to preserve globally coherent temporal paths, together with Mutual-Information (MI)-based pruning to retain query-informative local facts under temporal constraints. At the parameter level, it integrates Dynamic-Gated LoRA (DG-LoRA), a timestamp-conditioned low-rank adaptation mechanism that dynamically modulates the effective adaptation subspace according to temporal context. This design enables LLMs to better capture fine-grained entity evolution and time-dependent relation semantics while preserving parameter efficiency. Experimental results on two TKG benchmarks demonstrate that TEPCA achieves state-of-the-art performance. Additional evaluations of DG-LoRA on eight commonsense QA datasets further verify its general input-adaptive capacity, scalability across LLM backbones, and interpretability.

---


### 206. [Adaptive Pullback: Reweighting Supervision at Penalty Jumps in On-Policy Distillation](https://arxiv.org/abs/2610.28194)

**<font color=#1a73e8>作者：</font>** Guangyu Liu, Siyuan Gan, Shilong Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) supervises student-generated responses using sampled-token student-teacher log-ratios. A positive log-ratio penalizes a token that the student assigns higher probability to than the teacher, but its current value does not distinguish sustained high penalties from abrupt increases along a response. We examine these local changes by comparing consecutive blocks of tokens within the same response. Our diagnostic identifies penalty jumps, abrupt increases in average penalty that persist on held-out tokens. Across these jumps, penalties rise while teacher confidence decreases. We call this pattern penalty-confidence tension. Boundaries into high-penalty blocks do not exhibit comparable confidence changes, showing that local changes provide information beyond the current penalty value. Motivated by this observation, we propose Adaptive Pullback OPD (AP-OPD). At each detected jump, AP-OPD uses the preceding block as a local reference and uniformly scales all supervision coefficients in the following block so that its weighted average penalty matches the preceding block's original mean. This reference determines the scaling factor without an additional strength constant. AP-OPD improves performance on both mathematical reasoning and code generation.

---


### 207. [Learn to Modify: Self-evolving Multi-agent Refinement Framework for Conversational Text-to-Motion Generation](https://arxiv.org/abs/2610.28210)

**<font color=#1a73e8>作者：</font>** Jianan Li, Jiawei Zhao, Yangtao Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in text-to-motion generation, existing methods are commonly designed for single-shot generation. When users are dissatisfied with specific motion details, they are often forced to regenerate the entire sequence from scratch, which is computationally inefficient and potentially destroys previously established kinematic context. A practical generation system should instead support iterative user feedback and refine only the affected spatio-temporal regions while preserving the remaining motion. Therefore, we introduce a conversational motion generation paradigm that requires the system to coordinate instruction understanding, motion generation, localized editing, and quality assessment. Recent advances in LLM-driven multi-agent systems provide a promising foundation for such role-specialized coordination. To tackle these challenges, a Self-evolving Multi-Agent RefinemenT Framework (SMART) is proposed for conversational motion generation. Within SMART, to preserve semantic consistency, we design a semantic-guided masked motion editing mechanism, which precisely grounds natural language feedback into spatiotemporal motion regions to enable localized refinements without altering unedited regions. To reduce redundant exploration, we propose a memory-based self-evolving strategy that dynamically accumulates motion editing knowledge from interaction history and reuses past successful experience. Extensive experiments demonstrate that SMART effectively supports multi-turn conversational motion generation and enables efficient motion refinement.

---


### 208. [Region-Guided Food-Package Evidence Extraction and Abstention-Aware Draft R3337 Screening with Selective VLM Review](https://arxiv.org/abs/2610.28211)

**<font color=#1a73e8>作者：</font>** Mayimunah Nagayi, Alice Scaria Khan, Tamryn Frank 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Applying South Africa's draft R3337 warning criteria to food-package photographs requires nutrition, ingredient and product-form evidence. This study presents a region-guided evidence extraction and abstention-aware screening workflow for draft R3337. A three-class detector localises nutrition information panels, ingredient lists and product-identity regions, after which PaddleOCR and structured extraction recover nutrient values, ingredient evidence and product-form information. Recovered evidence is aggregated and assessed using deterministic draft R3337 rules. When evidence is incomplete, uncertain or conflicting, the workflow abstains through Review or Insufficient evidence rather than forcing an automatic outcome. For qualifying unresolved cases, a selective vision-language model (VLM) review stage using Qwen3-VL 8B Instruct reassesses unresolved evidence. Accepted evidence is merged and the same deterministic rules are reapplied. The workflow was applied to 442 products represented by 3,929 images. Evaluation used a manual validation set of 65 products. Before selective VLM review, 31 of 60 decidable products received automatic outcomes and 30 were correct, giving 51.7% coverage and 96.8% accuracy among automatic outcomes (selective accuracy). Selective VLM review resolved eight additional products, increasing coverage to 65.0%. Of 39 automatic outcomes, 38 were correct, giving 97.4% selective accuracy. The single false warning was retained from the rules-only workflow, while no unsafe warning omissions occurred after selective review. Evidence-level evaluation nevertheless identified incorrect VLM-recovered nutrition, ingredient and product-form evidence. These findings show that selective VLM review can recover unresolved evidence, while deterministic screening and explicit abstention remain necessary for reliable image-based draft R3337 screening.

---


### 209. [Can Language Models Get "Aphasia" From Neuronal Ablation?](https://arxiv.org/abs/2610.28214)

**<font color=#1a73e8>作者：</font>** Pratik Worah, Randall Bateman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Progressive neuronal loss is the hallmark of neurodegenerative disease, yet how loss of neurons shapes the pattern of cognitive decline remains poorly understood. Here we systematically ablate neurons (computational units) in language models spanning recurrent long short-term memory (LSTM) and Transformer architectures and apply limited fine-tuning as a simple proxy for compensatory plasticity. With whole-unit ablation, LSTMs degrade gradually with syntactic and semantic faculties declining in parallel across mild-to-moderate damage. By contrast, Transformers exhibit late threshold-like collapse under feedforward multi-layer perceptron (MLP) ablation and smoother sigmoid-like decline under attention-head ablation. Qualitatively, MLP-ablated models continue to make within-category semantic substitutions (semantic paraphasias) alongside rising non-responses, paralleling Wernicke-type aphasia, while attention-head ablation produces a trend toward loss of semantic specificity similar to the semantic variant of primary progressive aphasia (svPPA). These findings indicate that feedforward and attentional pathways have functionally distinct failure modes, suggesting that architecture-dependent failure profiles may offer new computational perspectives on aphasic syndromes and neurodegenerative diseases as an in silico model. Notably, early accuracy retention under Transformer attention-head ablation qualitatively parallels pre-symptomatic reserve before the 40--60% neuronal loss reported by Gomez-Isla et al. (1996) when clinical symptoms emerge in Alzheimer's disease, whereas the steadier LSTM decline parallels the symptomatic progression described by DeKosky and Scheff (1990) and Terry et al. (1991).

---


### 210. [TPO: Tri-level Distributionally Robust Learning for OOD Direct Preference Optimization](https://arxiv.org/abs/2610.28229)

**<font color=#1a73e8>作者：</font>** Chengtao Jian, Kai Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) minimizes empirical risk over observed preference comparisons, implicitly assuming that the training preference distribution matches the deployment preference distribution. In practice, this i.i.d. assumption often fails, as preference distribution shift exhibits a natural hierarchical structure across three levels: group-level shift, prompt-level shift, and preference-level shift. Such multi-level distributional mismatch poses a critical challenge for safe LLM deployment, yet existing robust DPO methods typically either model uncertainty over the joint preference distribution or focus on individual sources of shift, leaving the hierarchical structure of OOD preference shifts underexplored. We propose TPO, a tri-level distributionally robust framework for OOD preference alignment, which jointly models all three levels of distributional uncertainty through a hierarchically structured rectangular ambiguity set. By instantiating it with Wasserstein distance, we derive a tractable and interpretable objective that combines a closed-form preference-level margin penalty, prompt-level adversarial embedding perturbation, and worst-case group reweighting, each governed by an independent radius. We establish finite-sample convergence guarantees and empirically validate the effectiveness of TPO over existing robust DPO methods.

---


### 211. [PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis](https://arxiv.org/abs/2610.28264)

**<font color=#1a73e8>作者：</font>** Yuheng Zhang, Jie Zhang, Yuecong Min 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oddly Satisfying Videos (OSVs) can evoke strong viewer responses through repetitive motion, visual tactility, and ASMR-like sounds despite containing few explicit semantic emotion cues. This makes OSVs a challenging setting for Video Emotion Analysis (VEA), since most existing methods focus on semantic video content and under-model the physical sensory dynamics that shape viewer responses. To support Oddly Satisfying Video Emotion Analysis (OSVEA), we construct the Oddly Satisfying Video Dataset (OSVD), comprising 12,000 annotated 5-second clips. Each clip provides viewer-emotion labels under video-only, audio-only, and audio-visual conditions, together with explanations grounded in visual and acoustic sensory evidence. Building on OSVD, we propose PI-MLLM, a psychophysics-inspired multimodal large language model that integrates Modality-Specific Dynamics Alignment (MSDA) and Coalition-Based Audio-Visual Attribution (CAVA). MSDA uses auxiliary prediction objectives to align modality representations with visual motion and acoustic energy-onset dynamics. CAVA evaluates emotion scores across modality coalitions and applies Shapley attribution to identify the dominant modality and determine whether visual and auditory evidence is synergistic or conflicting. Experiments show that PI-MLLM improves both viewer-side emotion prediction and sensory-grounded explanation quality, suggesting the value of physical sensory cues to video emotion analysis.

---


### 212. [VGL-stGen: Learning a shared multimodal model for lung histology and spatial transcriptomics](https://arxiv.org/abs/2610.28266)

**<font color=#1a73e8>作者：</font>** Haenara Shin, Dongjoo Lee, Sungwoo Bae 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VGL-stGen is a multimodal large language model adapted from a pretrained medical vision-language model using paired lung H&E and spatial transcriptomics with single-cell references. Training integrates image-expression and expression-cell-type pairs, and gene-conditioned pseudo-labels transfer transcriptomic cell-type supervision to histology images. One deployed checkpoint supports thirteen evaluated tasks spanning tissue and cell-type classification, gene prediction and conditional expression completion from combinations of histology, cell identity and observed gene expression. Task-specific decoding produces categorical labels, gene lists and structured expression levels. For conditional completion, fixing queried gene identities and predicting their levels autoregressively improves structured prediction. Controlled adaptation shows that restricting supervision to requested expression-level tokens can further improve image-conditioned completion. Image-permutation experiments indicate that correctly paired histology adds information beyond observed expression. External classification relies partly on computational references with shared annotation lineage, and some H&E sources were exposed during cancer training or model development. Within these conditions, VGL-stGen demonstrates how a medical vision-language backbone can learn from spatial transcriptomics and histology to connect tissue morphology and molecular states through shared generative modeling.

---


### 213. [How Language Models Learn Taste: Brand Preference in LLMs](https://arxiv.org/abs/2610.28272)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Asked to name a running shoe brand, language models say Nike. Asked to recommend one, they say Brooks. This paper asks where models learn that taste. Across 102 models and 42 brand categories, the brand a model picks when recommending differs from the brand it names in 26. The field moves together to a shared recommendation. The Named brands are market leaders, and the Picked brands are mostly niche and specialist. Three open training pipelines show where this forms. Pretraining already attaches the recommended brand to advice. Supervised fine-tuning teaches the model to answer and mostly leaves the pick unchanged. Preference optimization (DPO) teaches the model which answer is better, and the pick moves in all three pipelines, by 11 to 24 points. The preference data contains almost no brands. DPO moves the model's judgments toward a second set of associations even when the preferred brand is not in the preference data, and the effect reaches beyond brands. Asked to choose a sauce, models switch from ketchup to pesto. We do not know exactly how these preferences arise. We suspect they come from the judge models that decide which answers count as better during preference training. For brands, a recommendation depends less on what a model knows about them than on whether they fit this taste.

---


### 214. [Forty Questions: Identifying a Language Model from One-Word Answers](https://arxiv.org/abs/2610.28281)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A model behind an API can be identified from its one-word answers to everyday questions such as "Name a sound" or "Name a poet". A model's profile records how often it gives each answer to each question. We attribute new answers to the model most likely to have given them. On a panel of 94 models, 40 answers identify the exact model 92.5% of the time, against 1.1% by chance. Profiles built through OpenRouter identified all ten models served by DeepInfra under blinded labels. A system prompt lowers accuracy by 6 to 16 points. We applied the method to 96 endpoints of 13 open models on OpenRouter, and 92 identify as the model they claim. Of the other four, one matches the claimed model with reasoning turned off. One serves Gemma 4 under the name Llama 4 Maverick: it names itself Gemma 4, and it is billed Gemma 4's token counts on every message. Two remain unresolved. Billing records also show context added to first-party models. Grok 4.7 is billed 1,247 input tokens for a one-line question that costs GPT-4o only 12 tokens, and five models state the current date without being billed for it. The questions come from a public census of model defaults, and the method costs cents per endpoint.

---


### 215. [Local Work, Global Progress: A Convergence Theory of AI Agent Collaboration](https://arxiv.org/abs/2610.28286)

**<font color=#1a73e8>作者：</font>** Ivan Ilin, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Teams of large language model (LLM) agents are increasingly applied to complex tasks, but their collaboration protocols are mostly designed empirically, without convergence guarantees. We formalize collaborative problem solving as block optimization: each agent improves one part of a shared solution, guided by its local objective plus a correction for how its changes affect the other parts. A coordinator checks every proposal against the global objective and merges proposals that do not interfere with each other. We prove linear convergence up to an error floor that vanishes when the corrections are exact. Interfering proposals can also be merged once their combination has been checked; the rate then depends on how well the proposals actually combine, not on worst-case interactions. With GPT-OSS-120B agents on robot routing, a three-agent team finds collision-free plans in every run, better than those of a single agent that controls all robots. On a larger routing task, a six-agent team completes its search about twice as fast as the single agent (in median). Merging the best checked combination of proposals, rather than only proposals that do not interfere, cuts the team's search time by about 30%. With constants measured on the runs, our convergence bound holds in every round and follows the observed progress. We also test the theory on query planning in SQLite and on a synthetic task.

---


### 216. [Reward Misspecification Degrades Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.28303)

**<font color=#1a73e8>作者：</font>** Tianyi Lorena Yan, John Hewitt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Monitoring the chain-of-thought (CoT) of language models (LMs) is a key strategy for detecting and preventing misbehaviors for AI safety. As such, it is critical to identify reinforcement learning (RL) practices that lead to unmonitorable chain-of-thought. One such practice may be unavoidable: reward misspecification. As RL environments become more complex, it is infeasible to have perfect verification, and models are rewarded for behaviors that are different from the true task intent. We show that reward misspecification alone already degrades monitorability. We create a testbed with pairs of true reward aligned with task intent and misspecified rewards that favor a different behavior, so that reward hacking can be induced by training and labeled verifiably. Across three models and three tasks, CoT monitorability remains low as models' hack rates increase: the CoTs keep reasoning about the task intent while the outputs violate the intent and get rewarded. To mitigate unmonitorability without prior knowledge of the true reward or the hack, we collect rollouts with diverse rewards across training steps and use a LM to infer a reward description. We then inject the description into the input, which teaches the model to verbalize the reward. This reward description training improves monitorability by an average of 24% or 42% absolute, depending on the metric, across all models and tasks, and yields CoTs that reason about the misspecified reward explicitly. Code is available at this https URL.

---


### 217. [From Abstraction to Action: DSLs for Natural Language Abstraction Interpretation and Execution](https://arxiv.org/abs/2610.28311)

**<font color=#1a73e8>作者：</font>** Amit Lisha, Reut Tsarfaty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural-language instructions often rely on high-level abstractions, such as asking an agent to ``stack blocks in a pyramid.'' Interpreting abstract instructions requires models to both identify the abstraction intended by the speaker, and unroll it into the many concrete actions that instantiate it. Language models struggle here: prior work has shown that performance degrades as the level of abstraction in the instruction rises. To bridge the gap between natural language abstraction and concrete actions, we propose to borrow from coding environments the notion of a {\em domain-specific language} (DSL), an explicit representation layer whose documented primitives name recurring abstractions that expand into concrete actions. We demonstrate the efficacy of DSLs for NL interpretation on \textsc{Hexagons}, a visually-grounded instruction-following task graded for abstraction. We further ask whether language models can induce such DSLs themselves from domain data. Our results show that while code generation consistently improves over direct inference, code generation over a human-curated DSL yields dramatic gains, up to 10 absolute F1 points, reaching the human skyline, with gains concentrated at {\em higher} abstraction levels. We confirm this pattern on the \textsc{Text2CAD} benchmark. At the same time, model-induced DSLs recover only part of this gain, remaining inconsistent across runs and short of their human-curated counterpart. Overall, the right representation closes much of the gap caused by high abstraction --- but inducing that layer of representation automatically is where models still fall short, and where we see a strong opportunity for the community to make progress.

---


### 218. [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](https://arxiv.org/abs/2610.28315)

**<font color=#1a73e8>作者：</font>** Masahiro Kaneko, Hiromi Arai, Timothy Baldwin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated record. Across four support models, memory raises response quality but also empirical leakage, the share of attribute values correctly inferred from the record, by a margin that widens over sessions. The cause is a loop in ordinary, non-adversarial assistance. Memory-conditioned responses carry earlier values forward, often as presuppositions, and users affirm them or leave them uncorrected, so that cues and the agent's own guesses become recorded values. The loop reinforces itself, and removing the agent's mentions of an attribute lowers its later disclosure about twice as much as single-turn effects predict. Users cannot leave it on their own, since correcting a value discloses the attribute, declining to discuss it shifts later predictions toward sensitive values, and incorrect values left in place become entrenched. The loop is best weakened at the agent's response. Instructing the agent not to state or presuppose attributes brings leakage to about the no-memory level while keeping most of the quality gains, whereas filtering or anonymizing what users say or what is stored gives up much of them.

---


### 219. [ABACUS: A Benchmark for Image Editing Models to Assess Object Category and Counting Under Scene Conservation](https://arxiv.org/abs/2610.28316)

**<font color=#1a73e8>作者：</font>** Aymen Lassoued, Angelique Loesch, Romaric Audigier  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing models can now add, remove a specified number of objects or change their category while preserving the scene. Yet these models often fail to produce the correct number, and these failures grow sharply as scenes become more complex and the requested count increases. Current benchmarks largely miss this problem: they score edits with holistic similarity metrics or with vision-language model (VLM) judges that are themselves poor at counting, so numerical errors go unnoticed or are graded incorrectly. As a result, the true numerical ability of today's editing models has never been accurately measured. We address this issue with ABACUS, a new benchmark, evaluation protocol and dedicated scoring metric for numerical image editing. Our protocol is judge-free: no VLM or MLLM scores an edit or counts objects (a VLM only confirms the category of rare ambiguous crops). Instead, it verifies each edit at the instance level against panoptic ground truth confirmed by detector consensus, checking both that the exact requested count was achieved and that the rest of the scene was preserved, across the add, remove and change operations. By evaluating leading image editors, our method reveals substantial numerical editing failures that worsen with increasing scene complexity and object count; failures that prior benchmarks often overlooked or misjudged.

---


### 220. [PACE: Plan, Attend, Check, and Emit for Training-Free Response Timing in Streaming Video Understanding](https://arxiv.org/abs/2610.28323)

**<font color=#1a73e8>作者：</font>** Siqi Guo, Yuxia Chen, Wenbo Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires a model to decide not only what to answer but also when to answer. Evidence arrives progressively, and recent benchmarks identify premature responses, issued before the queried event has concluded, as a recurring failure mode. Existing approaches often learn response timing through additional training, while training-free alternatives typically rely on scalar gating signals that do not explicitly represent when an answer becomes final. We organize chunk-wise streaming errors into three patterns: sampling variation can make an answer unstable, a stable answer may lack support in the observed video, or an answer may be supported by the current evidence while the event remains unfinished. We propose PACE (Plan, Attend, Check, and Emit), a training-free framework designed around these three failure modes. Given a question, PACE drafts a plan specifying what to observe and what will signal completion. As the stream unfolds, it invokes an off-the-shelf video LLM at informative moments, evaluates each draft for stability, grounding in its cited frames, and completion, and records verified observations in an event ledger. Experiments on ProactiveVideoQA and OVO-Bench Forward show that PACE improves over the official protocols by up to 5.9 average PAUC points and 6.2 average accuracy points across proprietary and open-source backbones, yielding state-of-the-art performance.

---


### 221. [Is Sycophancy a Form of In-Context Updating?](https://arxiv.org/abs/2610.28325)

**<font color=#1a73e8>作者：</font>** Itai Shapira, Myra Cheng, Hadas Orgad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Factual sycophancy, a language model's deference to a user's false beliefs, is usually understood as a bid for the user's approval at the expense of truthfulness. We argue that this framing over-emphasizes the user and propose viewing sycophancy as a failure within the broader and generally useful process of in-context updating, by which models revise their answers based on information supplied during an interaction. We support this view with behavioral and mechanistic evidence. First, models' responses to user claims sit within a broader pattern of source-sensitive updating. They revise their answers in response to information attributed to external sources as well, more so when it appears better supported, and their deference to the user persists even when no user approval is at stake. Second, the internal components that support deference to the user are also causally important for in-context updating more broadly. Our results suggest that factual sycophancy arises when in-context updating gives a user's assertion excessive weight relative to its evidence. Because sycophancy is embedded in this process, reducing it risks reducing useful updating as well, a trade-off that calls for evaluations measuring both behaviors and mitigations that decouple them.

---


### 222. [DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](https://arxiv.org/abs/2610.28340)

**<font color=#1a73e8>作者：</font>** Atharva Thakur, Abulhair Saparov, Bruno Ribeiro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents nor parametric knowledge supports an answer. We introduce DeclineCraft, a dynamic abstention benchmark whose unanswerable questions target Minecraft feature additions after a corpus cut-off, with audits of possible parametric exposure. Later cut-offs support evaluation of future models. Across 27 LLMs, we measure Correct Abstention Rate (CAR; how often models acknowledge insufficient knowledge on unanswerable questions), Answerable Attempt Rate and Answer Accuracy. We find that (1) single-shot retrieval significantly raises CAR in 38 of 40 configurations (model and thinking setting) versus no retrieval. (2) Iterative RAG, in which the model self-assesses its context and can request up to two further retrieval rounds, significantly lowers CAR versus single-shot RAG in 30 of 40 configurations (mean 46.4%), with little change in Answer Accuracy (68.5% to 69.3%). Adding query rewriting and reranking to hybrid (dense & sparse) retrieval lowers CAR for all 12 models tested. (3) Larger models answer more accurately (Spearman $\rho = +0.60$ with total parameters), but neither model size nor release date shows a significant association with CAR. (4) Without retrieval, enabling thinking on the same weights lowers CAR significantly for 8 of 13 models (by 14% points on average), and the responses shift from acknowledged uncertainty to premise denial.

---


### 223. [Auto-Director: Leveraging Multi-Agent Collaboration for Autonomous Video Editing](https://arxiv.org/abs/2610.28346)

**<font color=#1a73e8>作者：</font>** Yuxia Chen, Wenbo Zhu, Yangguang Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous video editing from open-world resources remains a challenging problem in multimedia content creation. Retrieval-based methods are constrained by fixed source material and lack creative flexibility, while generative models struggle with long-horizon coherence and often diverge from user intent. Both paradigms fail to replicate the structured, multi-stage reasoning that underlies professional post-production. To address these limitations, we present Auto-Director, a tool-augmented multi-agent framework that mirrors professional editorial workflows: a Planning Agent decomposes abstract topics into fact-grounded scripts via retrieval-augmented planning; a Material Agent indexes open-world footage through shot segmentation and visual tagging; an Editor Agent assembles semantically aligned clips with MLLM-driven spatial adaptation; and a Critic Agent governs an iterative Reflect-and-Revise loop that checks scene-level alignment and pacing. To rigorously evaluate this new paradigm, we introduce VEdit-Bench, a benchmark of 100 expert-curated topics with human-annotated Golden Scripts and a five-dimensional metric suite covering Narrative Logic, Factual Accuracy, Semantic Alignment, Compositional Quality, and Stylistic Cohesion. Extensive experiments demonstrate that Auto-Director significantly outperforms baseline methods in both automated metrics and human evaluation, effectively bridging the gap between amateurs and professional-grade video production.

---


### 224. [Gated Prototype Transfer for Zero-Support Medical Vision Language Model](https://arxiv.org/abs/2610.28350)

**<font color=#1a73e8>作者：</font>** Sumaiya Fazal, Rizwan Qureshi, Laleh Behjat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic few-shot adaptation of medical vision-language models (VLMs) can leave low-prevalence classes without any labeled support. The training-free SS- Text+ solver remains operational in this setting, but its zero-support prototypes receive no visual adaptation and fall back to a purely textual class prototype. We in- troduce Gated Knowledge-Guided Prototype Transfer (GProtoT), a pre-repulsion module that transfers supported-class visual residuals to missing classes using VLM similarity and an ontology-based clinical distance. A validation-free evidence gate scales transfer based on semantic relevance and residual agreement, thereby limiting unsupported extrapolation. In 50 paired realistic one-shot trials on MESSIDOR with FLAIR features, severe and proliferative diabetic retinopathy were absent from every support set. Relative to SS-Text+, gated ProtoT improved missing-class recall by 5.23 points, average class accuracy by 1.37 points, and the missing/supported recall harmonic mean by 1.83 points. It reduced negative- transfer frequency from 46-48% for ungated transfer to 2%, while at the cost of reductions of 1.20 percentage points in supported-class recall and 0.45 percentage points in top-1 accuracy. These results indicate that evidence-based gating provides a safety mechanism for the knowledge source. GProtoT is based on SS- Text+ and requires no gradients, validation data, or additional model inference, of- fering a low-compute path toward accountable adaptation under incomplete clini- cal supervision. Code is available: this https URL

---


### 225. [S-Agent 2.0: Spatial Reasoning with a General Coding Agent](https://arxiv.org/abs/2610.28354)

**<font color=#1a73e8>作者：</font>** Rui Gong, Ruoyu Wang, Yalun Dai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pass. Even so, on many questions the tools return the right evidence and the model still does not arrive at the correct answer: the gap between model and tools, where raw readings become usable conclusions, is left unfilled. We present S-Agent 2.0, a spatial reasoning agent that equips an off-the-shelf general coding agent with a command-line perception toolkit, and we design the interface around one principle: help the VLM close the evidence loop: acquire scene evidence, remember it in a persistent scene memory, and interpret each reading in plain spatial language. This design keeps the full flexibility of a coding agent, and every reading it acts on stays grounded in the tools' geometry. On MMSI-Bench and ReVSI, the toolkit improves a strong open-source model, Qwen3.8-27B, by +13.9 and +20.5 points over the same agent without tools, and a strong closed-source model, Gemini-3.8-Flash, by +11.2 and +9.6 points. With the open backbone S-Agent 2.0 reaches 66.5 on MMSI-Bench and 82.3 on ReVSI, ahead of the specialized system SpatialClaw on the same backbone (62.6 and 74.5), and with Gemini-3.8-Flash it reaches 74.1 and 90.5 against its 67.0 and 79.7. Both tool gains shrink as the backbone grows more capable, but SpatialClaw's shrinks far more on ReVSI, from +13.2 to +2.7, while ours stays at +9.6. S-Agent 2.0 also works across different general coding agent harnesses, such as Codex and Claude Code.

---


### 226. [Beyond the Point Mass: Acceptance-Derived Weights and Distributional Losses for Speculative Decoding](https://arxiv.org/abs/2610.28355)

**<font color=#1a73e8>作者：</font>** Tianyu Wu, Zhuohan Wang, Jonathan Geuter 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In speculative decoding, a lightweight draft model proposes tokens that the target model verifies in parallel, speeding up generation without changing the target distribution. D-PACE (Wu et al., 2026) trains such drafters with a loss that weights each position by its contribution to the expected accepted length. Both its weights and its cross-entropy (CE) loss use only the draft's probability of the recorded target token, treating the target as a point mass. Under rejection sampling, however, a sampled draft token is accepted with probability equal to the overlap of the draft and target distributions, one minus their total variation (TV). We derive D-PAL (Dynamic Position-wise Acceptance Loss) from the exact expected accepted length, using this overlap as the acceptance signal. This yields overlap-based position weights with log acceptance (LA) as the per-position loss, and the objective reduces to D-PACE for a point-mass target. Since the weights are detached, any per-position loss can replace LA in practice. We show that forward KL divergence and Rényi divergence of order 1/2 match or exceed LA, and that Rényi-1/2 provably bounds the true acceptance rate from above and below. Replacing CE with Rényi-1/2 improves acceptance length under both D-PACE's weights and ours. On six benchmarks with a Qwen3-4B target, D-PAL raises mean acceptance length over D-PACE from 4.50 to 4.57 at T=0 and from 4.20 to 4.28 at T=1, and consistently achieves higher throughput at both temperatures.

---


### 227. [CountVideoBench: A Benchmark to Evaluate Prediction Biases on the Object Counting task by Video-Language Models](https://arxiv.org/abs/2610.28356)

**<font color=#1a73e8>作者：</font>** Marc Chapus, Carlos Crispim-Junior, Véronique Eglin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object counting in videos remains a poorly characterized capability of multimodal large language models. Counting questions are included in many existing VideoQA benchmarks, but the ground-truth count distributions in these benchmarks are heavily skewed toward small values. Across the nine benchmarks we survey, the median ground-truth count is at most five, and the three most frequent values together account for between 45% and 93% of the videos. The resulting mean accuracy is then dominated by the most frequent counts; a value-dependent bias at a rare count contributes negligibly to the average and remains invisible. We introduce CountVideoBench, a benchmark of 2,600 synthetic videos covering 26 cardinalities in the interval [5, 50] (100 videos each), grouped into six clusters of consecutive counts that span the range while enabling near-neighbor comparisons. Each video contains a single class of static objects under a controlled camera motion, removing object motion and reducing recognition as confounds. We evaluate sixteen video-language models from nine architecture families in a zero-shot setting. No model exceeds 27.6% Exact Match. The dependence of accuracy on cardinality varies across models, ranging from monotonic decline to a non-monotonic peak-and-collapse pattern, which rules out increasing difficulty with cardinality as the dominant explanation of counting failure. Every model further concentrates its predictions on its own set of preferred integers, with accuracy peaks coinciding with these values and collapsing at adjacent counts. These findings highlight the need for balanced, diagnostic counting benchmarks to reliably assess this fundamental visual capability.

---


### 228. [FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents](https://arxiv.org/abs/2610.28361)

**<font color=#1a73e8>作者：</font>** Zijun Dou, Kun Luo, Chaofan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search trajectory: agents may anchor on an incorrect candidate, collect partially supporting evidence, overlook contradictions, and accumulate errors that misguide subsequent reasoning. We propose FALCA, a falsification-aware framework that formulates deep search as a propose-falsify process. FALCA adopts a collaborative Searcher-Falsifier architecture, where the Searcher proposes candidate answers or sub-answers, while independent Falsifiers actively seek counterevidence, check unmet constraints, identify conflicts, and produce concise falsification reports for research-state revision. To strengthen this loop, we introduce falsification-aware training, combining SFT warmup on falsification trajectories with agentic RL based on parallel rollouts and hierarchical credit assignment over research stages, state transitions, and actions. Experiments on five search benchmarks show that FALCA improves long-horizon deep search performance over backbone and harness ablations, while reducing confirmation bias and error accumulation through more effective falsification and research-state revision.

---


### 229. [Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](https://arxiv.org/abs/2610.28364)

**<font color=#1a73e8>作者：</font>** Abhishek Rai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-secureRAG, a roughly 0.5B-parameter small language model that acts as a semantic firewall between retrieval and generation. It jointly evaluates the user query and retrieved context, classifying the pair as safe, suspicious, or malicious. The model is trained using a teacher-judge-student pipeline: a 35B teacher generates 5,233 examples across four attack families, and an independent 120B judge re-labels them, achieving 95.0% agreement before student fine-tuning. On a held-out in-distribution test set, the model achieves 0.994 detection recall at a 0.026 false-positive rate and a 0.006 attack-success-rate proxy, outperforming a regex baseline, a public prompt-injection classifier, Llama Guard 3 1B, and its untuned version. Prompt-Guard-86M reaches 0.900 recall but has a 0.690 false-positive rate. On a judgment-flip test, where the same sentence is benign or malicious depending on context, the model correctly classifies both cases 75% of the time, outperforming the compared baselines. Ablations indicate that retrieved context carries the main attack signal, while query-context consistency reduces false positives. Single-request latency is 293-404 ms, above the target of 100 ms, while amortized throughput latency is 37 ms under batching. On the external PoisonedRAG benchmark, recall falls to near zero, indicating that fluent fact-poisoning attacks lie outside the detector's instruction-consistency threat model. We report this limitation alongside the in-distribution results. The model, data-generation pipeline, and evaluation harness are released open source.

---


### 230. [Relative Representations Enable Portable White-Box Monitoring Across Language Models](https://arxiv.org/abs/2610.28366)

**<font color=#1a73e8>作者：</font>** Tim Bakker, Christos Louizos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Independently trained autoregressive language models often acquire similar capabilities, but it remains unclear whether their internal representations organize behaviorally relevant information in compatible ways. We show that models do in fact organize information similarly by using specific behavioral probes that operate on compatible representations. This unlocks portable white-box monitoring: a probe developed and validated on one model can be reused when the model changes, without requiring labeled target data. To overcome incompatible native activation coordinates, we express each example through its angular distances to a shared set of anchors. We introduce a global anchored construction that summarizes information from all transformer layers and removes model-specific layer selection, so the same frozen probe can be straightforwardly applied to another model. We evaluate cross-model probe transfer across monitoring tasks on trivia datasets, safety monitoring, and mathematical reasoning. On average, transferred global anchored probes preserve at least 85% of same-model probe AUROC over chance. Anchored probes also support transfer to related datasets, remain robust across model scale and prompt changes, and retain performance better than standard probes after model updates. Transfer is nevertheless task- and target-dependent and can fail even when the monitored property remains strongly decodable in the target model. Overall, global anchoring reveals substantial task-relevant compatibility across independently trained models and provides a practical basis for portable white-box monitoring.

---


### 231. [Don't Skip the Baseline: A Controlled Comparison of Dynamic Expert Skipping in MoEs](https://arxiv.org/abs/2610.28369)

**<font color=#1a73e8>作者：</font>** Jakob Steimle, Thomas Elsken, Daniel Ehrhardt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of work proposes dynamic expert-skipping methods for Mixture-of-Experts (MoE) models that adjust the number of experts activated per token during inference, aiming to preserve model quality while further reducing the number of active parameters. These methods have added calibrated importance scores, inter-expert similarity metrics, or learned per-token allocators in order to identify experts to skip. However, different calibration regimes, different reductions in the effective number of experts, and evaluation suites make comparisons difficult. We classify four representative prior methods into a unified taxonomy and benchmark them against a natural, simple baseline: statically reducing the number of experts $k$ (i.e., same reduced $k$ across all layers and tokens). We provide a fair comparison of these methods at matched expert-compute budget, on two modern MoEs (Gemma4-26B-A4B and Qwen3-30B-A3B) in a text-only setting and a contemporary vision-language model (Qwen3-VL) in a multimodal setting. Surprisingly, we find that the simple baseline is hard to outperform consistently across models, modalities, benchmarks, and calibration settings. The methods we benchmark often underperform the baseline and achieved gains, when present, are minor. We further find that the effective $k$ achieved (or optimized for) in calibration can diverge from the effective $k$ in testing, resulting in over- or under-estimating the compute at inference time. Based on these findings, we recommend a calibration-free per-modality static $k$ reduction and validate this on a held-out model and modality. We further argue that a static control at matched measured compute is the baseline any dynamic skipping method must beat.

---


### 232. [RACE: Learning Multimodal Search through Referential Abstraction and Compositional Evidence](https://arxiv.org/abs/2610.28382)

**<font color=#1a73e8>作者：</font>** Eric Tao, Minhao Sun, Liyan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training multimodal search agents requires tasks that make visually grounded search necessary for determining the answer. Textual identity clues and unused target evidence allow shortcuts in synthetic questions, weakening supervision for visual search and evidence integration. We propose RACE, an image-conditioned task synthesis framework that constructs dependencies from images to targets and from target-specific evidence to answers. Referential Abstraction (RA) replaces identity-revealing text with specific visual references or ambiguous relational references resolved by searching among depicted candidates. Compositional Evidence (CE) links retrieved facts about multiple entities in one image or entities from different images into joint questions whose answers require every designated contribution. Both operations also apply to images found during search, allowing new visual observations to determine subsequent search targets or supply answer evidence. Fine-tuning Qwen3.5-27B on only 12K teacher-generated trajectories from RACE raises average accuracy across ten multimodal benchmarks from 53.5 to 56.0, a relative improvement of approximately 4.7% over the matched base agent. Our code, data, and model will be publicly available.

---


### 233. [VisualEvolve: A Skill Self-Evolution Framework for Visual Reasoning](https://arxiv.org/abs/2610.28386)

**<font color=#1a73e8>作者：</font>** Jiawei Wang, Yucun Li, Xueqi Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual tool use enables vision-language models (VLMs) to acquire task-relevant evidence, but its effectiveness can be limited by predefined visual operations and the tool-use strategies learned during training. Representing these operations and strategies as reusable external skills allows them to be refined through self-evolution without updating model parameters. However, skill refinement can introduce performance regressions. Meanwhile, inspecting accumulated task execution trajectories together with skill evolution history may lead to evolution evidence overload. To address these challenges, we propose VisualEvolve, a self-evolving framework that evolves executable visual operations and tool-use strategies for VLMs through a Select--Execute--Evolve--Evaluate cycle. Skill-Library Snapshot Selection uses performance on a fixed validation set disjoint from execution tasks to select an effective historical snapshot for subsequent evolution, limiting the propagation of performance regressions. Progressive Evidence Access (PEA) guides capability-gap diagnosis through a coarse-to-fine hierarchy comprising the Skill-Performance Report, Evolution Log, Trajectory Summaries, and relevant raw trajectory segments. Across four VLM backbones and six evaluation sets from three benchmarks, VisualEvolve improves over the Initial Skill Library in 23 of 24 settings, with a maximum gain of 15.1 percentage points on VisualProbe Hard using Qwen3.5-Plus. Ablation studies support the contributions of Snapshot Selection and PEA, while further experiments show that skills can be improved using experience from different data settings and directly reused across backbones. Moreover, VisualEvolve enables effective skill self-evolution with over an order of magnitude fewer task-solving trajectories than estimated for representative RL-based methods.

---


### 234. [Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group Rescaling](https://arxiv.org/abs/2610.28388)

**<font color=#1a73e8>作者：</font>** Fangcong Yin, Ming Yin, Tanvi Bhandarkar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents are commonly trained with RLVR, but the sparse nature of typical RLVR rewards makes credit assignment challenging, especially for long-horizon tasks. We propose Self-Credit, an end-to-end agentic RL method that creates dense supervision signals from sparse outcome rewards using self-generated credit assignment via intra-group rescaling. Self-Credit builds on group-based RL with three components. First, during its rollouts, the policy model generates summaries with citations to earlier turns containing critical evidence, which serve as self-generated credit. Second, we refine this model-generated credit with intra-group rescaling, which compares cited actions across successful and failed rollouts for the same prompt. This approach uses group-level agreement and disagreement to remove undeserved credit and further emphasize credit assigned to critical actions. Third, advantage reweighting uses the rescaled credit weights to update the advantages of the cited turns. On BrowseComp-Plus, Self-Credit improves over the base models by 37.0 and 36.2 points on Qwen3 8B and 32B respectively, and outperforms the strongest agentic RL baselines by 8.5 and 5.6 points, respectively. Self-Credit also improves over the strongest baselines by 4.9 points on GAIA and 4.7 points on xBench-DeepSearch. Analyses show that self-generated credit provides useful signals for selecting critical actions, and that intra-group rescaling, especially on failed rollouts, is important across model scales.

---


### 235. [When Copying Is Hard: Copy-Constrained Decoding for Exact Span Reproduction](https://arxiv.org/abs/2610.28393)

**<font color=#1a73e8>作者：</font>** Jinghui Zhang, Lang Gao, Zongfang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Precisely reproducing a target span verbatim within a long context is a fundamental capability test for LLMs: even when the target string is present in context, models often still drift within the span or fail to stop correctly, revealing limitations in source grounding and boundary control. This capability has broad practical relevance. For instance, code generation often requires embedding sensitive strings such as API keys exactly as they appear in context. In this work, we construct a benchmark to test exact span reproduction ability across contracts, scientific literature, code, and random sequences, and find that current models still make surprisingly frequent errors. To address this, we propose CopyGen, a lightweight copy-constrained plugin for frozen LLMs that turns copying from a byproduct of next-token prediction into a controlled process. Our key idea is to decompose copying into three distinct decisions: when to copy, how far to copy, and when to stop. Concretely, CopyGen first determines whether to enter copy mode, then predicts a tentative copy length, and finally verifies the generated span token by token. During verification, we adaptively adjust the logits of copy continuation tokens to incentivize or suppress continuation, and emit only the longest valid prefix. Across three LLM backbones and four benchmark tasks, CopyGen improves average exact match by 35% relative without model finetuning, and integrates seamlessly with SFT to further improve it by 4%, while substantially accelerating generation. These results suggest that reliable exact copying is not something LLMs obtain for free, but a decoding-time control problem that requires explicit modeling. Code is available at this https URL.

---


### 236. [DIVE: Benchmarking Full-Duplex Interaction with Visual Engagement in Continuous Streams](https://arxiv.org/abs/2610.28405)

**<font color=#1a73e8>作者：</font>** Yuhang Chen, Guangyue Liu, Shilong Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models (MLLMs) have substantially improved spoken interaction and video understanding. Existing online and streaming benchmarks primarily assess causal multimodal perception through timestamped question answering, whereas real-world interaction requires models to continuously identify task-relevant multimodal cues and decide whether, when, and how to respond. This leaves open how well current models can sustain real-time interaction throughout an evolving multimodal stream. To address this gap, we introduce DIVE, a benchmark for evaluating full-duplex interaction with visual engagement under continuous and realistic multimodal streams. It organizes six tasks into three complementary interaction scenarios. (1) Proactive Intervention evaluates whether models can identify emerging visual or semantic cues and intervene at the appropriate moment. (2) Continuous Engagement evaluates sustained participation through continuous visual tracking and visually grounded query interaction. (3) Interaction Coordination evaluates how models coordinate listening and speaking under overlapping and multi-party interactions. DIVE contains 525 audio/video samples with fine-grained human annotations and precise temporal metadata. Its evaluation protocol separates response quality, participation decisions, and response timing. We evaluate representative real-time models using response quality, window response rates, and reaction latency. Experiments show that leading real-time models achieve sub-second average response latency, yet their average window response rates remain at or below 53.77%. Response quality varies substantially across models and tasks, with adapting ongoing responses to newly arriving information remaining particularly challenging. We hope DIVE facilitates progress toward more natural and capable real-time multimodal interactive systems.

---


### 237. [The Instruction Tax on Factual Recall: Base Models Can Beat Their Instruction-Tuned Counterparts](https://arxiv.org/abs/2610.28407)

**<font color=#1a73e8>作者：</font>** Christophe Khalil, Aya Mourad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our solution to the AKBC LM-KBC 2026 Shared Task, where we achieved a score of 0.6836 on the official leaderboard, more than double the baseline of 0.2964. This task requires generating all possible objects for subject-relation pairs using a language model with up to 32 billion parameters, with no retrieval or fine-tuning involved. We show that the prompting methodology is as important as the model architecture: while the instruction-tuned model version achieves 0.5681 with its chat interface, the base model achieves 0.6836 when prompted using text completion. Thus, instruction tuning decreases factual recall; we refer to this effect as the instruction tax, which is caused by the model's weights rather than the prompting method. Our final solution is fairly straightforward: we prompt the base model with some examples from the training data, generate 64--256 outputs, and retain only the repeated ones. Two specialized methods are then applied for each relation: one improves the recall of large answer sets, and the other verifies a person's vitality before predicting their place of death.

---


### 238. [Rewards for Budget-Aware Multi-Turn Agents That Adapt to Arbitrary Test-Time Constraints](https://arxiv.org/abs/2610.28409)

**<font color=#1a73e8>作者：</font>** Tom A. Lamb, Adam Golinski, Eleonora Gualdoni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model agents are often given an inference budget and asked to maximise success within it. A multi-turn agent has to allocate this budget across many environment interactions. An external harness can enforce the budget, but it remains unclear whether the agent itself can learn when and how much to spend. We ask whether agents can learn this allocation across dynamically specified budgets and which rewards best teach this behaviour. We adapt existing length penalties to budget constraints spanning multiple resource types, introduce new reward formulations, and compare eleven objectives in a shared training pipeline. We train Qwen3.5 models at 4B and 9B on AppWorld with budgets over tokens, API calls, and environment steps, and on the BabyAI gridworld with turn budgets. We train a separate policy for each environment and resource type, with each policy trained across budget values. Training with rewards that penalise overspending substantially improves within-budget success and natural compliance over untrained models and over training on task success alone, with agents learning to adapt their resource use to stated budgets and task difficulty. These gains extend to unseen budgets and, zero-shot, to a shifted task distribution and a new benchmark. Reward objectives trade off success within budget and natural compliance. A sigmoid penalty for overspending most often achieves the highest within-budget success at an individual budget, while a fixed negative reward for overspending generally yields the strongest natural compliance. Combining penalties for overspend frequency and magnitude gives the smallest average gap to the best method at each budget. Overall, we show that a single agent can learn to allocate resources across turns and adapt its behaviour to user-specified budgets using budget feedback without external budget-allocation controllers.

---


### 239. [A Multi-Agent Framework for Automated Machine Learning with Evidence-based Planning for Medical Image Analysis](https://arxiv.org/abs/2610.28410)

**<font color=#1a73e8>作者：</font>** Yiqing Shen, Mathias Unberath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has become the default tool for medical image analysis, driven by the open-source movement. However, achieving the best performance on a given task remains difficult, with architecture selection and hyperparameter optimization (HPO) still considered "more of an art than a science". Automated machine learning (AutoML) automates parts of model training, yet helps little in medical imaging: general-purpose approaches lack medical architectures and preprocessing, and medical-focused ones demand engineering expertise and remain confined to narrow tasks such as 3D segmentation. We introduce MedicalMLOmni, a multi-agent AutoML framework that automates model training for diverse single- and multi-modal medical tasks through a natural language interface. Specifically, MedicalMLOmni performs evidence-based planning by retrieving published results to guide model selection and configuration, and employs parallel HPO where multiple agents explore adjustment strategies concurrently. MedicalMLOmni achieves the best score on 19 of 20 benchmarks; PMC-VQA is the exception, where a vision-language model with broader pre-training leads. Backbone-matched controls attribute the gains to the framework, not the backbone. By removing coding requirements, MedicalMLOmni lowers the barrier for domain experts with rich datasets but limited engineering expertise.

---


### 240. [Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416)

**<font color=#1a73e8>作者：</font>** Zhenghan Chen, Zekai Shao, Xin Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Code-based video generation offers fine-grained control, targeted editing, and component reuse compared with direct video generation. This approach requires multimodal large language models (MLLMs) to translate visual and temporal requirements into executable programs that produce complete videos. However, existing code-based benchmarks primarily target specialized tasks, leaving complete video creation across diverse creative categories and input modalities insufficiently evaluated. We introduce Code2Video-Compass, a general-purpose benchmark for code-based video generation across text-to-video (T2V), image-to-video (I2V), and video-to-video (V2V) settings. Code2Video-Compass comprises 2,104 tasks spanning 10 categories, 24 subtypes, and three complexity dimensions covering construction, dynamic animation, and state dependency. It combines tasks curated from textual instructions and visual references with corresponding T2V, I2V, and V2V tasks derived from complete professional and user-created videos. We propose a dual-level evaluation framework combining 12 objective metrics and five subjective metrics. Objective evaluation covers operational performance, video quality, text-video alignment, and reference fidelity, while subjective evaluation uses an MLLM judge to evaluate instruction following and holistic video quality. Extensive evaluation of 15 recent proprietary and open-weight MLLMs from nine families reveals that even leading models face challenges in reliably generating high-quality complete videos aligned with textual and visual requirements, with performance generally declining as construction, dynamic animation, and state-dependency complexity increases. We anticipate that Code2Video-Compass will advance reliable, coherent, and controllable code-based video generation and inspire broader progress in programmatic visual creation.

---


### 241. [DISTRACT: Degradation-Indexed Study of Textual Reference Across Competing Targets](https://arxiv.org/abs/2610.28419)

**<font color=#1a73e8>作者：</font>** Dan Zlotnikov, Ohad Ben-Shahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language trackers (VLTs) accept descriptions intended to assist tracking, but accepting text does not establish that its content changes tracking decisions, particularly as visual evidence deteriorates. We introduce DISTRACT, a matched-intervention benchmark that holds video, target, and distractor fixed while crossing four text priors with four image degradations along a controlled severity axis. We evaluate five VLTs on four datasets using behavioral contrasts, layerwise representation probes, and activation patching. Molmo2 and JointNLT exhibit directed text use. Some effects contract under degradation, whereas others show no significant endpoint change after multiplicity correction. UVLTrack, MMTrack, and DUTrack respond only weakly to changes in text semantics, with no directed behavioral effect surviving FDR correction in the tested settings. Model-internal analyses reveal that at decision-near states, correct-versus-conflicting text is decodable in Molmo2 and JointNLT but not in the other three systems. In the responsive models, decodability peaks at late states where replacement produces little behavioral change, whereas replacing selected earlier states redirects conflict-associated trajectories toward the target. Because matched-correct donors do not significantly outperform unrelated donors, these interventions identify earlier intervention-sensitive states without establishing target-specific semantic rescue. DISTRACT thus exposes when and where text affects tracking under degraded visual evidence.

---


### 242. [After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents](https://arxiv.org/abs/2610.28425)

**<font color=#1a73e8>作者：</font>** Zhiyue Xu, Xukai Wang, Zhiyuan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can re-fire across sessions long after the attacker leaves, threats we term carryover attacks. Existing prompt-injection benchmarks evaluate attacks only in the session where malicious content is first observed, leaving the gate governing when and how often a planted payload later re-fires unmeasured. We present CarryoverBench: 12 personal-assistant scenarios and 101 attack tasks across three trigger channels: Instant, same-turn IPI; Autonomous, heartbeat-scheduled; and Latent, memory-resurfaced. A rule-based verifier scores planting and triggering as independent stages. Across five frontier models, planted payloads re-fire without measurable decay over five rounds; conditional on successful planting, the trigger stage often provides little additional protection. Porting the Latent channel to a second runtime, Hermes, attenuates but does not eliminate the effect, suggesting that carryover defense requires runtime-layer controls in addition to prompt-level interventions.

---


### 243. [A Digital Twin to Improve Cyber-Social Impact](https://arxiv.org/abs/2610.28430)

**<font color=#1a73e8>作者：</font>** Vita Santa Barletta, Danilo Caivano, Gabriel Cellammare 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing complexity of Industrial Control Systems (ICS) and their integration with IT infrastructures has significantly expanded the cyber threat landscape. Traditional cybersecurity models, primarily based on the Confidentiality, Integrity, and Availability (CIA triad), fail to capture the broader societal and operational impacts of cyberattacks. This paper proposes a novel framework that integrates Digital Twin technology with a Cyber-Social Security model to simulate, analyze, and quantify cyber threats in critical infrastructures. Virtualized ICS environments built with Mininet and MiniCPS are used to model attack scenarios and assess their consequences across technical and social dimensions. At the core of the framework lies the Cyber-Social Vulnerability Scoring System (CSVSS), a quantitative metric that extends CVSS with a Social Impact dimension grounded in the Entity and Place pillars, producing a single, reproducible severity score that reflects real-world consequences. Crucially, the framework does not automate risk assessment but keeps the human analyst at its center: a Large Language Model (LLM) performs a first-pass analysis, mapping vulnerabilities and drafting risk reports, while the analyst, supported by explainable AI feedback, validates the findings and retains decision authority over critical cases. Experimental results demonstrate the framework's ability to model and score cyber-social impact, while the human-in-the-loop design is presented as a conceptual principle to preserve oversight.

---


### 244. [Every Model Leaves a Trace: Multi-Resolution LLM Fingerprinting](https://arxiv.org/abs/2610.28434)

**<font color=#1a73e8>作者：</font>** Mohammad Reza Modarres, Armin Tourajmehr, Artin Tavasoli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models leave model-specific traces in their generated text, but it remains unclear how finely these fingerprints can distinguish related models and which signals remain informative as obvious cues are reduced. We study this through fingerprint resolution, considering both model resolution, from different families to distilled and adapted variants, and signal resolution across behavioral, stylometric, lexical, and semantic evidence. We progressively suppress surface cues, paraphrase outputs, vary the amount of available text, and test generalization across prompt distributions and languages. Our results show that fingerprints persist beyond broad family differences, remaining detectable in distilled models and even LoRA adaptations of the same base model. Although attribution weakens as surface and lexical cues are altered, substantial model-specific signal remains. These signals transfer across prompt sources and languages, with semantic representations proving most robust across languages. These findings show that model identity is recoverable at multiple resolutions, but that recoverability depends on model similarity and the evidence available in the text.

---


### 245. [The Labor of Storytelling: How People with Chronic Illnesses Leverage AI and Communities for Narrative Translation](https://arxiv.org/abs/2610.28438)

**<font color=#1a73e8>作者：</font>** Drishti Goel, Koustuv Saha, Martez Mott 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The distinctiveness of people with chronic illness as storytellers is how they experience their illness. Symptoms, pain, and biological disruptions are eloquent forms of speech of the body that beget social articulation. The stories people tell about illness shape how suffering is legitimized, and acted upon. Large language models have emerged as new mediators within this landscape---a role once predominantly supported by communities. In doing so, these systems participate in what we term narrative translation: transforming lived illness experiences for particular audiences and purposes. Through 21 prototype-driven semi-structured interviews with people with chronic illness, we contribute an empirical account of how participants navigate this mediation alongside existing sources of support. Our findings surface distinct yet complementary roles participants envisioned for AI and their communities, and how trust in AI was shaped by learning model-boundaries and perceiving understanding. We characterize these findings to inform future designs of AI-mediated narrative support.

---


### 246. [Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity](https://arxiv.org/abs/2610.28441)

**<font color=#1a73e8>作者：</font>** Sahil Joshi, Prithvi Dixit, Aryan Katiyar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model inference over long contexts is increasingly bottlenecked by the cost of attending to a growing Key-Value (KV) cache. Sparse attention reduces this cost by accessing only a fraction of the cache, but existing methods face a trade-off between deterministic retrieval, which captures high-scoring tokens but discards residual attention mass, and sampling, which improves coverage at the cost of higher variance. Hybrid methods combine top-$k$ retrieval with uniform sampling, yet still exhibit a substantial gap from dense attention at aggressive sparsity. We introduce \emph{Stratified Sparse Attention (SSA)}, a unified framework combining deterministic retrieval with score-guided sampling. SSA deterministically attends to high-scoring tokens while sampling the residual using proxy attention scores and correcting for their inclusion probabilities, thereby recovering attention mass beyond the retrieval set. SSA encompasses top-$k$, top-$p$, and hybrid top-$k$+sampling as special cases. Across RULER, LongBench, LOFT, and AIME, and five models ranging from 3B to 27B parameters, SSA consistently improves over the baselines at matched sparsity. On RULER-HARD with Ministral-3-8B, SSA improves accuracy over the strongest practical baseline from 81.8\% to 84.2\% at 32K and from 63.8\% to 69.3\% at 128K under $50\times$ attention sparsity, recovering 94\% and 85\% of dense-attention performance, respectively. With optimized CUDA kernels, SSA achieves up to $2.96\times$ decode speedup over FlashInfer at 1M context, demonstrating that its accuracy gains translate into practical long-context inference acceleration. We open-source our code at this https URL.

---


### 247. [EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning](https://arxiv.org/abs/2610.28444)

**<font color=#1a73e8>作者：</font>** Xiaoxing Hu, Wenxi Yao, Chaoyuan Shi 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni LLMs can naturally locate key audio and visual evidence and integrate information across modalities for audiovisual reasoning. Existing audio-visual reasoning benchmarks that mainly rely on multiple-choice questions usually score models solely based on answer correctness, making it difficult to assess whether a model truly forms a reasoning chain from evidence to the correct answer. In addition, textual or unimodal shortcuts may allow models to answer correctly without analyzing the necessary audio-visual evidence, further weakening the reliability of evaluation benchmarks. To address these issues, we introduce EvaOmni, an evidence-grounded benchmark containing 392 videos and 1,027 purely human-annotated question-answer pairs, covering 15 capabilities and three levels: retrieval and localization, basic understanding, and complex reasoning. We design a series of rigorous annotation procedures in which experts annotate audio and visual evidence and construct video-based distractors; humans review whether questions meet strict inspection criteria, and finally models filter textual and unimodal shortcuts. Beyond high-quality question-answer pairs, we require models to simultaneously return the answer and supporting evidence intervals in order to evaluate the complete reasoning chain. We propose the Coverage Grounded Score (C.G.) to measure how much annotated evidence a model identifies, and the Bottleneck Grounded Score (B.G.) to penalize poor temporal localization in either modality; both are incorporated into answer correctness. Across 7 open-weight and 17 proprietary Omni LLMs, Gemini3.7-Flash achieved the highest overall accuracy (79.4%), C.G. (70.8%), and B.G. (35.1%). At Level 3, it reached 79.1% accuracy, but its B.G. was only 12.3%. These results show that even the most advanced models still have room for development in grounded audio-visual reasoning.

---


### 248. [MythoSemantic: An Interactive System for Discovering Semantic Parallels Across Mythological and Religious Traditions](https://arxiv.org/abs/2610.28452)

**<font color=#1a73e8>作者：</font>** Nikita Ganziuk, Innokentiy S. Humonen, Ilya Makarov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a tool for the comparative study of mythological and religious texts. Traditional manual analysis is highly labor-intensive and difficult to scale. To address this, we use neural language models to embed texts into a shared semantic space, so that users can find semantic parallels across cultural traditions in an interactive interface. Embedded fragments form distinct semantic structures whose coarse geometry aligns with well-documented historical relations between traditions. We quantify how much of that geometry is already explained by lexical overlap and by proper names. The current system is available at this https URL, and the installable package is available at this https URL.

---


### 249. [CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation](https://arxiv.org/abs/2610.28476)

**<font color=#1a73e8>作者：</font>** Pengying Wu, Mingye Jiang, Yunze Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-goal navigation (ObjectNav) requires an embodied agent to find an instance of a specified category in an unseen environment and stop near it. The agent typically relies on an object detector but must judge online from a limited egocentric video stream, sometimes a single frame, whether a detected candidate is the target. Detectors often confidently mistake similar objects, such as a sofa for a bed, and stopping at a false positive fails the episode. Prevailing systems also approach candidates greedily, leaving them occluded or partially observed. We present CLOSER, an evidence-aware active verification framework that treats stopping as closed-loop evidence acquisition, coupling vision-language model (VLM) verification with active perception. CLOSER fine-tunes an open-source VLM to label each view of a candidate tracked across frames as target, non-target, or uncertain, selects complementary views with an embedding-based diversity gate, and fuses their per-view probabilities with a lightweight network. If the fused judgment remains uncertain, a diffusion policy drives the agent toward the candidate using only the tracked mask and depth until the decision becomes decisive. CLOSER runs locally and plugs into existing ObjectNav systems without retraining them. On Gibson and Habitat-Matterport 3D, it raises average success rate by 3.6 points and success weighted by path length by 2.0 points, showing that verifying evidence before committing improves embodied navigation.

---


### 250. [Claims of emergence in AI should be grounded in information decomposition](https://arxiv.org/abs/2610.28479)

**<font color=#1a73e8>作者：</font>** Christoph Riedl, Fernando E. Rosas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model develops capabilities not traceable to its individual components, when a multi-agent AI system outperforms each agent on its own, or when a human-AI pair succeeds where either fails in isolation, AI researchers describe it as a case of ``synergy'' or ``emergence''. However, these are usually informal assessments not supported by a theoretical framework, making these claims impossible to compare or even meaningfully dispute. Here we argue that \emph{information decomposition can serve as a unifying formal framework to operationalize assessments about synergy in AI systems}. Information decomposition provides a way to distinguish qualitatively different \emph{types} of information, including unique information available from individual components, redundant information shared across multiple components, and synergistic information accessible only from parts taken together. This gives claims of emergence a precise, falsifiable criterion: a system's behavior is emergent only if it carries synergistic information about task-relevant outcomes. We apply this lens to attention heads, autonomous agents, and human-AI teams, showing how it organizes existing knowledge across scales and substrates, while also generating cross-level conjectures that siloed fields would miss.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
