# 🧠 大模型相关研究 | 2026年06月23日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 51. [Is Our Benchmark Enough? An Analysis of Continual Learning for MLLMs](https://arxiv.org/abs/2606.20961)

**<font color=#1a73e8>作者：</font>** Van-Tuan Tran, Shruthi Gowda, Merim Dzaferagic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual adaptation is essential for multimodal large language models (MLLMs) deployed across evolving domains, but the state-of-the-art MR-LoRA method highly relies on the assumption that a MLLM-based router is necessary to process complex multimodal inputs. This paper revisits this claim on the MLLM-CL benchmark and argues for two claims. \textbf{First}, routing does not require an MLLM: a simple training-free, replay-free ptotypical routing method (\textsc{RePRo}), uses frozen pretrained features and task prototypes to match the MLLM-based router of MR-LoRA at far lower computational cost. \textbf{Second}, shared experts do not improve continual learning for MLLMs, despite their theoretical appeal. We show that these findings arise from two structural limitations of MLLM-CL: (1) its tasks are \textbf{highly separable} in representation space, and (2) its fixed task order makes conclusions \textbf{sensitive to a single curriculum} rather than robust across diverse continual-learning trajectories. As a result, the benchmark primarily rewards learning in isolation rather than genuine continual transfer. This motivates a new design for future benchmarks of continual MLLM learning, with overlapping task manifolds, multiple task orders, fine-grained domain shifts, and evaluation protocols that reward forward transfer as well as retention.

---


### 52. [AutoACSL: Synthesizing ACSL Specifications by Integrating LLMs with CPG-Based Static Analysis](https://arxiv.org/abs/2606.20969)

**<font color=#1a73e8>作者：</font>** Han Zhou, Yu Luo, Dianxiang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating formal specifications for C programs remains a challenge in formal verification due to the manual effort, expertise, and semantic precision required. While recent advancements in large language models (LLMs) offer promise in automating specification synthesis, current approaches often lack semantic depth and produce unverifiable or incomplete contracts. To address these limitations, we introduce AutoACSL, a novel framework that integrates LLM prompting with semantic features extracted from Code Property Graphs (CPGs). AutoACSL performs static analyses to extract key semantic elements, including arithmetic operations, loop and recursion structures, and return value propagation, which are encoded into structured prompts. These prompts enable the LLM not only to generate normal behavioral specifications but also to include constraints that prevent inputs leading to runtime errors. AutoACSL employs a feedback-driven synthesis loop, where candidate specifications are verified using Frama-C/WP and refined iteratively until verification succeeds or a termination condition is met. Evaluated on 604 programs drawn from diverse datasets, AutoACSL achieves a 98% specification generation success ratio and a 96% full proof ratio when paired with Gemini-3. Compared to a code-only baseline, AutoACSL improves the full proof ratio by 24.7% to 51.7% across four LLMs (GPT-o4 Mini, GPT-5.2, Grok-4.1, and Gemini-3), demonstrating that integrating large language models with CPG-based static analysis substantially enhances both generation robustness and verification effectiveness for automated ACSL specification synthesis.

---


### 53. [Building Agent Harnesses for Scientific Curation from Multimodal Sources](https://arxiv.org/abs/2606.21005)

**<font color=#1a73e8>作者：</font>** Sheng Zhang, Qin Liu, Renqian Luo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery workflows often depend on structured curation from the literature. This is difficult for current agents because the key evidence is scattered across long text, dense tables, and figures, and the final records often require reasoning across multiple evidence fragments rather than copying a single span. We study scientific curation from multimodal sources and introduce Beaver, an agent harness that extracts structured information from scientific papers while preserving provenance to the supporting evidence. Beaver combines a frontier agent with multimodal evidence tooling, task scaffolding, and artifact-grounded autoresearch. These components turn curation into a staged, auditable workflow and enable an iterative evaluate--diagnose--revise loop, where persistent run artifacts expose stage-localized failures and guide harness updates. Experiments show that Beaver reaches 81.0 on Gold-Referenced Attribute Score (GRAS), an attribute-level measure of agreement with gold curated records, outperforming frontier agents by over 23 absolute points. Ablations show that task scaffolding, multimodal evidence tooling, and provenance traces each contribute meaningfully to performance, while attribute-level analysis shows the largest gains on high-value attributes that require cross-modal reasoning and normalization. These results show that, for scientific curation from papers with multimodal evidence, harness design is a central determinant of agent performance.

---


### 54. [The Metanym Game: A Self-Contained, Self-Consistent LLM Peer-Community Benchmark for Structural Intelligence](https://arxiv.org/abs/2606.21008)

**<font color=#1a73e8>作者：</font>** David Nordfors  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The metanym game is a competitive word game for LLMs that measures structural intelligence against established cognitive-science constructs. No content is given in advance; the contestants create all of it -- a new kind of analogy test, analogical production falsifiable sentence by sentence, with no fixed test set to leak into training (contamination-resistant by construction). In the council-of-peers benchmark, the contestants also rate each other's creations. We introduce the first spectral solution, to our knowledge, to the wicked problem of benchmarking LLMs' factual accuracy without golden keys or oracle models: one singular value decomposition of the evaluators' ratings matrix yields their competence as both generators and judges of true statements at once. Competence on the subjective criteria comes from each judge's rating consistency as the yardstick shifts. The factual rating correlates with GPQA Diamond at Pearson r = 0.92. Scored separately, making and judging dissociate -- judging is the scarcer skill: the strongest generators are middling judges, the sharpest judge a mid-pack generator. To scale, the strongest players form a council that does the official benchmarking; its seats are contestable -- a stronger model earns one on the benchmark's own rating. The benchmark is entirely self-contained and self-consistent, a stable gauge over time.

---


### 55. [Agentic Time Machine as an Infrastructure for Future-Event Forecasting](https://arxiv.org/abs/2606.21013)

**<font color=#1a73e8>作者：</font>** Jingyi Chai, Bingyang Zheng, Xiangrui Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting future events is a critical challenge for large language model (LLM) agents, spanning domains from elections and monetary policy to financial markets. However, evaluating progress on this task presents a fundamental trade-off between efficiency and environment fidelity. While live evaluation benchmarks suffer from an inherently slow feedback loop, existing retrospective replays typically restrict agents to static, pre-frozen databases that sacrifice the environmental realism of actual deployments. To tackle this issue, we introduce Agentic Time Machine (TM), an infrastructure that approximately reconstructs the web state at any chosen past time by filtering post-cutoff content. Leveraging this evaluation infrastructure, we further propose a planner-solver-aggregator multi-agent framework that breaks each question into diverse analytical angles, gathers evidence in parallel, and combines the results into a single forecast. Experiments show that offline scores under TM correlate strongly with live FutureX scores, validating that TM offers a fast and reliable sandbox for forecasting-agent evaluation. On FutureX-Past and Polymarket evaluated under TM, our framework achieves the highest score among strong closed-book, tool-augmented, and self-consistency baselines. On the official FutureX live leaderboard, our system achieves the best average rank over four consecutive weeks, including 1st place in May Week 1. As of June 17, it also ranks 1st on FutureX's official eight-week overall leaderboard.

---


### 56. [Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](https://arxiv.org/abs/2606.21023)

**<font color=#1a73e8>作者：</font>** Zhenting Zhu, Lucas Thai, Shan Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement. While practitioners use greedy decoding to eliminate algorithmic stochasticity, empirical deployments with 16-bit precisions still exhibit catastrophic output divergence across heterogeneous GPUs. Through SASS-level profiling, we reveal that this inconsistency is fundamentally driven by truncation errors introduced during downcasting at kernel boundaries. However, achieving reproducibility via a global FP32 pipeline incurs prohibitive system penalties: bypassing 16-bit hardware accelerators hurts compute efficiency, while upcasting the KV cache doubles memory overhead. To bridge this gap, we propose Hybrid Error ALleviation (HEAL), a targeted intervention that approximates FP32 precision while resolving hardware constraints through two targeted mechanisms. First, recognizing that floating-point formats underutilize their bit-width for Q, K, V tensors, HEAL applies INT16 quantization that preserves numerical stability without expanding the KV cache footprint. Second, HEAL synthesizes high-precision matrix multiplications via an algebraic error compensation strategy, executing entirely on high-throughput 16-bit Tensor Cores. To evaluate our approach practically, we introduce MCR-Bench, a benchmark targeting reproducibility in mission-critical tasks. HEAL achieves the same level of reproducibility on downstream tasks as the FP32 baseline while reducing the performance overhead by up to 7.1x.

---


### 57. [Event Ontology Expansion via LLM-Based Conceptualization](https://arxiv.org/abs/2606.21048)

**<font color=#1a73e8>作者：</font>** Weicheng Ren, Zixuan Li, Long Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event ontology expansion aims to discover emerging event types from data and extend them to appropriate positions in the existing event ontology.. Existing methods typically cluster contextualized trigger representations and attach induced clusters to the ontology based on instance-level similarity. However, ontology expansion requires concept-level semantics that characterize event types, whereas contextualized trigger representations often conflate these semantics with surface contextual variation, leading to unstable clustering and unreliable hierarchy expansion. To address this issue, we propose ConceptE, a conceptualization-enhanced framework for event ontology expansion. ConceptE first derives concept-level semantics by prompting an LLM with the sentence and event trigger, producing a concise concept name and a natural-language description. It then jointly encodes these semantics with trigger information to build concept-enhanced representations aligned with ontology-level reasoning. This representation design supports more coherent event clustering, more reliable hierarchy expansion, and ontology-consistent type naming. Experiments on ACE, ERE, and MAVEN demonstrate that ConceptE consistently outperforms state-of-the-art approaches across all subtasks of event ontology expansion. In particular, it achieves improvements of up to 12.37\% in BCubed-F1 for event clustering and 6.48\% in Taxo\_F1 for hierarchy expansion, demonstrating the effectiveness of the proposed ConceptE method.

---


### 58. [FiLM-Coordinated Dual-Branch Transformer for Global-Local Dependency Modeling in Language Modeling](https://arxiv.org/abs/2606.21075)

**<font color=#1a73e8>作者：</font>** Zhiqiang Zhou, Xu Ling, Junliang Dai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard Transformers use a single self-attention pathway to model both global dependencies and local patterns, creating tension between long-range structural reasoning and fine-grained local representation learning. We propose a FiLM-coordinated dual-branch Transformer for language modeling, where each layer explicitly contains a global branch and a local branch, and feature-wise linear modulation (FiLM) is used for dynamic cross-branch coordination instead of simple concatenation or static addition. The key idea is that the two branches represent different dependency views of the same input, making channel-wise calibration more suitable than heavy token-level interaction. We therefore design a bidirectional FiLM module in which each branch generates per-channel scaling and shifting parameters to condition the other. Experiments on multiple small-scale language modeling settings show that the proposed structure consistently outperforms same-width single-branch baselines and weakened dual-branch variants under a fixed lightweight configuration. On TinyShakespeare and a 1M-character subset of WikiText-2, the full dual-branch FiLM model achieves the best results among same-width structural baselines. Multi-seed results support the stability of the gains, while mechanistic analyses show that FiLM learns input-dependent, layer-dependent, and channel-selective modulation patterns rather than static scaling. Parameter-matched widened single-branch baselines also indicate that the current design still leaves room for improvement in parameter efficiency.

---


### 59. [A Validation-Gated Mechanistic Account of Suicidality Detection in LLMs](https://arxiv.org/abs/2606.21078)

**<font color=#1a73e8>作者：</font>** Nafiz Ahmed, Sarah Sharif, Dingjing Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly proposed for mental-health applications such as detecting suicidal content, raising the question of what they rely on. We study this mechanistically and use it to ask a narrower question: how to make a causal claim about a model's internal features more trustworthy. Our validation-gated framework, with suicidality detection as a case study, interprets a behavior only after the model is shown to perform it: a concept is admitted only once the model ranks it above a simple lexical baseline, and each subsequent property is tested against a matched control. This discipline yields negative as well as positive results. The gate rules out one task at the outset: on DeepSuiMind (Li et al. 2025), Llama-3.1-8B-Instruct cannot separate implicit suicidal intent from ordinary distress, so we do not analyze it. We turn to binary suicide detection, which it does perform. There we find a mid-network feature that appears semantic rather than keyword-based, is causally implicated in the decision (ablating it degrades the judgment; a random direction does not), is low-rank, and recurs across three model families and three suicide datasets. A register-matched control (suicide versus depression) suggests it tracks suicidality more specifically than general distress. Steering raises the model's response, but for unrelated questions too, so we treat it as necessary but not sufficient. The clearest pattern separates encoding from use: smaller models already represent suicidality, yet only larger ones appear to act on it. The positive evidence is English Reddit text, which limits the clinical reading.

---


### 60. [Coherence Under Commitment: Probing Generalization and Vacuous Memorization in LLM Logical Reasoning](https://arxiv.org/abs/2606.21083)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Mahmudul Hasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed for logical reasoning in knowledge-intensive domains exhibit a subtle but critical failure: coherence can be vacuously achieved through systematic abstention. A model that withholds commitment to either entailment or refutation satisfies negation consistency while providing no utility. We introduce Coherence Under Commitment (CUC), a dual-query evaluation paradigm that jointly measures consistency and decisiveness. CUC contributes three innovations: (1) a commitment score $c(\varphi) = p(\varphi) + p(\lnot\varphi)$ quantifying probability mass allocated to decisive outcomes; (2) a \textbf{deterministic elicitation protocol} via normalized YES/NO log probabilities, eliminating sampling variance; and (3) a 3-way decision framework (True/False/Uncertain) operationalizing the coherence-commitment trade-off into metrics. Experiments on four open-weight LLMs (1B-3B) across 204 FOLIO examples expose a sharp frontier. Qwen2.5-3B achieves near-zero contradiction ($\mathbb{E}[v_{\mathrm{neg}}]{=}0.025$) but only $7.4\%$ coverage, while TinyLlama-1.1B reaches $79.4\%$ coverage with violations on every example. Coherence-only evaluation would rank the abstaining model first; CUC exposes this as vacuous, and the frontier generalizes to LogiQA~v2 ($\rho{=}0.97$). We argue that evaluation must report both coherence and non-vacuous commitment and release a toolkit for standardized assessment.

---


### 61. [Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines](https://arxiv.org/abs/2606.21089)

**<font color=#1a73e8>作者：</font>** Jianzhe Lin, Fei Wang, Xiaolin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial LLM teams often ship behavior updates by repeatedly DPO-training a base model on sequences of related preference-data campaigns. The dominant failure mode in this regime is not always classical catastrophic forgetting: a pipeline may preserve previously learned behaviors while still failing to accumulate reusable methodological knowledge about how to train the next campaign. We call this failure mode scientific amnesia. This paper turns that practitioner intuition into a measurable industrial problem. We contribute: (i) a diagnostic suite for amnesia, (ii) a Program-based pipeline that chains FSDP-sharded DPO checkpoints across Qwen2.5-7B-Instruct runs, (iii) a 30-campaign HumanEval subdomain benchmark, and (iv) a comparative diagnostic study of five strategy proposers: random memory, rule-based scheduling, retrieval-only memory, warm-start Bayesian optimization, and MSCL, a meta-scientific memory and reasoner candidate. Across a single-seed 5-condition * 3-step real-LM chain, 4 of 5 candidates degrade in step-level peak pass@1, including MSCL; only the deliberately conservative rule-based schedule improves. Follow-up pilots qualify rather than overturn this finding: in a heterogeneous chain, MSCL is the only completed candidate that improves, whereas in a small multi-seed homogeneous sweep, retrieval-only has the best mean Delta and no pairwise candidate gap is statistically distinguishable. The contribution is therefore diagnostic, not a claim that MSCL solves the problem: scientific amnesia is observable in a production-like continual-DPO pipeline, and conclusions about interventions depend sharply on chain regime, evaluator design, and seed coverage.

---


### 62. [Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training](https://arxiv.org/abs/2606.21090)

**<font color=#1a73e8>作者：</font>** Jianzhe Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improvement can self-regress. In REINFORCE post-training for code, a model can quickly improve on its optimized metric and then collapse within the same training campaign. We study this in a controlled multi-seed testbed using Qwen-2.5-3B and Qwen-2.5-7B, trained on competitive-programming tasks with binary CodeGrader reward across 10 sequential 20-step campaigns. Across campaigns, pass@1 shows a robust rise-then-collapse pattern: it peaks within tens of gradient steps and then falls back, sometimes to near zero. This is not cross-task catastrophic forgetting, but within-task policy over-optimization on a fixed distribution; KL- and EWC-style constraints do not prevent it.
We ask where the control loop should sit. We compare three levels: CARE, a between-campaign memory mechanism with a capability posterior, transfer gate, and regression-aware belief revision; ES, a within-campaign early-stop rule that rolls forward the peak checkpoint and sets the next budget to peak_step+3; and GRPO, which changes the RL update using group-relative reward normalization.
The answer is regime-dependent. On Qwen-2.5-3B, where naive REINFORCE is fragile, CARE v2 nearly doubles end-of-chain pass@1 from 4.9% to 9.5%, with paired bootstrap 95% CI [+0.4,+8.9] and gains in 4/5 seeds. On Qwen-2.5-7B, CARE reaches parity with naive REINFORCE, 13.8% vs. 11.8%, while ES reaches 22.2% [14.1,28.0]. Out-of-the-box GRPO reaches 20.7% [15.7,25.1], nearly matching REINFORCE+ES.
GRPO raises the floor but does not remove the cliff. Its 7B gain mainly comes from better between-campaign carryover, while the within-campaign peak-to-end gap remains about 17 points under both REINFORCE and GRPO. GRPO+ES gives mixed evidence: 2/3 seeds improve, but one final cliff lowers the mean to 17.0% [0.0,28.1]. A Gemma-3-4B pilot shows the same signature, suggesting the phenomenon is not limited to Qwen.

---


### 63. [GRAG: Generic Response-Augmented Generation Framework for Personalized Conversational Systems](https://arxiv.org/abs/2606.21097)

**<font color=#1a73e8>作者：</font>** Junfeng Liu, Christopher T. Symons, Ranga Raju Vatsavai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying highly capable personalized conversational agents in resource-constrained or privacy-sensitive environments remains a significant challenge. We identify a fundamental bottleneck in the existing approaches: current training paradigms treat personalization and grounding as a single monolithic learning problem. Under these paradigms, language models are forced to simultaneously address what to say (content grounding) and how to say it in a user-specific way (personalization), which introduces significant computational and optimization challenges. Consequently, contextual grounding is often sacrificed for persona adherence, or vice versa, resulting in responses that are either weakly grounded in the conversational history or insufficiently personalized. In this work, we propose the Generic Response-Augmented Generation (GRAG) framework that decouples these competing objectives by leveraging offline, generic responses from high-capacity, general-purpose LLMs as a semantic and structural scaffold to guide the fine-tuning of smaller, task-specialized models seamlessly in resource-limited environments. By decoupling the content grounding from personalization, GRAG allows the model to focus exclusively on persona injection while remaining firmly anchored to the conversational context. We instantiate the GRAG in two post- and pre-fusion-based architectural variants and evaluate them on multiple benchmark conversational datasets that cover diverse personalization structures. Our results demonstrate that GRAG significantly outperforms state-of-the-art methods that do not use auxiliary scaffolding, yielding up to 47% improvements in ROUGE-2 and 36% in BLEU scores. Ultimately, GRAG offers a generalizable blueprint for building grounding-aware personalized conversational systems in resource-limited environments.

---


### 64. [LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations](https://arxiv.org/abs/2606.21098)

**<font color=#1a73e8>作者：</font>** Younghan Park, Hoyeon Lee, Hawon Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of phrase break annotations is crucial, as subtle variations in prosodic boundaries directly affect the clarity and naturalness of speech. However, existing approaches exhibit major limitations: single-reference evaluation assumes a unique gold phrasing for an utterance despite multiple valid phrasings, while human judgment, though flexible, is labor-intensive and unscalable. To address these, we propose LLM-based Multi-Reference Evaluation (LMRE) for phrase break annotations that models the one-to-many nature of prosodic phrasing and generates multiple valid phrasings from minimal demonstrations. On a Korean testbed of 1,356 annotations covering five strategies, LMRE shows stronger alignment with human judgment than single-reference evaluation in both acceptance behavior and score correlation. Our findings demonstrate that LMRE effectively achieves both scalability and multi-reference support, highlighting the potential of LLMs for evaluation in the speech domain.

---


### 65. [MammoExpert: Benchmarking Chain-of-Thought Reasoning in Mammography Diagnosis](https://arxiv.org/abs/2606.21119)

**<font color=#1a73e8>作者：</font>** Di Dai, Bo Liu, Youcheng Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mammography is an essential tool for breast cancer detection, with millions of examinations conducted annually. However, publicly available high-quality mammography datasets for AI development remain limited in both scale and annotation richness, particularly regarding pathological subtype coverage and structured diagnostic reasoning annotations. In this paper, we present MammoExpert, the first mammography dataset with Chain-of-Thought reasoning annotations across three diagnostic phases: (i) primal observation, (ii) factual assessment, and (iii) diagnostic synthesis. Comprising 2,379 mammography images covering 67 WHO-classified histopathology subtypes, each exam provides 42 radiographic features annotated by nine senior radiologists. We evaluate its performance on the breast lesion classification task, demonstrating superior accuracy and reasonability compared to existing classification models. Combining public dataset CBIS-DDSM with MammoExpert yields 7.1\% classification accuracy improvement, while the training model to learn CoT reasoning achieves another 4\% gain on the MammoExpert test set. Similar improvements are observed on INBreast and Vindr datasets, where the full approach yields accuracy gains of 6.9\% and 6.7\%, respectively. MammoExpert can serve as a benchmark for interpretable breast lesion diagnosis through explicit CoT reasoning.

---


### 66. [Answer Engineering: Local Trajectory Editing for Protocol-Constrained Decision Making in Large Language Models](https://arxiv.org/abs/2606.21121)

**<font color=#1a73e8>作者：</font>** Victor Lavrenko, Anastasiia Molodnitskaia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can produce confident but protocol-invalid answers in domains where procedural compliance is critical. This paper presents Answer Engineering, a deterministic runtime and authoring layer that applies localized rule-guided interventions to the visible reasoning trajectory during standard autoregressive generation, without retraining, modifying model weights, or performing global search. The method is evaluated on a controlled clinical benchmark for sudden sensorineural hearing loss (SSNHL), where correct management depends on protocol-consistent interpretation of symptom timing, Weber/Rinne tuning-fork findings, and otoscopic findings. In the benchmark, step-by-step reasoning shifted rather than eliminated errors: compliant outcomes for SSNHL decreased from 54.5% under unguided generation to 25.1%, while acceptance on the conductive contrast condition increased from 1.6% to 58.9%. Local trajectory editing increased SSNHL compliance to 83.5% and conductive-case adherence to 77.9%, raising balanced accuracy from 42.0% under reasoning-only generation to 80.7%. The results support a systems-level view in which protocol adherence can be improved through auditable runtime control of reasoning trajectories, while also identifying limitations caused by rule coverage, trigger reliability, and persistent diagnosis-first generation dynamics.

---


### 67. [A Multi-Agent Audit Framework for High-Stakes Reasoning: Evaluation and Interpretability in Clinical Mental Health Screening](https://arxiv.org/abs/2606.21123)

**<font color=#1a73e8>作者：</font>** Jingchen Ye, Yanpei Yu, Luyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-stakes reasoning tasks necessitate transparent and verifiable workflows, yet conventional single-model large language models (LLMs) often struggle with hallucination and low interpretability under zero-shot paradigms. To address this general AI challenge, we propose a Multi-Agent Audit Framework that simulates a collaborative, multi-step verification process. We empirically validate this architecture in the sensitive domain of clinical mental health screening using a modular LangChain workflow. Our framework decomposes the reasoning process into a Perception Agent, Knowledge Retrieval-Augmented Generation (RAG), Chain-of-Thought (CoT) clinical inference, and a critical Audit verification stage. We evaluated this framework on the DAIC-WOZ dataset using locally deployed open-source models. Experimental results demonstrate that our multi-agent pipeline significantly outperforms single-agent baselines, reducing the Mean Absolute Error (MAE) for PHQ-8 depression severity prediction from 5.35 to 5.02. By exposing cross-agent validation traces, the framework mitigates reasoning drift and provides highly interpretable diagnostic rationales, offering a generalizable paradigm for reliable AI-assisted decision support beyond isolated model scaling. We make data and code open access on GitHub for replicability.

---


### 68. [What Accuracy and Gradient Cosine Miss: Evaluating Feedback Alignment via Scale Stability, Reference Validity, and Depth Utility](https://arxiv.org/abs/2606.21126)

**<font color=#1a73e8>作者：</font>** Yuren Hao, Xiang Wan, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the success of deep learning, training deep networks in biologically plausible and hardware-efficient ways remains an open challenge. Feedback alignment (FA) methods address this by replacing backpropagation's symmetric backward weights with fixed random matrices, but their effectiveness depends critically on whether they can be accurately evaluated. The standard evaluation relies on two quantities: task accuracy and cosine similarity between the method's credit signal and the backpropagation gradient. We show that this reporting pair is insufficient by identifying two independent failure modes, both silent under current reporting: (1) measurement degeneracy, where the BP reference gradient collapses to the numerical floor in terminal-LayerNorm residual architectures, rendering cosine uninterpretable; and (2) aggregation collapse, where the aggregate cosine masks layerwise heterogeneity that concentrates credit at one end of the network. To address these limitations, we propose a diagnostic evaluation protocol based on three checks -- scale stability, reference validity, and depth utility -- together with per-layer rather than aggregate cosine reporting. Across multiple architectures and methods, the standard reporting pair gives no signal of failure in any audited case, while our protocol identifies all failures with wide calibration margins. The two failure modes are causally independent: a per-block scale penalty alleviates Mode 1 (residual scale explosion driving reference collapse) without affecting Mode 2 (cosine ranking that contradicts every functional metric we measured). Identifying these silent failures prevents researchers from building on non-functional credit assignment and provides actionable guidance for developing FA methods that genuinely train deep layers.

---


### 69. [Odoriko: A Shape-Aware Multimodal Diffusion Framework for Human Motion](https://arxiv.org/abs/2606.21135)

**<font color=#1a73e8>作者：</font>** Dongseok Shim, Julian Tanke, Kengo Uchida 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion generation has been widely studied across diverse input modalities, text, music, and video, and recent efforts have unified these into single multimodal frameworks. However, while morphological factors such as gender and body shape are known to produce distinct kinematic signatures, no existing unified framework incorporates this into generation, treating all subjects as morphologically equivalent. We present Odoriko, the first unified multimodal motion generation framework that reflects subject bio-morphological information directly in synthesized motion output. Rather than averaging over subject variation, Odoriko generates motion that is consistent with who is moving, not just what they are asked to do, across text, music, and video conditions within a single model. When explicit morphological information is unavailable, Odoriko additionally recovers subject morphology alongside motion, unifying estimation and generation in one framework. Extensive experiments across text-to-motion, music-to-dance, and video-to-motion benchmarks demonstrate that Odoriko matches or exceeds prior specialized models on standard metrics, while enabling morphology-consistent generation that no existing unified framework supports.

---


### 70. [AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents](https://arxiv.org/abs/2606.21144)

**<font color=#1a73e8>作者：</font>** Xingyu Chen, Rui Wang, Zhaopeng Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory systems for Large Language Model (LLM) agents typically try to \emph{remember everything}, extracting memories uniformly to retain as many facts as possible. In production, however, inference cost and finite context budgets make this untenable: beyond consolidating raw dialogue into memory, an agent must exert \emph{write control}, efficiently keeping only the information each user actually cares about. Otherwise, long-horizon personalized interactions suffer \emph{memory bloat}, where irrelevant trivia crowds out useful information and steadily erodes question-answering (QA) accuracy. We argue that what is worth remembering is role-dependent, and propose \textbf{AdaMem} (Adaptive Memory), a method that \emph{learns what to remember} for each user from feedback. AdaMem maintains a structured, role-specific Memory Policy and refines it from weekly QA feedback through a lightweight, patch-style self-reflection step with failure rollback. To study this setting, we build \textbf{AdaMem-Bench}, a benchmark that simulates weeks of interaction with week-by-week QA. Across two extraction models and two feedback modes, AdaMem improves QA accuracy by up to \textbf{+9.0\%} over the uniform Mem0 baseline while shrinking memory volume by \textbf{9\%}.

---


### 71. [Dementia-Agents: A Multi-Modal Multi-Agent System for Dementia Staging and Phenotyping](https://arxiv.org/abs/2606.21168)

**<font color=#1a73e8>作者：</font>** Yaling Shen, Maja Christensen, Yiwen Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dementia diagnosis requires integrating multi-modal clinical assessments from diverse informants and clinicians under incomplete and heterogeneous data conditions. Yet most AI-driven approaches remain Alzheimer's disease (AD)-centric, framing the problem as binary AD detection or three-stage AD progression modeling within well-curated research settings. This pathology-driven paradigm overlooks the broader, syndrome-level nature of dementia, which spans multiple stages, phenotypes, and etiologies. In this paper, we propose Dementia-Agents, a clinically aligned multi-agent framework for real-world dementia staging and phenotyping. The framework follows a three-step workflow: (1) a data agent translates structured clinical records into semantically faithful textual representations that preserve missing-data signals and routes them to domain-aligned experts; (2) five fine-tuned expert agents generate domain-level predictions; and (3) a coordinator agent performs probabilistic aggregation to produce final staging and phenotyping decisions. We develop and evaluate Dementia-Agents on a real-world clinical cohort of 1,066 patients from two cognitive neurology services. Compared with monolithic multi-modal large language models (MLLMs) and prior medical multi-agent systems, our approach achieves consistent improvements in diagnostic performance for real-world syndrome-level dementia staging and phenotyping, while preserving domain-level interpretability.

---


### 72. [BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving](https://arxiv.org/abs/2606.21172)

**<font color=#1a73e8>作者：</font>** Zhe Shuai, Xiaopeng Xie, Yikun Zeng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are increasingly used in autonomous driving to forecast future scene evolution and provide future-aware spatio-temporal representations for downstream action prediction. In perception-to-action pipelines, these representations can directly influence ego-vehicle waypoint planning, making the learned future dynamics a critical security-sensitive component. Despite their promise, the training-time security risks of autonomous-driving video world models remain largely unexplored. We present BadDreamer, a transferable spatio-temporal backdoor attack that targets the perception side of this pipeline. Unlike conventional backdoors that manipulate image labels, prompt outputs, or action supervision, BadDreamer poisons the learned transition dynamics of a video world model. It constructs trigger-erasure sequences in which an oncoming yellow delivery rider is visible in the observed context frames but erased from the future frames. After fine-tuning on a small fraction of such sequences, the compromised world model learns a hidden conditional association: when the physical trigger appears, it hallucinates a future where the rider disappears and the road appears clear. We further show that this corrupted future-aware representation can transfer to the downstream action module without directly modifying ego-trajectory labels, inducing unsafe non-evasive waypoint predictions. Our experiments instantiate this attack on a representative open-source perception-to-action pipeline, revealing a representation-level safety risk in autonomous-driving video world models and highlighting the need for backdoor-aware validation beyond clean generation quality.

---


### 73. [Inverting the Bellman Equation: From $Q$-Values to World Models](https://arxiv.org/abs/2606.21173)

**<font color=#1a73e8>作者：</font>** Alistair Letcher, Mattie Fellows, Alexander D. Goldie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based and model-free reinforcement learning are traditionally viewed as separate paradigms: instead of learning a model of the transition kernel $P$, model-free agents typically estimate value functions tied to a specific policy and reward. In this paper, we challenge this dichotomy by proving that value-based agents trained on a sufficiently rich set of reward functions, e.g. using goal-conditioned RL, implicitly encode a unique and accurate world model. To extract this model in practice, we introduce \textit{$P$-learning}, an inverse analogue to $Q$-learning that samples from an agent's $Q$-values, policies and rewards to decode its internal model of the environment. We then provide sufficient conditions on the type and number of goals for which agents encode the true kernel $P$, covering both stochastic and deterministic MDPs over finite or continuous state spaces. Even when our assumptions are violated, we empirically demonstrate that agents trained on a handful of reward functions encode accurate dynamics in $\texttt{Reacher}$, $\texttt{MountainCar}$ and stochastic variants of $\texttt{FourRooms}$. Surprisingly, we find that policies trained exclusively on a \texttt{Reacher} agent's implicit world model are quasi-optimal on out-of-distribution, velocity-based goals despite position-only training -- suggesting that agents contain hidden generalisation capabilities and providing a new lens into the connection between model-based, model-free, and goal-conditioned RL.

---


### 74. [MEDLAYXPLAIN: Benchmarking the Expert-Lay Gap in Medical Vision-Language Models](https://arxiv.org/abs/2606.21194)

**<font color=#1a73e8>作者：</font>** Han Jang, Junhyeok Lee, Songsoo Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (Med-VLMs) achieve strong expert-level performance, yet their ability to generate patient-accessible descriptions remains underexplored. With the 21st Century Cures Act now mandating immediate patient access to diagnostic imaging results, evaluating whether Med-VLMs can bridge this Expert-Lay Gap is both urgent and clinically consequential for patient education and shared decision-making. To this end, we introduce MedLayXPlain, the first large-scale multimodal benchmark and evaluation framework for Medical Lay Language Generation (MLLG). MedLayXPlain-122K provides 122,789 region-grounded samples across 8 imaging modalities from 12 publicly available source datasets, each comprising a medical image with paired expert and lay captions anchored in a three-level Unified Medical Language System (UMLS) ontology hierarchy spanning 7 semantic groups, 43 semantic types, and 2,411 medical concepts. Lay captions are constructed via Hierarchical Ontology-Verified Refinement (HOVER), a three-step pipeline combining patient-centric vocabulary mapping, LLM-based constrained rewriting, and cross-model visual verification to enforce semantic equivalence while preventing hallucination. We further introduce MedLayEval, a lightweight 3B evaluator distilled from a 27B verifier that scores expert-lay alignment across five clinically grounded attributes, addressing the poor correlation between standard NLG metrics and clinical judgment. Benchmarking 33 VLMs on MedLayXPlain-122K reveals a systematic Expert-Lay Gap: medical VLMs achieve strong expert captioning but suffer significant lay-register degradation, while general-purpose VLMs produce more accessible language yet lack clinical precision, confirming that neither current paradigm adequately serves patient-facing communication.

---


### 75. [Beyond Hooking Onto the World: Referential Profiles and the Numerical Structure of LLM Grounding](https://arxiv.org/abs/2606.21195)

**<font color=#1a73e8>作者：</font>** Joo Yull Rhee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper revisits the grounding problem for large language models in light of recent vector-grounding accounts. I accept the shift from classical symbol grounding to vector grounding, but argue that the current debate remains incomplete in two respects. First, reference is often treated too thinly, as if it were a fixed link between an isolated expression and an object. I argue instead that reference is profile-based, context-sensitive, discourse-level, affectively shaped, and norm-governed. Even in the human case, reference is publicly stabilized through patterns of use, correction, distinction, inference, and continuation rather than through identical private representations. Second, vector grounding requires an account of numerical realization. LLMs do not acquire reference through human perception, memory, intention, embodiment, or understanding. Rather, through optimization, they parameterize linguistic traces of human world-directed practice. In a finite vector system, referential profiles must be distributed, may be superposed, and are recovered through context-sensitive computation. Weights, activations, attention-mediated hidden states, softmax-trained contrasts, and inner-product alignments are the mathematical sites at which inherited linguistic relations become stable and causally active. Mechanistic interpretability findings, including entity-like features, knowledge neurons, and emotion-related activation directions, provide indirect support for this view. They do not show that LLMs possess human reference. They support a more limited thesis: LLMs may possess derivative, language-mediated, profile-based, and numerically structured forms of reference.

---


### 76. [Extraction and Analysis of Multimodal Concepts in Vision Language Models through Sparse Autoencoders](https://arxiv.org/abs/2606.21197)

**<font color=#1a73e8>作者：</font>** Sergio Lanza, Jae Hee Lee, Stefan Wermter  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have demonstrated impressive performance in tasks requiring joint understanding of images and text, such as image captioning and Visual Question Answering (VQA), but our understanding of their internal processes remains limited. Recently, Sparse Autoencoders (SAEs) have emerged as a promising tool to support the interpretation of concepts encoded in VLMs. However, most SAE-based approaches focus only on textual or visual concepts separately, ignoring multimodal concepts.
This limitation hinders a comprehensive understanding of VLMs, since concepts that integrate both modalities can be misclassified.
Moreover, previous visual approaches often produce low-quality visual concept descriptions that are vague or incomplete, limiting their usefulness for understanding model reasoning. We propose a framework based on SAEs to extract and analyze visual, textual, and multimodal concepts from VLMs. For each neuron, we propose a candidate human-interpretable concept and compute the alignment between the concept and the dataset samples using cosine similarity scores. Experiments on a VQA dataset (LLaVA-NeXT) demonstrate that our framework improves visual concept quality by up to 45\% compared to existing SAE-based methods, while maintaining high textual concept quality and enabling systematic identification of multimodal concepts. This work contributes new insights into the conceptual space of VLMs, providing a structured approach to distinguish between visual, textual, and multimodal concepts.
The code is available at this https URL

---


### 77. [When Context Misleads: Surprisal, Energy and Attention Entropy as Metrics of Coherence Illusions in LLMs](https://arxiv.org/abs/2606.21203)

**<font color=#1a73e8>作者：</font>** Ece Takmaz, Nitin Kumar, Li Kloostra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Psycholinguistics studies show that human readers fall for coherence illusions: an incoherent discourse can seem coherent simply because a distractor matches what comes next. We investigate whether Dutch language models (6 monolingual and 4 multilingual) show the same behavior on texts that link back to earlier context with words such as 'again' and 'too'. First, we find that surprisal at the critical word tracks human acceptability judgments and eye-tracking data. Models are more surprised by incoherent continuations, but a matching distractor in the prior context reduces this surprisal. Second, attention entropy at the critical position identifies heads that behave differently under coherence vs. incoherence. We find that ablating these heads shows transfer effects across experiments, suggesting a shared mechanism. Third, we introduce energy from the associative-memory literature as a metric to quantify discourse coherence. Taken together, our results show that coherence illusions arise in Dutch LLMs, with entropy and energy exposing mechanisms that operate across settings.

---


### 78. [DCD-PFN: A Decoupling-Aware Foundation Model for Causal Discovery](https://arxiv.org/abs/2606.21212)

**<font color=#1a73e8>作者：</font>** Zhengkang Guan, Yikang Chen, Yi He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery is critical for understanding complex data-generating mechanisms, yet traditional algorithms often struggle with highly non-linear and noisy systems, or suffer from severe computational bottlenecks. Recent tabular foundation models based on Prior-Data Fitted Networks (PFNs) have demonstrated remarkable zero-shot inference capabilities, but their potential for explicit structural causal discovery remains underexplored. To bridge this gap, we propose DCD-PFN, a decoupling-aware foundation model for causal discovery. Instead of directly amortizing global graph reconstruction, DCD-PFN focuses on local causal discovery through a decoupling-based paradigm. Through pre-training on diverse synthetic Structural Causal Models (SCMs), the model learns sample-wise decoupling weights that enable Markov boundary (MB) identification. Furthermore, by leveraging parallelized local discovery, DCD-PFN efficiently reconstructs global causal graphs while remaining grounded in the theoretical foundations of decoupling-based causal discovery. Experiments demonstrate that our foundation model achieves robust zero-shot generalization.

---


### 79. [Sakana Fugu Technical Report](https://arxiv.org/abs/2606.21228)

**<font color=#1a73e8>作者：</font>** Yujin Tang, Edoardo Cetin, Jinglue Xu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The capabilities of frontier Large Language Models (LLMs) continue to advance, with different providers increasingly specializing in distinct domains. This raises a natural next objective: how to combine the individual specializations of various LLMs into a collectively intelligent system. To this end, we report the development of Sakana Fugu, a family of orchestrator models that harness and amplify the capabilities of an LLM agent team. Fugu models are themselves language models trained to understand user queries and dynamically devise agentic scaffolds to solve them. Through these adaptive scaffolds, Fugu accesses performance beyond any individual LLM agent, achieving state-of-the-art results compared to other publicly accessible models across a range of challenging tasks, including SWE-Bench Pro, Terminal Bench, LiveCodeBench, GPQA-Diamond, Humanity's Last Exam, and CharXiv Reasoning. We release two models: Fugu, which balances performance with latency for everyday use, and Fugu-Ultra, which prioritizes answer quality on the hardest problems. We describe our training paradigm, which encompasses large-scale fine-tuning, evolutionary algorithms, and reinforcement learning approaches, along with the infrastructure and core design principles that turn these methods into a production system. We hope this report encourages further research into multi-agent systems and dynamic, query-adaptive agentic scaffolds as a path toward the next frontier of AI capabilities, accessed through collective intelligence.

---


### 80. [SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services](https://arxiv.org/abs/2606.21255)

**<font color=#1a73e8>作者：</font>** Zhuoyun Li, Boxuan Wang, Changshun Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rejecting inputs outside the defined in-distribution (IND) service scope is critical for large language model (LLM) services, where unsupported requests should be filtered before full generation. Existing out-of-distribution (OOD) detectors often rely on final outputs or final-layer representations, leaving unclear where service-boundary signals are most clearly encoded inside the model; they also lack a theoretical guarantee for held-out inputs. In this paper, we introduce SCOPE (Sequential Conformal OOD Probing and Evaluation), a framework that selects a readable hidden layer, constructs a conformal gate with IND calibration, and uses a supermartingale e-process to certify persistent service-boundary evidence. Experiments across multiple LLM backbones and six carefully designed boundary conditions show that SCOPE improves gate-level rejection over standard final-layer detectors, while revealing how different OOD boundaries take different geometric forms in hidden space.

---


### 81. [ARCO: Adaptive Rubric with Co-Evolution for Multi-Step LLM-Based Agents](https://arxiv.org/abs/2606.21262)

**<font color=#1a73e8>作者：</font>** Zihang Tian, Jingsen Zhang, Rui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for multi-step LLM agents often relies on scalar rewards that indicate success but cannot explain why a trajectory is good or bad. Rubric-based rewards improve interpretability through natural-language criteria, but existing methods score at the trajectory level and freeze the scorer behind a closed-source judge, leaving step-level credit assignment unresolved and the judge itself static. We propose ARCO (Adaptive Rubric CO-evolution), a rubric framework in which a same-scale model $\mu$ shares a backbone with two heads: a generation head that produces per-step criteria, and a score head that predicts rubric-conditioned step-level rewards. A trajectory decomposition constraint ties the sum of step rewards to the terminal outcome, enabling credit assignment without step-level labels, while $\mu$ and the policy $\pi$ are jointly updated on on-policy data so that the rubric content and the scoring function co-evolve at the parameter level. Across HotpotQA, 2WikiMultiHopQA, and MuSiQue with two open-source backbones, ARCO improves the best EM in every setting over strong outcome-, rubric-, and process-reward baselines, and analyses show that its rubrics are step-specific, robust to design choices, and useful for diagnosing agent behavior. Codes and data are available at this https URL.

---


### 82. [Reward-free Pretraining for Reinforcement Learning via Occupancy Coverage Maximization](https://arxiv.org/abs/2606.21271)

**<font color=#1a73e8>作者：</font>** Marco Pratticò, Pietro Novelli, Massimiliano Pontil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse rewards pose a central challenge in reinforcement learning, since agents receive no informative signal until they reach their goal. Intrinsic-reward methods address this issue by optimizing non-stationary objectives such as novelty, prediction error, or skill diversity, thereby injecting a supervision signal into the problem. While effective, these methods often require that the extrinsic (sparse) reward can be evaluated -- either online or during offline relabeling of the stored transitions. This limitation is particularly vexing for multi-task, meta-, and continual reinforcement learning, where agents' interactions with the environment are usually reward-free. In this work, we present a method to pre-train transferable exploration policies that rapidly adapt to sparse rewards at downstream task time. Our objective maximizes state-space covering for the occupancy measure, and can be framed in terms of entropy maximization. Its algorithmic implementation, ROVER, leverages recent advances on the operatorial formulation of RL to estimate occupancy with a learned resolvent world model, bypassing common hurdles associated with density and entropy estimation. ROVER further introduces a virtual "sink" state for unexplored regions, balancing coverage of known states with expansion into unseen ones and preventing cyclic expansion-collapse behavior during learning. In tabular and pixel-based sparse navigation tasks, ROVER produces more uniform aggregate coverage and stronger initializations for downstream tasks than standard reward-free baselines.

---


### 83. [Lightweight 3D Feature Pretraining by Bayesian Inversion of 2D Foundation Models](https://arxiv.org/abs/2606.21292)

**<font color=#1a73e8>作者：</font>** Marwane Hariat, Gianni Franchi, David Filliat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Casper3D, a lightweight probabilistic framework for converting noisy multi-view 2D foundation-model embeddings into a latent 3D semantic representation. We model view-level semantic features as noisy observations of an underlying 3D semantic state and infer this state with a set-based variational model that incorporates relative pose during multi-view reasoning. Casper3D is trained by predicting held-out semantic observations from novel viewpoints, while remaining aligned with visual and text semantic spaces for open-vocabulary 3D understanding. The framework is backbone-agnostic and applies to both language-aligned and self-supervised embeddings. Experiments show that Casper3D produces more stable 3D semantics than simple multi-view pooling, especially in ambiguous and noisy settings.

---


### 84. [Social World Model for Lifelong Social Intelligence](https://arxiv.org/abs/2606.21315)

**<font color=#1a73e8>作者：</font>** Yu Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social intelligence is a core competency for language agents, yet current research primarily focuses on static capability evaluation rather than how these skills are continuously shaped and accumulated. This gap calls for a shift toward sustainable learning paradigms. Currently, two methodological pain points exist: social interaction trajectories lack unified structured representations to form iterable learning signals, and capability improvement and retention are typically studied in isolation, hindering the assessment of continuous evolution.
To bridge this gap, we propose the Social World Model. We decompose social interaction into five dimensions (scene setting, observation, mental state, action, and dialogue) to build a closed-loop learning framework. In this setup, agents collect interaction experiences, convert them into preference signals for model updating, and redeploy the updated policy for continued learning. Additionally, we provide a reusable data synthesis mechanism and a lifelong learning benchmark, transforming social capabilities from an "object of evaluation" into an "object of sustainable training".
Validating our framework on the ASCENT-Bench, the interactively trained Qwen2.5-7B model outperforms its baseline across all five core metrics. Notably, it matches the closed-source Gemini 3 Flash in completion rate, exceeds it in pass rate, and achieves zero forgetting across three difficulty levels. Unlike prior works that merely report static comparisons or capability decay, this end-to-end approach provides a trainable, verifiable, and retainable pathway, demonstrating that small open-source models can sustainably acquire competitive social coordination capabilities.

---


### 85. [Objective-Behavior Alignment: Diagnostics for MORL Policy Selection](https://arxiv.org/abs/2606.21321)

**<font color=#1a73e8>作者：</font>** Antonio Mone, Zuzanna Osika, Florian Felten 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world decision-making often requires optimizing multiple competing objectives simultaneously. In reinforcement learning (RL), this is typically addressed by combining reward signals into a single scalar objective via a scalarization function, which can be fragile: small changes in the weights can induce drastically different policies. Multi-objective reinforcement learning (MORL) instead produces sets of policies that explicitly represent trade-offs between objectives. However, these policies are typically presented to the decision maker only through their value vectors, which can obscure substantial behavioral variation: policies that induce distinct trajectories may appear indistinguishable when evaluated solely by expected returns. We propose an exploratory diagnostic workflow that automatically highlights behavioral variation along the Pareto front that objective values alone do not reveal, providing both quantitative and visual tools to support policy inspection. We validate our approach on simple grid examples and scale it to continuous control benchmarks, demonstrating that it remains effective as problem complexity increases.

---


### 86. [DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams](https://arxiv.org/abs/2606.21337)

**<font color=#1a73e8>作者：</font>** Cong Wan, Zeyu Guo, Zijian Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Massive unstructured multimodal streams suffer from high "data entropy," impeding both efficient human knowledge acquisition and high-quality AI post-training. Existing passive annotation paradigms, heavily reliant on heuristic rules or general VLMs, are costly, monotonous, and fail to unlock the deep procedural logic embedded in raw data. We elevate data processing to a learnable capability, proposing a paradigm shift towards Agentic Data Tailoring, which actively refining and structuring data to align with diverse user and downstream intents. To overcome the data scarcity bottleneck in training such high-order capabilities, we design a two-stage pipeline grounding generative semantic synthesis in deterministic Factual Anchors, yielding a large-scale dataset spanning five core physical and digital domains. Building upon this, $\text{DataClaw}_0$-9B model synergizes Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO), achieving robust alignment with complex refinement and tailoring intents. To systematically quantify this capability, we construct $\text{DataClaw}_0$-val, the first benchmark dedicated to data refinement. Crucially, we adopt downstream post-training as the ultimate validation touchstone. Evaluations on video generation, real-world VQA, and GUI navigation confirm that $\text{DataClaw}_0$ delivers high-information-density tailored data, facilitating efficient model adaptation to new tasks under limited training data regimes. Project page: this https URL

---


### 87. [Factual Retrieval in LLMs Is a Redundant, Distributed and Non-Contiguous Process](https://arxiv.org/abs/2606.21345)

**<font color=#1a73e8>作者：</font>** Hail Hochman, Natalie Shapira, Yoav Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) store and recall factual knowledge, yet the precise mechanism of how entity representations are transformed to enable specific attribute retrieval remains underexplored. In this work, we investigate this mechanism through the lens of an "attribute-computation path"-a sequence of computational steps over the entity representation required to elicit a target attribute. We then propose an iterative patching protocol to identify a minimal subset of layers necessary for this computation. Applying our method to LLaMA 3.1 8B and Qwen3 8B, we find that these paths are non-contiguous, often skipping layers, and that models possess multiple, functionally-equivalent paths for the same entity and fact, highlighting a high degree of redundancy in attribute computation. This implies that knowledge computation is highly distributed, potentially explaining the localization-editing mismatch and suggesting that knowledge storage and retrieval in LLMs is far from being well understood.

---


### 88. [SOHET: Sequence Of Heterogeneous Events Transformer with Self-Supervised Pre-Training](https://arxiv.org/abs/2606.21356)

**<font color=#1a73e8>作者：</font>** Kees Jan de Vries, Mustafa Radha, Mathijs de Jong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning applications rely on heterogeneous event streams to make predictions, either causally as events arrive or bidirectionally over complete sequences. We propose SOHET (Sequence Of Heterogeneous Events Transformer), a hierarchical architecture combining event-type-specific tabular encoders with temporal and type embeddings, processed by a causal or bidirectional transformer. We introduce three self-supervised pre-training objectives for the causal setting. On a proprietary large-scale real-world this http URL fraud detection task with 17 event types, SOHET outperforms FlexTPP, NAPPT, and CIPPT by 5.8%. Pre-training yields an additional 2.6% gain and 2.4% faster convergence. On the EBES benchmark, bidirectional SOHET matches or exceeds the published best on 6 out of 8 tasks.

---


### 89. [Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs](https://arxiv.org/abs/2606.21359)

**<font color=#1a73e8>作者：</font>** Raia Abu Ahmad, Nikolas Rauscher, Ekaterina Borisova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to communicate and explain scientific concepts, yet their tendency to hallucinate poses significant risks in this high stakes use-case. Prior hallucination evaluation work remains largely restricted to the biomedical domain, treats hallucination as a binary task, and has not examined the growing family of scientifically fine-tuned LLMs. We address these gaps with SciFactCheck, a benchmark of 2,500 prompts across five scientific domains, paired with a modular evaluation framework targeting three factuality hallucination types: unverifiability, overclaim, and attribution. Using a controlled minimal-pairing design, we evaluate 18 LLMs by comparing each scientifically fine-tuned model against its general-purpose base. Our results indicate that 1. Scientifically fine-tuned models exhibit degraded factual reliability across all hallucination types and scientific domains, and 2. Fine-tuned models are internally less confident yet linguistically more assertive. A human pilot study further reveals that current fact-checking tools show only modest agreement with expert judgments on scientific content, and that defining scientifically check-worthy claims remains contested even among human annotators. Our findings fundamentally challenge current methods of domain-specific fine-tuning for factuality and call for developing improved verification infrastructure for scientific content.

---


### 90. [Graph-of-Differences: Anatomy-Structured Difference Alignment for Medical Image Re-Identification](https://arxiv.org/abs/2606.21368)

**<font color=#1a73e8>作者：</font>** Nichula Wasalathilaka, Abhijit Das, Imran Razzak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image re-identification (MedReID) enables longitudinal patient linkage but remains vulnerable to shortcut learning and often produces decisions that clinicians cannot audit against named anatomy. We propose Graph-of-Differences (GoD), which grounds identity comparisons in explicit anatomical structure. Each image is represented as an anatomy graph whose nodes correspond to named anatomical regions; given an image pair, soft node correspondence is established, and differences are computed over matched anatomy. A graph-level difference alignment objective ties these anatomy-matched differences to the global backbone difference, ensuring the retrieval signal is anchored in homologous structures rather than arbitrary spatial tokens. Explanations are defined over named graph nodes and quantitatively audited via node insertion/deletion tests, replacing unstable pixel heatmaps with verifiable structure-level evidence. On internal benchmarks, GoD improves Rank-1 by +7.1 pp on fundus and +3.1 pp on CXR over a strong frozen-backbone baseline, with further gains on zero-shot external transfers confirming that anatomy grounding improves both accuracy and generalization. Code is available at this https URL.

---


### 91. [Enhancing Creativity in 3D Generative Design via a TRIZ-Inspired Text-to-CAD Framework](https://arxiv.org/abs/2606.21378)

**<font color=#1a73e8>作者：</font>** Dongeon Lee, Leekyo Jeong, Soyoung Yoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have demonstrated significant potential in supporting engineering design tasks, including computer-aided design (CAD) automation. However, most existing LLM-based 3D CAD generation approaches primarily focus on geometric precision and instruction-following performance, often overlooking the fundamental aspect of creative design exploration. This study presents a TRIZ-inspired text-to-CAD framework that leverages LLMs to generate high-quality, editable CAD models while systematically exploring creative design alternatives. The framework integrates the Theory of Inventive Problem Solving (TRIZ)-embedding deep human insights from extensive patent records-into LLM prompting strategies, enabling autonomous generation of innovative CAD variants that address technical contradictions. Through a comprehensive three-stage pipeline of design generation, enhancement, and optimization, the framework produces structurally diverse CAD models from well-crafted prompts. The present study implements and evaluates the first two stages, while positioning the design optimization stage as future work. A product design case study (chair) demonstrates that the TRIZ-inspired text-to-CAD framework generates multiple creative design alternatives by systematically applying TRIZ inventive principles such as segmentation, anti-weight, dynamics, and composite materials, achieving 4.0-14.7% mass reduction across all enhanced designs while maintaining structural integrity. The key findings suggest that integrating systematic innovation methodologies with LLM-based 3D CAD generation bridges the gap between precision-focused synthesis and creativity-focused exploration, advancing toward autonomous design systems where AI makes design decisions independently, supporting human decision-making in human-AI collaborative design for engineering applications.

---


### 92. [EnTrust: Modeling Inter-Modal Conflict for Trustworthy Multimodal Medical Image Analysis](https://arxiv.org/abs/2606.21384)

**<font color=#1a73e8>作者：</font>** Dwarikanath Mahapatra, Abhijit Das, Behzad Bozorgtabar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal medical imaging fuses complementary anatomical and functional information, yet modalities frequently disagree in pathologically heterogeneous regions. Current segmentation models handle this in one of two inadequate ways: deterministic fusion that averages away disagreement, or post-hoc uncertainty estimation decoupled from the fusion process that produces it. Both obscure the clinically critical question: why is this prediction unreliable? We present EnTrust, a framework that treats inter-modal conflict as the primary source of predictive uncertainty. Our EnFuse module decomposes multimodal features into three disentangled components: shared anatomical consensus (F_c), modality-specific cues (F_{u,m}), and spatially localized conflict signals (F_{cf}), with independence enforced via a cross-covariance objective. This structured decomposition conditions SegDiff, a diffusion-based generative segmentation model whose sampled hypotheses diverge specifically in regions of modal disagreement. TrustMap then translates this hypothesis divergence into calibrated, pixel-wise uncertainty using ensemble entropy, conflict-guided perturbation probing, and a learned calibration head, enabling clinicians to understand not only where predictions are uncertain, but why. Across four benchmarks spanning brain, cardiac, lesion, and oncology domains, EnTrust achieves state-of-the-art segmentation accuracy while reducing calibration error by 40% compared to the strongest baseline. Notably, it outperforms 5x deep ensembles using a single model at roughly half the memory footprint. Code and checkpoints are available at this https URL.

---


### 93. [Atomistic Language Models Understand and Generate Materials](https://arxiv.org/abs/2606.21395)

**<font color=#1a73e8>作者：</font>** Sathya Edamadaka, Krithik Ramesh, Ju Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Atomistic structure and natural language have long been modeled separately, with language models either calling atomistic models as tools or being fine-tuned on lossy textual encodings that discard atomistic information. We introduce Atomistic Language Models (ALMs) to pursue native multimodality, in which a single language backbone understands atomistic structures, generates materials from natural language, and optimizes crystal structures as instructed by text. By unifying a pretrained atomistic encoder, large language model, and denoising diffusion model through purely continuous projectors and staged training, ALMs achieve state-of-the-art results on crystal structure prediction and de novo generation. ALMs are enabled by a continuous bridge that maps language model embeddings directly into the steering space of atomistic diffusion, and are assisted by Text-to-Crystal Feynman-Kac (T2C-FK), a particle-based sampler that scores partial denoising trajectories to enforce stoichiometric targets at inference time. To evaluate the ability of ALMs to optimize and generate materials from natural-language prompts and 3D atom-coordinate inputs, we introduce ALM Bench, the first benchmark for text-conditioned crystal generation and optimization. Code, training data, and model weights will be released soon.

---


### 94. [Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention](https://arxiv.org/abs/2606.21399)

**<font color=#1a73e8>作者：</font>** Chubin Zhang, Zhenglin Wan, Xingrui Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime oversight for LLM agents is commonly framed as scalar risk prediction: estimate failure likelihood, confidence, or uncertainty, then intervene once the score crosses a threshold. We argue that this framing targets the wrong object for control. The relevant question is not how likely the agent is to fail if it continues, but whether an available intervention would improve the outcome. Two trajectory prefixes can have the same risk estimate while requiring different actions, because one remains recoverable and the other does not. We formalize this mismatch as target error and identify intervention advantage, the expected utility gain from intervening rather than continuing, as the decision object for oversight. To measure this mismatch, we introduce prefix branching, a same-prefix counterfactual protocol that executes candidate actions from identical trajectory states. Across four benchmarks, action-conditioned control yields regime-dependent gains over scalar routing. In a calibration decomposition, recalibrating the same scalar score improves prediction metrics but leaves control regret unchanged, showing that calibration alone does not repair target error. A simple prefix-only action-conditioned controller substantially reduces regret in the strongest interactive regime, from 0.506 to 0.110 on ALFWorld. Gains shrink when interventions are weak or when scalar routing already preserves intervention-relevant information. These results suggest that LLM-agent oversight should move from calibrated risk scoring toward action-conditioned value estimation.

---


### 95. [Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents](https://arxiv.org/abs/2606.21409)

**<font color=#1a73e8>作者：</font>** Chubin Zhang, Zhenglin Wan, Xingrui Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented agents are typically evaluated by their gains under reliable external feedback. Yet these gains leave open a key counterfactual: when feedback is unreliable, would the agent be better off receiving no task evidence? We study this question with a controlled matched-loop comparison that fixes the agent loop, prompt, action space, and decoding, while varying only the returned observation: faithful, misleading, or absent. Across question answering and fact verification, persistent misleading feedback produces a value inversion: agents that benefit from clean tools can perform worse than the matched no-feedback fallback. On HotpotQA, Qwen2.5-7B reaches 44.8 F1 with clean retrieval and 22.3 F1 with no feedback, but drops to 4.7 F1 under shuffled retrieval. The inversion persists under stronger clean retrieval and locally plausible distractors, but weakens when later clean evidence can repair the trajectory. Early trajectory signals predict many failures, yet simple repairs remain fallback-limited: rejecting bad evidence helps only when the exposed fallback is reliable. These results show that clean-tool gains can overstate tool value, and that matched no-feedback fallback controls are necessary for evaluating tool-augmented agents.

---


### 96. [MIRCaps: A Large-Scale Mixed-Domain Dataset with Image-Level and Region-Level Captions for Fine-Grained Vision-Language Learning](https://arxiv.org/abs/2606.21419)

**<font color=#1a73e8>作者：</font>** Arlindo Luciano Tulumba Roberto, Hyungjoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in Vision-Language Models (VLMs), mixed-domain image-caption datasets for both general-purpose and CCTV-based video surveillance systems remain limited. To address this gap, we introduce a large-scale multimodal dataset comprising 141,364 images, 981,947 image-level captions, 1,742,264 region-level captions, and 1,391,779 bounding box annotations. Each image is associated with an average of seven image-level captions describing different aspects of the overall scene, as well as seven region-level captions for each annotated bounding box. These complementary caption types are designed to help VLMs learn fine-grained visual attributes, including object categories, estimated sizes, colors, actions, states, and surrounding environmental context. We demonstrate the effectiveness of the dataset on two important downstream tasks: image captioning and object detection. Experimental results show that lightweight VLMs, including SmolVLM-256M-Instruct, BLIP, BLIP2, and Qwen2.5-VL 3B-Instruct, can be effectively fine-tuned using our dataset. Our dataset and code are publicly available at this https URL.

---


### 97. [AutoRAS: Learning Robust Agentic Systems with Primitive Representations](https://arxiv.org/abs/2606.21445)

**<font color=#1a73e8>作者：</font>** Yang Yue, Xuancheng Zhu, Yuyang Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The automated design of agentic systems offers a promising pathway for scaling large language models (LLMs) beyond single-agent reasoning. While prior work has advanced task performance through handcrafted or automatically generated multi-agent workflows, robustness is often treated as an afterthought, leaving systems vulnerable to external adversaries and internal failures. We propose AutoRAS, a framework for the Automated design of Robust Agentic Systems. AutoRAS formulates system design as generating a sequence of symbolic primitives that jointly encode structural connectivity and behavioral actions, and learns to optimize this sequence using execution-derived safety signals and flow-based sequence-level objectives. Extensive experiments show that AutoRAS achieves the best performance in both vanilla and adversarial settings, with the smallest performance degradation under attacks. Further analyses demonstrate strong transferability, stable optimization behavior, stability across primitive sets, and favorable cost trade-offs. Our code is available at $\href{this https URL}{\text{this https URL}}$.

---


### 98. [Fast-TurboQuant: A Multiplier-Free Online Vector Quantization Approach](https://arxiv.org/abs/2606.21448)

**<font color=#1a73e8>作者：</font>** Pedro M. R. Pereira, Felipe A. P. de Figueiredo, Rausley A. A. de Souza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models scale, memory bandwidth for key-value caches and retrieval-augmented generation systems becomes a critical bottleneck. While 1-bit quantization addresses this constraint, recent TurboQuant relies on dense random rotation matrices to condition the vector distribution before quantization. This projection demands millions of floating-point multiplications per embedding, making it difficult to deploy on constrained edge silicon. We introduce Fast-TurboQuant, a multiplier-free projection architecture that replaces the dense matrix with a structured fast Johnson-Lindenstrauss transform. By applying a Rademacher phase inversion followed by a fast Walsh-Hadamard transform (FWHT), the method leverages sub-Gaussian concentration to satisfy the prerequisites of scalar Lloyd-Max quantization without Gaussian projections. This substitution reduces the arithmetic complexity to only additions, eliminating hardware multipliers. Evaluation on DBpedia OpenAI-3 Large embeddings demonstrates a 19.7 times algorithmic speedup under sequential execution. Furthermore, the dimension expansion due to the FWHT zero-padding reduces the mean squared error and improves Recall@10.

---


### 99. [CORTIS: Text-Only Adaptation of Spoken Language Models for Task-Oriented Voice Agents](https://arxiv.org/abs/2606.21453)

**<font color=#1a73e8>作者：</font>** Youngwon Choi, Hyeonyu Kim, Taeyoun Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Task-oriented voice agents need to map spoken user requests to structured outputs such as semantic frames, executable actions, and function calls. A common approach is to cascade ASR with a text-based LLM, but transcription errors can propagate to downstream structured output generation, especially under noisy conditions. Spoken language models (SLMs) offer a direct speech-based alternative, yet adapting them to new tasks typically requires paired speech-target annotations. Motivated by this gap, we present CORTIS, a text-only adaptation framework for task-oriented voice agents. CORTIS fine-tunes SLMs using text-form task supervision, enabling speech-based structured output generation at inference time without task-specific speech-target annotations during adaptation. We evaluate CORTIS on two Qwen2.5-Omni backbones and three task-oriented speech datasets, including an in-house product dataset, and compare it with matched ASR-LLM cascades trained with the same text-form task supervision. Results show that CORTIS performs competitively with matched cascades and offers clearer advantages under acoustic degradation, particularly in preserving high-level task semantics. These findings suggest that text-only fine-tuning of SLMs can serve as a practical adaptation strategy for voice agents when paired speech-target data are costly to collect.

---


### 100. [Post-Training Speech Enhancement Language Models with Perceptual Rewards](https://arxiv.org/abs/2606.21458)

**<font color=#1a73e8>作者：</font>** Frédéric Berdoz, Luca A. Lanzendörfer, Antonis Asonitis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech enhancement language models achieve strong results when trained on discrete audio tokens, but their optimization relies on token-level cross-entropy rather than the perceptual metrics used for evaluation. We introduce a post-training stage for autoregressive speech enhancement language models using Group Sequence Policy Optimization (GSPO) with multi-metric perceptual rewards. Our method directly optimizes non-differentiable quality metrics (DNSMOS, WER, and UTMOS) as reward signals, without learned surrogates or offline preference pairs. Applied to two autoregressive base models, UniSE and GenSE, our approach achieves state-of-the-art results on the DNS2020 benchmark. A human evaluation ablation further shows that the composite multi-metric reward is preferred over any single-metric variant, confirming that multi-reward optimization avoids the reward hacking observed with single-metric training.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
