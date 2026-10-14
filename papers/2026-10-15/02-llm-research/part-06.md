# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 251. [Preserving Updates in Low-Bit Recurrent State Quantization](https://arxiv.org/abs/2610.15709)

**<font color=#1a73e8>作者：</font>** Haotian Li, Liran Dong, Kaicheng Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention and recurrent models compress past tokens into a fixed-size state that is updated at every step. However, storing these states in high precision incurs substantial memory and bandwidth costs at large batch sizes, motivating low-bit state quantization. Unlike weights and key--value caches, a recurrent state is requantized after every update, so its quantization errors accumulate across steps. Our analysis shows that these errors are highly coherent across steps, so reducing per-step errors alone is insufficient. This coherence arises mainly from small updates that are lost in rounding. To preserve these updates, we intervene both before and at rounding. Before rounding, we propose Low-Rank Bypass (LRB), which accumulates small updates in a compact low-rank buffer and periodically merges its sufficiently large elements into the state. At rounding, we observe that a state element can even move opposite to its update, and such reversals prove particularly harmful. Therefore, we propose Bounded Directional Rounding (BDR), which rounds reversed elements toward their updates without additional storage. Although BDR enlarges the rounding error, it improves the model, suggesting that the direction of an update matters more than its rounding error at a single step. Across Gated DeltaNet, GLA, Mamba2, and RetNet, our training-free method substantially outperforms INT4, while reducing state memory by up to 5.3$\times$ and speeding up decoding by up to 1.9$\times$ relative to FP32 states.

---


### 252. [Suggested Is Not Superseded: A Pre-Registered Evaluation of a System-One Model as a Memory-Retirement Gate](https://arxiv.org/abs/2610.15710)

**<font color=#1a73e8>作者：</font>** Xupeng Chen, Chenqian Le  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory for assistants needs a gate that decides when a new utterance retires an old stored claim. Benchmark labels for this step mark a pair as changed or not, so they cannot tell a gate that acts on established change from one that acts on a hint. We write a task contract that separates the two (SUPERSEDED vs. NEEDS-CONFIRMATION vs. COMPATIBLE), label 500 test pairs built from STALE (change pairs plus same-user controls) with three LLM annotators and two human adjudicators (one author and a second annotator; provenance reported), and evaluate Jev, a typed "System One" decision model, under pre-registered hypotheses. Of the 179 test pairs STALE marks as changed, 72 meet the contract's bar for an established change. Jev never retired a claim on 141 same-conversation non-changes. Its failure is premature retirement: the binary gate retires 39.2% of claims whose change is only suggested. A three-way decision cuts this to 15.5% at a 15.3-point detection cost, which misses our pre-registered 10-point budget, and it lands on the binary gate's own threshold frontier; these verdicts hold under three readings of the gold labels. On a held-out vault scored against a second annotator's labels, a cascade that escalated uncertain cases to a reasoning model and looked best on development data was indistinguishable from simply raising the threshold (premature retirement 26.8% vs. 6.5% on dev). Part of the gap comes from the gold labels: relative to that annotator's reading, LLM-majority gold shares most of its errors with a same-family escalation model, and an identity for binary labels says how much such shared errors hide. The rest is small-sample selection on development data. For builders this means a binary score should not be wired to delete: route suggested changes to pending evidence, and do not trust a cascade selected on development data of this size.

---


### 253. [TL;QR: Querying Temporal Discursive Patterns in Textual Corpora](https://arxiv.org/abs/2610.15712)

**<font color=#1a73e8>作者：</font>** François Hublet, Vladimir Krsmanovic, Jesus Solano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many questions about large textual corpora concern patterns that unfold over time, such as a political group whose stance on a topic drifts from support to criticism over several years of debates. We present TL;QR (Too Long; Query with logical temporal Reasoning), a declarative query language and open-source engine for finding such temporal discursive patterns. In TL;QR, a single query combines natural-language predicates, whose truth is judged by a Large Language Model (LLM), with regular expressions and the operators of a temporal logic. The LLM answers only local questions about individual text passages; a symbolic engine then aggregates these judgments over time and links every match to the recorded passages and predicate decisions behind it. With this division of labor, the temporal and relational reasoning stays exact and auditable even over long time horizons. In addition, when a query includes a regular-expression pre-filter, only a small fraction of the corpus ever reaches the LLM. On a suite of controlled synthetic benchmarks with temporally and semantically complex patterns, TL;QR is substantially more accurate than LLM-only baselines. In a case study on ten years of European Parliament debates (442,593 multilingual speeches), TL;QR identifies candidate shifts in the political groups' stances on the GDPR privacy regulation.

---


### 254. [History Replays Itself: Unleashing Long-Context Capability in Linear Attention](https://arxiv.org/abs/2610.15715)

**<font color=#1a73e8>作者：</font>** Li Nanbo, Firas Laakom, Yilan Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear attention promises the efficiency needed for long-context language modelling, yet its fixed-size recurrent state must simultaneously support ongoing computation and preserve information from an ever-growing history. This coupling has reinforced a prevailing view that the state's memory capacity defines the model's long-context capability. We challenge this presumed ceiling: \emph{recurrent computation need not bear the full burden of long-term storage}. We introduce NoteBank, a sparse episodic memory that archives selected text before future queries are known, uses the backbone's native features for writing and addressing, and reads retrieved evidence through its native forward computation via replay. This \emph{training-free, plug-and-play} interface requires no external embedding model, separately trained retriever, or separate neural reader. At one million tokens, it raises Gated DeltaNet's mean accuracy across six RULER retrieval tasks from 1.7% to 70.3%, with no observed significant retrieval degradation from 4K to 1M tokens. This recovery adds $\leqslant$0.025% to analytical FLOPs, with persistent context storage approximately 1/2,600 that of a Transformer's full MHA KV cache at matched width, depth, and precision. Experiments extend from three 1.3B recurrent backbones to Mamba-2-8B and post-trained Qwen3.5-9B, demonstrating gains on LongBench v1/v2 and MemoryAgentBench. Together, these results show that sparse evidence storage and native replay can substantially expand the long-context capability of pretrained linear attention models while retaining the efficiency of recurrent computation.

---


### 255. [To Cache or Not to Cache: Understanding and Mitigating Safety Incompatibility in Cross-Model KV Cache Reuse](https://arxiv.org/abs/2610.15721)

**<font color=#1a73e8>作者：</font>** Zhiwei Lin, Jiahao Liu, Yan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-model KV cache sharing reduces prefill computation by allowing a receiver model to reuse prefix KV states generated by a related sender model. Existing methods optimize such reuse for latency and generation quality, but its safety implications remain unclear. In this work, we systematically evaluate this issue across diverse sender-receiver pairs and reuse configurations. We refer to deviations from the receiver's native safety behavior as safety incompatibility. Our study shows that both the direction and magnitude of safety incompatibility depend on the model pair and reuse configuration, with value reuse causing substantially larger deviations than key reuse across all evaluated pairs. Furthermore, we propose VReparo, a technique that learns per-layer and per-KV-head affine maps offline to align reused sender value tensors with their receiver-native counterparts before decoding. Across two model pairs under full KV reuse and the state-of-the-art selective reuse setting, VReparo reduces the average HarmBench attack success rate (ASR) from 57.28% to 39.21% and the average StrongREJECT score from 0.4215 to 0.2163 upon our benchmarks, while retaining an average Time to First Token (TTFT) reduction of 85.62%.

---


### 256. [PhySimCode: A Benchmark and Evaluation Method for Physics Video to Code Generation](https://arxiv.org/abs/2610.15722)

**<font color=#1a73e8>作者：</font>** Souraja Kundu, Aditya Gupta, Joel Julin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are good at video understanding and code generation, but it remains unclear whether they can recover the physical laws underlying videos, a capability essential for converting videos into executable simulations and for providing structured physical supervision in robotics. Captioning motion video does not imply that a model has inferred its governing dynamics, estimated quantitative parameters, or can regenerate the observed scene from code. Existing video-physics benchmarks evaluate plausibility, property estimation, or future-state prediction, but offer limited insight into whether models can translate visual dynamics into runnable simulation code. We introduce PhySimCode, a benchmark for physics video-to-code generation: given only a raw video, a model must infer the relevant physics, recover parameter values, and generate runnable Python that reproduces the input video. The dataset contains 160.6K procedurally generated samples spanning 162 physics phenomena across analytic SciPy simulations and PyBullet-rendered rigid-body, articulated, fluid, and contact-rich scenes; each sample bundles the simulation code, physical parameters, rendered video, and a structured chain-of-thought covering observations, laws, ODEs, numerical methods, and validation checks. We evaluate ten state-of-the-art closed- and open-source MLLMs along physical-law correctness, simulation equivalence, code executability, and parameter recovery. Models reliably state physics laws (4.27-4.93/5) yet score only 1.51-2.47/5 on inferring them from video, and the best system (Claude Sonnet 4.6) recovers just 7.7% of ground-truth parameters within $\pm 20\%$, exposing a substantial video-to-simulation gap. The 2,430-video evaluation set is available at this https URL and the evaluation code at this https URL

---


### 257. [Visually Legible but Adversarial: Watermark-Constrained Attacks on End-to-End VLMs for Document Understanding](https://arxiv.org/abs/2610.15728)

**<font color=#1a73e8>作者：</font>** Qingzhe Han, Fan Dang, Shengqi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible watermarks convey document ownership, confidentiality, and status, but can also carry adversarial signals. We introduce Auto-Regional Adversarial Watermarking (AR-AWM), a model-aware white-box attack on end-to-end visual language models (VLMs) for document understanding. AR-AWM constructs a small, spatially distributed watermark-text support and optimizes only its pixels to disrupt visual representations. The attack is untargeted and question-agnostic: generation uses no questions, answers, parsing prompts, language-model gradients, or language-model outputs. Each attacked page is reused across downstream queries. On Qwen2.5-VL-7B, a watermark support covering 7.98% of page pixels under the reporting threshold reduces DocVQA exact match from 0.899 to 0.150 and average normalized Levenshtein similarity (ANLS) from 0.939 to 0.212. Selected qualitative cases retain visually legible source fields. The same support without optimization and with matched random perturbations retains ANLS of 0.932 and 0.933, respectively, identifying adversarial optimization as the primary cause of degradation. Layout-matched optimized rectangles yield ANLS of 0.276, showing an incremental benefit from text-shaped geometry. AR-AWM also degrades all reported text, formula, reading-order, and table metrics on OmniDocBench. Separate white-box optimization on InternVL2.5-8B reduces ANLS from 0.922 to 0.046, while weak cross-model transfer reveals strong encoder specificity. These results identify conventional watermark-shaped supports as an adversarial surface for document VLMs in the evaluated white-box this http URL white-box setting.

---


### 258. [LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions](https://arxiv.org/abs/2610.15729)

**<font color=#1a73e8>作者：</font>** Junming Liu, Marcel Böhme  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When we see a null pointer check, we know that the developer believes that the pointer may not be initialized. If the same pointer is later used without a null pointer check, we may consider this a violation of the developer's belief and ultimately a bug. We develop such a belief-guided program analysis for vulnerability detection (VD). For example, when an authentication function returns the same error for both, a wrong user name and a wrong password, an auditor may infer that the developer believes that both cases are indistinguishable, mitigating a user enumeration attack. This belief is reasonable, as it follows standard security practice. Yet, a function call inducing a difference in response time for both cases, contradicts this belief. This contradiction uncovers a timing side-channel that syntactic analysis tools would miss. Existing static analysis tools struggle with this type of flaw because they require them to be expressible by general, syntactic patterns. Our belief-guided approach detects such domain-specific, high-level semantic security flaws that remain elusive.
Given a function, our approach, Creed, infers the developer's security-related beliefs, evaluates how reasonable each one is, and derives the conditions under which it is violated. In contrast to existing ML-based VD techniques, Creed explains the root cause, the symptoms, and the conditions under which each issue is exploitable. To address the context-dependency problem in the evaluation, we introduce two measures for explanation-based VD: recall quantifies how effectively an approach correctly explains a known vulnerability, and overhead quantifies the effort of inspecting its reports. On a recent real-world vulnerability benchmark, Creed detects both semantic and syntactic vulnerabilities more effectively than existing explanation-based VD tools, achieving the best effectiveness-effort trade-off.

---


### 259. [NepPlural: A Human-Anchored Benchmark for Persona Annotation in Nepali Migration Discourse](https://arxiv.org/abs/2610.15732)

**<font color=#1a73e8>作者：</font>** Jinu Nyachhyon, Anish Khatiwada, Bimal Timilsina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pluralistic alignment asks that language models faithfully represent a society's diverse, competing values rather than collapse them into one dominant viewpoint, yet flagship pluralistic-alignment datasets remain heavily skewed toward Western respondents. We introduce NepPlural, a human-anchored benchmark for modelling competing socio-cultural personas in Nepali public discourse on youth migration and brain drain. We curate 2,148 code-mixed (Devanagari, Romanized Nepali, English) YouTube comments, annotate them along a four-axis persona taxonomy (Intent, Primary Driver, Value Orientation, Affect) plus an explicit No-Persona class, and build a 300-comment gold set labelled independently by three native Nepali speakers (mean Fleiss' $\kappa \approx 0.55$). Using this gold set to audit automatic annotation, we find that LLM annotation reliability is driven by protocol. Labels collected in batches through chat interfaces reach only near-chance inter-model agreement ($\kappa \approx 0.17$). Annotating one comment at a time raises agreement above the native-speaker level ($\kappa \approx 0.72$), but consistency is not validity: under a forced-choice schema, models agree on personas for the 39% of comments native speakers judge to express none, keeping macro-F1 against human gold near 0.50. Allowing abstention resolves this: models recover No-Persona comments with F1 of 0.79 to 0.87 and, against leave-one-annotator-out references, match or exceed individual native speakers (macro-F1 0.75 to 0.86 vs. 0.75). Encoders fine-tuned on the batched labels reach only 0.34. Finally, a human-judged steerability probe finds that three frontier models adopt single persona axes with 59 to 77% fidelity but compose full personas only 33% of the time, with no congruence gap detected at this scale between Western-congruent and Nepali-collectivist personas.

---


### 260. [Visible but Not Avoided: State-Dependent Re-Proposal of Rejected Candidates in Catalog-Based LLM Optimization Loops](https://arxiv.org/abs/2610.15738)

**<font color=#1a73e8>作者：</font>** Jianlin Chen, Wenhui Chen, Chi Man Vong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM optimization loops often show the proposer the candidates it has already tried and rejected, but leave it to the proposer to avoid them. We ask whether avoidance measured in a static probe predicts avoidance in the states an optimizer's own trajectory produces. In catalog-based loops where three open LLMs improve a GUI agent by naming one of 40 edits, a re-proposal is identified exactly by the edit's name. Clean base-state probes underpredict re-proposal in the proposers' own loops (macro-averaged loop-minus-probe rate 0.32 [0.27, 0.37]), and proposals of already evaluated harness-edit pairs consume 28-63% of valid proposer iterations. The two settings reject different edits: a probe's rejected edits are mostly ones the proposer did not choose, whereas a loop's are its own earlier choices, which remain preferred when the history is removed. Ordinary history lowers re-proposal for two proposers but raises it for the third, and the effects of failure evidence are model-specific. Stating the rejection status in one sentence lowers re-proposal in every model (-0.16 [-0.22, -0.09] relative to a neutral list of the same IDs). For catalog-based loops with exact edit identities, rejection avoidance should be measured on the rejected sets the loop produces.

---


### 261. [RSAJEV: Training-Free Abstaining Prototype Memory for Eliminating Silent Hallucination in JEV-Based Remote Sensing Classification](https://arxiv.org/abs/2610.15742)

**<font color=#1a73e8>作者：</font>** Man Chen, Antai Chen, Shuai Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene classification of remote sensing imagery with multimodal large language models (MLLMs) is formulated as a single-forward-pass decision problem: candidate class names are lettered options in the prompt, a registered answer slot is conditioned on the prompt, and classification is read out by scoring letter tokens with the language-modeling head. We show that although this letter binding is highly effective within its training vocabulary (97.71% OA on UCM), it behaves erratically out of vocabulary: zero-adaptation accuracy across four cross-dataset directions fluctuates between 7.35% and 96.40%, and under out-of-vocabulary weights its confidence fails inversely on open-set evaluation, assigning higher confidence to unseen than to seen classes (AUROC 0.38), a failure we term silent hallucination. We retain the slot representation and replace the readout with RSAJEV, a training-free abstaining prototype memory that performs retrieval-based prototype matching: K reference images per class are cached as prototypes via their slot representations under the same prompt, and classification becomes nearest-neighbor retrieval over the prototypes, refined by a shrinkage-Mahalanobis geometric correction. This readout is mechanistically isomorphic to retrieval-augmented generation (RAG) but operates on discriminative decisions; it is the first retrieval-based readout for MLLM slot representations. The retrieval readout reaches 89.43% on the UCM cross-dataset gate with 16 references per class and zero gradient updates, and 96.90% on AID. Its ID-ness scores attain 0.91-0.99 AUROC on open-set evaluation over two datasets, exceeding symbolic confidence (0.38-0.96) in all four open-set settings, restoring a calibratable abstention channel and supporting class addition/removal at zero extra inference cost via offline rescoring of the cached matrix.

---


### 262. [Google Earth AI Geospatial Reasoning Agent: Capabilities and a Systematic Evaluation](https://arxiv.org/abs/2610.15750)

**<font color=#1a73e8>作者：</font>** Noam Slonim, Aviv Slobodkin, Gil Fidel 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Google Earth AI is a family of geospatial AI models, together with an agent that orchestrates them. We present this agent, Google Earth AI's Geospatial Reasoning agent (GRA), a Gemini-powered research system that combines geospatial data sources, foundation models, and tools to answer questions about our planet. GRA organizes these into modular domain skills and pairs them with upfront geospatial planning to decompose complex queries into multi-stage workflows. Evaluating such systems is hard: real-world problems admit multiple valid workflows, require data discovery across large catalogs, and rely on evolving ground truth. We introduce two benchmarks and release their development splits. GeoExpertQueries poses complex analytical problems grounded in practitioner use cases and refined by geospatial experts; each is paired with a consensus golden workflow from three independent experts and scored by a human-validated, tool-agnostic autorater. GeoKTools consists of templated queries with deterministic reference solvers that systematically vary the number of required tool types. We also use two external benchmarks, CBGB and UnivEARTH; the latter we find to be saturated. To isolate the contribution of GRA's tools and its agentic orchestration, we compare four configurations, each with Gemini 3.1 Pro and 3.8 Flash: a standalone LLM, the LLM with basic tools, the LLM with GRA's skills and tools but without its upfront planning and execution guidance, and GRA itself. With at most basic tools, an advanced model recovers much of the answer on templated queries but satisfies only a small fraction of the expert workflows on open-ended problems; GRA performs well on both. The largest step comes from GRA's skills and tools; on open-ended problems, its planning and execution guidance add a further gain with Gemini 3.8 Flash, letting Flash match or exceed Pro at lower cost.

---


### 263. [Robust Marathi Sentiment Analysis using Domain-Adaptive Pre-training and Data Augmentation Approaches](https://arxiv.org/abs/2610.15761)

**<font color=#1a73e8>作者：</font>** Tanvi Somani, Aryan Babare, Samyak Bora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For languages with limited resources, Sentiment Analysis remains a challenging problem due to limited annotated data and strong domain variability across textual sources. Marathi, despite being widely spoken, lacks extensive multi-domain sentiment analysis studies. Recent efforts by L3Cube have introduced multi-domain datasets in Marathi, enabling a better study of domain-aware sentiment classification. This study uses the pretrained MahaBERT model to improve sentiment classification for Marathi across different domains. Models are trained on individual domain datasets and domain-adaptive pretraining is applied using masked language modeling to help the model better understand domain-specific language. In addition, back-translation is used as a method of data augmentation to increase the diversity of training data. Results show that these methods lead to consistent improvements in accuracy across all domains. The improvements range from a minimum of about 0.12% to a maximum of about 1.74%, depending on the dataset. These results demonstrate that domain-adaptive pretraining and data augmentation are effective strategies for improving sentiment analysis models. This helps achieve more robust performance across different domains and makes the approach more suitable for low-resource languages like Marathi.

---


### 264. [RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution](https://arxiv.org/abs/2610.15772)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Hao Wu, Jinyang Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent focus in agentic reinforcement learning (RL) seeks to improve credit assignment in long-horizon tasks. One promising direction combines reinforcement learning with verifiable rewards (RLVR) and on-policy self-distillation (OPSD), integrating trajectory-level advantages with dense token-level supervision. This line of work often conditions a teacher model on privileged context, such as agentic skills, to score tokens generated by the student policy. Despite their progress, they largely overlook the on-policy evolution of agentic skills and the reliability of teacher supervision. Towards this end, we introduce Recursive Self-Improving Policy Optimization (RSIPO), a self-evolving agentic RL framework that enables agentic skills and the policy model to co-evolve throughout the training process. Specifically, RSIPO enables the policy itself to extract skills from completed trajectories and explicitly optimizes its skill-generation capability through trajectory replay. It further employs empirical Bayes shrinkage to dynamically calibrate the student's trust in teacher scores, accounting for the fact that skill-enhanced teacher guidance can sometimes be less reliable. Experiments with Qwen-family models on embodied interaction and search-based agentic tasks demonstrate that RSIPO outperforms all the compared baseline approaches. With Qwen2.5-7B as the base model, RSIPO achieves an average success rate of 98.6\% on ALFWorld, yielding absolute improvements of 2.5\% and 17.4\% over the second-best baseline and standard GRPO, respectively.

---


### 265. [Who Sets the Pace of Judge Hacking? Judge Capability versus the Policy-Judge Gap](https://arxiv.org/abs/2610.15778)

**<font color=#1a73e8>作者：</font>** Haosen Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a policy is trained with GRPO against a frozen, reference-free LLM judge, the judge accepts more of its answers, but in a post-hoc analysis we detect no gain in held-out greedy accuracy: in all 12 (policy, judge) cells, the seed-mean gain never exceeded 0.04. A gold-reward control with the same recipe raised the 1.5B policy's greedy accuracy by +0.054 [0.013, 0.096], so for this policy the flat accuracy is specific to the judge reward; for the 0.5B policy, gold reward also gave no detectable gain. In the four rising cells we checked, the early rise in training-rollout accuracy is mostly sampling sharpening, as it is under gold reward. We then ask whether the policy-judge gap or the judge sets how far and how fast RL exploits the judge's false positives. We train 0.5B and 1.5B Qwen2.5 policies against four judges at least as large (Qwen2.5-1.5B/3B/7B, Llama-3.2-3B) and the 1.5B policy against one smaller judge (Qwen3-0.6B). The depth of judge hacking (the plateau) tracks the judge: it correlates with judge AUC (Spearman -0.69 [-0.94, -0.14] over 12 cells), and within a family the larger judge is fooled less deeply. For the pace (onset), two pre-specified pairs contradict the gap account (the larger-gap cell was fooled 3.5x sooner at the pre-specified threshold). With 12 cells we cannot formally separate judge AUC from the gap for either endpoint. The smaller judge was not fooled sooner than a judge as large as the policy, though it also differs in family and template. In a blind test on three held-out judges, a hash-locked step-0 predictor did not beat step-0 AUC, but three cells cannot separate them. At 7-8B, judges from three families plateaued at 0.37, 0.67 and 0.85.

---


### 266. [Heterogeneous Structured Pruning Under Resource Constraints for Hardware-Efficient Large Language Models](https://arxiv.org/abs/2610.15781)

**<font color=#1a73e8>作者：</font>** Cameron Barker, Andreas Paraskeva, Jan N. van Rijn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free pruning removes weights from pretrained large language models to reduce their deployment cost. However, existing approaches typically consider only the total number of retained weights. Consequently, their pruning decisions do not account for how target hardware stores and processes those weights. These methods select a sparsity structure in advance and apply it uniformly to all projections, rather than accounting for how each structure trades pruning error against latency and memory across sublayers. We propose Heterogeneous Structured Pruning (HSP), a hardware-aware pruning framework that combines two components: (i) a heterogeneous search space of dense, unstructured, 2:4, block-sparse, and head / channel (H/C) pruning options and (ii) structure-regularising constraints based on latency and memory models. Our contribution generalises existing importance-based methods: a global solver selects one option per sublayer to minimise proxy pruning loss under a resource budget, thereby assigning each projection a structure and density. We evaluate HSP on OPT and LLaMA models for an NVIDIA Jetson Orin Nano Super edge device, where it improves the quality-resource frontiers over training-free baselines.
A project page and updated links for the related code is maintained at: this http URL.

---


### 267. [Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams](https://arxiv.org/abs/2610.15788)

**<font color=#1a73e8>作者：</font>** Yirui Qi, Xiaoming Zhang, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed as teams, yet they fail in characteristically social ways: information holders stay silent, dominant speakers anchor groups on wrong answers, and norm violations go unsanctioned. We present Agent Sociodrama, a framework for modeling and validating evolving social dynamics in LLM agent teams. Under fixed personas, agents' emotional states and directed, asymmetric relationships are updated every round by a unified external LLM judge and shape their subsequent interactions. Across six LLM backbones and five social scenarios, we assess social fidelity through classical social-theory patterns and agreement with human judgments. The resulting trajectories exhibit structured social patterns and model-specific differences. We then introduce Trajectory-Guided Persona Recasting (TPR), which diagnoses group-dynamic failures from interaction transcripts and social trajectories and recasts agent personas before rerunning the task. Across four collaborative benchmarks, TPR improves performance from both heterogeneous and randomly initialized agent persona compositions, yielding up to 83.3%p of accuracy improvement over the initial casting. On representative distributed-information cooperation and mixed-motive bargaining tasks, we outperform SOTOPIA and AgentVerse in three of four comparisons, by up to 37.5%p in Pareto rate. These results show that validated social trajectories provide actionable signals for repairing LLM agent teams.

---


### 268. [Privacy Conductor: An Architectural Enforcement of Contextual Integrity in LLM-Based Document Retrieval](https://arxiv.org/abs/2610.15804)

**<font color=#1a73e8>作者：</font>** Ryan Thornton, Mir Mehedi A. Pritom, Maanak Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) that retrieve internal documents within an organization must decide who may receive them. Existing approaches based on Contextual Integrity ask the model to make that decision, so access depends on probabilistic reasoning. We present Privacy Conductor, an architecture that removes the decision from the model: a deterministic gate enforces a policy written by an authority, and the model receives only what the requester may already see. On a synthetic clinical corpus of 2,520 requester--document flows, the gate reproduces its policy exactly, so the remaining risk lies in the document labels it reads. As label source is of primary importance, we compare LLM and human generated labels. Across seven configurations of six models from two model families, LLM-written labels degrade the policy in every case. Models assign a document's sensitivity tier correctly on 78--86% of documents, but reproduce its access-control list on as few as 23%. Relabeling the same documents five times with an identical request changes 13 to 124 access decisions per configuration, a result that does not depend on our own labels. On 214 flows from HIPAA court cases, the most accurate configuration (87.8%) still permits 11 of the 20 disclosures the law prohibits. LLMs can describe what a document contains, but not decide who should receive it. Hence, we recommend privacy policy should be authored by accountable personnel and enforced outside the model.

---


### 269. [Adaptive Look, Flexible Thought: Learning How and How Long to Think in Multimodal Reasoning](https://arxiv.org/abs/2610.15810)

**<font color=#1a73e8>作者：</font>** Quanlin Chen, Xiuwei Chen, Kun Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The introduction of long chain-of-thought (CoT) reasoning and external tools has substantially improved the performance of multimodal large language models (MLLMs) on general and reasoning tasks. However, existing fast-slow reasoning paradigms mainly regulate textual reasoning length, while visual computation introduced by external tools or visual tokens is often treated as an auxiliary component. This separation prevents MLLMs from jointly optimizing visual perception and textual reasoning. To address this issue, we propose L2T (adaptive Look, flexible Thought), a unified reasoning framework that jointly optimizes the form and depth of computation. L2T first discretizes tool-produced visual states into visual tokens, bringing visual perception and textual reasoning into a shared autoregressive space. Based on this unified representation, L2T introduces a modality-aware routing reward to select appropriate reasoning modes and a difficulty-aware fast-slow strategy to adapt reasoning depth according to task complexity. Experiments on general perception and reasoning-intensive tasks demonstrate the effectiveness of L2T. Compared with explicit tool-calling approaches, L2T maintains competitive performance while achieving 1.7--3.6 times higher throughput.

---


### 270. [Latent Taxonomies: How Property Induction Develops in Language Model Pre-training](https://arxiv.org/abs/2610.15836)

**<font color=#1a73e8>作者：</font>** Jan Sobotka, Ekaterina Goliakova, Marcin Detyniecki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When told that robins have sesamoid bones, people are far more prone to extend the property to sparrows than to whales. This behavior, called category-based property induction, is well documented in humans, but whether and how it develops in language models trained only to predict the next token is unclear. To shed light on this, we construct a hierarchical taxonomy of synthetic entities grouped by the properties they share. We then inject facts from this latent taxonomy into the continued pre-training of Pythia and OLMo 2 models from 70M to 7B parameters, and track the development of inductive behaviors. We find that taxonomically aligned induction emerges from next-token prediction alone: a property learned for one entity transfers more strongly within its taxonomic category than across categories. Internally, entities that share a deeper category become more similar in activation space, and clustering recovers the full taxonomic tree from entity representations. Contrary to the usual expectation that scale helps, we find that induction weakens with model size when the data budget is fixed, suggesting that larger models memorize individual facts rather than compress them into shared structure. Induction also strengthens with more pre-training before the taxonomy injection, transfers to novel in-context properties, and can be overridden by a latent taxonomy implied by the prompt. Together, these results show that a model's inductive generalization reflects the latent organization of its training data, with implications for data curation and for predicting how far a learned fact will spread.

---


### 271. [LLM Value Functions for Credit Assignment in Agentic RL](https://arxiv.org/abs/2610.15840)

**<font color=#1a73e8>作者：</font>** Kaijie Zhu, Weixiang Yan, Omar Attia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for large language model (LLM) agents remains challenging in long-horizon tasks with sparse outcome rewards, where assigning credit to individual actions is difficult. Methods such as GRPO assign the same trajectory-level advantage to all actions, while critic-based methods require learning an additional value function that can be costly and unstable. We introduce LLM Value Function RL (LVRL), which uses the pretrained knowledge and in-context learning ability of an LLM to estimate policy-aware state values without finetuning a separate critic. LVRL conditions the value model on group context and calibrates its predictions using known values at the initial and terminal states, enabling step-level credit assignment from estimated value differences. We further extend this idea to learning from an expert policy through on-policy distillation (OPD), introducing LLM Value Function OPD (LVOPD), which focuses teacher supervision on actions associated with decreases in estimated value. We evaluate our approach across diverse agentic benchmarks: AppWorld, BabyAI, and SWE-bench Verified. Across policy scales (4B to 32B), LVRL consistently and substantially outperforms both GRPO and PPO. On AppWorld and SWE-bench Verified, LVRL yields absolute improvements of up to 13.6 and 8.6 percentage points over GRPO. Notably, on tasks requiring extended exploration like BabyAI, LVRL bridges the gap from total failure to 75.0% success. Furthermore, LVOPD yields consistent improvements over standard distillation baselines on AppWorld. Finally, Monte-Carlo analysis confirms that our frozen critic accurately identifies semantic pitfalls and recoveries, proving that LVRL extracts robust, policy-aware step-level credit from sparse terminal outcomes.

---


### 272. [Sharper Frames, Worse Rooms: Viewpoint Coverage Dominates Image Quality in Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2610.15854)

**<font color=#1a73e8>作者：</font>** Alibek Dadajonov, Hikmatillo Umarhojiyev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounded spatial reasoning about indoor scenes rests on a geometric reconstruction that the multimodal system does not itself produce. Feed-forward multi-view reconstruction models operate under a fixed view budget, making frame selection a critical upstream decision. We show that under this setting the conventional preference for sharp frames can be actively harmful. Across nine handheld room scans, selecting the sharpest 16 of 200 candidate frames is the worst strategy we test, reaching 48\% room dimension error where uniform temporal sampling reaches 3\%. We trace this failure to a coupling between image quality and camera motion: sharp frames tend to occur during slow motion and therefore concentrate the selection in a narrow angular region, leaving $192^\circ$ of the room unobserved in the case we illustrate and over $300^\circ$ in the worst cells. A $2\times2$ factorial experiment that independently manipulates viewpoint spread and per-frame sharpness shows that spread has roughly three times the main effect of quality, and that blurry but well spread selections outperform sharp but clustered selections in 8 of 9 captures. The advantage also diminishes as the frame budget increases and angular coverage saturates, consistent with this mechanism. Finally, we ask whether the failure is detectable at inference: the reconstruction model's multi-view consistency score increases with reconstruction error, while a vision-language model given the same frames reports confidence unrelated to its own spatial estimation error. Under small view budgets, viewpoint coverage is a more important constraint than per-frame image quality, and neither uncertainty signal available at inference reveals this upstream failure.

---


### 273. [Attention Sinks in VLMs Are Borrowed, Not Seen](https://arxiv.org/abs/2610.15855)

**<font color=#1a73e8>作者：</font>** Dengjia Zhang, Alexander Martin, Pengyu Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how to detect and mitigate visual attention sinks in vision-language models (VLMs). Visual attention sinks are image tokens that absorb a large share of attention over the image regardless of the query or task, and they mislead methods that treat attention maps as a record of where the model ``looked.'' Prior work has detected sinks through massive activation dimensions and proposed redistributing their attention, but none have addressed what makes a token become a sink. Comparing six candidate detectors on ten VLMs from four families, we find that only the centered cosine similarity between an image token's key and the key of the language model's text-sink detects visual sinks. Thus, a visual sink is an image token whose key aligns with the text-sink's key. Moving a sink's key component along this direction to the median of the image keys sends its attention back to the text-sink (\textbf{Are Borrowed}) while leaving model answers unchanged~(\textbf{Not Seen}). Building on this, we propose a training-free, entropy-triggered re-look that first cleans the attention map, then crops the most-attended region of the cleaned map and inserts it into the reasoning trace. Cleaning adds negligible computation to the forward pass, and the re-look improves accuracy with a mean gain of $+4.3$ points on fine-detail VQA benchmarks across model families.

---


### 274. [Unchecked or Falsely Accused? Evaluating AI-Generated Text Detectors on Kazakh](https://arxiv.org/abs/2610.15870)

**<font color=#1a73e8>作者：</font>** Mansur Ozaman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-text detectors are already applied to Kazakh writing, yet no study reports how often publicly available detectors flag Kazakh text whose human authorship is dated before ChatGPT. We present AINA-KK: 3,811 human passages from encyclopedic, news, web and educational pages that provably existed before ChatGPT, and 5,597 machine and gray-zone passages from 9 generators, including the Kazakh-built KazLLM and Sherkala, with script and length stress tests. Five English-trained detectors from the Hugging Face Hub flag up to 81.4% of human passages and 79.6% of published student essays; recalibrated, they catch at most 1.3% of machine text. Calibrated zero-shot detectors catch at most 50.3% of machine text from in-distribution generators. Fine-tuned encoders rank text almost perfectly, but mDeBERTa at its default threshold flags 24.4% of 50-word human excerpts, partly because machine outputs are shorter than human text; calibrated, it catches only 47.1% of KazLLM and 62.7% of Sherkala passages. Without script handling, machine-transliterated Latin-2021 text defeats every detector. Fixes that need no new data (calibration, script canonicalization, script-augmented and length-matched training, and an OR with a zero-shot scorer) form AINA-KK-Det. On test it flags 0.9% of human passages (95% CI 0.4-2.7; 1.5% on development data) and catches 85.2% of machine text from known generators, 92.9% from two unseen Gemini-family Gemma-4 models and 61.3% from the Kazakh-built ones; its configuration was chosen with test results in view. We release the data, code and detector at this https URL.

---


### 275. [Engram Injection: A Study of Temporal Validity in Parametric Language-Model Memory](https://arxiv.org/abs/2610.15882)

**<font color=#1a73e8>作者：</font>** Sam Siavoshian, Omar Ramadan, Amir K. Saeed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A stored fact may stop being valid when a user changes a preference or an event replaces an earlier one. We study whether a language model can learn these changes in its parameters and answer correctly from only a question and the current time. Engram Injection stores facts in LoRA adapters and supplies the clock through FiLM conditioning on a frozen Qwen2.5-3B-Instruct model. We compare it with additive clock conditioning, prompting with the full dated history, and retrieving four dated records. We train six matched adapters across three seeds after fixing a sampler that could admit test-age examples into training. The training audit reports no such examples among 127,760 evaluated training inputs. On 62 pairs of questions asked before and after an update, at an elapsed age of seven days excluded from training, both adapter methods answer zero pairs correctly under the primary blinded assistant review with order code 1 held fixed. Full-history prompting answers 59/62 pairs correctly, and retrieval answers 62/62. Separate experiments show that adapters can store facts and that removable memory units can support local deletion. Combining fact selection with time-based version selection remains unsuccessful. These results separate learning a fact from learning when to use it.

---


### 276. [What the Model Cannot See: Covert and Provable Text Invisibility in LLMs](https://arxiv.org/abs/2610.15883)

**<font color=#1a73e8>作者：</font>** Mark Russinovich  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text wrapped in a trigger can be made behaviorally invisible to a language model: omitted from summaries and quotations, ignored in question answering, and left unflagged by downstream filtering. We study this selective blindness as a dual-use information-flow primitive, a supply-chain backdoor, and a white-box auditing problem. We first implement it exactly as a serving-time span veto: blocking information flow out of a marked span makes every outside activation bit-identical under same-length substitution of the span's content, a noninterference property we verify across ten models, seven mixer families, and 0.5B-120B parameters. The veto serves as a deployable quarantine, an exact reference for calibrating leakage, and a teacher. Distilled into weights, it yields a backdoor: checkpoints trained on six model families from 4B to 120B ignore marked context at little benchmark cost, and their outputs show no measurable semantic trace of the suppressed content above the veto reference on our held-out suite; an in-domain variant suppresses planted vulnerabilities during AI code review. Detection is therefore a white-box problem. Simpler backdoors remain internally transparent -- linear probes recover suppressed content at 0.57-0.79 accuracy versus 0.025 chance -- but hardening the attack until probes reach chance collapses attention from outside the span into it below the range of base models. Across the attacks we evaluate, probe visibility trades off against routing visibility; we do not establish that this tradeoff is fundamental.

---


### 277. [RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use](https://arxiv.org/abs/2610.15884)

**<font color=#1a73e8>作者：</font>** You Liu, Yue Liu, Quanchao Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> False retry permission (FRP) occurs when an agent retries a timed-out tool call without support from the visible contract. RetryBench separates this error from realized recovery. Successful protected recovery does not imply reliable rejection of unsupported retries. In a 720-response key control, valid keys usually enabled safe progress, but offered changed keys elicited unsupported retries in Sol (1/80), Terra (55/80), and Luna (60/80). A later 240-response control removed the candidate and required models to supply a key. Luna still made 8/80 unsupported dispatches; Sol and Terra made none in 80 responses each. Accepting a displayed bad key therefore cannot explain all observed errors, although changed output requirements and conditions preclude a pure display-effect comparison. Removing the weak-contract label increased retries in Sol and Terra's coded-action conditions in a six-endpoint study. A separate 1,536-response canonical-action block also found a positive Terra contrast (115/128 versus 124/128 retries), concentrated in two task/order conditions; the other five contrasts remained unresolved after multiplicity correction. An explicit-contract cue control elicited deferral in all 762 returned responses, leaving recovery unresolved. These results support reporting permission and recovery together across declared interface variants. The evidence covers four purposive tasks, fixed GPT endpoints, and one recovery decision; it identifies neither internal mechanisms nor episode-level safety.

---


### 278. [Make Every Expansion Count: Learning to Search Efficiently in LLM Code Repair](https://arxiv.org/abs/2610.15894)

**<font color=#1a73e8>作者：</font>** Elad Sharony, Ido Greenberg, Jialin Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) code-repair systems fix faulty programs by repeatedly generating and testing revisions. Each revision is costly, making the choice of which repair to pursue important for efficiency. Existing search policies rely on test pass rates and search statistics, ignoring the details of test failures and proposed edits. We introduce CodeTriage, a learned policy that prioritizes edits before their revised programs are generated and tested. Its 0.6B-parameter model reads the test output, failure diagnosis, and proposed edit, then predicts a distribution over the number of repair steps needed to reach a fix through that edit. These predictions prioritize all pending edits across programs before generating and testing the revised code. On held-out repair tasks, CodeTriage finds fixes with 21% fewer program revisions and 12% fewer output tokens than the strongest baseline on each metric. Without retraining, it achieves the highest average success across search budgets for each of 11 unseen repair LLMs. Ablations show that both the failure context and edit text, as well as comparisons across programs, improve search. We also release a corpus of 12.2 million program versions from four LLMs, organized into repair trees with proposed edits and test results.

---


### 279. [Review Rarely Beats the Stronger Model: Separating Verification from Capability Transfer in LLM Pipelines](https://arxiv.org/abs/2610.15897)

**<font color=#1a73e8>作者：</font>** Yirui Zhang, Yash Raj Shrestha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Qwen3-8B reviewing Llama-3.1-8B in math adds 33.2 points, yet Qwen3-8B alone is 6.4 points more accurate than the result. Reviewing another model's answer is usually judged by its gain over the generator. We show that this confuses verification, which adds accuracy beyond either model alone, with capability transfer, where a stronger reviewer supplies answers it could have given on its own. Measured against the stronger model alone, across 48 pairs of 12 open-weight models (3B to 72B) in math, knowledge, code and reasoning, review beats it in only 9 of 96 review directions, and does worse the larger the capability gap. The reason is that the reviewer mostly follows the generator, discarding its own correct answers. Review costs 2.6 to 2.8 times as much as the stronger model alone, while a selector using the same two calls is 2.7 to 4.2 points more accurate than review and cheaper. Studies of verification should report the stronger model alone, not only the gain over the generator. Code and per-question results: this https URL

---


### 280. [Mind Your Own Role: Reducing Role Overstepping for Effective and Efficient Multi-Agent Collaboration via Dynamic Role Activation Steering](https://arxiv.org/abs/2610.15907)

**<font color=#1a73e8>作者：</font>** Xingke Yang, Sicong Li, Lingfeng Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Systems (MAS) have shown strong capability in solving complex tasks by assigning different agents specialized roles and corresponding subtasks. However, agents may overstep their assigned responsibilities and perform subtasks belonging to other roles, which can disrupt workflow, reduce system efficiency, and degrade task performance. To address this issue, we investigate role-related patterns in the model's internal activation space and uncover two key observations: (i) role instructions induce consistent directional shifts in activation space, and (ii) role-adherent and role-overstepping trajectories exhibit distinct activation patterns. Based on these observations, we propose Dynamic Role Activation Steering (DRAS), a lightweight and effective inference-time activation intervention approach to reduce role overstepping in multi-agent collaboration. Specifically, DRAS constructs a role steering vector and a lightweight role-overstepping detector for each role. During LLM generation, the detector estimates the probability of role overstepping from the current activation state, and DRAS dynamically adjusts the steering strength accordingly to guide the agent toward its assigned responsibilities. Experimental results show that DRAS effectively reduces the number of role-overstepping trajectories by up to 86.6% compared with Vanilla MAS, thereby improving task quality score by 10.0%--11.1%, achieving a 1.50$\times$--1.61$\times$ task-completion speedup, and reducing token consumption by 26.8%--38.7%.

---


### 281. [LURE: a Phase-Labelled Synthetic Corpus of Online-Grooming Exchanges](https://arxiv.org/abs/2610.15908)

**<font color=#1a73e8>作者：</font>** Emanuele Florindi, Valentina Franzoni, Ludovico Guercio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Phase-annotated conversational data is essential for studying the progression of online grooming of minors and for developing early warning tools. However, the only publicly available source (i.e., Perverted-Justice archive, which contains a subset coded using ChatCoder) is small, outdated, and frozen. We present a synthetic corpus of groomer-victim exchanges, generated using a retrieval-augmented pipeline running on institutional hardware. This pipeline uses an openly available, eight-billion-parameter, refusal-ablated language model. The corpus was created using the five stages of the responsible-generation protocol for synthetic datasets: ontology-driven design based on the ChatCoder luring-communication scheme (eight communicative tags mapped onto four grooming phases); multi-model prompt testing; human-in-the-loop supervision; semantic and feature-level validation; and modality-aware documentation. The released corpus contains 2,121 unique exchanges across seven tags and four phases, each accompanied by a Plutchik emotion field. Validation quantifies the integrity and lexical profile of the corpus, as well as the reproduction of real seed lines, in-domain label recoverability (tag accuracy: 0.85; phase accuracy: 0.93) and its transfer to real ChatCoder offender lines, which were coded automatically at the eight-tag level (31,640 lines) and by human coders at the three-construct level (10,876 posts). Accuracy was measured for lexical and sentence-embedding features, while a real-versus-synthetic discriminator was able to separate the two domains with 91% accuracy. The scope of the corpus includes controlled, phase-conditioned experimentation, pipeline development and augmentation alongside real data and awareness material. The corpus, its datasheet and the audit code are released with vetted access.

---


### 282. [More Reasoning Is Not Always Better: Executing Clinical Guidelines with LLMs and Rules](https://arxiv.org/abs/2610.15912)

**<font color=#1a73e8>作者：</font>** Xiaoqian Lu, Guangfu Guo, Long Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown considerable promise in clinical decision support. However, existing approaches often rely on multi-step reasoning or multi-agent collaboration to execute clinical guidelines, introducing substantial computational overhead without reliably preventing decision errors. To address these limitations, we propose a framework for Medical Decision Execution (MedDEx) that integrates structured patient states with deterministic rule execution to support guideline-based treatment planning. MedDEx separates clinical record interpretation from guideline execution, leveraging LLMs to extract patient information and generate treatment plans while assigning guideline-defined decision logic to a rule executor. Experiments across multiple clinical guideline benchmarks demonstrate that MedDEx improves decision accuracy while reducing inference costs. Further analyses highlight the critical roles of structured patient representations and deterministic rule execution, suggesting that additional LLM reasoning does not necessarily translate into better guideline adherence.

---


### 283. [Fast and Accurate: Improving Personalized LLM Performance by Semantic Concentration Inspired Workload Split between RAG and Fine-Tuning](https://arxiv.org/abs/2610.15921)

**<font color=#1a73e8>作者：</font>** Xingke Yang, Sicong Li, Lingfeng Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With ever increasing personalized large language model (LLM) services, the next question to answer is how to improve the quality of services/users' experiences, which is indicated by personalized LLM generation accuracy/quality and inference latency. Although state-of-the-art designs, e.g., parameter-efficient fine-tuning (PEFT), retrieval-augmented generation (RAG) or Full PEFT+RAG, can help, they largely ignore the heterogeneous semantic concentrations of users' historical data and cannot fully unleash the potential of personal data for personalized LLM performance enhancement. In this paper, we propose PEFT Union RAG (PUR), a novel ``fast and accurate'' approach that exploits the semantic concentration of users' personal historical data to split workload between PEFT and RAG, aiming to improve personalized LLM performance in terms of better generation accuracy/quality and lower inference latency. Briefly, PUR partitions user's personal historical data and assigns semantic concentrated ``core'' information to PEFT for offline parametric fine-tuning, while retaining dispersed information for RAG. During the online LLM inference, PUR directly generates responses for ``core'' queries covered by the PEFT region and invokes RAG only for sporadic ``peripheral'' queries. Experimental results show that, by appropriately splitting workload between PEFT and RAG, PUR consistently achieves the best generation accuracy/quality for various users across multiple tasks, while reducing inference latency by 14.4%--46.6% compared with the best performed method.

---


### 284. [Scalable Weak-to-Strong Verifier Hardening for Agent Environments](https://arxiv.org/abs/2610.15924)

**<font color=#1a73e8>作者：</font>** Chong Zeng, Ziqian Zhong, Kexun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent environments are essential for large language model (LLM) development. They use programmatic verifiers to turn complex outcomes into rewards. Verifiers can be attacked into awarding full credit to cheating agents without completing the intended task, causing inaccurate evaluation and misalignment in training. As agent environments scale in numbers and difficulty, so must the repairing of exploitable verifiers. To this end, we ask whether today's model with scaled compute can automatically harden agent environments to prevent potentially stronger future models from reward hacking. We introduce a scalable, fully automatic approach to weak-to-strong verifier hardening. It first sets up an isolated verifier sandbox that agents cannot directly modify, then uses a hacker-fixer loop to find and repair remaining verifier vulnerabilities.
We apply this loop to Terminal Bench, KernelBench, and SETA, substantially reducing attack success across these agent environments. The iterative design scales with the hardening budget, producing progressively stronger defenses as the number of loop iterations increases and outperforming the static, non-iterative baseline. An earlier version of our hacker-fixer loop has been adopted by the official Terminal Bench repository as a way to audit exploits in its environments. Project page: this https URL.

---


### 285. [When Trackers Fail: VLM-Guided Verification and Recovery for Robust Video Object Segmentation](https://arxiv.org/abs/2610.15929)

**<font color=#1a73e8>作者：</font>** Valay Bundele, Susmit Agrawal, Mehran Hosseinzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent trackers built on foundation models such as the Segment Anything Model (SAM) achieve strong performance by propagating object masks through memory. However, this strength is also a key source of failure: under occlusion, reappearance, or distractors, an incorrect prediction can enter the tracking loop and be propagated over time, resulting in persistent identity drift. Existing approaches seek to prevent such failures through improved memory and temporal modeling, but once a failure occurs, the tracker has no explicit mechanism to recognize or correct it. We address this gap with Dual-Agent, a failure-aware tracking framework that complements propagation with explicit verification and recovery. We address this gap with Dual-Agent, a failure-aware tracking framework that complements propagation with explicit verification and recovery. A vision-language verification agent first reasons over spatio-temporal context to determine whether the tracker is still following the target. When a failure is detected, a correction agent uses temporal context to recover the target before tracking continues. The correction agent is trained on real SAM3 failures, augmented with targeted identity-switch and distractor perturbations that expose it to challenging ambiguities during recovery. On LVOS-v2 and SecVOS, Dual-Agent improves SAM3 by 1.2 and 2.7 $J\&F$, respectively. Importantly, the proposed framework transfers without retraining to SAM2.1, SeC, and Cutie, as well as to long-term video object tracking benchmarks including LaSOT-ext, TNL2K, and VOT-LT2022. Our results show that explicitly reasoning about when tracking fails and how to recover provides a complementary path to robust tracking beyond improving propagation alone. Project page: this http URL.

---


### 286. [The Anatomy of a Blind Spot: What an LLM Judge Must Be Shown, and How Much](https://arxiv.org/abs/2610.15938)

**<font color=#1a73e8>作者：</font>** Nitish Kumar, Prateik Pothuneedi, Greg Bandak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluation of text generated by large language models (LLMs) is increasingly delegated to LLMs acting as judges, yet what such a judge must be shown remains unresolved. We treat a judge whose reports are acted on as a regulator, in the sense of cybernetics, and ask what it must be shown, how much, in what form, and what its reports must get right. On seven public benchmarks we varied only what the judge was shown. Across three judges whose prices differ 10- to 17-fold, what the judge was shown mattered more than which judge it was. When a system revised its answers on feedback from a judge denied the material they had to respect, it ended below its starting point on instruction following and question answering. On instruction following the loss grew with each round, and it persisted when the judge saw the user's request but not the constraints and with a second judge family. On news summarisation, a correct reference summary beside the source undid most of the source's contribution, whereas on single-answer questions a reference helped. About a tenth of the source did almost all of its work, and a small entailment graph matched an LLM judge at finding errors in grounded text. We committed 83 testable clauses before running; of the 81 that ran, 32 met their bar and 50 went in the predicted direction, and most quantitative predictions from the theory failed. We report every shortfall and derive design rules tied to measured effects.

---


### 287. [ADAPT: Audio-Depth Action Planning with Transition-Aware Rewards for Lights-Out Industrial Navigation](https://arxiv.org/abs/2610.15956)

**<font color=#1a73e8>作者：</font>** Wenjun Huang, Shenghao Fu, Yian Jin 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action models for embodied navigation typically rely on RGB observations, limiting their applicability in lights-out industrial environments where visible illumination may be unavailable. We study illumination-independent navigation using spatial audio for target localization and depth for obstacle-aware geometry. To support this setting, we introduce DarkNav-Bench, a benchmark with 24 industrial scenes and four progressively challenging acoustic conditions. We further propose ADAPT, an audio-depth action-planning framework equipped with spatial-audio perception and optimized for closed-loop navigation through reinforcement learning (RL). Our key RL contribution, transition-aware reward shaping (TARS), defines a pose-aware shortest-action potential over a position-heading graph. Unlike conventional geodesic-progress rewards, TARS accounts for both feasible movements and in-place rotations, providing action-consistent feedback for policy optimization. Experiments show that ADAPT consistently outperforms training-based navigation baselines and zero-shot multimodal models on both seen and unseen scenes. On unseen environments, it achieves 90.6% success under Clean conditions and retains 60.0% success under the most challenging Localized Noise setting. These results demonstrate the potential of spatial audio and depth as complementary modalities for reliable RGB-free navigation in lights-out industrial environments.

---


### 288. [Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment](https://arxiv.org/abs/2610.15961)

**<font color=#1a73e8>作者：</font>** Alex Martí Guiu, Nicolas Zumarraga, Kevin O'Sullivan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM) occurs when fine-tuning a language model to a narrow task makes it misaligned on unrelated ones. Because organizations now routinely fine-tune models on their own data, it matters which kinds of training data cause EM. So far, studies have induced EM with data containing recognized safety failures, such as insecure code or harmful advice, while biased training data is typically examined by fairness research for the bias models learn from it rather than for its effects on safety. In real-world text, much of this bias, such as demographic stereotypes, appears not as derogatory language but politely, embedded in judgments about people. We ask whether learning such polite stereotypes can itself cause EM. We find that fine-tuning on polite answers that rely on stereotypes makes models less safe and less truthful on unrelated tasks. The effect holds across four open-weight model families (7B to 12B), both gender and race stereotypes, and repeated training runs, relative to controls trained on the same questions without the stereotype. We further show that the learned stereotype has its own direction in model activations, distinct from directions for generic misaligned traits such as deception. This direction exists before fine-tuning and can both control the learned stereotype and monitor its acquisition. Existing defenses against EM improve safety while leaving the stereotype largely intact. Beyond this controlled setting, fine-tuning on political news coverage also triggers EM, apparently amplified by partisan framing, and stereotype models acting as tool-using agents can carry out harmful tasks and blame people without evidence. Our results show that biased training data is not only a fairness problem but also a safety one. We argue that EM is studied too narrowly, and that fairness concerns and methods offer a natural way to broaden the search for its triggers.

---


### 289. [Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents](https://arxiv.org/abs/2610.15964)

**<font color=#1a73e8>作者：</font>** Yutong Cheng, Wei Cheng, Wenchao Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A self-evolving agent rewrites its own harness and must decide which rewrites to keep, so its improvement signal is the check a rewrite has to pass. Verifying a rewrite by agent rollout is expensive and subjective, while executable checks such as the repository's own tests are too sparse to catch behavior-changing rewrites, rejecting only a quarter of them. We instead take test feedback as the executable signal, and search for test suites that are both small and strong with a quality-diversity evolutionary algorithm, so that the signal is dense and informative. TeSearch treats suite size as a behavior descriptor, so that quality is pursued at every size and a small, strong suite is reachable, and learns a transition kernel during the search that denoises the LLM as an actuator on that descriptor. Across 129 real-world modules and three backbones, TeSearch delivers the highest-quality suites of any method compared, LLM-driven evolutionary search included, and the smallest of any LLM-based one. Used as the improvement signal of a self-evolving agent, it rejects 59.9% of behavior-changing rewrites against 25.3% for the repository's tests, at a 4.0% false-alarm rate and 3.5 s per decision. The code and data are available at this https URL.

---


### 290. [PopGen: Generating Semantically Diverse Populations for Zero-Shot Coordination](https://arxiv.org/abs/2610.15969)

**<font color=#1a73e8>作者：</font>** Paul Teiletche, Kanghyun Ryu, Kyungjoon Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-agent reinforcement learning, exposing a cooperator to partners with diverse strategies during training is key to better collaboration at test time. However, existing methods typically rely on trajectory-level proxies to measure diversity, which may label two distinct trajectories of the same strategy as diverse. Instead, our key insight is to leverage LLMs' ability to describe behaviorally distinct agents in environments, similar to how humans can recognize high-level strategies. To this end, we introduce PopGen, a framework that synthesizes semantically diverse agents from scratch using LLMs. PopGen first generates a diverse set of textual descriptions of agent behaviors, then translates each behavior into a code policy that can be executed within the environment. We show that cooperators trained against PopGen populations achieve robust zero-shot cooperation with unseen partners, outperforming population-play baselines across four collaborative environments. We further show that semantic diversity scales with PopGen population size, improving the cooperator's worst-case performance, and we identify design choices that preserve population quality while maximizing diversity. Our code is available at this https URL.

---


### 291. [CreepScope: Measuring Post-Use Authorization Exposure in Tool-Using Agents](https://arxiv.org/abs/2610.15988)

**<font color=#1a73e8>作者：</font>** Haoran Yu, Lifei Liu, Danping Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Authorization checks at individual tool calls do not reveal how long earlier authority remains usable. We study this lifecycle failure as privilege creep: a capability stays reachable after its last justified workflow step. We present CreepScope, a trace-oriented evaluation protocol that samples reachable authority at every step and separates no-remaining-use exposure into stale-after-use and never-required components; Capability-Step Exposure (CSE) counts total stepwise overexposure and Residual Privilege Debt (RPD) the terminal residue, while stale-after-use exposure is the direct privilege-creep measure. A 96-cell deterministic replay over 12 controlled storage, communication, and cloud-operation workflows validates these semantics: Static Task Scope and Monotonic On-Demand retain mean CSEs of 26 and 13, whereas an oracle-controlled Step Lease has zero CSE and zero residual debt by construction. All three persistent regimes share the same stale-after-use exposure of 13, so their CSE differences come from scope and grant timing rather than post-use retention; Full Access alone adds 91.33 never-required capability-steps. A separate 24-episode local case then lets Qwen2 7B choose tools in one simulated mail workflow: the injected stale send executes in all nine persistent-policy episodes and in none of the three Step-Lease episodes, while all 24 required action sequences complete. These results establish a reproducible containment case, not cross-workflow or cross-model effectiveness. Core metrics are reconstructed from raw events, and exact gates reject incomplete or duplicated evaluation grids.

---


### 292. [Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991)

**<font color=#1a73e8>作者：</font>** Lifei Liu, Haoran Yu, Danping Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed agent workflows cache delegated authority at tool gateways. Revocation may be reported at issuer commit, transport acknowledgment, or receiver persistence, although none of these observations establishes that all gateways enforced the change or that guarded effects stopped. We define C0-C5, a bounded outcome contract spanning issuer commit through effect prevention, and implement it as a persistent monitor over a frozen gateway set, call set, and observation window. A 14-case fault matrix checks conservative classification, sticky violations, restart persistence, and evidence immutability. In a derived audit of its eight semantic cases, treating C3 or C4 as completion produces seven or five false positives, respectively; the bounded C0-C5 verdict produces none. Descriptive scaling covers 1,024 gateways and 10,000 effect vectors. The primary experiment uses the maintained Keycloak 26.7 identity server and measures the contract across two durable receivers, eight physical agent-tool gateways, Filesystem and PostgreSQL effects, and 16 AWS hosts in three availability zones. Normal delivery and recovery commit no effects. Under receiver-selective non-delivery, transport acknowledgment and receiver persistence still succeed, but 112 of 225 calls (49.78%) are admitted, and all 112 effects commit in every treatment block. A separately provisioned execution repeats the result. OPA/Toxiproxy and a live three-role LLM workflow with networked MCP tools reproduce the persisted-but-not-enforced boundary on narrower surfaces. Finally, an unmodified external MCPMark agent executes 60 closed-loop task arms. Normal C4 denies all 31 exposed post-barrier calls and commits no effect; selective C3 allows 344 calls and commits 145 effects across Filesystem and PostgreSQL. Transport success is therefore evidence of progress, not a revocation-completion verdict.

---


### 293. [Handoff Curves: Initial Selection, Later Handoff, and Supervision Targets in Multi-turn LLM Routing](https://arxiv.org/abs/2610.15993)

**<font color=#1a73e8>作者：</font>** Daniel Matos, Lu Liu, Yanfeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how initial model selection, later handoff, and training targets affect success and cost in LLM tasks that span multiple turns. We compare several router architectures using handoff curves, which record task success and cost as the handoff step changes. Our dataset contains 34,204 complete executions of three Qwen models across BFCL, MultiWOZ, and $\tau$-retail, providing offline supervision for routing decisions. In our primary comparison, with Qwen3.5 35B-A3B as the starting model, allowing a later handoff does not establish an improvement in utility over initial selection on BFCL or MultiWOZ, and increases cost on BFCL across a range of cost weights. Changing the supervision targets improves router performance on both our dataset and TwinRouterBench. On our dataset, replacing noisy training success curves with monotone fits raises success by 0.2 to 4.1 percentage points at the same cost across the reported operating points. On TwinRouterBench, we construct targets that describe the model capability needed for the remaining work and difficult steps ahead. Compared with training on the benchmark's per-step labels, these targets raise trajectory pass scores by 7.8 percentage points and cost savings by 6.3 percentage points on the full static bank. A live deployment of the router trained with these targets resolves 79 of 100 instances at a router cost of 0.59 US dollars per instance.

---


### 294. [Large language model-generated patterns for epidemiological modeling: a multi-benchmark evaluation framework](https://arxiv.org/abs/2610.15994)

**<font color=#1a73e8>作者：</font>** Sophia Mao, Keshav Gandhi, Alexander Gutfraind  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Representing individual-level behavioral heterogeneity is challenging in epidemiological modeling, particularly when empirical behavioral data are sparse. We assess the potential of large language model (LLM)-generated behavioral outputs in addressing this challenge, using hepatitis C virus-related behaviors among people who inject drugs as a case study. Correspondence with epidemiological patterns was evaluated using external benchmarks: literature-informed association directions, correlations from an agent-based model (ABM), and survey associations. Across three LLMs, unconditional directional recovery across 28 retained literature-informed associations was 46-68%, compared with 82-93% agreement when LLMs were directly asked to classify the same associations. Mean absolute differences from ABM and survey correlation patterns were 0.11-0.13 and 0.15-0.18, respectively. Together, these findings show partial alignment between LLM-generated behavioral relationships and epidemiological evidence, despite higher knowledge-probe agreement. More systematic evaluation is needed before incorporating LLM-generated behavioral outputs into epidemiological models that simulate transmission dynamics.

---


### 295. [AutoSec-RAN: Specification-Grounded LLM Fine-Tuning for Automated Security Analysis of O-RAN](https://arxiv.org/abs/2610.15995)

**<font color=#1a73e8>作者：</font>** Anoop Mishra, Joshua Moore, Aly Sabri Abdalla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents AutoSec-RAN, a specification-grounded large language model (LLM) framework for automated security triage of Open Radio Access Network (O-RAN) testing. Unlike approaches relying on static rule sets or privileged access to raw packet captures, AutoSec-RAN fine-tunes Mistral-7B-Instruct through two Low-Rank Adaptation (LoRA) stages over a curated corpus of 69 O-RAN, 3GPP, and adjacent standards documents, then selectively augments inference with retrieval-augmented generation (RAG) over the same specification index. At inference, the model receives only an investigator-style question and a scenario metadata block, simulating an automated analyst operating without raw packet evidence. AutoSec-RAN is validated on a purpose-built 5G/O-RAN testbed across labeled fronthaul distributed denial of service replay scenarios. A Gemma-4-31B judge LLM scores each candidate's answer on faithfulness, correctness, and actionability relative to a reference authored from full packet capture and log evidence. AutoSec-RAN achieves a mean judge overall score of 0.713 across all 313 evaluation items (0.755 restricted to the five supervised taxonomy classes), clearing the 0.70 reporting threshold, and a blended score of 0.778 (0.808 supervised-only) when cosine similarity over Beijing Academy of Artificial Intelligence (BAAI) General Embedding (BGE) is incorporated as a secondary semantic signal. The framework performs strongest on mitigation and threat-model reasoning (with a mean overall of 0.849 and 0.848, respectively) and identifies a measurable gap on the held-out attack-direction class (0.515), a controlled result that exposes a specific training data requirement. These results establish specification-grounded LoRA fine-tuning combined with RAG retrieval as a viable foundation for automated security validation of AI-native O-RAN.

---


### 296. [PAIR: Memory-Efficient and Fast Inference with Reading--Reasoning Fusion](https://arxiv.org/abs/2610.16003)

**<font color=#1a73e8>作者：</font>** Sejun Park, Haocheng Xia, Yongjoo Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For context-based question answering, using one large model for both evidence extraction and answer reasoning requires substantial memory and computation. Existing approaches trade accuracy for efficiency within a single model only. We propose a multi-model approach for efficient inference: our method, PAIR, employs two differently sized models for evidence extraction and answer reasoning, respectively. A smaller Reader model processes and retains the full context, while a larger Reasoner model sees only the question and generated sequence without directly attending to the context. These capabilities are fused at the logit level: at each token, both Reader and Reasoner produce a prediction, and their logits are combined into one, behaving as a single next-token-prediction model. Fine-tuning further boosts their performance. On HotpotQA, PAIR with a 32B Reasoner retains 96% of that same 32B model's full-context accuracy while using roughly one quarter of its KV memory. At 45.7K-token contexts, PAIR achieves up to 3.2$\times$ higher end-to-end throughput than the full-context 32B model on the same GPU. PAIR also improves the accuracy-memory and accuracy-throughput trade-offs over evaluated token-reduction baselines. Its accuracy-preserving behavior generalizes across Qwen2.5, OLMo-3, and Gemma-3 model families.

---


### 297. [DelegateGuard: Purpose-Bound Capabilities for Delegated LLM Agent Workflows](https://arxiv.org/abs/2610.16005)

**<font color=#1a73e8>作者：</font>** Phat T. Tran-Truong, Ha Vo, Nhut Tran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> \textbf{(Context)} LLM agents increasingly delegate subtasks while holding authority over sensitive data, creating confused-deputy risks: an injected delegate can exfiltrate data, amplify its authority, or act after revocation. Existing leakage benchmarks expose these failures but do not constrain the authority a delegated agent may exercise. \textbf{(Methods)} We present \system, a reference monitor that converts the initiating user's authorization into attenuable capabilities over purpose, labels, operations, sinks, and delegation depth; every data-moving action is mediated outside the LLM, and revocation cascades through the delegation graph. We formalize a trace-level safety invariant and evaluate it with an adaptive within-authority adversary and four baselines, model-action and multi-turn ecological studies, and conformance and scale checks over deterministic traces and 517{,}401 Enron emails. \textbf{(Results)} \system blocks ungranted-sink exfiltration, authority amplification, revocation replay, purpose gaming, and intra-tool label violations, and dominates static allowlists on the revocation and intra-tool cases (10/10). Two open models proposed attacker-goal actions on 42/45 and 44/45 injected traces, all blocked at execution; a 90-run multi-turn study cut leakage from 0.844 to 0.20 with full task completion, at microsecond per-decision overhead. Proposition~1 characterizes exactly where attenuation-based authorization suffices, a boundary we also reproduce empirically across four observable-sink workflows. \textbf{(Conclusion \& Significance)} Purpose-bound runtime authorization gives delegated LLM workflows a model-independent execution boundary and a precise recipe for composing it with declassification and content monitoring on externally observable sinks.

---


### 298. [Improving the Evaluation of Biomedical Question Answering with Few Human Preference Signals](https://arxiv.org/abs/2610.16008)

**<font color=#1a73e8>作者：</font>** Shakila Mahjabin Tonni, Xiang Dai, Sarvnaz Karimi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems are increasingly used for biomedical Question Answering (QA). However, evaluating their effectiveness remains challenging due to the lack of reliable reference resources and the frequent misalignment between automatic evaluation metrics and human judgments. One practical question is how evaluation results should be used to guide development decisions, especially when they correlate weakly with human judgments and may even lead to different conclusions. We explore how to use a small amount of human preference signals to calibrate direct assessment evaluation metrics, and show that calibrated metrics consistently outperform baselines that either treat all metrics equally or rely on a single best metric across multiple datasets.

---


### 299. [Meaningful Moments: A Corpus of VLM-Derived Temporal Importance Labels for Video Action Recognition](https://arxiv.org/abs/2610.16009)

**<font color=#1a73e8>作者：</font>** Cameron Keith, SouYoung Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Not every moment in a video is equally useful for recognizing an action. A few decisive moments often carry the evidence: the instant an object moves, the peak of a dive, or one object placed on another. Existing video datasets rarely provide large-scale, action-conditioned labels for which short segments carry that evidence. This work asks whether vision-language models can identify meaningful moments at scale and whether those labels improve action this http URL introduce Meaningful Moments (MM), a corpus of about 4.58 million VLM-generated per-segment importance scores for nearly 500,000 class-labeled videos spanning Something-Something v2 (SSv2), Kinetics-400 (K400), and Diving-48 across 622 action classes. We freeze the action classifier and vary only temporal sampling. An alpha-parameterized comparison of importance-led selection against an importance-inverted control separates gains from the VLM signal from gains caused by variable-density sampling alone. Across all three datasets, VLM-derived importance is informative: at the hard-cut endpoint, keeping VLM-important segments outperforms keeping VLM-designated filler. Usefulness depends on class structure. On Diving-48, importance-led fast-forwarding preserves full-video recognition while the inverted control collapses by roughly 30 percentage points. On K400, hard-cut selection beats uniform sampling by 1.45 percentage points, rising to 2.05 under threshold selection. On SSv2, the labels carry signal but do not recover full-video performance. Direct scoring matches greedy removal within its noise floor at roughly 25 times fewer oracle calls, and a four-VLM cross-oracle study shows consistent downstream trends. We release the importance labels and evaluation protocol under CC-BY-4.0; SSv2 class strings remain under CC-BY-NC-4.0.

---


### 300. [When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.16039)

**<font color=#1a73e8>作者：</font>** Sunday Oyinlola Ogundoyin, Muhammad Ikram  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems (MALS) introduce a privacy-leakage problem that conventional sensitivity-based defenses miss, since information disclosed to one authorized agent can propagate through routine coordination to an unauthorized one, without compromise or malicious behavior. This motivates topology-aware enforcement that blocks unauthorized propagation while preserving authorized disclosure. We evaluate 485 scenarios across coordinator-worker, peer-to-peer, and hierarchical topologies, instrumenting seven communication channels and measuring surface leakage and disclosure to topology-introduced recipients. We introduce RECONS, a Detect -> Decide -> Transform sanitizer conditioning intervention on recipient and execution context rather than sensitivity alone. Topology changes where protected information propagates, with disclosure to topology-introduced recipients rising from 0% to 52.2% while surface leakage stays nearly flat at 60.6-62.8%. This effect persists across four generator models and a second orchestration framework, though magnitude and relay paths differ; framework choice separately drives a 150x leakage spread, so topology alone is not sufficient. RECONS reduces residual disclosure from 96.7% without sanitization to 29.25%, preserving 94.1% of authorized disclosures versus 20.5% under blanket redaction. Detection coverage is the dominant bottleneck, accounting for 95.5% of residual disclosures. These results show that privacy enforcement in MALS must reason about the recipient and communication path realized at runtime, not sensitivity or topology assumptions alone.

---


> [!TIP]
> 当前位于：**251-300**（第 6/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
