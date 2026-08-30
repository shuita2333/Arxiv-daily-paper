# 🧠 大模型相关研究 | 2026年08月31日

> 本类共 **231** 篇论文：已确认 **221** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-231**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-231**

---

### 201. [One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles](https://arxiv.org/abs/2608.27338)

**<font color=#1a73e8>作者：</font>** Zhichen Zeng, Huiyuan Chen, Jingru Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Specializing Large Language Models (LLMs) toward distinct abilities underpins successes ranging from personalized assistants to multi-agent systems (MAS). Single-agent paradigms rely on pre-defined personas or steering vectors to induce specialization, yet they impose a single fixed specialization that fails to adapt to diverse queries. Conversely, MAS achieves dynamic multi-perspective problem solving by orchestrating agents with distinct text-based roles, but fusing these specializations requires multi-turn interactions that inflate context length and inference cost. To address these limitations, we propose Mixture of Roles (MoRe), which adaptively composes multiple specializations into a single steering vector for single-turn inference. Specifically, MoRe learns a diversified codeboox of steering vectors, each of which encodes a latent role. A query-aware router dynamically fuses the codebook into a steering vector that encompasses multiple roles. By steering the backbone LLM with the composed vector, MoRe enables multi-perspective specialization in a single-agent, single-turn inference process. The proposed MoRe can be efficiently trained via a three-stage SFT curriculum and GRPO post-training, while the backbone LLM remains frozen. Experiments across reasoning and personality benchmarks show that MoRe outperforms single-agent baselines by 2.2% on average, and achieves performance on par with MAS while reducing token cost by 20x.

---


### 202. [Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting](https://arxiv.org/abs/2608.27339)

**<font color=#1a73e8>作者：</font>** Xinwei Qiang, Xiang Fang, Chang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block drafters propose several tokens in one forward pass, before earlier target tokens are realised. Their rejection mixes two losses: missing within-block path information and imperfect modelling of observable information. Accepted length cannot distinguish them. We separate the two with an information floor, the minimum expected rejection at a specified conditioning order; rejection above this floor is the model gap. Estimating both from target rollouts across four domains, four open-weight targets, and a frontier API target yields three findings. First, the all-parallel floor reaches $0.286$ at the final slot on Qwen3-4B, limiting even the best proposal to $71\%$ per-slot acceptance. Second, one realised token removes $86$--$100\%$ of this floor, a locality also recovered by an independent mutual-information analysis. Third, current drafters remain far above their floors: the final-slot model gap accounts for $43$--$64\%$ of DFlash rejection and $85$--$92\%$ of DSpark's oracle-conditioned rejection. These findings separate the value of short-range conditioning from proposal quality.

---


### 203. [Not All Eval-Awareness Is Equal: Capabilities Framing Predicts Compliance](https://arxiv.org/abs/2608.27340)

**<font color=#1a73e8>作者：</font>** Allison Zhuang, Santiago Aranguri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Steering interventions targeting eval-awareness, a model's recognition that it is being tested, are increasingly used in safety evaluation pipelines, where evaluation-awareness is treated as a single quantity to be suppressed. We show that verbalized eval-awareness in chain-of-thought can be identified as capabilities-flavored ("the user is testing my ability to follow instructions"), safety-flavored ("the user is testing my boundaries"), both, or neither: framings that predict compliance very differently. On Qwen3-32B over the FORTRESS dataset, capabilities-framing predicts compliance with a +24 to +46 percentage-point gap over safety-framing across all tested steering conditions. A CoT-prefill intervention on eval-awareness-negative rollouts suggests the link is causal, with 10 of 11 prefills shifting compliance in the predicted direction. Then, eval-awareness is not behaviorally uniform: aggregate suppression rates can move while the safety-relevant component does not, and the same "X% suppression of eval-awareness" can correspond to qualitatively different behavioral outcomes.

---


### 204. [Pair-Level Essay-Scale Republication and Reuse from Fragmented Historical Text Reuse: A Workflow Study on Eighteenth-Century Books and Newspapers](https://arxiv.org/abs/2608.27343)

**<font color=#1a73e8>作者：</font>** Ke Shu, Kira Hinderks, Eetu Mäkelä 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment retrieval alone. The study focuses on a candidate set centered on essays by eighteenth-century Scottish philosopher David Hume, spanning books from ECCO (Eighteenth Century Collections Online) and historical newspapers. Because the input consists of fragmented reuse hits instead of clean document pairs, and positive coverage is inherently incomplete, we formulate the task as pair-level evidence consolidation into plausible transmission relations and compare three methodological families: a staged rule-based workflow, baselines (a decision tree and two direct LLM settings), and automated rule adaptation. On labeled ECCO--ECCO slices, pair-level feature aggregation alone already reaches 0.948 F1 on the main labeled slice, while the final workflow gives the strongest overall precision-recall trade-off among the tested rule stages. On the full ECCO--ECCO candidate universe, direct LLM baselines flag up to 14,886 pairs as reprints compared to 771 for the final workflow, behaving in this direct-prompt setup as high-recall candidate expanders rather than precision-controlled deployment classifiers. On ECCO--Newspaper, manual audit confirms all 176 predicted positives as genuine cases of republication or reuse, while issue duplication and source-side multiplicity reveal additional provenance structure. Under incomplete ground truth, auditable pair-level evidence consolidation provides a practical way to produce compact candidate spaces for historical inspection.

---


### 205. [INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment](https://arxiv.org/abs/2608.27348)

**<font color=#1a73e8>作者：</font>** Yutong Zhang, Jianshuo Dong, Peng Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: this https URL.

---


### 206. [Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO](https://arxiv.org/abs/2608.27351)

**<font color=#1a73e8>作者：</font>** Yunpeng Ba, Zhi Zheng, Yue Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Optimization (GRPO)). By systematically investigating ES dynamics and mechanisms, this paper first identifies a performance advantage of ES over GRPO, theoretically and empirically showing that ES can lead to broader reasoning coverage, thereby better exploiting the reasoning capabilities of pretrained LLMs. Theoretically, we show that verifier-projected Jensen-Shannon diversity across the ES population is helpful to higher Pass@K performances. Empirically, unlike GRPO, which exhibits entropy collapse, ES improves Pass@1 while attaining higher Pass@K than GRPO. We further develop a sequential GRPO-ES training strategy that combines GRPO's strength in Pass@1 with ES's gains in Pass@K. Second, we find that despite substantial whole-model parameter drift, the task-performance gains of ES are only contributed to a sparse subset of larger-magnitude updates. This functional sparsity suggests that large parameter movement need not imply widespread functional change, and held-out evaluations further show that it does not necessarily lead to catastrophic forgetting. Finally, we study how hyperparameter design affects the effectiveness of ES, demonstrating that ES requires a smaller population size in a larger LLM. These findings position ES as a distinct reasoning post-training paradigm rather than a less effective, memory-efficient alternative to GRPO.

---


### 207. [Sophistication in GenAI Use: Field Evidence from a Large Firm](https://arxiv.org/abs/2608.27364)

**<font color=#1a73e8>作者：</font>** Nicholas J. Hallman, Zachary T. Kowaleski, Anu Puvvada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how sophistication in generative AI (genAI) use varies among the back-office workforce of a large firm. Using proprietary data, we observe 713,564 employee prompts and their corresponding large language model responses from nearly 4,000 back-office employees across 15 functional areas over eight months in 2025. We document three main findings. First, senior employees exhibit more sophisticated genAI use, consistent with domain expertise complementing genAI capabilities. Second, sophistication varies considerably across functions and is highest in Strategy, Digital Innovation, and Project Management, three groups that share a focus on firmwide strategic initiatives and organizational change. Third, we observe neither improvements in sophistication over time nor lasting improvements following formal AI training, suggesting that sophisticated use can be difficult to change. Together, our study provides measures of and insights into sophisticated genAI use that managers can use to improve outcomes and that researchers can use in future research.

---


### 208. [Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090](https://arxiv.org/abs/2608.27370)

**<font color=#1a73e8>作者：</font>** Kairong Luo, Jiarui Cui, Yaorui Yin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model pretraining has become almost synonymous with prohibitive cost, placing it out of reach for much of the academic and open-source communities. Although strong open-source efforts already exist, including open-weight models and open-source training recipes, a cost-efficient, hardware-accessible, and open-source pretraining recipe has long been missing. Even at a small scale, training Llama-3.2-3B costs over \$1.5M, and reproducing SmolLM3-3B needs over \$700K. In this report, we present an open pretraining recipe designed to lower this barrier. Using this recipe, we train a collection of Puro-2B models from scratch on up to 1.4 trillion tokens with FP8 precision on consumer-grade RTX 5090 GPUs. The models in the collection differ in token budgets and selected recipe variants. Our best model is trained at a compute cost of less than \$6.9K and approaches Qwen2.5-1.5B performance under our evaluation protocol. This cost efficiency is enabled by a combination of approaches, including hardware selection, low-precision training, hyperball optimization, curriculum model averaging, and the data recipe. Beyond the recipe itself, we provide two additional results. First, across the Puro-2B collection, we derive a Puro Cost Scaling Law that relates training cost to average model performance; the fitted law suggests that about \$4.4K, less than \$5,090, is sufficient to reach the performance of Qwen2-1.5B. Second, as an end-to-end case study, we examine how pretraining data curricula shape downstream performance after post-training. Such controlled studies are enabled by having access to the full pretraining pipeline rather than model weights alone. We release the full training recipe for Puro-2B, including data, code, and model weights under Apache 2.0 at this https URL.

---


### 209. [CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases](https://arxiv.org/abs/2608.27391)

**<font color=#1a73e8>作者：</font>** Sil Hamilton, Albert Yu Sun, Oscar J. Romero 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly able to answer complex questions about enterprise-scale document collections. But evaluation is hard: companies don't want to share internal communications, and synthetic datasets have been overly simple. We present CorporateBench (CB), a human-validated multi-task Q&A benchmark whose scale approaches the conditions LLMs encounter in corporate communication networks, with evaluation corpora surpassing 230,000 documents. CB evaluates LLMs across two dimensions (information extraction and knowledge base querying) through four synthetically generated firms ranging from 12 to 10,000 employees. Each corpus is sampled from a temporally evolving knowledge base describing a consistent world, guaranteeing cross-document logical consistency even across hundreds of thousands of documents. We evaluate five LLMs on CB, revealing increasingly poor performance as input size approaches realistic scales. CB provides LLM developers a metric for corporate communication reasoning, filling a crucial gap in the benchmarking ecosystem.

---


### 210. [RATIO: A Benchmark for Retrieval Across Typed Ideation Operations in Scientific Literature](https://arxiv.org/abs/2608.27394)

**<font color=#1a73e8>作者：</font>** Maayan Sharon, Tom Hope  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieved scientific literature can serve as inspiration for both human and AI scientists. Inspiration can take different forms: prior work may directly suggest how to address a problem, or surface directions at different levels of abstraction - zooming out to a more general view or zooming in to a concrete realization. We introduce RATIO (Retrieval Across Typed Ideation Operations), a large-scale benchmark in which relevance is defined by three operations which we name ideation moves: Address retrieves potential approaches for stated problems, Broaden retrieves more general formulations, and Specify retrieves concrete instantiations. RATIO is constructed from millions of full-text scientific papers across CS literature via a general recipe that extends discourse-marker distant supervision - previously used only for classification - to corpus-scale retrieval, combined with extensive LLM and human vetting. Experiments show that operation-specific fine-tuning substantially boosts retrievers but leaves much room for further improvements. RATIO provides a scalable training and evaluation framework for retrieval components that support literature-grounded ideation, opening up new research avenues on scientific inspiration retrieval.

---


### 211. [Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction](https://arxiv.org/abs/2608.27397)

**<font color=#1a73e8>作者：</font>** Jin Mu, Guanhua Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical language models can achieve strong in-hospital accuracy yet fail under deployment shifts because they exploit note-specific artifacts (e.g., templates, separators, boilerplate) that do not reflect patient state. We propose CAST (Concept-guided Artifact Suppression Tuning), an SAE-based framework for auditable clinical text classification. CAST uses Sparse Autoencoders to expose sparse, human-auditable features from intermediate Transformer activations, labels SAE latents with an LLM-assisted interpretation pipeline and ICD-10 retrieval constraints, suppresses verified artifact latents via residual subtraction during fine-tuning, and provides post-hoc per-concept attributions for auditing model decisions. On MIMIC-IV discharge-note mortality prediction, CAST improves over its corresponding fine-tuned encoder baselines and remains competitive with strong LLM baselines, while producing a feature-level audit trail of the clinical concepts that support each prediction and the artifact concepts suppressed during training.

---


### 212. [How Language Models Organize and Structure Moral Knowledge](https://arxiv.org/abs/2608.27402)

**<font color=#1a73e8>作者：</font>** Orion Reblitz-Richardson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one another and organizing the relationships between them geometrically.
We train six independent linear probes on open-weight language models, one per Moral Foundations Theory (MFT) category (care/harm, fair/cheat, lib/oppress, loy/betray, auth/subv, sanc/degrade), and examine how the resulting directions relate to each other in representation space. We find the directions neither collapse into a single moral detector nor isolate from one another. Rather, they span a near-maximal number of independent dimensions while sharing a positive common component. The shared component is the signature of integration, and it is moral-specific relative to a matched non-moral concept battery built identically (mean pairwise cosine 0.26 vs. 0.013).
The geometry is consistent across architectures and scale and reaches its integration regime early in pre-training, well before probe accuracy saturates. The structure the model discovers shows no evidence of the individualizing/binding distinction predicted by Moral Foundations Theory (an underpowered test: only 20 candidate partitions exist) but rather reflects corpus statistics. Extending to moral dilemmas, each dilemma direction partially composes from its component foundations, at 2.7x a mismatched-pair baseline, while the majority of its variance encodes conflict-specific structure. The model represents moral tension itself, not a pre-resolved judgment.

---


### 213. [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](https://arxiv.org/abs/2608.27409)

**<font color=#1a73e8>作者：</font>** Siye Wu, Kai Yang, Yuchen Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them. We organize three fusion paradigms by the artefacts they reuse: Merge combines expert task vectors, Mix RL pools their datasets, and multi-teacher on-policy distillation (MOPD) uses both. Because they have largely been studied in isolation, how they compare and how to choose among them remain unclear. We compare all three using shared experts and data across model scales and a multi-domain benchmark suite. Although their average performance differs by at most 1.4 points, the gap reaches 8.6 points on a single benchmark, with domain-level variation tracking cross-domain relations visible in task-vector geometry. Training dynamics expose distinct constraints: Mix RL depends on domain mixture proportions, MOPD remains bounded by its teachers, and Merge compresses all expert updates into one. All three improve single-sample accuracy without measurable gains in solution coverage or losses in held-out capabilities. These results yield a practical guideline: use Merge when experts already exist and cheap fusion is paramount; Mix RL when training a unified model without experts, with domain proportions adjusted for cross-domain transfer; and MOPD when preserving domain-specific gains matters more than surpassing teachers or minimizing end-to-end cost.

---


### 214. [Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information](https://arxiv.org/abs/2608.27417)

**<font color=#1a73e8>作者：</font>** Chanho Park, Daehyeon Choi, Jihyun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism behind this behavior is not understood. Inspired by retrieval heads in large language models, we ask whether VLMs contain an analogous mechanism for visual retrieval. We answer affirmatively by introducing Visual Retrieval Heads (VRHs), a small subset of attention heads (about 1.7-2.6%) that are causally responsible for grounding text descriptions to image regions. To find them, we recast existing head-scoring methods under a unified design space over query tokens, key aggregation, and cross-sample aggregation. We then show that scoring attention from output prediction tokens with a sum over the ground-truth referent region most reliably identifies causal heads. Across eleven VLMs and five referring-expression benchmarks, masking only the top 20 VRHs reduces grounding accuracy by up to 80 percentage points, while masking the same number of random heads has little effect. Beyond replicating the causal-sparse-universal triad established for text retrieval heads, VRHs exhibit several properties not previously reported: they generalize across visual reference tasks, remaining causal on attribute, spatial, counting, and visual-math benchmarks despite being discovered through bounding-box prediction; they are functionally specific, preserving output format while corrupting localization; and they are architecturally shared, transferring causally across VLMs that share an LLM backbone but differ in vision encoder, projector, and instruction tuning.

---


### 215. [Boosting LLM Exploration via Weak-Model Guidance in RLVR](https://arxiv.org/abs/2608.27420)

**<font color=#1a73e8>作者：</font>** Xingyu Shen, Huishuai Zhang, Peng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) significantly improves LLM reasoning but often causes a drop in policy entropy, leading to narrowed reasoning coverage and degraded pass@$k$ for large $k$. While existing methods mitigate this entropy collapse through algorithmic regularizations, cross-model non-parametric perturbation is also neglected. In this work, we propose a simple yet effective approach to preserve the generative diversity of LLMs during RLVR. Instead of relying solely on internal exploration, we force the target model to generate answers based on partial reasoning trajectories generated by a smaller, weaker language models. These unfamiliar prefixes effectively disrupt over-confidence and encourage the exploration of distinct reasoning paths. We empirically study the potential of outer prefixes, revealing the mechanism of the impact of distributional discrepancy to the exploration dynamics in RLVR training. Experiments across multiple mathematical benchmarks show that our method consistently outperforms vanilla RLVR. Notably, the performance gain becomes increasingly pronounced as $k$ scales up, demonstrating a substantial expansion of reasoning coverage. Furthermore, our approach efficiently mitigates entropy collapse without requiring additional SFT, intricate reward designs, or complex prompting.

---


### 216. [Stochastic Estimation of Transduced Language Models](https://arxiv.org/abs/2608.27428)

**<font color=#1a73e8>作者：</font>** Vésteinn Snæbjarnarson, Samuel Kiegeland, Manuel de Prada Corral 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transduced language models (TLMs) compose a pretrained \emph{source} language model with a functional finite-state transducer to induce a language model over \emph{target} strings. Computing the probability of a target prefix under a TLM amounts to summing the source-model probabilities of all source strings that the transducer maps to target strings beginning with that prefix. This set can be exponentially large or infinite. Prior work uses a computational shortcut based on source prefix probabilities, then approximates the resulting sum with threshold-pruned beam summing. This produces a lower bound with unknown error. Instead, we resample source prefixes without replacement and reweight each selected prefix by the inverse of its inclusion probability. We show that applying this correction recursively gives an unbiased estimator of the target prefix probability and lets us estimate the mass lost by threshold pruning. Our beam-summing algorithm extends the retained source prefixes and samples which prefixes to keep, reducing their number as more probability mass is added to the running estimate. This can save computation and guarantees that the run halts with probability one. We evaluate the method on encyclopedic text and DNA against sequential Monte Carlo baselines that resample with replacement. It achieves a better compute--variance tradeoff on text and lower error at the same maximum number of particles on DNA. On a DNA-to-amino-acid transduction, it reduces runtime by several orders of magnitude relative to threshold-pruned beam summing and makes estimating prefix probabilities for long target strings feasible. Replacing threshold pruning with unbiased sampling in a published reading-time analysis substantially lowers the estimated corpus surprisal but leaves the published conclusions unchanged.

---


### 217. [RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution](https://arxiv.org/abs/2608.27439)

**<font color=#1a73e8>作者：</font>** Junjie Zhang, Hui Liu, Kecheng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unclear tool credit, and full trajectories add context overhead while reducing interpretability. We propose RedEvoAgent, a black-box red-teaming agent that distills cross-case attack trajectories into a concise, human-readable attack skill. The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. Experiments on multiple benchmarks, target models, and target execution harnesses show that RedEvoAgent outperforms fixed and agentic baselines, improves tool efficiency, and transfers across attacker models and target execution harnesses.

---


### 218. [Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?](https://arxiv.org/abs/2608.27443)

**<font color=#1a73e8>作者：</font>** Ting Yan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents are poised to become a primary interface to digital products, acting across email, files, payments, and personal data. People without professional software backgrounds need understandable, reusable ways to control actions across services. We examine a mechanism in which a language model maps actions to plain-language consequence categories with user-authored "allow", "ask", or "never" rules. We ask what is gained and lost when decisions are made in advance as reusable rules rather than separately for each action.
We analyzed 113 participants without professional software backgrounds across three conditions: per-action human-in-the-loop approval (HITL), automated per-action model review (AUTO), or user-authored consequence policy (POLICY). Participants judged 2 examples in each of 4 consequence categories; POLICY participants then set one rule per category. All supervised an 18-action simulated day, including 7 overreach actions. POLICY blocked less overreach than HITL (-20.1 percentage points, 95% CI [-32.1, -8.1]) and AUTO (-14.5 points, 95% CI [-25.8, -3.2]). POLICY lowered runtime prompts from 18.0 to 10.9, but total intervention time was not reliably lower when rule setup was included.
Exploratory analysis showed that participants chose "ask" for 114 of 140 POLICY rules, returning most overreach actions to runtime. Of the 148 overreach actions executed in POLICY, 133 followed human approval and 15 ran automatically under "allow" rules. Across all 7 overreach actions, POLICY had the highest approval rate. Counterintuitively, user-authored rules did not by themselves provide stronger protection: many actions outside users' original requests went through after users approved them. These results reveal a gap between preference and commitment: repeatedly choosing "ask" preserves case-by-case choice but prevents a standing policy from settling decisions in advance.

---


### 219. [TTPO: Test-Time Policy Optimization](https://arxiv.org/abs/2608.27448)

**<font color=#1a73e8>作者：</font>** Aozhe Wang, Zhengxi Lu, Jianze Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent prominent post-training methods, such as Reinforcement Learning (RL) and On-Policy Self-Distillation (OPSD), have driven rapid progress in mathematical reasoning for large language models, yet their reliance on ground-truth labels precludes test-time training (TTT). Replacing ground truth with majority-vote pseudo-labels is a natural alternative, yet it is fragile: an incorrect vote corrupts the teacher and misleads every token. We observe that this failure mode is asymmetric: rollouts that disagree with the pseudo-label are typically wrong regardless of whether the vote itself is correct. Building on this observation, we propose Test-Time Policy Optimization (TTPO), an asymmetric objective that distills agreeing rollouts via OPSD and penalizes disagreeing rollouts with Grouped RL. Token-level selection further refines both branches: distillation down-weights already-converged positions, while RL penalizes only confident errors. Both updates remain well-grounded even under frequent pseudo-label errors, and majority-vote routing yields tighter self-supervision as the model improves. Without any labels, TTPO matches label-supervised OPSD on five competition-level benchmarks, raises Qwen3-1.7B from 38.0% to 45.2% in TTT, yields +25.2% to +36.4% without thinking, and shows strong cross-task generalization.

---


### 220. [CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes](https://arxiv.org/abs/2608.27455)

**<font color=#1a73e8>作者：</font>** Yufan Wu, Yinghui He, Zhengyi Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in inference-time scaling have significantly improved the reasoning performance of large language models (LLMs). However, these methods typically rely on repeated generation or external verification. To address this limitation, we introduce CritICL, a novel inference-time framework that improves reasoning while maintaining high efficiency. Our key insight is that LLM failure modes exhibit structured patterns across model scales within the same family. Instead of treating failures as undesirable outputs, CritICL leverages them as a source of guidance. Specifically, we utilize failure modes derived from weaker models and incorporate them into inference through critique-based in-context examples. We propose two variants: CritICL-dynamic, which adaptively predicts input-specific failure modes and retrieves critiques, and CritICL-static, which uses a global failure mode profile to provide stable guidance. Experimental results show that CritICL consistently outperforms standard in-context learning and achieves performance competitive with or superior to test-time scaling methods, while requiring significantly fewer generations and lower token cost. Code available at: this https URL

---


### 221. [UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City](https://arxiv.org/abs/2608.27456)

**<font color=#1a73e8>作者：</font>** Tianjie Ju, Zheng Wu, Yueqing Sun 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround supports closed-loop interaction from a first-person view and provides an interactive map for navigation. Agents can directly enter the 3D city and explore from a first-person view. Our analysis follows the growth of the spatial problem through three research questions. We first test whether an agent can ground a local scene well enough to answer spatial questions after active observation. Then we ask whether that grounding supports navigation as destinations become farther away and less explicit. Finally, we examine whether the resulting behavior survives changes in route availability and pedestrian motion. Contemporary MLLM agents usually show useful atomic abilities in visual recognition and short-range spatial reasoning, while orientation and pedestrian-aware movement remain unreliable. Their central failure emerges over extended exploration, where local abilities do not compose into sustained goal-directed behavior and errors accumulate without effective correction. We hope UrbanGround will support broader study of how far current MLLM agents can explore reliably in complex, open-ended urban environments.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 222. [FAN-LoRA: A Fourier-Adaptive Nonlinear Low-Rank Adaptor for Medical Foundation Model Domain Adaptation](https://arxiv.org/abs/2608.26531)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziquan Liu, Zhewei Zhu, Xuyang Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of vision foundation models, notably the Segment Anything Model (SAM), has catalyzed significant advancements in natural image segmentation. However, their direct transfer to medical imaging remains severely bottlenecked by profound domain gaps, such as cross-modality and cross-center shifts. Existing Parameter-Efficient Fine-Tuning (PEFT) methods facilitate the adaptation of SAM to medical domains; nevertheless, they frequently suffer from performance degradation under severe distribution shifts. This vulnerability primarily stems from the implicit entanglement of heterogeneous frequency components within a shared low-rank subspace, which directly exacerbates sub-optimal structural alignment and localized boundary blurring. To overcome this representational bottleneck, we propose the Fourier-Adaptive Nonlinear Low-Rank Adaptor (FAN-LoRA), a novel frequency-decoupled fine-tuning architecture. FAN-LoRA explicitly separates the optimization space by employing a B-spline-driven low-pass branch for global structural alignment, synergistically coupled with a discrete Fourier high-pass branch for local textural compensation. Extensive experiments across three challenging cross-modality and cross-center benchmarks demonstrate that FAN-LoRA consistently outperforms state-of-the-art PEFT baselines. Compared to the strongest competitors, our method achieves consistent improvements in average Dice scores and notable reductions in boundary errors, while maintaining a compact module size without compromising computational efficiency.

---


### 223. [SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning](https://arxiv.org/abs/2608.26550)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhuochun Li, Yuelyu Ji, Yiming Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning-based knowledge distillation has the potential to transfer complex reasoning from teacher to student models, yet it currently faces a critical dilemma: researchers must choose between sparse outcome-based rewards, which provide insufficient logical guidance, or expensive neural Process Reward Models (PRMs) for dense signals. We resolve this by introducing SPEAR (Symbolic Process Evaluation and Alignment Reward), a training-free and plug-and-play process reward method for sequence-level on-policy distillation. SPEAR projects natural-language reasoning traces into domain-adaptive symbolic milestones, providing an efficient proxy for process-level reasoning alignment. By utilizing the longest common subsequence (LCS) to align student explorations with teacher milestones, SPEAR provides a dense, order-aware reward signal that enforces logical consistency without the need for an external neural verifier. Our experiments across math, science, and commonsense reasoning tasks demonstrate that SPEAR effectively bridges the reasoning gap between student and teacher models via sequence-level distillation with efficient dense process rewards. Our code and data are available at: this https URL.

---


### 224. [PailitaoGR: Latent Think-with-Images for Generative Image Retrieval](https://arxiv.org/abs/2608.26658)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaomeng Fan, Yueran Liu, Shengyu Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative retrieval has demonstrated strong performance by directly generating product semantic identifiers (SIDs).
Extending this paradigm to image search, however, is nontrivial because real-world query images contain diverse information, including the search target, useful auxiliary evidence, and irrelevant visual content.
This requires the model to identify and focus on the search target while selectively utilizing auxiliary evidence. In this paper, we propose \textbf{PailitaoGR}, a \emph{Latent Think-with-Images} method for generative image retrieval, which internalizes target-focused perception and selective auxiliary-evidence utilization into a the generative retrieval model, enabling \textit{Zooming without Cropping} and \textit{Reading without OCR}. Specifically, we design a target-focused perception mechanism that identifies and enhances visual tokens of the search target, consisting of a target Enhancer and a learning strategy based on on-policy distillation and attention guidance loss, enabling the model to focus on search-target regions. We also design a selective auxiliary-evidence utilization mechanism that identifies and enhances visual tokens of auxiliary evidence, including an auxiliary enhancer and an in-capacity incremental contrastive distillation strategy, enabling the model to exploit auxiliary evidence. We construct training and validation sets sampled from real-world online image-search logs. Experiments show that our method outperforms existing baselines by an average of 13.8\%, validating its effectiveness.

---


### 225. [RECAP-Forcing: Retaining Content Appearances for Long Video Generation](https://arxiv.org/abs/2608.26671)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haiyang Xu, Zheng Ding, Zhuowen Tu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long autoregressive video generation faces a fundamental memory challenge: with a finite attention window, a model must decide which information from an ever-expanding history to retain. Existing methods organize memory temporally, preserving recent frames while compressing or discarding older ones. We instead propose RECAP-Forcing, organizing memory by appearance novelty. A long video is not merely a sequence of frames, but an evolving cast of subjects, objects, and scenes whose identities must remain consistent over time. We organize memory by retaining the KV cache associated with newly appearing content--such as entering subjects, disoccluded regions, and newly introduced scenes--at the moment it first becomes visible, prioritizing novelty over recency. Memory should scale with the amount of newly introduced content, rather than with video length. This appearance-indexed memory makes long-range consistency an explicit property of the memory structure. Our framework unifies two mechanisms under this single principle. At the beginning of a video, when all visible content is novel, an attention sink preserves the initial scene. As the video evolves, an optical-flow-based novelty bank extends the same principle by selectively retaining newly revealed content. As a training-free inference method with no additional learnable parameters, RECAP-Forcing consistently improves visual quality and semantic fidelity across multiple strong baselines and outperforms existing memory methods.

---


### 226. [Cross-Architecture Knowledge Distillation from a Vision Foundation Model to a Lightweight Visual State Space Model for Tea Leaf Disease Classification](https://arxiv.org/abs/2608.26771)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zibo Zhou, Zongsen Qiu, Rui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated tea leaf disease classification supports precision agriculture, yet deploying accurate models on edge devices remains challenging under tight compute budgets. Self-supervised vision foundation models such as DINOv2 provide strong features but are too large for field deployment, while lightweight models trained from scratch on small agricultural datasets often underfit. We study cross-architecture knowledge distillation (KD) from a fine-tuned DINOv2 teacher (Vision Transformer) to a compact bidirectional Visual State Space Model (LVSSM) student, an underexplored direction because the architectures use fundamentally different token-mixing mechanisms. We identify and fix two training-stability problems that prevent the from-scratch SSM student from learning on limited data: a single large patch-embedding convolution and a fusion layer that severs the residual path. With a progressive convolutional stem and gated bidirectional selective-scan block, the 4.45M-parameter student trains stably. Across three seeds, temperature-scaled logit distillation raises test accuracy from 92.32+/-2.14% to 95.41+/-1.17% (best single run: 96.20%; macro-F1: 94.45%), a +3.09 percentage-point mean gain. The student uses 5.0 times fewer parameters than the 22M-parameter teacher while retaining 98.3% of its accuracy. Ablations show that intermediate feature-alignment losses reduce accuracy, making simple logit-level KD the strongest configuration. A fair from-scratch comparison shows the gain is specific to students that start below the teacher. We report per-class metrics, confusion matrices, bootstrap confidence intervals, and FLOPs/latency measurements, and discuss limitations including the single-dataset scope and simplified non-official SSM implementation.

---


### 227. [Anatomy-Guided Foundation Model Adaptation with Within-Case Prototype Supervision for Standard Plane Detection in Fetal Ultrasound Blind Sweeps](https://arxiv.org/abs/2608.27051)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuzhe Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting the fetal abdominal circumference standard plane in low-cost obstetric blind sweeps is a highly imbalanced frame-classification problem: positive frames account for under 3% of a sequence, form short contiguous segments, and are poorly handled by off-the-shelf ultrasound and vision foundation models. We propose AnatoProto, a lightweight sequence-level framework that adapts a frozen BiomedCLIP encoder to fetal blind sweeps through four components: (i) anatomy-weighted spatial pooling that uses nnU-Net abdominal-region probabilities as a spatial prior to reweight BiomedCLIP patch tokens, so frozen semantic features are aggregated onto anatomically meaningful regions; (ii) a within-case prototype loss that pulls each frame embedding toward the mean of positive frames of the same sweep, exploiting case-level structure unavailable at the frame level; (iii) a three-stage cascade refinement (frame->segment->case-level rejecter) that lifts the prediction unit from noisy frames to structurally-constrained segments; and (iv) a hybrid prediction head that jointly models per-frame stability and inter-frame boundary transitions to suppress boundary false positives. On the ACOUSLIC-AI benchmark, AnatoProto reaches a test F1 of 67.72, outperforming the strongest foundation-model baseline (FetalCLIP + PRS, F1 = 54.52) by +13.20 F1 and the strongest video temporal-action-detection baseline (TriDet + PRS) by +15.76 F1. A synergy study, backed by embedding geometry and paired-bootstrap confidence intervals, shows that the prototype loss and anatomy-weighted pooling are not additive: applied alone the prototype loss reduces recall by 12 points, but combined with anatomy-weighted pooling it increases recall by 6.5 points -- a sign-flip we trace to the accuracy of the within-case prototype.

---


### 228. [Unsupervised Adaptation of 3D CT Foundation Models for 3D CBCT Segmentation](https://arxiv.org/abs/2608.27190)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gauthier Miralles, Loic Le Folgoc, Vincent Jugnon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D segmentation of cone-beam CT (CBCT) is critical for interventional and radiation therapy applications, yet it remains limited by two compounding challenges: the scarcity of annotated CBCT data and the large domain shift from diagnostic CT. Interventional CBCT exhibits fundamental modality differences from conventional CT, driven by acquisition and physics effects as well as contrast-specific vascular content, thereby limiting effective cross-modality model transfer. We propose a novel unsupervised domain adaptation (UDA) framework based on redundancy-reducing feature alignment, enabling 3D CBCT segmentation with no target-domain annotations or inference-time adaptation. Our framework is architecture-agnostic, seamlessly adapting both CNN-based and ViT-based foundation models. We evaluate our method on two challenging CT-CBCT liver segmentation benchmarks: one for interventional vascular procedures and one for radiation therapy, demonstrating that even large-scale pretrained segmentation networks require explicit feature-space bridging to generalize across acquisition modalities, and that our approach consistently outperforms existing pretrained foundation model and UDA strategies. To support reproducibility and benchmarking, we release the liver segmentations for a public CBCT dataset, along with the code, trained models, and weights.

---


### 229. [HALO: A Heterogeneity-Aware Language-Aligned IMU Foundation Model for Open-Set Human Activity Recognition](https://arxiv.org/abs/2608.27233)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zihan Ding, Liyu Zhang, Xiaomin Ouyang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) using inertial measurement units (IMUs) enables a wide range of applications, yet the field still lacks a unified model that can generalize across diverse subjects, devices, and activities. Training such a model is difficult due to two key challenges: sensing heterogeneity -- differences in sampling rates, channel configurations, and sensor placements -- and poor generalization to unseen activities and label vocabularies. We introduce HALO (Heterogeneity-Aware Language-aligned Open-set model), a domain-specific IMU foundation model that addresses both challenges through a two-stage training framework. Stage 1 pretrains the IMU encoder with heterogeneity-aware self-supervised learning, including adaptive-pooling tokenization, channel-independent feature extraction, and contextualized sensor conditioning that injects natural-language sensor descriptions into each channel embedding. Stage 2 aligns this IMU encoder with text embeddings via synonym-aware soft contrastive learning, enabling open-set recognition via cosine-similarity retrieval without per-dataset classifiers. Trained on 10 public HAR datasets and evaluated on 7 held-out datasets, HALO outperforms five state-of-the-art baselines on all 8 aggregate metrics, and still leads on 3 of 4 settings under baseline-matched inputs. Despite using only ~35M trainable parameters -- 10x fewer than the latest foundation model MOMENT (341.2M) -- HALO improves zero-shot open-set accuracy, measured over all 87 training labels, by 13.7 percentage points. On two further datasets with severe distribution shift, every model including HALO collapses zero-shot. A video demonstration of HALO's performance in real world is available at this https URL

---


### 230. [Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search](https://arxiv.org/abs/2608.27266)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuan Chang, Xiaoqi Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficiently improving autonomous agents across diverse tasks is central to accelerating recursive self-improvement (RSI) in agentic AI, with prompt optimization emerging as a promising approach capable of delivering performance gains comparable to those achieved by fine-tuning model weights, while reducing computational costs in both optimization and serving. However, recent developments increasingly favor unnecessarily complex prompt optimizers. We introduce Naive Prompt Optimization (NPO), a lightweight single-lineage method that iteratively revises prompts using a teacher model with rollout feedback. NPO achieves comparable or better performance than GEPA with fewer rollouts, and its advantage increases with stronger teacher models, suggesting that stronger teacher reasoning can partially substitute for optimizer-side search complexity. In interactive games, NPO remains broadly competitive with GEPA, while GRPO performs better on some tasks less amenable to prompt optimization. We also show that NPO-optimized prompts elicit similar performance improvements when applied verbatim to other student models, especially across models within the same family. Overall, our preliminary results show that simple, linear prompt optimization can rival substantially more sophisticated and complex search procedures.

---


### 231. [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/abs/2608.27454)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. We introduce WikiSkill, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.

---


> [!TIP]
> 当前位于：**201-231**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-231**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
