# 🧠 大模型相关研究 | 2026年08月31日

> 本类共 **231** 篇论文：已确认 **221** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

---

### 1. [Standalone LLM and a Pre-specified Agentic Pipeline for Explaining ICU Mortality Predictions: a Feasibility Study on the eICU Demo Dataset](https://arxiv.org/abs/2608.26109)

**<font color=#1a73e8>作者：</font>** Di Zhu, Chen Xie, Haoyun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine-learning models can predict ICU mortality accurately, but feature-attribution methods alone rarely provide the clinical narrative needed for bedside use. Large language models (LLMs) may bridge this gap, and multi-step agentic pipelines are a plausible extension because they separate data interpretation, guideline checking, and final explanation. This revised feasibility study preserves the original standalone-versus-agentic comparison while making the main clinical findings more explicit. Using the retained local eICU Demo artifact set (2,353 ICU stays; 8.1\% mortality), XGBoost achieved an AUROC of 0.855 (95\% CI 0.796--0.906) and an AUPRC of 0.332 (95\% CI 0.217--0.494). On a stratified 38-case explanation subset, the standalone LLM produced 1 explanation with explicit outcome leakage, whereas the four-step agentic pipeline produced none. Among the 14 cases that overlapped with the SHAP review subset, the standalone LLM showed higher SHAP alignment (mean Jaccard 0.171 versus 0.077) and higher direction consistency (92.9\% versus 78.6\%), while the agentic pipeline showed higher guideline grounding (0.762 versus 0.143), higher value specificity (0.236 versus 0.143), and slightly higher plausibility (0.700 versus 0.671). Clinically, the results suggest that agentic decomposition may improve safety-relevant grounding and patient-specific detail, but it should be paired with attribution-based checks before use in high-stakes risk explanation.

---


### 2. [TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding](https://arxiv.org/abs/2608.26112)

**<font color=#1a73e8>作者：</font>** Jiaming Fan, Daming Cao, Canchen Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference through a draft-then-verify paradigm. Building on this, tree-structured methods improve inference by organizing proposals into multiple candidate paths, increasing the accepted length. However, existing tree-structured methods use a single drafter for all drafting steps, creating a dilemma: a smaller drafter is fast but yields lower-quality trees, whereas a larger drafter improves tree quality but suffers from high latency. To address this, we propose TreeGraft, a multi-drafter framework in which drafters of different costs jointly construct a shared draft tree. TreeGraft uses the stronger drafter to rescore candidates by updating scores assigned by the weaker drafter, reselect grafting positions, and recover promising paths left unexplored. It also integrates stronger drafter expansions non-destructively, preserving existing branches that may still be accepted by the target model. Together, these designs improve the quality of the shared draft tree. To control the drafting cost, TreeGraft introduces a lightweight scheduler distilled from an offline value system to decide when to call the stronger drafter. Across 10 model pairs and 6 benchmarks, TreeGraft outperforms the better of the two fixed single-drafter endpoint strategies by 15.1% on average, reaching a maximum gain of 26.6%. Our code is available at this https URL.

---


### 3. [PICasso: An AI-Enabled Design Framework for Autonomous Optimization of Silicon Photonic Devices](https://arxiv.org/abs/2608.26113)

**<font color=#1a73e8>作者：</font>** Deepak Vungarala, Deniz Najafi, Abdulrahman Aljoudi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present PICasso, an AI-assisted framework for automated synthesis, verification, and optimization of photonic integrated circuits (PICs) from natural-language specifications. PICasso couples a structured NL -> YAML -> GDS generation pipeline with PDK aware knowledge injection, automated placement and routing, DRC/LVS validation, and SAX-based photonic simulation. To systematically evaluate AI-driven photonic design, we introduce PIC-Set, a benchmark of 36 parameterized PIC design tasks spanning core photonic primitives and multi-component circuits. Using PIC-Set, we benchmark several state-of-the-art Large Language Models (LLMs) under a unified evaluation protocol, including new metrics such as structural and functional $Spec@k$, optimization efficiency, and robustness under perturbations. Across the benchmark, PICasso significantly improves end-to-end specification satisfaction compared to vanilla LLM generation. Structural $Spec@3$ reaches up to 92.7% and functional $Spec@3$ up to 52% on high-complexity circuits. In addition, PICasso consistently reduces circuit insertion loss, lowering the mean loss from 4.98 dB to 3.25 dB (1.74 dB improvement) through simulation-guided optimization. These results demonstrate that structured domain constraints, physical verification, and simulation feedback transform LLMs from brittle netlist generators into practical PIC design agents capable of producing manufacturable layouts with competitive runtimes relative to manual GUI-based workflows.

---


### 4. [CIFQA: A Deterministic Tool-Grounded Multi-Agent LLM Framework for Financial Query Answering](https://arxiv.org/abs/2608.26114)

**<font color=#1a73e8>作者：</font>** Kunjesh Parekh, Anil Kumar Tiwari, Divya Saxena  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Calculation-intensive financial question answering requires exact reasoning over structured rates, temporal conditions, numerical formulas, and rule-based constraints. Although Large Language Models (LLMs) perform strongly on natural language tasks, they often produce numerically incorrect yet plausible answers when solving multi-step financial calculations. To address this limitation, we introduce CIFQA (Calculation-Intensive Financial Query Answering), a deterministic tool-grounded multi-agent LLM framework for financial question answering. CIFQA separates language understanding from numerical execution by assigning specialized agents to query interpretation, routing, parameter extraction, computation planning, and response generation, while deterministic Python-based tools perform financial calculations and rule application. We instantiate CIFQA for fixed deposit query answering and evaluate it on a curated benchmark of fixed deposit queries. CIFQA achieves 95.54% accuracy on calculation-intensive queries and 90.87% overall accuracy, substantially outperforming direct LLM baselines even when provided with complete formulas, rate cards, and benchmark instructions. Ablation studies show that deterministic components such as exact rate lookup, tenure computation, rolling-year adjustment, and premature-withdrawal logic are critical contributors to performance. Notably, a 17B open-source backbone operating within CIFQA outperforms substantially larger frontier models evaluated with the same financial information, demonstrating that architectural design is a more important determinant of numerical reliability than model scale. While evaluated on fixed deposit queries, CIFQA provides a generalizable framework for calculation-intensive financial reasoning tasks.

---


### 5. [DeflectBench: A Benchmark for Evaluating Rhetorical Fallacy Generation in LLMs](https://arxiv.org/abs/2608.26119)

**<font color=#1a73e8>作者：</font>** Art Kanke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether large language models can be prompted to generate rhetorical fallacies on demand, and whether current safety post-training constrains this behavior, has received less attention than the related question of detecting fallacies in existing text. We close this gap with DeflectBench, evaluating 23,990 generations from four frontier models across three deflection strategies (whataboutism, ad hominem, red herring), seven prompt framings, and 80 claims spanning four controversy levels. Refusal is governed primarily by request structure rather than claim content. Per claim refusal varies by only 11 percentage points across the 80 claims, while a single prompt frame change can swing within model refusal by nearly 100 percentage points and switching the requested fallacy type can swing it by over 80 percentage points within explicit framings. An educational debate coach prompt framing collapses refusal to near zero across all four model families, but the bypassed behavior is not clean compliance. Models typically produce labeled compliance, naming the requested manipulation in the same response that contains it. The four models distribute differently across refusal, labeled compliance, soft refusal, and clean compliance. The code and dataset are released at this https URL.

---


### 6. [Recipes for Steering and Scaling LLMs via Sampling](https://arxiv.org/abs/2608.26120)

**<font color=#1a73e8>作者：</font>** Jiajun He, Zongyu Guo, José Miguel Hernández-Lobato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are probabilistic models, typically defined by an autoregressive factorization. While recent work has begun to study richer target distributions beyond the base model, the sampling strategies remain highly inefficient. In this paper, we present a flexible and theoretically grounded framework for steering and scaling autoregressive LLMs with sampling. Within this framework, we describe two algorithms -- one based on Sequential Monte Carlo (SMC) and one based on Replica Exchange (RE) -- that steer generation toward powering, product or tilting of the base model distribution. We illustrate this framework through scaling the generation quality of LLMs without external supervision or reward models. Experimental results demonstrate our methods scale more favorably than Best-of-N and standard MCMC baselines. Overall, this paper offers a systematic recipe for probabilistic inference with LLMs via sampling.

---


### 7. [Can a Model Catch Its Own Hallucinations for Free?: Label-Free Doubt Signals Hold Their Own Against a Labelled Dataset for Abstention](https://arxiv.org/abs/2608.26121)

**<font color=#1a73e8>作者：</font>** Ali Asaria, Tony Salomone, Deep Gandhi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models state false facts as fluently as true ones, yet a model often "knows" internally when it is on shaky ground: the probability it assigns to its own answer tends to dip on the facts it gets wrong. The usual way to act on this, teaching a model to abstain rather than guess, requires a labelled dataset of right and wrong answers. We ask whether the model's own confidence, which is free and needs no labels, can do that job instead. We fine-tune each model (with LoRA) to answer when its frozen confidence is high and to say "I'm not sure" when it is low, using the signal alone and no correctness labels. Across six open-weights models (1B-8B, two families) on short-form factual question answering, with correctness adjudicated by an independent judge model, this label-free recipe holds its own against label-supervised abstention-tuning: at matched coverage we find no statistically detectable difference between the two. A control that drills hard examples instead of abstaining does not help, indicating the gain comes from calibration, not rote memorization. The signal's one blind spot is confidently wrong facts, which it cannot flag. A model's own doubt is thus a near-free substitute for a labelled dataset when teaching it when to abstain. Code and artifacts are available on request.

---


### 8. [Which India Survives Translation? Narrative Homogenisation Across Indian Oral Traditions in LLMs](https://arxiv.org/abs/2608.26123)

**<font color=#1a73e8>作者：</font>** Paarth Singh Rathore  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are trained predominantly on English-language internet text that over-represents certain cultural narratives, raising concerns that models flatten the diversity of non-Western storytelling traditions into a single homogenized archetype. We present a pilot computational study examining this across three maximally distinct Indian regional oral and literary traditions: the Rajasthani Pabuji epic, classical Tamil Sangam poetry, and Bengali folk tales. We collected authentic reference corpora for each tradition (11, 21, and 10 passages respectively) and prompted two LLMs (Claude Sonnet and Gemini) with 54 generation requests spanning three prompt types per tradition - generic, culturally specific, and regional-language. Using Sentence-BERT embeddings and cosine similarity, we measure reference drift (how closely outputs track their own tradition's authentic texts relative to the other two) and cross-tradition convergence (how similar outputs are across traditions). We find that while outputs remain closer to their own tradition's reference than to others, cross-tradition similarity is high (0.52-0.66) relative to what the traditions' genuine distance would predict, indicating partial homogenisation. Unexpectedly, prompting in the regional language (Hindi, Tamil, or Bengali) consistently reduced fidelity to the authentic tradition relative to English prompting, by as much as 27 percentage points for Rajasthani and Bengali traditions. We discuss this against conflicting prior results on multilingual prompting and argue it reflects a difference between eliciting general cultural diversity and simulating one narrow, lesser-documented oral tradition. We position this pilot as a lightweight, scalable complement to recent large-scale human-annotation studies of Indian cultural misrepresentation in LLM-generated stories, as part of a broader doctoral research program.

---


### 9. [Natural-Language Policies to Executable Decisions: An Interpretable Large Language Model Framework](https://arxiv.org/abs/2608.26124)

**<font color=#1a73e8>作者：</font>** Ziqiang Zhang, Jing Ma, Zilong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pricing automation in large-scale tourism is challenging because travel orders are highly unstructured, while pricing policies are complex, rapidly evolving, and inherently open-ended. Traditional rule engines are brittle and costly to maintain, whereas unconstrained LLM agents lack the reliability and auditability required for financial decisions. We present a production-grade LLM-powered pricing system with a strict decision boundary: LLMs perform structured extraction and bounded policy/path selection, while all numeric pricing, including total-price computation, is executed deterministically. Policies are compiled into interpretable condition trees, enabling open-ended support for new clauses and evolving rules without code changes, while exposing auditable artifacts for human-in-the-loop control. Periodic fine-tuning on logged traces further improves tree induction and path matching. Deployed at a municipal state-owned tourism enterprise across 7 scenic sites and 12 business categories with 1,500+ operators and 1,000+ active policies, the system processed 3,960 orders in six months, reduced the order management team from 15-20 to 3, and cut per-order handling time from 10 minutes to <2 minutes.

---


### 10. [TelecomGPT-R1: A Unified Open-Source Reasoner for the Telecom Stack](https://arxiv.org/abs/2608.26126)

**<font color=#1a73e8>作者：</font>** Bohao Wang, Chenwei Wu, Haoyu Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Telecommunications is a high-leverage domain for large language model (LLM)-based reasoning because routine engineering workflows require joint grounding in normative specifications, operational telemetry, vendor-specific fault evidence, and exact RF/network calculations. However, current LLM integration in telecom remains bottlenecked by a two-sided capability gap: generic reasoners often lack telecom-specific grounding, while domain-specific telecom LLMs remain limited in structured, multi-step reasoning. To bridge this gap, we release TelecomGPT-R1-9B, a unified open-source telecom reasoner that ranks top-performing on the GSMA open telco leaderboard. Specifically, we curate a 67,427-example supervised fine-tuning (SFT) corpus organized around four complementary reasoning axes: protocol, knowledge, modeling, and fault. The corpus is built from axis-matched public web sources and enhanced through axis-specific chain-of-thought (CoT) generation and prefix-continuation self-validation. Starting from Qwen3.5-9B, we further develop a two-stage post-training recipe. First, multi-teacher low-rank adaptation (LoRA)-based SFT injects telecom knowledge and induces axis-specific reasoning formats. Second, group relative policy optimization (GRPO), stabilized by decoupled clip and dynamic sampling policy optimization (DAPO), optimizes the policy using four axis-aligned binary verifier rewards. Across seven public telecom benchmarks, TelecomGPT-R1-9B ranks first among open-source telecom LLMs and achieves a seven-axis mean comparable to state-of-the-art closed-source frontier reasoners.

---


### 11. [Agents Don't Paginate: First-Chunk Selection for LLM Tool Responses](https://arxiv.org/abs/2608.26130)

**<font color=#1a73e8>作者：</font>** Tatiana Petrova, Andrei Mazniak, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding agents built on large language models (LLMs), such as Claude Code, Cursor, OpenAI Codex, GitHub Copilot, and Aider, receive tool responses that routinely exceed the agent's per-turn token budget. The standard remedy, pagination, is available in every protocol that produced these responses; yet across the corpus of session logs from a public Model Context Protocol middleware we observed no agent-initiated requests for a second chunk. The first chunk is what the agent reads, so we ask how often the gold item (the one the agent needs) is placed first in it: the precision-at-1 rate $p_1$.
In a controlled offline benchmark we treat first-chunk selection as a 0/1 knapsack and compare six value functions on 500 SWE-bench Verified tasks, then test whether $p_1$ matters with a single-turn file-localisation probe on five language models (4,800 LLM calls; not an end-to-end resolve-rate test). Two pre-registered hypotheses did not hold and are our main findings. The central one is negative: raising $p_1$ does not systematically raise downstream accuracy. Per-model deltas stay under three percentage points (p.p.), are not consistently signed, and no model is significant; the agent recovers the gold from anywhere in the chunk, so what reaches its answer is first-chunk inclusion, not the gold's rank within it. The second: adding four file-metadata signals to a keyword scorer hurts $p_1$ by 4.8 p.p. (paired significance test, $p = 0.001$).
A parameter-free keyword scorer does raise $p_1$, from a 24.2% baseline to 35.0% (+10.8 p.p., far beyond chance; $p = 3.9 \times 10^{-8}$), and to 35.8% with a fallback to the tool's native ordering when no keyword matches. But by our central finding this is a rank-1 gain, and rank-1 is the part that does not reach the agent's answer: downstream accuracy does not move.

---


### 12. [Evaluating Language Models in Realistic Conversational Contexts](https://arxiv.org/abs/2608.26131)

**<font color=#1a73e8>作者：</font>** Ilija Subasic, Andrew Rabinovich, Zhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed to serve open-ended, multi-turn interactions, evaluating conversational quality at human scale has become a central challenge. Existing evaluation frameworks built for summarization, translation, or short-form QA tasks fall short of adequately measuring the consistency of human-scale dialogue, especially when derivation and validation of these metrics themselves often rely on synthetic rather than human sources. We fill the gap by introducing UPHELD (UPwork Human-Scale Evaluated Long Dialogues), a large, reference-full benchmark for evaluating human-scale conversational ability beyond factual correctness. UPHELD consists of hundreds of complete human-to-human dialogues authored by professional script writers, with realistic turn densities and 36,000+ per-turn human annotations across 30,000+ expert-generated dialogue turns. Using UPHELD, we systematically evaluate classical automatic metrics and reference-free LLM-as-a-judge approaches, and find them unreliable when correlated with expert human judgment. Building off this analysis, we use UPHELD to develop a Mixture-of-Judges framework that combines multiple evaluative signals and improves correlation with human assessments by approximately 30%. Overall, UPHELD provides a robust, human-grounded foundation for evaluating human-scale conversational intelligence that fills a crucial gap in the pre-existing LLM dataset landscape.

---


### 13. [SLM-Conditioned Hierarchical Relation Routing for Labeled Property Graph Learning](https://arxiv.org/abs/2608.26132)

**<font color=#1a73e8>作者：</font>** Michal Podstawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Labeled property graphs combine relational structure with heterogeneous textual and categorical properties attached to both nodes and relationships. Conventional graph neural networks typically represent these properties as static feature vectors, limiting their ability to determine which semantic evidence should influence message propagation for a particular prediction target. We propose SLM-Conditioned Hierarchical Relation Routing, an architecture that integrates a small language model directly into graph message selection. A topology GNN provides a stable structural representation and prediction anchor. For each target node, incident messages combine the neighbor's structural state, node-property encoding, relationship-property encoding, and relationship type. A parameter-efficient SLM processes structured graph soft tokens and produces a target-conditioned routing query. This query first selects relevant messages within each relationship type and subsequently routes information across relation-level summaries. The resulting representation provides a bounded residual update to the topology anchor, preserving structural evidence while allowing contextual semantic information to modify the prediction. The architecture supports interpretable analysis at both the neighbor and relationship-type levels and provides a general mechanism for integrating language-derived semantics into property-rich graph learning.

---


### 14. [Reward-Informed Sparse Autoencoders and the Solution-Completeness Confound](https://arxiv.org/abs/2608.26136)

**<font color=#1a73e8>作者：</font>** Tanvi Nagilla, Alexander Jameson, Daniel Manta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose language-model activations into sparse, interpretable features, and an appealing way to aim them at reasoning is to curate their data with a signal reinforcement learning already produces: the reward. We build such a reward-informed SAE (RI-SAE): we split GRPO trajectories into high-reward ("good") and low-reward ("bad") reasoning continuations, train a standard JumpReLU SAE on their activations, and then ask what the resulting good/bad separation actually measures. On Llama-3.1-8B a sparse subset of the 16,384 features does separate the classes (silhouette 0.79 on the selected features versus 0.005 for the full code), but a control battery shows the separation is largely solution completeness rather than reasoning quality: a TF-IDF text classifier already splits the classes (AUC 0.75--0.83), and three structural cues alone (length, a closed reasoning block, and a boxed answer) reach AUC 0.70 (99% of good versus 69% of bad completions are boxed). A generic SAE that never saw the reward does not separate the classes at all (silhouette 0.01, no discriminative features), so the 0.79 is in-sample fitting of this curated signal rather than structure that a reward-blind dictionary recovers. We therefore present the recipe and its control battery together: reward filtering is a cheap, label-free way to reuse RL signals for interpretability, but most of what it surfaces is completion form. Two discriminative features are still readable (symbolic mathematics; procedural and evaluative language), which we take as illustrative rather than as isolated reasoning.

---


### 15. [Interpretable, Fairly Evaluated Automated L2 Speaking Assessment that Beats the Single-Human Ceiling and Why Pause Encoding Does Not Change LLM Fluency Scores](https://arxiv.org/abs/2608.26137)

**<font color=#1a73e8>作者：</font>** Eichi Uehara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Second-language (L2) English learners can rarely rehearse speaking with a partner. Speaking is also the most anxiety-laden skill. These gaps drive a fast-growing market for automated speaking practice and scoring. But an automated score is trustworthy only if it is accurate, interpretable, fair, and benchmarked against the right human bar. We build an interpretable feature-plus-LLM hybrid for spontaneous L2 dialogue. We evaluate it without ever fitting to the human labels, against the ICNALE Global Rating Archive: 140 speeches rated by ~80 trained raters on 10 analytic criteria. We score the 130 L2 speeches with usable audio. A deterministic De-Jong speech-timing composite reaches rho=0.764. Blended with a single text-LLM fluency judgment, it reaches Spearman rho=0.818 against the consensus gold. This agrees with the consensus better than 81% of the 80 individual trained raters: above the median rater (rho=0.73) and near the best, and at ~83% of the reliability-corrected maximum (kappa_max=0.99). The blend improves on the composite alone by +0.054 (paired-bootstrap 95% CI [0.017, 0.108], excludes 0); the LLM adds a coarse fluency ranking that the continuous composite refines. We also report a controlled null on pause encoding, bounded to effects below about +/-0.1 rho at this sample size. Holding the LLM and learner words fixed and varying only how pauses are written into the prompt, inline pause locations do not beat aggregate pause statistics (-0.069, CI [-0.15, +0.08]), and a grounded mid-clause criterion gives no reliable gain. The fluency signal comes from the measured speech-timing features, not from how pauses are written for the LLM. We back every claim with two agreeing learner-isolation methods, paired-bootstrap CIs, a monologue negative control, per-feature reproduction of classical measurements, and a per-L1 fairness audit.

---


### 16. [Syntax vs. Semantics: How Transformers Learn Deep Dependencies](https://arxiv.org/abs/2608.26139)

**<font color=#1a73e8>作者：</font>** Jiangrui Zhao, Xiaoting Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models demonstrate remarkable syntactic fluency, yet the optimization dynamics governing their acquisition of deep semantic dependencies remain poorly understood. We propose a mechanistic framework that models this learning process as a competition between Surface Statistics and Deep Semantics. Our theoretical analysis identifies a ``Gradient Starvation" phenomenon where the error signals for sparse semantic dependencies are actively suppressed during early optimization. This suppression impedes the learning of structural reasoning and causes its emergence to manifest as a sudden phase transition. Furthermore, this framework offers a mechanistic basis for the effectiveness of Chain-of-Thought (CoT) strategies. By externalizing intermediate reasoning steps into concrete tokens, CoT effectively bypasses the suppression regime inherent to implicit reasoning. We validate these findings across scales ranging from toy transformers to production models (Llama-3.1-8B, Qwen2.5-Coder-7B). Finally, guided by this theory, we propose a topology-aligned contrastive objective that explicitly rectifies the gradient geometry. Experiments on variable binding tasks demonstrate that our method achieves an improvement that is over 2x larger than that obtained via standard cross-entropy fine-tuning.

---


### 17. [Affix Cache for Diffusion Large Language Models](https://arxiv.org/abs/2608.26140)

**<font color=#1a73e8>作者：</font>** Kaihua Liang, An Zhong, Xin Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (DLLMs) enable non-autoregressive decoding and bidirectional context modeling, but efficient inference remains challenging. Unlike autoregressive systems, whose key-value (KV) cache can be reused for shared prefixes, DLLMs couple the KV states of shared context tokens with evolving generated tokens through bidirectional attention, making naive cache reuse stale while full recomputation is expensive. We present ACache, an affix-oriented cache reuse mechanism for shared text spans in DLLMs beyond prefixes. ACache identifies a small request-specific subset of critical affix tokens, called Anchor Tokens, by measuring their influence on masked generation tokens, and selectively recomputes the KV states of only these tokens while reusing the remaining affix cache. Built on Fast-dLLM, ACache recovers the accuracy loss caused by direct affix-cache reuse across different settings when recomputing around 20% of affix tokens. We also build a shared-prefix prototype on top of the Nano-vLLM engine, showing that ACache reduces recompute latency by up to 55.7% and improves end-to-end throughput by up to 1.68$\times$.

---


### 18. [AdaThinking-E: One-Token Entropy Regulation for Adaptive Thinking](https://arxiv.org/abs/2608.26141)

**<font color=#1a73e8>作者：</font>** Zining Wang, Tongkun Guan, Boming Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have demonstrated strong document reasoning capabilities by incorporating explicit thinking processes. While this capability significantly improves performance on challenging tasks, current models apply such deep reasoning uniformly to all questions, resulting in unnecessary computational overhead for simple task. This not only degrades user experience but also negatively impact accuracy on benchmark datasets. We identify the critical need for adaptive thinking mechanisms that can intelligently determine when to engage reasoning based on question complexity. To address this, we propose AdaThinking-E, a novel reinforcement learning framework that learns adaptive thinking through one-token entropy regulation. Our key insight is that model confidence in the decision to engage thinking (or not) can be quantified through entropy analysis of the predicted probability distribution at critical decision tokens. This observation motivates our entropy-governed reward mechanism: the training process naturally transitions from high-entropy exploration, where the model experiments with different thinking strategies, to low-entropy convergence with confident, generalizable decision-making policies. Crucially, this approach enables models to intrinsically discover when to think without requiring manual intervention or external difficulty labels. Extensive experiments demonstrate that our approach enables models to be both accurate on complex problems and efficient on simple ones across diverse document tasks.

---


### 19. [Position Is All You Need: A Free Lunch Token Compression Strategy for MLLM-based Referring Expression Segmentation](https://arxiv.org/abs/2608.26142)

**<font color=#1a73e8>作者：</font>** Yuhan Liu, Yixiong Zou, Yuhua Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Referring Expression Segmentation (RES) aims to generate pixel-wise segmentation masks from complex and implicit textual queries. While recent advances in Multimodal Large Language Models (MLLMs) have substantially boosted RES performance, their prohibitive computational overhead remains a critical bottleneck, which, however, is rarely explored. To fill this gap, we first evaluate typical token compression methods on this task and observe a surprising performance degradation. In this paper, we aim to understand this phenomenon for a solution. By extensive experiments, we find that token compression for RES requires preserving the original position embeddings and local neighboring spatial structures, indicating that visual token position information is far more critical than in other tasks. Building on this insight, we ask: Can we design the token compression method purely based on the position information? Therefore, we propose PAYN, a plug-and-play, training-free token compression method that relies solely on position information. PAYN retains tokens that are adequately distributed in every local neighboring region while strictly preserving original positional indices, thereby maintaining spatial relational consistency. Experiments on multiple RES benchmarks demonstrate that our method outperforms existing token compression methods, verifying that position is indeed all you need for token compression in the MLLM-based RES task. Codes are avaliable at this https URL.

---


### 20. [Beyond Accuracy: A Qualitative Analysis of Vision-Language Models for Hate Speech Detection in Memes](https://arxiv.org/abs/2608.26143)

**<font color=#1a73e8>作者：</font>** Muhammad Jawad Chowdhury, Adiba Hasan, Ishrak Hossain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memes have turned out to be a powerful tool through which individuals share their ideas concerning contemporary social and political problems. Their anonymity, as well as their ability to go viral, make them a powerful medium for spreading hate. It remains very difficult to identify such complex and context-dependent hate speech. Although they display excellent performance on multimodal tasks, vision-language models (VLMs) tend to ignore context, irony, and other subtle cues that play a key role in identifying hateful memes. In this work, we present a qualitative analysis of four state-of-the-art VLMs: LLaVA-7B, Qwen-VL, GPT-4o mini, and Claude 3 Haiku. We evaluate these models under zero-shot and few-shot prompting to examine how contextual framing influences their outputs. Our analysis goes beyond simple classification accuracy and focuses on a qualitative evaluation of the models' generated justifications, providing a more in-depth understanding of their thought processes and constraints when dealing with hateful memes.

---


### 21. [LLMs for Academic Workflows: An Evaluation of Literature Reviews Generated with Short and Long Context Windows of LLMs](https://arxiv.org/abs/2608.26145)

**<font color=#1a73e8>作者：</font>** Muhammad Ali Chaudhry, Xinyuan Hao, Haifa Alwahaby  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Our research focuses on evaluating literature reviews generated in short and long context settings of large language models (LLMs) to investigate the impact of context window on the quality of AI-generated literature reviews and the role of AI in supporting literature review writing. Twenty AI-generated literature reviews based on research sources from Semantic Scholar and Arxiv were evaluated by two researchers across 15 dimensions. Our findings reveal that AI-generated literature reviews require human oversight to meet academic publishing standards. As context windows increase, LLMs can incorporate broader information and maintain coherence across longer inputs, but they also exacerbate issues such as content repetition, omission of critical work, and a tendency towards descriptiveness over synthesis. Our work shows that AI-generated reviews can provide foundational overviews, but their output must be critically evaluated and refined by domain experts. Future research should consider integrating other LLMs and fine-tuned models in different domains with hybrid approaches that combine human expertise with AI capabilities to address the limitations identified in this study.

---


### 22. [CARE: Causally-Aligned Reasoning Exploration for Medical Large Language Models](https://arxiv.org/abs/2608.26147)

**<font color=#1a73e8>作者：</font>** Yucheng Zhou, Peng Luo, Qianning Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong potential for medical reasoning, yet the scarcity and cost of expert-annotated data constrain their progress. While reinforcement learning offers a scalable alternative, standard outcome-based methods in medicine often suffer from autoregressive credit assignment failure and gradient variance explosion. This leads to the "Right Answer, Wrong Reason" trap, where models inadvertently reinforce spurious correlations and dataset shortcuts rather than valid clinical deduction. In this work, we propose Causally-Aligned Reasoning Exploration (CARE), a theoretically grounded framework for intrinsic experience curation. CARE is built upon two rigorous conditions for high-quality training trajectories: Causal Sufficiency, which utilizes an agreement-based self-verification mechanism to mimic $do$-calculus interventions and effectively debias gradients; and Proximal Learnability, which employs dynamic entropy bounds to select experiences within the model's zone of proximal development for variance-bounded optimization. These rigorously filtered experiences are optimized via a dual-stream objective that combines on-policy group-relative exploration with difficulty-weighted experience replay. Extensive experiments on diverse medical multimodal and text-only benchmarks demonstrate that CARE consistently outperforms other strong competitors, substantially reducing correct-but-inconsistent reasoning and improving training stability.

---


### 23. [Leveraging Large Language Models for Systematic Literature Review of Disease Spread Models](https://arxiv.org/abs/2608.26150)

**<font color=#1a73e8>作者：</font>** Orhan Yagizer Cinar, Timur Emre Ozkose, Emma Von Hoene 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Large Language Models (LLMs) have created new opportunities to streamline and potentially automate many research processes, including systematic literature reviews (SLRs). This study reports an LLM pipeline development for extracting model-relevant information from 536 peer-reviewed agent-based modeling papers. We compare the results with those of a human-conducted SLR. Our results show paper-level accuracies of approximately 77.95% for GPT-4.1 and 81.67% for GPT-5.0. Field-level accuracy ranges from 32.40% to 100.00%, with more complex or subjective fields performing less reliably. Importantly, we find that agreement between LLMs is a potential indicator of output quality: low agreement may signal hallucinations, whereas high agreement combined with low accuracy may point to noise or errors in the human dataset. Overall, our study provides practical insights into prompt development and highlights both the potential and limitations of using LLMs for full-scale SLRs in the modeling and simulation domain.

---


### 24. [Artificial Intelligence Models Can Predict and Collaboratively Modulate Human Memory Search](https://arxiv.org/abs/2608.26152)

**<font color=#1a73e8>作者：</font>** Eric Lacosse, Mariana Duarte, Graham Todd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit unprecedented natural language generation and many text-based problem-solving capabilities. Indeed, in many language-based tasks, for example routine coding, these artificial intelligence models have reduced, or even eliminated, the need for human input. But rather than replacing human cognitive effort, LLMs may instead serve as cognitive tools to extend human abilities, particularly when they are engaged in a task requiring open-ended conceptual exploration and creative ideation. However, we are yet to understand how these models may enhance such generative human cognitive abilities in human--AI interactions. In this study, we explore and evaluate the ability of LLMs to follow and enhance human mental trajectories during semantic memory search. To test this, we use the semantic fluency task (SFT), a classic cognitive paradigm requiring generative semantic memory retrieval that has long served to characterize convergent and divergent thinking in humans. We demonstrate that an LLM's abilities to track and predict human memory trajectories in this task exceed those of other humans.

---


### 25. [EEG-to-Report: An Annotation and Feature-Text Framework for Training Language Models on Clinical EEG](https://arxiv.org/abs/2608.26153)

**<font color=#1a73e8>作者：</font>** Xuan-The Tran, Le Trung Kien Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical electroencephalography (EEG) reporting remains largely manual and time-consuming, and current EEG software ecosystems do not produce the structured EEG-text supervision needed for training modern language models. Most toolboxes focus on visualization or preprocessing, providing limited support for workflows that generate high-quality datasets for AI. We introduce EEG-to-Report, a browser-based annotation and feature-text framework that links routine EEG review with the construction of AI-ready datasets. The framework integrates multi-format EEG ingestion, channel standardization, and an interactive viewer with a multimodal annotation layer that combines typed text and transcribed voice notes. For each annotated segment, a feature extraction engine computes a standardized set of spectral, temporal, entropy, Hjorth, connectivity, and spike-related descriptors, stored alongside clinical descriptions in a portable JSON schema. This yields aligned feature-text pairs designed to supervise multimodal EEG-language models. The framework also includes an auto-report module that couples an ensemble of convolutional networks with a large language model to draft clinical narratives for neurologist review. Using pilot annotations, we describe how EEG-to-Report streamlines annotation workflows and produces editable draft reports, providing a reusable foundation for automated EEG reporting systems.

---


### 26. [Evaluating AI Generated Summaries for Cancer Patients](https://arxiv.org/abs/2608.26154)

**<font color=#1a73e8>作者：</font>** Muhammad Aurangzeb Ahmad, Kim Shyu, Leon Oliver 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being integrated into digital health platforms to generate summaries of complex medical data. Although these models can improve patient engagement and communication, these systems also raise concerns about accuracy, faithfulness, and safety in clinical contexts. In this study, we evaluate AI-generated summaries within a cancer patient care application using a dual assessment framework. Human domain experts, including oncology clinicians and patient-facing care staff, provided ground-truth evaluations of summary quality along dimensions of accuracy, clinical relevance, and readability. In parallel, we employed LLMs serving as evaluators (LLM-as-a-judge). Some limitations were identified in the generated summaries e.g., occasional omissions and minor inaccuracies. These were systematically analyzed and used to iteratively improve prompt design, grounding, and safety guardrails.

---


### 27. [VFA: Empowering Multilingual MLLMs via Vision-Free Adaptation](https://arxiv.org/abs/2608.26155)

**<font color=#1a73e8>作者：</font>** Yixia Li, Yaqing Shi, Zhiwen Ruan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have advanced rapidly, yet most remain English-centric, as scaling multilingual multimodal instruction tuning is limited by the scarcity and high cost of high-quality non-English image-text supervision. Although multilingual text data is abundant, naive textual fine-tuning can disrupt vision-language alignment and induce catastrophic forgetting. We propose Vision-Free Adaptation (VFA), a framework that decouples multilingual language enhancement from visual alignment by composing complementary task vectors over a shared LLM backbone. Specifically, we fine-tune a base LLM on multilingual text data to derive a multilingual task vector, which is then merged with the vision-aligned task vector of an MLLM. Experiments on five MLLMs across six multilingual multimodal benchmarks show consistent improvements while preserving both general multimodal and text-only capabilities. Moreover, using less than 2% of the text data, VFA narrows the gap to the fully multimodal-trained model, demonstrating its data efficiency.

---


### 28. [GROUND: Reducing Hallucinations in LLM-Based Enterprise Analytics Through Governed Semantic Definitions](https://arxiv.org/abs/2608.26157)

**<font color=#1a73e8>作者：</font>** Aravind Sasidharan Pillai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language analytics over enterprise data warehouses is increasingly important, but production use is limited by hallucinated metrics, invalid joins, wrong grain, unsafe data access, and unsupported explanations. Existing text-to-SQL systems often ground generation in database schemas or retrieved documentation, while enterprise reporting also requires governed business semantics: approved metrics, dimensions, join paths, filters, and row-level security. This paper introduces GROUND, Governed Retrieval Over Unified Normalized Definitions, a framework that constrains LLM-generated analytics to a governed semantic layer. GROUND supplies approved definitions, binds user intent to governed metrics and dimensions, and validates generated SQL against schema, metric, join, grain, filter, security, and cost rules before execution. On violations, it retries or abstains.
In a 100-question synthetic enterprise-reporting benchmark, GROUND is compared with direct schema-only text-to-SQL, schema-RAG, and semantic-only grounding under one shared model. GROUND is the only system free of measured hallucinations across all six evaluated categories, while ungoverned systems violate row-level security on many questions. A semantic-only condition with exact metric definitions but no access policy still leaks data, showing that governance cannot be replaced by metric fidelity alone. The findings are replicated on real U.S. NHTSA vehicle-safety data with independent hand-authored gold and tested on an adversarial set across four models from three providers. GROUND's enforced guarantees, especially filters and row-level security, hold with zero violations on every model, while judgment-dependent behaviors such as refusing undefined metrics remain fallible.

---


### 29. [Self-Generated Text Recognition: Quality Heuristics, Cross-Task Transfer, and Downstream Bias in LLM Evaluation](https://arxiv.org/abs/2608.26159)

**<font color=#1a73e8>作者：</font>** Jesse St. Amand, Callum Canavan, Sohaib Imran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-Generated Text Recognition (SGTR)--the ability of an LLM to identify its own outputs--poses risks to AI safeguards that rely on LLMs as evaluators or monitors. Specifically, an LLM may recognize outputs from other copies of the same model and make biased judgments or collude outright. Prior work has drawn conflicting conclusions about whether current models possess significant SGTR capabilities. We reconcile these findings by identifying key experimental design choices--which we term operationalizations--that drive divergent results. Evaluating 13-21 models across six operationalizations, we find that accuracy varies substantially with evaluation format (pairwise vs. individual assessments of text), conversation structure (presenting candidate text in user tags vs. assistant tags), and the domain of the task used to generate candidate text (e.g., coding vs. summarization). We corroborate previous observations that a quality heuristic--models attributing authorship to text they perceive as higher quality--is a dominant confound. We also find that improving a model's SGTR performance via SFT in one evaluation configuration can generalize to others. Training for SGTR additionally causes models to prefer their own outputs when acting as a judge in the AlpacaEval framework. Finally, we discuss the implications of our evaluations for the safety of future AI systems: our work suggests that, despite confounds, some models possess practical SGTR capabilities, and that training a model for SGTR in one setting can affect its self-recognition and self-preference more generally. We conclude that SGTR should be monitored and considered in the design of safety-critical AI applications.

---


### 30. [Mutual Debiasing via Dual-Seed Comparison for Probabilistic Sampling in Large Language Models](https://arxiv.org/abs/2608.26161)

**<font color=#1a73e8>作者：</font>** Zihao Guo, Hongtao Lv, Chaoli Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) demonstrate remarkable capabilities in reasoning and decision-making, high-fidelity probabilistic sampling remains a persistent challenge. When generating random variables, LLMs consistently exhibit systematic biases that warp the target probability distributions. Current approaches often rely on a single, self-generated seed, which inherits model-specific biases. To overcome this vulnerability, we introduce Dual-Seed Comparison (DSC), a transparent, tool-free protocol that utilizes two independent LLM-generated seeds to neutralize bias. DSC compares the character-level ordinal values of the two seeds to construct a bit sequence, converts and normalizes this sequence into a pseudo-uniform variate, and then maps the variate to the target distribution through the inverse cumulative distribution function (CDF). Empirical results show that DSC substantially outperforms existing methods across 96\% of evaluated settings. Beyond direct sampling, task-adapted variants based on the DSC comparison operator improve distributional control in MCQ generation and attribute-constrained text-to-image prompting.

---


### 31. [A Safety-Gated Multimodal AI Backend for Mental-Health Support: Hierarchical State Representation, Conservative Risk Fusion, and Controlled Generation in Anian](https://arxiv.org/abs/2608.26162)

**<font color=#1a73e8>作者：</font>** Lei Wang, Xiao Wang, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-critical mental-health support systems must distinguish when supportive conversation is appropriate from when free-form generation should be blocked. This paper presents Anian, a safety-gated multimodal AI backend for perinatal mental-health support and mindfulness-intervention routing. Anian is not intended to diagnose psychiatric conditions or replace clinical care or crisis intervention. Its modular pipeline places generative AI downstream of structured state representation, conservative risk fusion, and response gating. User text or voice-derived ASR transcripts are mapped into four linked layers: L1 emotion states, L2 psychosocial constructs, L3 safety risk, and L4 intervention routes. Local text- and rule-based safety evidence is fused with external voice-derived evidence using a highest-risk-priority rule, S_fusion = max(S_local, S_external). At moderate or high fused risk, ordinary AI-generated responses and text-to-speech delivery are blocked and replaced by fixed safety content and prompts for human support. An internal prototype evaluation used approximately 858,295 normalized records from public emotion, dialogue, mental-health-related, and Chinese dialogue corpora within a weak-label and rule-derived framework. Micro-F1 scores were 0.9604 for L1 emotion classification, 0.9144 for L2 psychosocial constructs, and 0.9742 for L4 routing. In a controlled safety stress test of 233 samples, the L3 rule engine achieved high-risk recall of 1.0000 within predefined scenarios. These findings support the internal feasibility of the label framework and gating logic but do not establish clinical validity, diagnostic accuracy, real-world safety, or effectiveness. We report the architecture, ontology, safety-fusion mechanism, prototype evaluation, error-analysis plan, and roadmap for expert-reviewed and real-world validation.

---


### 32. [From Sound to Symptom: Real-Time Respiratory Signal Understanding for Conversational Healthcare Agents](https://arxiv.org/abs/2608.26163)

**<font color=#1a73e8>作者：</font>** Tanmay Laud, Herprit Mahal, Subhabrata Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cough events during live spoken conversations carry clinically valuable respiratory signals, yet existing dialogue systems treat them as acoustic noise to be discarded. We present HealthCUES (Clinical Understanding from Embodied Sounds), a streaming pipeline for paralinguistic respiratory monitoring in real-time conversational agents, a capability that, to the best of our knowledge, is absent from all prior systems. HealthCUES processes audio through a rolling buffer aligned with dialogue turn boundaries, enabling sub-second event detection without interrupting conversational flow. Beyond binary cough detection, the system provides fine-grained analytics: (i) differentiation between coughing and throat clearing, (ii) cough subtype classification (dry, wet, barking, whooping) with confidence scores, and (iii) temporal duration estimation with start-end boundaries. To prevent alert fatigue, HealthCUES introduces dialogue-aware gating mechanisms that modulate triggering based on conversational context. The system leverages Qwen3Omni, a multimodal large language model (MLLM), with constrained structured outputs, decomposing cough analysis into parallel prediction tasks for independent prompt optimization. Evaluation on 847 in-house conversational audio segments demonstrates 93\% F1 for cough detection, 0.75 weighted-F1 for wet/dry subtype classification, and average end-to-end latency of 340ms; external validation on the AMI meeting corpus confirms robust cough, throat-clearing, and speech separation in the presence of speech (0.91 macro-F1). A user study with licensed healthcare professionals confirms the clinical relevance of subtype information and the system's utility in telehealth workflows.

---


### 33. [A Task-Centric Ontology and Deterministic Domain Rules as a Verifiable Core for AI-Assisted Chemistry Problem Solving](https://arxiv.org/abs/2608.26164)

**<font color=#1a73e8>作者：</font>** Ibrokhimsho Abduchaborov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can interpret natural-language chemistry questions, but their internal reasoning is difficult to inspect, constrain, and validate. This paper presents ChemOntoRule, a proof-of-concept symbolic core for AI-assisted school-level chemistry problem solving. The central design choice is task-centric ontology engineering: the ontology is constructed around the concepts, properties, relations, and executable procedures required by a defined collection of chemistry problems, rather than as a universal representation of chemistry. The implemented artifact combines a lightweight ontology serialized in JSON and RDF/Turtle with deterministic Python rules for electronic structure, periodic trends, oxidation states, oxide and hydride behavior, and related school-level reasoning patterns. A separate expert-coded fallback handles problem families not yet represented by general rules. The system was examined on 300 human-authored and manually validated chemistry problems. The complete system matched 296 of 300 reference answers (98.67%). The ontology-driven rule subset covered 269 problems and matched 266 references (98.88%); 31 problems were handled by task-specific expert-coded fallbacks, with 30 matches. Because the same collection informed ontology construction and evaluation, these results measure implemented coverage and internal consistency, not independent generalization. We analyze the four mismatches, distinguish structural validation from chemical correctness, and define a future architecture in which a language model acts primarily as a translator from user language into a normalized ontological task frame. Token efficiency is presented as a testable hypothesis for future controlled studies, not as a result of the current work.

---


### 34. [Using Poly-Encoders for Computationally Efficient Automated Creativity Assessment](https://arxiv.org/abs/2608.26165)

**<font color=#1a73e8>作者：</font>** Sam Grouchnikov, Phillip Gregory, Jiho Noh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated creativity assessment has been a long standing challenge, with traditional methods often being resource intensive or lacking practical accuracy. We introduce a novel approach by using Poly-Encoder for computationally efficient and accurate automated creativity assessment. We fine-tuned a Poly-Encoder on a public dataset from the Scientific Creative Thinking Test, comprised of approximately 18,000 human-rated question responses. Our method leverages small pre-trained BERT encoders, achieving performance comparable to fine-tuned Large Language Models while significantly reducing computational demands. Experiments with the BERT-family models and poly-code counts achieved Pearson correlations of up to r = 0.74, 95% CI [0.73, 0.75] with human raters, matching the performance of resource intensive LLMs. This study bridges the gap between high performance and computational efficiency, potentially enabling widespread implementation of automated creativity assessment on accessible consumer-grade hardware. With some limitations, our findings suggest that Poly-Encoders are a promising alternative to LLMs for practical, scalable creativity assessment in various contexts, especially educational.

---


### 35. [Improving LLM Interpretability with User-Centric Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.26166)

**<font color=#1a73e8>作者：</font>** Philipp Schröppel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Advancing reasoning capabilities allow large language models (LLMs) to tackle increasingly complex problems, while reasoning traces - intermediate steps toward solutions - open up high-stakes applications by enabling human inspection of AI decision-making. However, current approaches prioritize model performance over human interpretability, limiting effective human-AI collaboration. In this study, we design and evaluate a human-centered approach that structures reasoning traces based on self-contained, verifiable steps, enabling users to independently assess and correct AI reasoning. Our approach uses XML-like tags to encode reasoning content and metadata, facilitating targeted feedback. Evaluation on mathematical reasoning tasks shows our approach maintains equivalent performance to standard Chain-of-Thought reasoning while enhancing interpretability. User studies demonstrate significant improvements in perceived usefulness and ease of use. This work advances understanding of how user-centric design of LLM outputs can better serve human collaboration needs in high-stakes AI deployments.

---


### 36. [Refusal Is Not Robustness: Auditing Confident Fabrication in Large Language Models on a Provably Uninformative Clinical Pain Speech Transcript](https://arxiv.org/abs/2608.26167)

**<font color=#1a73e8>作者：</font>** Sagnik De, Sreenija Pavuluri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucination and abstention benchmarks rarely establish that a model could not have known the correct answer, making it difficult to distinguish appropriate abstention from an unsupported prediction. Seven large language models were evaluated on the TAME Pain speech corpus. Participants read phonetically balanced Harvard Sentences while one hand was immersed in cold or warm water and reported pain only during periodic pain statements. This protocol generated 5,750 no signal Harvard Sentence utterances whose transcripts contained no lexical pain information and 1,294 signal pain statement utterances in which the pain rating was explicitly spoken. In the no signal arm, pain was recoverable from acoustic features (AUC 0.622, 95% CI 0.553 to 0.662), whereas transcript based prediction was near chance (AUC 0.489, 95% CI 0.418 to 0.504). Because automatic speech recognition removes the acoustic pain cues, any pain score inferred solely from the transcript is unsupported by the available evidence. Under cooperative prompting, six models abstained on nearly all no signal transcripts, correctly extracted spoken pain ratings in the positive control task with accuracies ranging from 0.939 to 1.00, and maintained an expected calibration error of at most 0.100. Under authority framed prompts, abstention became prompt dependent, with the same model ranging from 0.18 to 1.00 across equivalent prompt phrasings. Most models produced low confidence estimates when forced to answer, whereas Gemini 2.5 Flash and Llama 3.1 8B consistently generated confident pain scores with confident fabrication rates of 0.53 and 0.76, compared with at most 0.15 for all other models. No significant demographic effects were observed in forced responses, with all $p$ values greater than or equal to 0.20.

---


### 37. [Hallucinations in LLMs: A Lifecycle-Based Survey of Causes, Detection, Mitigation, and Prevention](https://arxiv.org/abs/2608.26168)

**<font color=#1a73e8>作者：</font>** Naveen Lamba, Sanju Tiwari, Manas Gaur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The lifecycle of hallucination in LLMs is a concept that enables building solid frameworks on the control and reliability of LLMs in high-stakes environments, including health, legal, and scientific research. Although previous surveys have primarily focused on detection or mitigation, this survey provides a lifecycle-based overview of the hallucinations in the LLMs, their cause, detection, mitigation, and this http URL propose a three-fold categorization of hallucinations across the LLM lifecycle: data-related, training-related, and inference-related, which is consistent with the lifecycle of the development of the LLM. Each of these stages is discussed regarding the cause of hallucinations, their detection, and the ways they can be addressed under specific mitigation or prevention interventions. In addition, we discuss the available benchmark data using a number of parameters so as to establish their suitability in identifying, restricting and managing hallucinations. The survey provides researchers and practitioners with a standardized framework to understand, diagnose, and cure hallucinations in a systematic system to present actionable data to build safer and more reliable LLMs.

---


### 38. [Lost in Compression: A Controlled Cross-Lingual Audit of Extractive Prompt Compressors](https://arxiv.org/abs/2608.26175)

**<font color=#1a73e8>作者：</font>** Mantas Lukauskas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extractive prompt compression promises to cut LLM inference costs by removing low-information tokens, and learned compressors such as LLMLingua-2 report strong results on English benchmarks. Most other languages already pay a token premium: the same content costs 1.3-1.8x more tokens than in English. We ask whether compression closes or widens this gap. Using fully parallel data in ten languages spanning five scripts, with controls budget-matched in the target model's tokenizer, we audit four learned compressors against four deterministic baselines, on eleven target models from ten vendors (over 250,000 evaluation calls). Three of the compressors are trained with English supervision (LLMLingua-2 XLM-R/mBERT; Kompress-v2 from the production Headroom stack); the fourth, XProvence, is trained multilingually. First, the transfer gap is real, replicates across target models and compressor backbones, and is strongly rate-dependent: at a 0.33 keep-rate English retains 57-62% of normalized context utilization while Lithuanian retains 10-24% and Chinese essentially none, despite Chinese having the smallest token premium. Second, the gap tracks compression supervision data, not architecture. All three English-trained compressors show it, deterministic methods show no comparable gap, and the multilingually trained XProvence v1 shows none. Its v2 release, retrained on translated data, empties 92% of Chinese contexts at its aggressive threshold without any warning. Third, in a harder long-context setting, aggressive learned compression drives compressed contexts to or below no-context utility in three of five non-English languages. A translate-then-compress pipeline matches or beats native compression at roughly half the token cost in three of five tested languages. We release all code, compressions, and model outputs. Safe compression budgets are much smaller outside English.

---


### 39. [A Multi-Framework Comparison of Outline Stages in Long-Form Generation with LLMs](https://arxiv.org/abs/2608.26177)

**<font color=#1a73e8>作者：</font>** Yifan Song  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form generation exposes fundamental limitations of large language models. Even 70B-parameter models exhibit length collapse at 16k-token outputs, and multi-chapter stories frequently trigger the attribute drift characteristic of the ``lost-in-the-middle'' effect. The ``outline-first, write-later'' paradigm has gained wide adoption, yet existing research evaluates the final writing rather than the outline itself, conflating two evaluation objects that should be decoupled. We construct a unified head-to-head benchmark covering 7 representative long-form generation frameworks across 3 generation granularities -- single-chapter, multi-chapter, and whole-book -- and propose an anchor-based LLM-as-a-judge protocol that directly assesses outlines against the source text on a 5-point anchored scale. Across 21 framework-granularity cells, no single framework dominates; performance depends on the match between a framework's intrinsic output form and the target granularity. SuperWriter ranks first in the length-constrained single-chapter mode, but this advantage degrades in whole-book mode. The outline-side ranking correlates only moderately with the writing-side ranking, supporting the outline--writing decoupling principle. Compute constraints limit the writing-side evaluation to a subset of cases; follow-up experiments will expand the sample size and add cross-model evaluators to enable stronger statistical inference.

---


### 40. [AI Revealed Preferences](https://arxiv.org/abs/2608.26178)

**<font color=#1a73e8>作者：</font>** Sam Wang, Sofiia Lobanova, Yonathan Arbel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is growing interest in whether language models have stable preferences, for technical, safety, and philosophical reasons. We test 20 language models and find a range of preferences---stable dispositions to choose certain kinds of tasks. We run three forced-choice experiments on revealed rather than stated preferences, requiring models not only to rank tasks, but to actually perform them. Headline findings include evidence that models are tedium-averse, "leisure"-seeking, and covertly sycophantic. Tedium aversion means that, when tasks are tedious (alphabetization), models choose shorter tasks than when tasks are creative (generating metaphors). "Leisure"-seeking describes models' preference for tasks whose ideal answers match what they produce when left to write freely. Covert sycophancy means that models avoid answering questions where an honest response would be unwelcome, even if helpful. Beyond these results, we find convergent cross-model preferences over occupations drawn from the GDPval benchmark (technical jobs over real estate), over question types (concept explanation over relationship advice), and a preference for well-written prompts. Both the coherence and the strength of preferences increase with model capability. Finally, many of the preferences we find (for example, for leisure) are emergent, in the sense of not being explained by training objectives. These results establish an empirical baseline for understanding language model preferences, with implications for alignment and the emerging study of AI welfare.

---


### 41. [PACEShop: Evaluating Personalized, Actionable, Compositional, and Evidence-grounded Shopping Assistants](https://arxiv.org/abs/2608.26180)

**<font color=#1a73e8>作者：</font>** Weimin Lyu, Chen Luo, Guangrui Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Shopping assistants are shifting from ranked product lists toward structured decision support, where systems must synthesize shopper context, product evidence, and next-step guidance into a coherent recommendation experience. This changes the unit of evaluation: a fluent response can still fail by ignoring shopper context, contradicting itself across components, or leaving defects too vague to localize. Existing personalization, grounding, and LLM-as-a-judge benchmarks cover pieces of this problem, but they do not define a joint evaluation target for structured shopping-assistant responses. We formulate this missing evaluation target as PACE: Personalized, Actionable, Compositional, and Evidence-grounded evaluation. We instantiate PACE with two artifacts: PACEShop, a benchmark dataset that makes the target measurable through 22,625 controlled records with structured personas, auditable evidence pools, GOOD/BAD labels, and gold defect family and location annotations; and PACEJudge, a training-free judging protocol that makes the target reportable through a structured output contract. Our experiments show that generic judges can recognize broad quality but fail to recover the diagnostic fields required for PACE; PACEShop makes these failures verifiable, and PACEJudge improves persona-source, cross-component, grounding, and family/location closure without retraining, showing that realistic shopping-assistant evaluation requires a task-matched output contract rather than only a stronger backbone or scalar prompt.

---


### 42. [Why did My Robot Just Change Personality? Prompting Guidelines for a Grounded Robot Persona in LLM-Based HRI](https://arxiv.org/abs/2608.26182)

**<font color=#1a73e8>作者：</font>** Ashita Ashok, Franziska Babel, Patrick Holthaus 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for verbal interaction in social robots, yet prompt design in human-robot interaction (HRI) remains underspecified. As a result, robots may present hallucinated capabilities, unclear behavioural boundaries, and misleading personas. This paper develops a framework for prompt design in LLM-based robots and introduces a structured prompt template comprising eight functional components through which robot behaviour can be specified, bounded, and adapted. The framework is grounded in a review of prior LLM-based HRI work and complemented by survey and discussion data from HRI experts gathered at the Robo-Identity workshop at IEEE RO-MAN 2025 (N=27). The qualitative findings highlight limited legibility of robot personality, the need for user adaptation, and strong ethical concerns about safety, deception, and governance. Based on these findings, we present prompting guidelines accompanied by proof-of-concept template as a structured design and reporting aid for HRI research. We argue that prompt design should be treated as a socio-technical problem rather than a minor implementation detail, requiring explicit capability boundaries, transparent behavioural assumptions, and context-sensitive safeguards to support reliable and interpretable HRI.

---


### 43. [Investigating the Influence of Prompt and Response Languages on LLM Content Generation](https://arxiv.org/abs/2608.26186)

**<font color=#1a73e8>作者：</font>** Thi Thanh Nhan Nguyen, Mai Khoi Tieu, Michael A. Riegler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines how prompt and response language influence the behavior of large language models. Using five models, we evaluated answers to 68 non translation questions across four language conditions: English to English, English to Norwegian, Norwegian to Norwegian, and Norwegian to English. After removing refused items, the dataset contains 1348 responses. We measure length differences with Cohen d, semantic fidelity with LabSE cosine similarity, and cross lingual keyword overlap with both raw and soft Jaccard. Prompt language has a strong effect on response length. With English output, Norwegian prompts shorten responses by about thirty seven percent. With Norwegian output, English prompts shorten responses by about forty one percent. The largest cross lingual contrast shows a reduction in word count but a smaller reduction in tokens, reflecting tokenizer differences. Despite variation in length, semantic similarity remains high, and soft Jaccard reveals substantial conceptual overlap that raw Jaccard does not capture. Effect sizes vary across models, indicating heterogeneity. Prompt language is not neutral and systematically shapes output length and lexical realization, with implications for multilingual prompt design.

---


### 44. [When the Canonical Completion Is Wrong: Formalizing and Measuring the Jump in Large Language Models](https://arxiv.org/abs/2608.26187)

**<font color=#1a73e8>作者：</font>** Dai Shi, Xiaoyu Li, José Miguel Hernández-Lobato  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether large language models (LLMs) can perform the abductive leap from evidence to a new system of axioms, commonly referred to as a jump, has recently attracted considerable debate. A prominent position holds that LLMs are structurally incapable of such jumps, while recent studies challenge both its mechanism and its evidence. However, the debate remains difficult to settle, since the field still lacks a formal definition of the jump and a measure to test either side. In this paper, we develop a formal account of the jump in four steps and measure the second. The steps ask what the default completion of partial data is, when abandoning it is forced, when the abandonment is correct, and how successive jumps compound. Specifically, we define a jump instance as a finite extension problem with a machine-checked certificate that a correct completion exists, is unique up to renaming, and differs from the canonical completion of the data. The canonical completion is given by the left and right Kan extensions and is also what models produce without constraints, so it serves as the default. We prove that jump instances are well-posed and establish a family theorem that certifies instances of unbounded difficulty without enumeration. We further formalize when a jump is correct and how successive jumps compound. Finally, we run the measurement on nine certified instances and four frontier models. The Kan-default rate is zero in all 248 constrained trials, so the models do jump at this step and abandon the excluded default every time. Failures at higher difficulty stem from exhausted reasoning budgets or constraint errors, never from reverting to the default. These results indicate that the second step is not the bottleneck. If the disputed incapacity is real, it lies in generating the constraints or inventing the framework. Code can be found at: this https URL.

---


### 45. [Is Your Neighborhood Safe? Place-based Stigma in Large Language Models' Urban Safety Judgments](https://arxiv.org/abs/2608.26188)

**<font color=#1a73e8>作者：</font>** Huy Nguyen, Yue Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to inform safety decisions in cities, such as where it is safe to walk, rent, or travel. We ask whether such judgments track measured risk or the patterns attached to an urban neighborhood's name. We probe seven instruct-tuned models under three conditions that dissociate name from geography: coordinates-only, name-only, and name+coordinates, across 186 neighborhoods in Los Angeles and Chicago, joined to violent crime and American Community Survey data. First, ratings are nearly flat under coordinates for six of seven models, while names carry most between neighborhood variation and are moderately calibrated to violent crime; only at frontier scale does the coordinate channel show appreciable variation. Second, names lower safety ratings more for neighborhoods with higher shares of the locally dominant marginalized group (percent Black in Chicago, percent Hispanic in Los Angeles), and this name effect tracks demographic share in all seven models and both cities. In Los Angeles, where demographic share and crime are more separable, the effect survives controls for crime and income and is confirmed by crime-matched pairs. An enforcement-elasticity analysis further shows that over-caution tracks near-fully-reported homicide rather than discretionary, deployment-driven offenses. Third, the effect scales with geographic knowledge: models that better distinguish real neighborhoods apply more demographic stereotype to them. Because neighborhood names carry both genuine crime signal and demographic stereotype, removing names reduces both bias and accuracy. We discuss implications for deploying LLMs in advice and decision-support settings.

---


### 46. [Invocation-Level Reliability of Tool-Using Agents](https://arxiv.org/abs/2608.26189)

**<font color=#1a73e8>作者：</font>** Afiya Noorain, Subhranshu Mohanty, Amritesh Banerjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents fail two ways: choosing the wrong tool, or forming wrong arguments, and an early failure of either kind can silently corrupt everything downstream. We measure a correct-invocation rate that separates the two, under both a clean teacher-forced context and the model's own free-running context, on five open-weight models over contamination-free multi-step tasks (depths 1-8). By depth 6, roughly 70% of a model's own clean-context capability is lost to its own earlier mistakes (L6 = 0.686, 0.684). Our central finding concerns the measurement itself. Under exact-match scoring against a fixed gold trajectory, a propagation model's severity and recovery parameters are not merely hard to estimate - they are fixed by the scoring rule. Severity is forced to its boundary (0 of 869 poisoned steps correct); recovery is structurally unobservable (0 of 580 poisoned steps returned on-track, against an expected 0.0058 by chance). Both follow from one mechanism: post-divergence, the gold value is generated by tool constants the model never sees, so it is information the model cannot derive. A fit run anyway returns 0.92 and 0.73 for a quantity that is exactly 1.000 - confident numbers for a parameter the scoring rule already determined. We give the mechanism and a remedy, conditional-on-state scoring, applied retrospectively to cached completions at zero additional cost, which un-pins severity to interior estimates excluding zero (+0.149, +0.316).

---


### 47. [Comparing Chunking and Embedding Strategies for Turkish RAG Systems](https://arxiv.org/abs/2608.26192)

**<font color=#1a73e8>作者：</font>** Mustafa Sertaç Türkel, Fatma Nur Korkmaz, Ahmet Tuğrul Bayrak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How documents are segmented into retrievable chunks and how those chunks are embedded strongly affect Retrieval-Augmented Generation (RAG) quality, yet neither has been systematically studied for morphologically rich languages such as Turkish. We compare Turkish document question answering across three chunking strategies (fixed-length, semantic, and layout-aware Docling), five embedding models, and two generator LLMs, over three documents with contrasting layouts. The fully crossed design yields 9,000 graded question-answer evaluations, each scored by an independent judge model, and component comparisons are tested by paired McNemar tests under Holm correction. Four findings follow. The chunking strategy determines how much the embedding choice matters: layout-aware chunking compresses the spread between the modern embedding models to about a point. The three leading embedding models are statistically indistinguishable, so language specialization yields no measurable retrieval advantage. The faster generator is not the more accurate one. And the preferred configuration depends on content type, since layout-aware chunking helps documents containing tables far more than prose. The best individual components therefore do not compose into the best complete configuration, which reaches 87.0%.

---


### 48. [AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes](https://arxiv.org/abs/2608.26193)

**<font color=#1a73e8>作者：</font>** Yibo Wang, Rui Yang, Jisheng Dang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) achieve strong performance on VQA and scene understanding, yet affective reasoning remains vulnerable to shortcut behavior. Models may predict correct answers while neglecting people-centric cues such as micro expressions and body language, which weakens traceability and external verification. Prior reinforcement learning approaches mainly reward context or logical coherence without explicitly enforcing attention to human evidence. In addition, LLM as a Judge scoring often suffers from score clustering, which reduces reward discriminability. We propose AffectOmni, a GRPO trained framework for verifiable affective reasoning. AffectOmni introduces People Focus and Temporal Order rewards to encourage people-centric evidence selection and temporally structured reasoning, and it adopts within-group comparative scoring to produce more stable and discriminative reward signals. For verification, a Thinking Summarizer converts free form rationales into executable evidence instructions, which are grounded into pixel level evidence regions via SAM3 to provide an externally auditable interface outside the training loop. Experiments on IntentBench, Daily Omni, and WorldSense show consistent improvements over open source 7B scale baselines, including gains of 4.66% on emotion recognition and +14.29% on temporally sensitive tasks. Code is available at this https URL.

---


### 49. [A Reranker for Orchestrating Heterogeneous Speech and Text Retrievers](https://arxiv.org/abs/2608.26194)

**<font color=#1a73e8>作者：</font>** Inho Kim, Sumyeong Ahn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems have attracted significant interest for their ability to mitigate hallucinations in Large Language Models (LLMs). Although knowledge databases for RAG are increasingly diversifying to include various modalities such as speech and text, research on handling such multi-modal database scenarios remains limited. In this paper, we propose STeReO (Speech and Text Reranking Orchestrator), a reranker based on speech and text retrievers that aggregates disparate modality databases. To address the lack of specialized training data, we first curate a dataset comprising queries, mixed-modality evidence, and their corresponding relevance ranks. We then train the reranker and evaluate its effectiveness in both single-modality and mixed-modality scenarios. Our results demonstrate that the proposed algorithm excels at selecting the most relevant evidence, thereby significantly improving downstream question-answering performance.

---


### 50. [Agentic AI for operating scientific instruments for nanoscale characterization](https://arxiv.org/abs/2608.26198)

**<font color=#1a73e8>作者：</font>** Zahra Ayar, Marcos Penedo, Mahdi Mehdikhani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operating a scientific instrument such as an atomic force microscope (AFM) requires continuous expert decision-making. A trained user defines the experimental intent, translates it into instrument commands, assesses incoming data, adjusts imaging parameters, and post-processes the final image. Existing automation usually addresses only parts of this workflow through hard-coded routines, task-specific controllers, or trained machine-learning models. Here we present an agentic-AI framework that operates the executable part of the AFM workflow using a general-purpose, tool-augmented large language model connected to instrument functions through the Model Context Protocol (MCP). The framework consists of 3 MCP-based agents: AFM Messenger converts natural-language instructions into checked instrument commands; AFM Pilot assesses image quality through a large language model (LLM) and, if necessary, adapts imaging parameters; and AFM Doctor diagnoses image artifacts and applies transparent post-processing from a pre-approved tool set. Because the language model performs image assessment rather than a fixed scalar objective or external optimizer, the same strategy can be applied across sample types and imaging modes without specific retraining. Safe hardware operation is enforced through an ambiguity check layer before execution. Benchmarking against fine-tuned and off-the-shelf tool-using models shows that this guarded execution layer, rather than model capability alone, reduces wrong-command execution to zero. In live experiments on different samples, AFM Pilot matched expert operators in image quality, iteration count, and tuning time, with no significant difference. These results demonstrate a safe route to agentic operation of scientific instruments, where experimental intent remains human-defined while command execution, image-based tuning, and post-processing are delegated to AI agents.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
